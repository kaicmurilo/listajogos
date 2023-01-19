"# jogotecaPy"

pip install Flask==2.0.2

DBMS (banco de dados) MySQL, para isso, basta seguir os seguintes passos:
pip3.exe install mysqlclient

Connect
pip install mysql-connector-python==8.0.28

EXECUTAR SCRIPT preparaBancModel.py para poder criar o banco no modelo de uso do site.

ORM SQL ACHEMY
pip install flask-sqlalchemy==2.5.1

Utilizamos uma extensão do Flask chamada Flask-SQLAlchemy, que dá suporte para o ORM SQLAlchemy. A tecnologia do ORM (Object-Relational-Mapper) se faz presente no desenvolvimento de aplicações web independentemente da linguagem utilizada para o desenvolvimento do projeto. O entendimento de seu funcionamento é essencial para um profissional da área.

Para aprender o que é um ORM basta pensar que o conceito de mapeamento relacional do objeto gira em torno da ideia de conseguirmos escrever queries em código SQL por meio do paradigma da orientação a objetos de uma linguagem de programação.

Isso é feito através do mapeamento dos parâmetros de um objeto e sua tradução para a estrutura de tabelas encontradas em um RDBMS (Relational Database, Management System - Sistema de Gerenciamento de Banco de Dados Relacional).

Cada linguagem (ou mesmo framework) que suporta orientação a objetos possui um ORM de utilização mais comum:

.Python e Flask: SQLAlchemy;
.Python e Django: Django ORM;
.Java: Hibernate;
.C#: Dapper ORM;
.PHP: Doctrine;
.NET framework : Microsoft Entity Framework.

Vantagens da utilização de um ORM:
.Possibilita que quem programa construir bancos de dados utilizando sua linguagem de programação de maior fluência, sem ter que se aprofundar nas complexidades do código SQL;
.Torna a aplicação independente do RDBMS utilizado. Isso facilita uma eventual migração de banco de dados, bem como a escrita de queries genéricas que se enquadram nos mais diversos RDBMS (MySQL, PostgreSQL, Microsoft SQL Server, etc);
.A conexão entre a aplicação e o banco de dados se torna robusta, segura e menos sujeita a erros de código, uma vez que poucas intervenções de código são necessárias;
.Alguns ORM como o SQLAlchemy possuem um toolkit completo de ferramentas extras que otimizam a interação com o banco de dados.

Desvantagens da utilização de um ORM:
.A integração de ORMs com sistemas legados pode ser problemática;
.Pode criar a ilusão para desenvolvedores iniciantes que não é necessária uma compreensão básica de linguagem SQL para se tornar um profissional completo de desenvolvimento de aplicações web.

Criar arquivo config.py na raiz com o seguinte codigo:


----------- CONFIG.PY -------------------
SECRET_KEY = 'sua palavra secreta'

SQLALCHEMY_DATABASE_URI = \
 '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
SGBD='mysql+mysqlconnector',
usuario='usuario do banco',
senha='senha do banco',
servidor='endereco do banco',
database='nome da database'
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

----------- END -------------------