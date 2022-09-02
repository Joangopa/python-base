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
import sys 


arguments = {
    "lang": None,
    "count": 1,
}



for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}` ")
        sys.exit()
    arguments[key] = value


current_language =  arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")
	#export LANG=it_IT.utf8  --- troca a lenguagem do terminal
	#LANG=pt_BR  ---- impor a linguagem na terminal

current_language = current_language[:5]
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

print(msg[current_language]*int(arguments["count"]))

# LANG = es_SP python3 hello.py 