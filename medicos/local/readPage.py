__author__ = 'fkfouri'

import urllib
import urllib.request as rq
from lxml import html
import json
import stampsBD as bd
import datetime


def readICD(ICD):
    '''Leitura do Site de ICD'''

    def formatICD(ICD):
        ''' responsavel por normaliar o ICD'''
        if '.' not in ICD:
            return '{}.{}'.format(ICD[:3], ICD[3:])
        else:
            return ICD

    def stampsICD(ICD):
        ''' responsavel por normaliar o ICD/CID do Stamps'''
        return str(ICD).replace('.','')

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

    lstCID_STAMPS, lstICD = [], []
    lstCID_STAMPS.append(stampsICD(ICD))
    lstICD.append(formatICD(ICD))
    out["CID_STAMPS"] = lstCID_STAMPS
    out["ICD"] = lstICD

    # p[@class="NLMattribution"]
    # info5 = tree.xpath('//p[@class="NLMalsoCalled"]/../p[not(preceding-sibling::ul)]/text()')

    refXpath = '//p[@class="NLMalsoCalled"]'
    refXpath = '//span[@class="glyphicon glyphicon glyphicon-plus-sign text-primary gi-1x margin-right-5"]'

    out["symptoms"] = tree.xpath(str(refXpath) + '/../ul[1]/li/text()')
    info = '\n'.join(tree.xpath(str(refXpath) + '/../p/text()|' + str(refXpath) + '/../ul/li/text()'))

    out["info"] = info
    out["done"] = 'NOK'

    '''
    try:
        import stampsTranslate as tr
        out["info"] = tr.Translate(info)
        out["done"] = 'OK'
    except urllib.error.HTTPError as err:
        out["info"] = info
        out["done"] = 'NOK'
    '''

    return json.loads(json.dumps(out, separators=(',', ':')))

ref = bd.GET_CID_10_SUBCATEGORIAS()
for item in ref:
    print(item['SUBCAT'])

    # le o site
    readSite = readICD(item['SUBCAT'])
    # verifica se ja existe algum registro parecido
    check = bd.GET_DETAIL(readSite['info'])

    if check is None:
        # insere caso nao tenha achado
        bd.INSERT_MONGO('DETAIL', readSite)
    else:
        # executa o update
        CID_STAMPS = list(set().union(check['CID_STAMPS'], readSite['CID_STAMPS']))
        ICD = list(set().union(check['ICD'], readSite['ICD']))
        bd.UPDATE_DETAIL(check['_id'], CID_STAMPS, ICD)

    print('------' + str(datetime.datetime.now().time()))


'''
resp = readICD("A000")
#print(resp)
print(resp['info'])
print(tr.translate(resp['info']))
'''
