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

for cliente in clientes:
    print(
        email_tmplt % 
        {
        "nome": cliente,
        "produto": "caneta",
        "texto": "Escrever muito bem",
        "link" : "https://canetaslegais.com",
        "quantidade" : 1,
        "preco" :  50.0
        }
        )