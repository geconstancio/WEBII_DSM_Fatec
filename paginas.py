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

from flask import Blueprint, render_template

paginas_bp = Blueprint('paginas', __name__, template_folder='templates')

@paginas_bp.route("/")
def index():
    return render_template('paginas/index.html', title="Página Inicial")