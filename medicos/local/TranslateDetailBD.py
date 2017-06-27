__author__ = 'fkfouri'

import urllib
import urllib.request as rq
from lxml import html
import json
import stampsBD as bd
import stampsTranslate as st
import datetime

collection = bd.GET_DETAIL_UNTRANSLATED()
for document in collection:
    _id = document['_id']
    symptoms = " § ".join(document['symptoms']).replace(' - ', '')
    info = document['info']

    # uma unica traducao, devido limitacao do Google
    temp = st.Translate(symptoms + " §§ " + info)

    #remonta as variaveis traduzidas
    info_PT = temp.split(" §§ ")[1]
    symptoms_PT = temp.split(" §§ ")[0].split(" § ")

    bd.UPDATE_DETAIL_TRANSLATE(_id, info_PT, symptoms_PT)

    info=info