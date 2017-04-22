__author__ = 'fkfouri'

import goslate
import urllib.request as rq

def tranlate(text):
    #proxy_handler = rq.ProxyHandler({"http":"http://proxy"})
    #proxy_opener = rq.build_opener(proxy_handler)
    gs = goslate.Goslate()
    gs = goslate.Goslate(opener=proxy_opener)
    return gs.translate('give me some love', 'pt-br')

