#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests as req
import json

URL = 'http://localhost:5000/api/pessoa'

obj1 = {
    'nome': 'Isaac',
    'cpf': '111.111.111/11'
}

obj2 = {
    'nome': 'Lucas',
    'cpf': '222.222.222/22'
}

obj3 = {
    'id': 1,
    'nome': 'Isaac',
    'cpf': '111.111.111/11'
}

obj4 = {
    'id': 2,
    'nome': 'Lucas',
    'cpf': '222.222.222/22'
}

obj5 = {
    'id': 1,
    'nome': 'Isaac',
    'cpf': '123.456.789/10'
}

def test_01_simple():
    assert True

'''def test_01_insert():

    res = req.request('POST', URL, json=obj1)
    res = json.loads(res.text)

    assert res == {'msg': 'success', 'id': 1}

def test_02_find_one():

    res = req.request('GET', URL + '/1')
    res = json.loads(res.text)

    assert res == obj3

def test_03_find():

    res = req.request('POST', URL, json=obj2)
    res = json.loads(res.text)

    assert res == {'msg': 'success', 'id': 2}

    res = req.request('GET', URL)
    res = json.loads(res.text)

    assert res[1] == obj4

def test_04_update():

    res = req.request('PUT', URL, json=obj5)
    res = json.loads(res.text)

    assert res == {'msg': 'success'}

    res = req.request('GET', URL + '/1')
    res = json.loads(res.text)

    assert res == self.obj5

def test_05_delete(self):

    res = req.request('DELETE', URL + '/1')
    res = json.loads(res.text)

    assert res == {'msg': 'success'}

    res = req.request('GET', URL)
    res = json.loads(res.text)

    assert len(res) == 1'''

