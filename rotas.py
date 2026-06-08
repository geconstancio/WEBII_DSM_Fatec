# -*- coding: utf-8 -*-
"""
Título: Blueprint de Páginas
Descrição: Arquivo contendo as rotas que renderizam templates HTML
Data: 02/06/2026
"""
__author__ = "Gleice Constâncio Rodrigues"
__email__ = "gleice.rodrigues@aluno.cps.sp.gov.br"
__turma__ = "DSM - 3º Semestre / Noturno"
__version__ = "1.0.0"

import re
from flask import Blueprint, request, jsonify

rotas_bp = Blueprint('rotas', __name__)

@rotas_bp.route("/message")
def message():
    return "Cadastro Salvo com sucesso"

@rotas_bp.route("/message/<int:status>")
def message_status(status):
    status_messages = {
        200: "200 OK: Sucesso geral.",
        201: "201 Created: Sucesso na criação.",
        400: "400 Bad Request: Erro do cliente (sintaxe).",
        401: "401 Unauthorized: Falta autenticação.",
        404: "404 Not Found: Recurso não encontrado.",
        500: "500 Internal Server Error: Erro no servidor.",
    }

    if status in status_messages:
        return status_messages[status], status

@rotas_bp.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        if username == "genivaldo" and password == "jerusa" :
            return jsonify({'status': 200, 'mensagem': 'OK: Sucesso geral.'}), 200
        else:
            return jsonify({'status': 401, 'mensagem': 'Unauthorized: Falta autenticação.'}), 401
        

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    # Validar primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    if digito1 != int(cpf[9]):
        return False

    # Validar segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    if digito2 != int(cpf[10]):
        return False

    return True

@rotas_bp.route('/cliente', methods=['POST']) 
def cadastrar_cliente():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')

    if not nome or not cpf:
        return jsonify({'status': 400, 'mensagem': 'Bad Request: Erro do cliente (sintaxe).'}), 400

    if validar_cpf(cpf):
        return jsonify({'status': 200, 'mensagem': 'OK: Sucesso geral.'}), 200
    else:
        return jsonify({'status': 400, 'mensagem': 'Bad Request: Erro do cliente (sintaxe).'}), 400

@rotas_bp.route('/convert/celcius/<float:temp>', methods=['GET'])
def converte_celcius(temp):
    fahrenheit = (temp * 9/5) + 32
    return jsonify({'celcius': temp, 'fahrenheit': fahrenheit}), 200

@rotas_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query is None:
        return jsonify({'status': 400, 'mensagem': 'Parâmetro de busca obrigatório.'}), 400
    else:
        return jsonify({'status': 200, 'mensagem': f'Você pesquisou por: {query}'}), 200

@rotas_bp.route('/api/register', methods=['POST'])
def validacao_maioridade():
    data = request.get_json()
    nome = data.get('nome')
    idade = data.get('idade')

    if idade < 18:
        return jsonify({'status': 403, 'mensagem': 'Forbidden: Cadastro permitido apenas para maiores de idade.'}), 403
    else:
        return jsonify({'status': 201, 'mensagem': f'Created: Usuário {nome} cadastrado'}), 201

@rotas_bp.route('/products', methods=['GET'])
def estoque():
    products = [
        {'id': 1, 'nome': 'Fone de Ouvido', 'preco': 129.99},
        {'id': 2, 'nome': 'Cabo HDMI', 'preco': 19.99},
        {'id': 3, 'nome': 'Caneta', 'preco': 2.49}
    ]
    if products is None:
        return jsonify({'status': 204, 'mensagem': 'No Content: Nenhum produto encontrado.'}), 204
    else:
        return jsonify({'status': 200, 'products': products}), 200

@rotas_bp.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():
    api_key = request.headers.get('X-Api-Key')
    if api_key == "secret123":
        return jsonify({'status': 200, 'mensagem': 'OK: Sucesso geral.'}), 200
    else:
        return jsonify({'status': 401, 'mensagem': 'Unauthorized: Falta autenticação.'}), 401