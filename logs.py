#!/usr/bin/env python3


import os
import logging
from logging import handlers 


## BOILERPLATE
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# nossa instancia
log = logging.Logger("logs.py", log_level)
#level
#ch = logging.StreamHandler() # Console/terminal/stderr
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=100,  #10**6
    backupCount=10,
)
fh.setLevel(log_level)
# formatacao
fmt = logging.Formatter( 
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
     )
fh.setFormatter(fmt)
# destino
log.addHandler(fh)

##

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral par usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critical("Erro geral ex: banco de dados sumiu")
"""


try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    # stdout
    # stderr
