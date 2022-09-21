#!/usr/bin/env python3


import os
import logging


## BOILERPLATE
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("logs.py", log_level)
#level
ch = logging.StreamHandler()
ch.setLevel(log_level)
# formatacao
fmt = logging.Formatter( 
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
     )
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

##

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral par usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""

print("---------")


logging.critical("Deu problema geral")

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    # stdout
    # stderr
