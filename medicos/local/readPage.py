__author__ = 'fkfouri'

import urllib.request as rq
from lxml import html
import json
import translate as tr


def readICD(ICD):
    '''Leitura do Site de ICD'''
    proxy_handler = rq.ProxyHandler({"http": "http://login:pwd@lnx237in.sjk.emb:9090"})
    proxy_opener = rq.build_opener(proxy_handler)
    rq.install_opener(proxy_opener)

    # "http://icdlist.com/icd-10/A98.4"'
    originalLink = "http://icdlist.com/icd-10/" + str(ICD)
    with rq.urlopen(originalLink) as url:
        page = url.read()

    tree = html.fromstring(page)

    out = {}
    # p[@class="NLMattribution"]
    # info5 = tree.xpath('//p[@class="NLMalsoCalled"]/../p[not(preceding-sibling::ul)]/text()')
    out["symptoms"] = tree.xpath('//p[@class="NLMalsoCalled"]/../ul[1]/li/text()')
    out["info"] = tree.xpath('//p[@class="NLMalsoCalled"]/../p/text()|//p[@class="NLMalsoCalled"]/../ul/li/text()')

    return json.loads(json.dumps(out, separators=(',', ':')))


resp = readICD("A98.4")
#print(resp)
print(resp['info'][0])
# print(tr.translate(resp['info'][0]))
