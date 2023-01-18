from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
listaJogos = [jogo1, jogo2, jogo3]


class Usuario:
    def __init__(self, nome, nickname, senha) -> None:
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario1 = Usuario("Kaic Nunes", "kaic", "kaic")
usuario2 = Usuario("Camila Ferreira", "mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", "louro", "python")

usuarios = {usuario1.nickname: usuario1,
            usuario2.nickname: usuario2,
            usuario3.nickname: usuario3}

app = Flask(__name__)
app.secret_key = 'kaicnunes'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=listaJogos,
                           usuario=session['usuario_logado'])


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # return redirect('/login?proxima=novo')
        return redirect(url_for('login', proxima=url_for('novo')))

    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    listaJogos.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar',  methods=['POST',])
def autenticar():

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            if (proxima_pagina == 'None'):
                return redirect(url_for('index'))
        # return redirect('/{}'.format(proxima_pagina))
        return redirect(proxima_pagina)
    else:
        flash('Erro em credenciais!')
        return redirect(url_for('login'))
    # if 'alohomora' == request.form['senha']:
    #     session['usuario_logado'] = request.form['usuario']
    #     flash(session['usuario_logado'] + ' logado com sucesso!')
    #     proxima_pagina = request.form['proxima']
    #     if (proxima_pagina == 'None'):
    #         return redirect(url_for('index'))
    #     # return redirect('/{}'.format(proxima_pagina))
    #     return redirect(proxima_pagina)
    # else:
    #     flash('Erro em credenciais!')
    #     return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Nao se encontra logado.')
        return redirect(url_for('login'))

    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))


    # trecho da app
app.run(debug=True)
