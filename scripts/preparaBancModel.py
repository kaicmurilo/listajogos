import mysql.connector
from mysql.connector import errorcode

print("Conectando....")
try:
    conn = mysql.connector.connect(
        host='endereco host',
        user='usuario',
        password='senha'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuario ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute("CREATE DATABASE `jogoteca`;")

cursor.execute("USE `jogoteca`;")

# criando tabelas

TABLES = {}

TABLES['Jogos'] = ('''
    CREATE TABLE `jogos` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) NOT NULL,
        `categoria` varchar(40) NOT NULL,
        `console` varchar(20) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin''')


TABLES['Usuarios'] = ('''
    CREATE TABLE `usuarios` (
        `nome` varchar(20) NOT NULL,
        `nickname` varchar(10) NOT NULL,
        `senha` varchar(100) NOT NULL,
        PRIMARY KEY (`nickname`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Ja existe')
        else:
            print(err.msg)
    else:
        print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ('kaic nunes', 'kaic', 'kaic'),
    ("Camila Ferreira", "Mila", "paozinho"),
    ("Guilherme Louro", "Cake", "python")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print('------------- usuarios ------------- ')
for user in cursor.fetchall():
    print(user[1])


# inserindo jogos
jogo_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
    ("Tetris", "Puzzle", "Atari"),
    ("God Of War", "Hack n Slash", "PS2"),
    ("Mortal Kombat", "Luta", "PS2")
]
cursor.executemany(jogo_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print('------------- jogos ------------- ')
for jogo in cursor.fetchall():
    print(jogo[1])

# Cleanup
conn.commit()
cursor.close()
conn.close()
print("Done.")
