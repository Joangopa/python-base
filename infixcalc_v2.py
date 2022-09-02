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


os resultados serao salvos em  `infixcalc2.log`
"""

__version__ = "0.1.1"


import os
import sys
from datetime import datetime
arguments = sys.argv[1:]

if not arguments:
    operation = input("operacao: sum, sub, mul, div:")
    n1 = int(input("primer numero:"))
    n2 = int(input("segundo numero:"))
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("Exemplo: `sum 5 6`")
    sys.exit(1)    
# print(sys.argv)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Operacaon inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []

for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums


if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2    
elif operation == "div":
    if n2 == "0":
        print("Nao pode dividir por zero")
    else:    
        result = n1/n2

path = os.curdir
filepath = os.path.join(path, "infixcalc2.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')


with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operation},{n1},{n2} = {result} \n")

print(f"O resultado é {result}")