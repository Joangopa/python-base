#!/user/bin/env python3

clientes = ["Maria", " Joao", "Bruno"]

 
email_tmplt = """
     Olá, %(nome)s
     
     Tem interese em comprar %(produto)s
     
     Este produto é óyimo para resolver %(texto)s
     
     Clique agora em %(link)s
     
     Apenas %(quantidade)d disponiveis!

     Preco promocional %(preco).2f
"""

import sys
import os

arguments = sys.argv[1:]

if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = argumens[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # email.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt


for line in open(filepath):
    name, email = line.split(",")

    print(f"Enviando email para: {email}")    
    print()

    print(templatepath.read 
    % 
        {
        "nome": name,
        "produto": "caneta",
        "texto": "Escrever muito bem",
        "link" : "https://canetaslegais.com",
        "quantidade" : 1,
        "preco" :  50.0
        }
      )

     print("-"*50)