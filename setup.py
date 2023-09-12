# Bot Blaze
import sys
import os
from cx_Freeze import setup, Executable

arquivos = ['relatorios', 'csv', 'graficos']


configuracao = Executable(
    script='alertas.py',
    icon='icones\\alerta.ico'
)

setup(
    name="Gerenciador de Alertas",
    version="2.7",
    description="Tratamento de alertas e geracao de relatorios",
    author='Ornilio Neto',
    options={
        'build_exe': {
            'include_files': '',
            'include_msvcr': True
        }
    },
    executables=[configuracao]
)
# executar o script no terminal para fazer a compilação
# python .\setup.py build

#pip install -r requirements.txt
