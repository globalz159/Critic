gitflow
gustavo guanabara
deschamps


GIT e GIT HUB ESSENCIAL PARA O DESENVOLVEDOR

## Iniciar repositório
>> git init            - inicia um novo repositório
>> git clone <link>    - Clona um repositório do git

## .gitignore  -> Arquivos que serão ignorados no controle de versão (não subirão para o git hub)

- é um arquivo criado com o nome '.gitignore'
- é composto por linhas com o nome/path de arquivos que serão ignorados pelo git

> Arquivos ignorados:
>> nome_arquivo.py

> diretórios ignorados:
>> **nome_diretorio


# Estágios dos Arquivos

- ***Untracked***: Arquivos NOVOS que não estão sendo controlados pelo git
- ***Unstaged***: Arquivos recém alterados que estão diferentes do último commit
- ***Staged***: Arquivos alterados que estão prontos para o commit (ja passaram pelo comando 'git add')
- ***Commited***: Snapshot de como o Projeto está alterado na branch, pronto para o push

## Hash ID

- Número de identificação para os commits
- Pode ser substituído por HEAD para indicar o ultimo commit feito


# Comandos de consulta

* **git status** - mostra os arquivos que estão diferente do ultimo commit

* **git log** < param> - Mostra historico de commits

>	- *Parâmetros*:

	< -10 >   		     	- Mostra os ultimos 10 commits
	< --oneline >          	- Mostra um resumo dos commits
	< --before="data" >    	- Mostra apenas commits feitos antes da data especificada         ex. data = '2020-02-20'
	< --after="data" >     	- Mostra apenas commits feitos depois da data especificada        ex. data = '2020-02-20'
	< --since="periodo" >  	- Mostra commits desde o periodo especificado                     ex. periodo = '2 days ago' 
	< --author="Fernando" >	- Mostra commits de uma pessoa específica
	
	
	- git help log: Mostra ajuda para utilização do comando log

* **git diff** < param> - Mostra diferenças entre o ultimo commit e o que está no parametro

>	- Parâmetros:
	
	< hash_id >             - Diferença entre ultimo commit e comid especificado pela hash_id
	< has_id..hash_id >     - Diferença entre 2 commits, sendo o primeiro mais antigo
	< --staged >            - O que está em staged e o ultimo commit


# Branches
### Criar uma branch
```$ git checkout -b nome_branch```    - cria e entra na branch
```$ git branch nome_branch```         - apenas cria

- branch master             -> é o ramo principal do projeto
- base                      -> é o ponto em que foi criada a branch a partir do ramo principal 

* **git branch** < param> - sem parâmetros mostra as branches existentes

>	- Parâmetros:
	
	< nome_branch >       - cria branch com o nome especificado
	< -d nome_branch >    - deleta branch
	< -D nome_branch >    - deleta branch sem se preocupar com segurança

Ainda em branch... **Merge**
### Merge
- serve para juntar conteúdo de uma branch na outra o pull é um tipo de merge
- é o momento que ocorre os conflitos

* **git merge** < param>     

>	- Parâmetros:
	
	< nome_branch >      - junta conteúdo da branch especificada na branch atual


* **git rebase** < param>     

>	- Parâmetros:
	
	< origin/branch >    - ajusta base com a branch especificada 
	< --continue >       - para continuar o rebase após corrigir o conflito
	< --skip >           - para parar o processo de rebase

# Commits

* **git add** < param> - adiciona arquivos modificados para a área de stage
	
>	- Parâmetros:

	< . >                - Adiciona todos o contúdo editado para a área de stage
	< path_arquivo >     - Adicona arquivos especificados para a área de stage

    * O path é o mesmo que aparece no git status

* **git commit** < param> - Cria commit para arquivos que estão em stage

>	- Parâmetros:

	< --amend >             - Adiciona conteúdo junto ao ultimo commit, usado para editar mensagens
	< -m "mensagem" > 	- Cria commit com uma mensagem

* **git restore** < param> - Serve para reverter operações

>	- Parâmetros:           

	< nome_arquivo >        - Descarta arquivos que estão em unstage (mesma forma que git checkout na area unstaged) 
    < --staged arquivo >    - Retorna arquivo em Stage para área Unstaged

* **git reset** < params> - Que nem o restore, serve para desfazer algumas alterações

>	- Parâmetros:

	< HEAD --hard >         - Apaga todo conteúdo que não está commitado
	< HEAD^ --hard >        - Apaga ultimo commit deixando o penultimo como HEAD
	< --hard hash_id >      - Apaga commits mais novos do que o commit de hash_id especificado
	< --soft hash_id >      - Coloca todo conteúdo de commits feitos antes do hash_id especificado para a área de Stage



# Alguns comandos:

	$ git fetch                        - atualiza o HEAD do repositório atual
	$ git pull origin                  - atualiza branch atual com conteúdo da branch que está depois do origin
	$ git checkout -b                  - checkout sem o '-b' muda de branch, com o '-b' cria uma branch e muda para ela
	$ git stash                        - adiciona arquivos com mudanças em uma pilha para serem reutilizados
	$ git mv <nome_arq> <novo_nome>    - renomear arquivo
	$ git rm <nome_arq>                - deletar arquivo
	$ git branch                       - mostra branches existentes e qual está selecionada


