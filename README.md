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

UPLOAD_PATH = os.path.dirname(os.path.abspath(**file**)) + '/uploads'

----------- END -------------------

flask wtf -> validacao de campos
pip install flask-wtf==1.0.0

O Cross-Site Request Forgery ou CSRF é uma vulnerabilidade na segurança da web que possibilita a um indivíduo mal intencionado se passar por um usuário inocente. Assim, a ameaça pode se disfarçar como o servidor e passar informações através do método POST.

Diferentemente do session token e dos cookies, o CSRF Token não pode ser utilizado por um hacker mal intencionado.

Dessa forma, a existência do CSRF Token é crucial em todo formulário da web, para que o envio de formulários não seja forjado por terceiros.

Criptografia
pip install flask-bcrypt==0.7.1
pip install werkzeug==2.0.0

O Bcrypt é uma ferramenta que utiliza um algoritmo baseado em hashing para garantir a segurança de senhas e dados gerais em aplicações web.

Encryption vs. Hashing
Hashing consiste em transformar um determinado input de dados dado pelo usuário em um hash por meio de uma fórmula matemática. Todo hash consiste em uma série de letras e números de mesmo tamanho, não importando o tamanho do dado fornecido pelo usuário.

O processo de hashing é considerada uma one-way conversation (conversa de uma única via), ou seja, uma vez que um determinado dado passou pelo processo de hashing, se torna impossível desfazê-lo para se encontrar o input original.

Essa característica reduz o risco de vazamento de informações armazenadas em bancos de dados e impõe mais dificuldades a ataques diversos. O hashing pode ser considerado um dos métodos mais eficientes de armazenamento de senhas.

Encryption é outro método de proteção de informações, porém, diferentemente do hashing, se trata de um método two-way conversation (conversa de mão dupla). Isso significa que uma informação que passou pelo processo de encryption pode ser descoberta com a inversão do processo.

Para isso, basta que se tenha um programa específico dedicado à inversão e a encryption key. Apesar de não ser tão seguro para armazenamento de senhas quanto o hashing, a vantagem do encryption é poder ser utilizado de forma mais abrangente em diversas situações, tornando-o mais versátil.

A Cifra Blowfish
O que torna o Bcrypt especial é que, além de usar o método de hashing, seu funcionamento implica a utilização conjunta de hashing e da cifra Blowfish.

Essa cifra é utilizada através da criação de certas keys que fazem parte de um processo de criptografia do próprio hash - a key faz parte do hash. Dessa forma, qualquer tentativa de ataque de força bruta acaba exigindo muito poder de processamento. Seria como trancar algo dentro de um cofre e colocar um cadeado. Contudo, o cadeado se encontra protegido por outro cadeado.

Portanto, o Bcrypt acaba por ser um mecanismo de proteção de senhas comprovadamente eficaz e mais utilizado pelas mais diversas aplicações web do mercado.
