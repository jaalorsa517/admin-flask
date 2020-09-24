#Script para configurar flask

import click
import os

def config():
    _flask_app()
    _mode()
    _environ()


def _flask_app():
    env= click.prompt('Ingrese el nombre del archivo principal para iniciar la aplicación',default='admin.py')
    os.environ['FLASK_APP']= env


def _mode():        
    if click.confirm('Development?'):
        os.environ['FLASK_ENV']= 'Development'
    else:
        os.environ['FLASK_ENV']= 'Production'

def _environ():
    if click.confirm('Debug?'):
        os.environ['FLASK_DEBUG']= '1'
    else:
        os.environ['FLASK_DEBUG']= '0'
    os.system('flask run')