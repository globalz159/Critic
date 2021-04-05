# Anotações Framework Django

- arquitetura cliente-servidor

## protocolo http :
 documentação na "RFC 7540" fornecida pela IETF 

 Hyper Text Transfer Protocol  ==  Protocolo de Transferência de HiperTexto

 porta http: porta 80      -> dados não criptografados
 porta https: porta 443    -> dados criptografados

> Ações do protocolo
 > Get              - buscar recursos
 > Post             - criar um novo recurso
 > Put / Patch      - atualizar um recurso
 > Delete           - deletar um recurso



##   Front-End      /    Back-End
- #### Front-End
  - telas
  - client view
  - html,css...
  - arquitetura
  - estático

- #### Back-End
  - banco de dados
  - comunica-se com front-end
  - segurança
  - python,java,C
  - dinâmico
<br><br>

- **Aplicações Web**: Aplicações que rodam no navegador
<br>

- **Linguagem Dinâmica**:
   - processada no servidor
   - back-end
- **Linguagem Estática**:
   - processada no navegador
   - front-end


### PYTHON SERVER HTTP

- Servidor incorporado no python 3
- Iniciar server na porta 8000:
   - entrar com o terminal na pasta do html e rodar:
   $ python3 -m http.server 8000


## INICIAR NOVO PROJETO

1. Criar um ambiente virtual(venv) na pasta do projeto

2. Instala o Django no venv: `$ pip install django`

3. Adiciona requirements.txt: `$ pip freeze > requirements.txt`

4. No terminal inicializar projeto:
`$ django-admin startproject nome_projeto .`
   ou        
`$ django-admin startproject nome_projeto`

OBS:
>Inicializar com '.' > cria o projeto e o arquivo manager.py na pasta atual
  
>Sem o '.' ->  cria uma pasta com o nome do projeto que tem o arquivo manager e outra pasta com o nome do projeto


## Rodar a aplicação 
- Para rodar o projeto deve rodar o comando
`$ python manage.py startserver`
- Depois acessar o localhost na porta 8000 :  localhost:8000/
- Para terminar a execução do servidor, digitar Ctrl + C no terminal que estiver sendo executado


## Estrutura de arquivos do projeto Django:

> manage.py
 - Arquivo main que roda a aplicação
   `$ python manage.py --options`
Alguns usos:
`$ python manage.py runserver` - Rodar a aplicação
`$ python manage.py makemigrations` - Criar as migrations
`$ python manage.py migrate` - Executar as migrations
`$ python manage.py shell` - Rodar o shell

> settings.py
 - Debug True   -> para desenvolvimento
 - Debug False  -> produção (deve especificar ALLOWED_HOSTS)
 - Declara caminho dos templates
 - Declara as aplicações existentes
 - Especifíca banco de dados

> urls.py
 - Mapear rotas para views
 - Arquivo onde preparamos as rotas para as views
 - Deve ter um arquivo urls.py na pasta do projeto e um na pasta de cada aplicação. 
 - importamos as views de 2 formas:
   1. Importando as funções da aplicação
   2. Importando o arquivo urls.py das aplicações

 ##### Mapeando rotas das  Views

1. Importando as Views(funções) declaradas no arquivo Views da aplicação
**Utiliza esse método no urls.py das aplicações*
   - importa as views do arquivo views
   - adiciona a view na lista urlpatterns usando a função path
   - `path('extensão_da_url', nome_da_view)` 

exemplo mapeando rota para view:

    from django.urls import path
    from .views import index, cadastro

    urlpatterns = [
        path('', index)
        path('cadastro', cadastro)
    }


2. Importando o arquivo urls da aplicação e usando o *include na lista 'urlpatterns'
**Utiliza esse método no arquivo urls.py da pasta do projeto*
   - Include deve ser importado da biblioteca django.urls junto com path

exemplo mapeando urls:

    from django.urls import path, include

    urlpatterns = [
        path('core', include('core.urls'))
    ]


## Aplicações:   
**São como módulos no Odoo*

- Criar nova aplicação
`$ django-admin startapp nome_aplicação`

- Um projeto possui várias aplicações
- As aplicações criadas devem ser declaradas no arquivo settings.py na variável INSTALLED_APPS
- O Django ja vem com algumas aplicações padrão
      
      INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',

          'core',  # <- aplicação criada
      ]


## Estrutura das aplicações:
> views
> urls
> models
> templates
> admin
> tests
### Views
- São declaradas como funções no arquivo views.py
- recebem request como parametro
- retorna a função render(request, 'nome_arquivo.html')
- definir index como a view principal

exemplo definição da view 'index':

    def index(request):
        return render(request, 'index.html')
