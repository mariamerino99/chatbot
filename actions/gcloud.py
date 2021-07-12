import logging
import os
import cloudstorage as gcs


# from google.appengine.api import app_identity

import string
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


number_of_strings = 1
length_of_string = 8
for x in range(number_of_strings):
  print(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('/home/maria/Descargas/prueba-e35e9-effc66479193.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('datos').document(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
doc_ref.set({
    'Nombre': u'Maria Merino',
    'Edad': u'21',
    'Antecendentes': 'si',
    'Prob_inicial':'0',
    'Definiciones':'5',
    'Nombres_propios':'5',
    'Lista_inmediata':'8',
    'Objetos':'5',
    'Lista_demorada':'9',
    'Identidad':'1',
    'Resultado_final':'33'


})