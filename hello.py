#!/usr/bin/env python3
"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente

Como usar:
	Tenha a variável LANG devidamente configurada ex:

	export LANG=pt_BR

Execuacao:

	python3 hello.py
	ou
	 ./hello.py
"""
__version___ = "0.1.0"
__author__ = "Jonatan"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]
	#export LANG=it_IT.utf8  --- troca a lenguagem do terminal
	#LANG=pt_BR  ---- impor a linguagem na terminal
	
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "es_SP": "¡Hola, Mundo!",
    "it_IT": "Ciao, Mondo",
}


#if current_language == "pt_BR":
#	msg = "Olá, Mundo!"
#elif current_language == "it_IT":
#	msg =  "Ciao, Mondo!"
#elif current_language == "es_SP":
#	msg =  "Hola, Mundo!"
#print(msg)

print(msg[current_language])

# LANG = es_SP python3 hello.py (correr el programa)