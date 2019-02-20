# -*- coding: utf -8 -*-
nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

if idade >=18:
    print('Pode entrar' + nome)

if idade <=11:
    print('Menor de idade, você ainda é criança')

elif idade <18:
    print('Menor de idade')
