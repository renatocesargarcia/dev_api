import json
from flask import jsonify

from flask import Flask, request

app = Flask(__name__)

desenvolvedores =[
    {
        'id': '0',
        'nome': 'Renato',
        'habilidades': ['Python', 'Django']
    },

    {
        'id':1,
        'nome': 'Andrea',
        'habilidades': ['Python', 'Flask']
    }
]

# devolve um desenvolvedor pelo ID, altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor da ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API"
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}


# Lista todas os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ =='__main__':
    app.run(debug=True)