***Contexto das views***
- views podem ter um contexto para passar parâmetros do python para o html
- o contexto é um dicionario definido na função
- é passado como parâmetro na função render

exemplo de view com contexto:

    def index(request):
        contexto = {'mensagem': 'Essa é uma mensagem no contexto'}
        return render(request, 'index.html', contexto)

_________
### Templates
- São os arquivos HTML
- Os templates devem ter o mesmo nome das views, assim ja carrega automaticamente com a view
- Normalmente é criado um diretório 'templates' em cada aplicação
- Adiciona os arquivos .html nesse diretório templates

- Contextos podem ser utilizados no html usando {{chave_do_contexto}}

exemplo:

    <h1>Bem vindo, {{user_name}}</h1>
*será renderizado como:*
## Bem vindo, Fulano
<br>

________

### Models
- models.py é o arquivo onde são definidos os modelos de dados
- Os modelos são definidos por classes que herdam do models.Model
  - cada classe é um model
- Os atributos são declarados como variáveis models.TipoDeDado(*parametros)

exemplo do model 'Produto':

    class Produto(models.Model):
        nome = models.CharField("Nome", max_length=100)
        preco = models.DecimalField("Preço", decimal_places=2, max_digits=5)

***Migrations:***
- após criar ou alterar models deve realizar as migrations para essas models
- as migrations são como controle de arquivos do git
- as migrations a serem feitas são alertadas na execução do servidor
- para realizar as migrations deve rodar os comandos

       $ python manage.py makemigrations   -> para adicionar as migrations no diretório migrations
       $ python manage.py migrate          -> para executar as migrations

__________

### Admin
- Podemos acessar a área administrativa do Django adicionando `/admin` na url
- Deve criar uma conta superuser para acessar a área administrativa

      $ python manage.py createsuperuser

- Para os Models aparecerem na área administrativa devem ser importados no arquivo admin.py da aplicação
- No arquivo admin.py deve adicionar as models da seguinte maneira:

      from django.contrib import admin

      from .models import Nome_model1, Nome_model2

      admin.site.register(Nome_model1)
      admin.site.register(Nome_model2)


***Vizualização Admin***

- Acessaando a página de administração podemos controlar modelos de dados, grupos e usuários.

- A vizualização da tabela dos models pode ser editada usando classes que herdam do `admin.ModelAdmin` da seguinte forma:

      
      from django.contrib import admin

      from .models import Filme, Livro, Serie

      class FilmeAdmin(admin.ModelAdmin):
          list_display = ('titulo', 'diretor', ano_lancamento)

      admin.site.register(Filme, FilmeAdmin)
      admin.site.register(Livro)
      admin.site.register(Serie)

______

# Sessão 2 - Programação com Banco de Dados

------
## Banco de dados
* Django usa por padrão o banco de dados sqlite
* Os bancos de dados são especificados no arquivo settings.py

### Manage Shell

* Abre o terminal python com as propriedades do Django
* Rodar o manage.py passando o parâmetro shell:
`$ python manage.py shell`
* O shell é uma boa forma para descobrir funcionalidades usando a função dir()
* Bom para encontrar erros e tirar dúvidas

##### Função dir()
* A função dir recebe um objeto como parâmetro e retorna uma lista de atributos/funções que podem ser acessadas a partir desse objeto
* Pode ser passado Strings, Funções, Objetos, qualquer tipo de dado
Exemplo:
`>>> from core.views import index`
`>>> print(dir(index))`


## Tabelas BD

### Instanciando Objetos

* Um objeto é instanciado da mesma forma que no python
* Dada a classe 'Cliente':

      class Cliente(models.Model):
          nome = models.CharField("Nome", max_length=100)
          sobrenome = models.CharField("Sobrenome", max_length=100)
          email = models.EmailField("Email")
   
* Para criar um Objeto e adicionar ao banco de dados deve instanciar a classe Python :

      new_cliente = Cliente(nome="Fernando", sobrenome="Saeta", email="fernando@gmail.com")


### Consulta na tabela

* A consulta ocorre utilizando o atributo objects da classe: `Filme.objects`
* Podemos obter todos os objetos na tabela utilizando `objects.all()`
* Para fazer selects podemos utilizar o `objects.filter` ou o `objects.get`

exemplos:

    from .models import Filme

    # Todos os Objetos
    todos_filmes = Filme.objects.all()

    # Filme de ID = 1
    filme_1 = Filme.objects.filter(id=1)

    # Filmes do Tarantino
    filme_tarantino = Filme.objects.filter(diretor='Quentin Tarantino')

    # Filmes de 2016
    filmes_2016 = Filme.objects.get(ano_lancamento=2016) # <- consulta com get lança erro se não encontrar nenhum objeto





