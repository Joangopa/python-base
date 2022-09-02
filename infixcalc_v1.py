#!usr/bin/env python3

"""Calculadora infix.

Funcionamento:

[operacao] [n1] [n2]

operacoes:

sum -> +
sub -> - 
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5 
50

$ inflixcalc.py 
operacao: sum
n1: 5
n2: 4
9

"""

__version__ = "0.1.0"


import os
import sys

# print(sys.argv)

if sys.argv[1] == "sum":
    print(int(sys.argv[2])+int(sys.argv[3]))
elif sys.argv[1] == "sub":
    print(int(sys.argv[2])-int(sys.argv[3]))
elif sys.argv[1] == "mul":
    print(int(sys.argv[2])*int(sys.argv[3]))    
elif sys.argv[1] == "div":
    if sys.argv[3] == "0":
        print("pode chorar")
    else:    
        print(int(sys.argv[2])/int(sys.argv[3]))
else:
    print("Volte e Escolha operacao valida")

    
operacao = input("operacao: sum, sub, mul, div:")
n_1 = int(input("primer numero:"))
n_2 = int(input("segundo numero:"))

    

if operacao == "sum":
    print(n_1 + n_2)
elif operacao == "sub":
    print(n_1 -  n_2)
elif operacao == "mul":
    print(n_1 *  n_2)
elif operacao == "div":
    if n_2 == 0:
        print("Nao posso dividir")
    else:
        print(n_1 /  n_2)
else:
    print("Volte e Escolha operacao valida")
