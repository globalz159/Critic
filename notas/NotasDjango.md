# Curso Framework Django

- arquitetura cliente-servidor

# protocolo http :
 documentação na "RFC 7540" fornecida pela IETF 

 Hyper Text Transfer Protocol  ==  Protocolo de Transferência de HiperTexto

 porta http: porta 80      -> dados não criptografados
 porta https: porta 443    -> dados criptografados

> Ações do protocolo
 > Get              - buscar recursos
 > Post             - criar um novo recurso
 > Put / Patch      - atualizar um recurso
 > Delete           - deletar um recurso



#   Front-End      /    Back-End
   - telas           - banco de dados
   - client view     - comunica-se com front-end
   - html,css...     - segurança
   - arquitetura     - python,java,C
   - estático        - dinâmico

- Aplicações Web: Aplicações que rodam no navegador

- Linguagem Dinâmica:
   - processada no servidor
   - back-end
- Linguagem Estática:
   - processada no navegador
   - front-end


# PYTHON SERVER HTTP

- Servidor incorporado no python 3
- Iniciar server na porta 8000:
   - entrar com o terminal na pasta do html e rodar:
   $ python3 -m http.server 8000


# INICIAR NOVO PROJETO

1- # Criar um ambiente virtual(venv) na pasta do projeto

2- # Instala o Django no venv:  $ pip install django

3- # Adiciona requirements.txt:  $ pip freeze > requirements.txt

4- # No terminal inicializar projeto:
$ django-admin startproject nome_projeto .
                 ou
$ django-admin startproject nome_projeto  

OBS:
  Inicializar com '.' > cria o projeto e o arquivo manager.py na pasta atual
  
  Sem o '.' ->  cria uma pasta com o nome do projeto que tem o arquivo manager e outra pasta com o nome do projeto


# Estrutura de arquivos do projeto Django:
- Para rodar o projeto deve digitar o comando
$ python manage.py startserver
- Depois acessar o localhost na porta 8000 :  localhost:8000/
- Para terminar a execução do servidor, digitar Ctrl + C no terminal que estiver sendo executado

> manage.py
 - Arquivo main que roda a aplicação

> settings.py
 - Debug True   -> para desenvolvimento
 - Debug False  -> produção (deve especificar ALLOWED_HOSTS)
 - Declara caminho dos templates
 - Declara as aplicações existentes

-> urls.py
 - Mapear rotas para views
 - Arquivo onde preparamos as rotas para as views
 - podemos importar as views de 2 formas:

# Importando Views

1- Importando as funções(views) do arquivo Views de determinada aplicação
- adiciona a view na lista urlpatterns
- sintaxe = path('caminho_na_url', view) 

exemplo mapeando rota para view:

from core.views import index, cadastro

urlpatterns = [
  path('', index)
}


! O RECOMENDADO É CRIAR UM ARQUIVO 'urls.py' EM CADA APLICAÇÃO E USAR O INCLUDE (próximo item)!
2- Importando o arquivo urls da aplicação e usando o *include na lista 'urlpatterns'
 - Include deve ser importado da biblioteca django.urls junto com path

from django.urls import path, include

urlpatterns = [
  path('', include('core.urls'))
]



# Aplicações:   -> São como módulos no Odoo

> Criar nova aplicação:
$ django-admin startapp nome_aplicação

- Um projeto possui várias aplicações
- As aplicações criadas devem ser declaradas no arquivo settings na variável INSTALLED_APPS

# Estrutura da aplicação:
________
> Views
- São declaradas como funções
- recebem request como parametro
- retorna a função render(request, 'nome_arquivo.html')
- index é a view principal

exemplo definição de view:

def index(request):
    return render(request, 'index.html')

# Contexto
- views podem ter um contexto para passar parâmetros do python para o html
- o contexto é um dicionario definido na função
- é passado como parâmetro na função render

exemplo de view com contexto:

def index(request):
    contexto = {'mensagem': 'Essa é uma mensagem no contexto'}
    return render(request, 'index.html', contexto)

_________
> Templates
- São os arquivos HTML
- Os templates devem ter o mesmo nome das views, assim ja carrega automaticamente com a view
- Normalmente é criado um diretório 'templates' em cada aplicação
- Adiciona os arquivos .html nesse diretório templates

- Contextos podem ser utilizados no html usando {{chave_do_contexto}}
exemplo:
<h1>{{item_do_contexto}}</h1>


________
> Models
- models.py é o arquivo onde são definidos os modelos de dados
- Os modelos são definidos por classes que herdam do models.Model
- Os atributos são declarados como variáveis models.TipodeDado()
exemplo de modelo:

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=5)

# Migrations
- após criar ou alterar models deve realizar as migrations para essas models
- as migrations a serem feitas são alertadas na execução do servidor
- para realizar as migrations deve rodar os comandos
$ python manage.py makemigrations      -> para adicionar as migrations no diretório migrations
$ python manage.py migrate             -> para executar as migrations






