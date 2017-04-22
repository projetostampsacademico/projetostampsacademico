__author__ = 'fkfouri'

import urllib.request as rq
from lxml import html
import json
import stampsTranslate as tr


def readICD(ICD):
    '''Leitura do Site de ICD'''

    def formatICD(ICD):
        ''' responsavel por normaliar o ICD'''
        if '.' not in ICD:
            part1 = ICD[:3]
            part2 = ICD[3:]
            return '{}.{}'.format(part1, part2)
        else:
            return ICD

    '''
    proxy_handler = rq.ProxyHandler({"http": "http://login:pwd@lnx237in.sjk.emb:9090"})
    proxy_opener = rq.build_opener(proxy_handler)
    rq.install_opener(proxy_opener)
    '''

    # "http://icdlist.com/icd-10/A98.4"'
    originalLink = "http://icdlist.com/icd-10/" + str(formatICD(ICD))
    with rq.urlopen(originalLink) as url:
        page = str(url.read()).replace('<li>', '<li> - ')

    tree = html.fromstring(page)

    out = {}
    # p[@class="NLMattribution"]
    # info5 = tree.xpath('//p[@class="NLMalsoCalled"]/../p[not(preceding-sibling::ul)]/text()')


    out["symptoms"] = tree.xpath('//p[@class="NLMalsoCalled"]/../ul[1]/li/text()')
    info = '\n'.join(tree.xpath('//p[@class="NLMalsoCalled"]/../p/text()|//p[@class="NLMalsoCalled"]/../ul/li/text()'))
    out["info"] = tr.Translate(info)
    out["CID"] = ICD

    return json.loads(json.dumps(out, separators=(',', ':')))


resp = readICD("A98.4")
#print(resp)
print(resp['info'])
'''
print(tr.translate(resp['info']))
'''