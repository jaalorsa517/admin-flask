# Script para configurar flask
from apps.auth import auth
from flask import Flask
from flask_login import LoginManager
from models.users import User
import click
import os

'''
User admin
nickname, password = root
root,pbkdf2:sha256:150000$uZH9iOgR$6e75353c21a99a6d06e14f1f93ed84bbb7aa4d8a1409eb3bd3cdcce5734c634b,True
'''

def config_app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    app.config['SECRET_KEY'] = '345226e25fe2e9909b9f331716502964bd897990391a0cbcc53a71736880b0e69c190973473f0f019bcdfd927f8d4473bd06e8b4d95124f9e402095dabe198d405cb0016ff6b12dce043d5f09f8c56d980941810b366260446127660b9fc238a5b60986ad8f0bcc9c43cb4bc673d9eac04b30ebda896e2a5e27c760bfeede4d8bad937901cd2775de848a261f29a8939f97bdecf372d247a75a6f5fec6622d9fafd12b7c3a97c3266801b1f03ebf9debe5165b9b4f00346324cdf55bf6c3c0673c36eb52a7176066076d15831dfd26185fd967ab53fa5fb92841f49ded289524a2fccbd4bd9f39091f6ecdf4991e8abc3e374e2d3868d01141a108eba9113a9376cdfde59dfa235a0c2fa1728c6c6709d2e9049370d82124dbab798e596f90143d72107836450a6cfbe91d45973c3b93c42fa0c6c1d29f8f59e38996bb5c273c2a8ded850ba94bf6165ca370625e1eb517bab804916101f2823588cc554ce46d3a3de09808ccd6fd559c62cecd99f8d3cc8a47f5dfd4a10f4243894c94c49f55ed987be3d4b0ddc1c8f0896d7f53ea4237b6065c72caed2e771c94a8acacea3a9d0b0ea3c4702e53be7c5cb018b8a7a721e27e013bf45e2cf2a31acd271ccf16b885c3764e1a769f30f8205133d00cf088923ed418a99eded657afcca786d2733e978c2f5041ebd5e392e6b145e4cbf82d57bd3f6775291dd4581186aa170b140dd3bc4cb96600a60c374ddc0e93e68de47b47b8c4b21477f9a47e3ba0d0adaf97bb31c6440b6aab33f732a8a3986e1b28d4a8f8e9c3d464ea78be2172fc34cf2c0fc3f2ebfce76881503f47fb1deecdcee2e66fb5688d7a403daec16919e6082d703d9e1656e6c1e3ad44ed9947f37ed5e052715a6a6ee1d28507604807a6375ab155007fe4be6da956ec076654b8416b21f0b2dd22a6f1b44f77627a95362f37c56632baca60178f0b015af4598c10b1e92c4701997478d2ac883948f7609de5fa32fe2749c20dbc31d4602dd13cb99800c1aa289a6be10975fae755f7da5f9560c2bc8001cd9075ac779f69bf4d37d9d905eec57ef192e277433f660d2107bc1f05ea1dfec0987ea813ebbb5b76c05ba57de919f6413f1e6560e0bfa78db4d65053864cda4c4dcbd389980d49a26794fb3fea682344c65d17265b0d2f6f5e931f3e77ac49b79ad8633142ce96c085f28ff33ca3e10ef26b40d42b82077ab92b3f17f95be598b9ae7cf33afceab313fff4deeb32ec69dfee91062b84bbf529210be164ca3b76189ac4ce471069eb4025b69b1fa674ebb6b3ef7e22cb6cd06d3dab6800a0a07e7e9a6d1da916de0e1acc440a7d4fb6612263fa5e4afa1bcfb63a3bf53c9cc2825b13ef9f52a1b8abee8aeb60a25fbc9c9b3032ea531e33777e8a479a9de436f1dd5339860f7226688947451cdf95318ec0182cc0d24696093c805dc32211ebe1c24d46fba29bbd4099159781ea938e0e0bcab04f739e29c30a0d64e7eff9a5bb792ae54e1e7f72e949f66b47baf16df01327984407af1ab0685ec053d473ca3507b9899ab97a728525b3ce862cc7928a957722cd6e7b748aabd3d99a2b63cfe188b9166ebbbc03c0afc6854d601f2c81e121923aa462ff158c05a9d13681009c260b5cee239e2c4e52c3ed4425c1428e49819194e3df4239103f4ea565e00bb504e131a71bccdf5051049c54a7e68303ccf2d0bb4a13dd1bd83ef65256d8c68619f8082517461c843610bb'

    login = LoginManager(app)
    login.login_view = 'auth.login'

    @login.user_loader
    def load_user(user):
        return User.getUser(user)

    return app


def config():
    _flask_app()
    _mode()
    _debug()


def _flask_app():
    env = click.prompt(
        'Ingrese el nombre del archivo principal para iniciar la aplicación', default='admin.py')
    os.environ['FLASK_APP'] = env


def _mode():
    if click.confirm('Production?'):
        os.environ['FLASK_ENV'] = 'Production'
    else:
        os.environ['FLASK_ENV'] = 'Development'

def _debug():
    if click.confirm('No Debug'):
        os.environ['FLASK_DEBUG'] = '0'
    else:
        os.environ['FLASK_DEBUG'] = '1'
