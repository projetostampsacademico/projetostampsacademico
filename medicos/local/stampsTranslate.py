__author__ = 'fkfouri'

import goslate
import urllib.request as rq
from translate import translator


def Translate(text):
    '''Traducao pelo Google Sites'''
    '''
    proxy_handler = rq.ProxyHandler({"http": "http://login:pwd@lnx237in.sjk.emb:9090"})
    proxy_opener = rq.build_opener(proxy_handler)
    gs = goslate.Goslate(opener=proxy_opener)
    '''
    '''
        
    gs = goslate.Goslate()
    return gs.translate(text, 'pt-br')
    '''

    return translator('en', 'pt-br', text)


print(StampsTranslate("that's a good idea"))