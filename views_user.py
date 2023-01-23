from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash


@app.route('/login')
def login():
    form = FormularioUsuario()
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, form=form)


@app.route('/autenticar',  methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(
        nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        if (proxima_pagina == 'None'):
            return redirect(url_for('index'))
        else:
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Nao se encontra logado.')
        return redirect(url_for('login'))

    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))
