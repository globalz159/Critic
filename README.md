# Prat-Analise-de-Sistemas

# Especificação de requisitos
## PROJETO: Aplicativo para Recomendação de Filmes, Séries e Livros
### Curso de Sistemas de Informação
### Prática Profissional em ADS
### Turmas 05K 
### 1º semestre de 2021


# Introdução

Este é um documento de especificação de requisitos para um novo aplicativo para recomendação de filmes, séries e livros.A promoção do engajamento de colaboradores é fundamental para o desenvolvimento de bons trabalhos no mundo corporativo. Nesta linha, empresas buscam formas de criar situações de compartilhamento de experiências para que as pessoas envolvidas se conheçam e promovam sinergia entre as pessoas, de modo a promover maior desempenho em grupos multidisciplinares, também conhecidos por Squads.Considerando que os serviços de streaming nunca estiveram tão em alta graças à pandemia do coronavírus, bem como, escolher entre milhares de filmes, séries ou livros disponíveis pode ser uma tarefa um tanto quanto estressante. Sendo assim, nossa empresa, optou por criar um aplicativo de recomendação para Filmes, Séries e Livros, capaz de permitir acesso e participação dos nossoscolaboradores, de modo a prover interação com contribuições na forma de dicas e recomendações sobre filmes, séries e livros

Este documento descreve os requisitos não-funcionais, modela os requisitos funcionais com casos de uso e modela os conceitos do domínio do problema.

# Informações sobre a empresa

A Empresa Solar Systems vende equipamentos para a geração de energia de formas alternativas e identificou tendências que causarão um aumento significativo na demanda por seus produtos.

Devido à natureza técnica e inovadora de seus produtos, a empresa possui vendedores capazes de orientar os clientes no processo de escolher um sistema de energia alternativa. A empresa possui também funcionários que têm a função de gerente do produto. O gerente do produto é um especialista em um determinado produto ou em uma determinada linha de produtos. Ele produz os *whitepapers*, documentos altamente técnicos e focados nas especificações dos produtos.


# Escopo do projeto

O escopo deste projeto é um sistema web que dá suporte à venda de produtos da empresa diretamente aos clientes, bem como à rede de vendedores. A publicidade de produtos, o controle de estoque e a cobrança não são parte deste projeto.

A engine de pesquisa web será adquirida como um componente pronto para o novo sistema. Os detalhes internos desta engine não fazem parte deste projeto. Questões de segurança do site, além da proteção por senha no próprio site, também não são parte do projeto.

> Observação do professor: neste exemplo, deixei como parte do projeto somente a proteção por senha, assumindo que as demais questões de segurança serão tratadas pela equipe de operações. No caso do projeto do seu grupo, será necessário tratar destes outros aspectos de segurança.

# Interessados

Aqueles que irão se beneficiar diretamente e aqueles que serão afetados pelo novo sistema:

* Clientes: Conseguirão navegar pelo site para encontrar e fazer pedidos de produtos. Poderão escolher entre pedir diretamente da empresa ou através de um vendedor.

* Vendedores: Conseguirão navegar pelo site e obter informações atualizadas, precisas e detalhadas dos produtos. Serão informados de clientes em potencial e conseguirão se comunicar com o gerente do produto.

* Gerentes do produto: Conseguirão atualizar diretamente as informações de seus produtos.

* Serviço de Atendimento ao Consumidor (SAC): O sistema reduzirá a carga de trabalho no SAC, pois os clientes conseguirão encontrar de forma mais fácil as informações que necessitam.

* Departamento de Marketing:: Os dados de navegação no site poderiam ser enviados para o departamento de marketing. Entendendo como um cliente usa o site ao fazer um pedido, o departamento poderá propor e implementar melhorias para manter os clientes.

* Departamento de Contabilidade: As informações dos pedidos serão enviadas diretamente para a contabilidade, permitindo uma cobrança mais ágil e eficiente.

* Departamento de Logística: As informações dos pedidos serão enviadas diretamente para o departamento de logística, que dará baixa no estoque e providenciará o envio do produto.

* Departamento de Tecnologia da Informação: Será responsável pela implementação da nova base de dados, hospedagem da aplicação web e manutenção do sistema.


# Objetivos funcionais

1. O sistema permitirá que os usuários façam alterações em seus cadastros.

   Para os clientes, isto eliminará a demora atual entre a sua decisão de comprar e a realização do pedido.

   Isto também reduzirá o tempo que o vendedor gasta para elaborar um pedido.

2. O cadastro do usuário deverá conter: nome completo, username, senha que usará para acessar o sistema, data de nascimento, cidade e estado.

   Isto reduzirá a quantidade de acessos a informações desatualizadas.

   Isto eliminará a atualização da informação em diversos documentos.

3. O sistema deve permitir que o usuário possa excluir o seu cadastro pessoal.

   Isto reduzirá o tempo para um funcionário encontrar e entrar em contato com o gerente de um determinado produto.

4. O sistema permitirá que cada membro possa avaliar filmes, séries e livro que desejar.

   Isto reduzirá o tempo para o cliente enviar uma requisição e receber uma resposta.

5. O cadastro de um livro deverá conter: título, autor(es), editora, país, ano de lançamento.

   Isto melhorará o atendimento ao cliente reduzindo problemas relacionados à cobrança.

6. O cadastro de um filme deverá conter: título, diretor, elenco principal, país, ano.

   Isto permitirá maior agilidade no processamento dos pedidos e na atualização do estoque.

7. O sistema deverá permitir que sejam realizadas pesquisas em todo o texto das páginas web a que o usuário tem acesso. O sistema deverá permitir as seguintes pesquisas:
   * pesquisar todas as palavras
   * pesquisar qualquer uma das palavras
   * pesquisar a frase exata

8. O cadastro de uma série deverá conter: título, diretor, elenco principal, país, ano, número de temporadas

   Isto permitirá que os clientes encontrem sozinhos as informações, reduzindo o custo de suporte ao cliente.

9. O sistema permitirá o acesso dos usuários através do login e senha.

    Isto reduzirá o tempo de visita do usuário, pois ele não precisará fornecer novamente dados que ele já entrou em uma visita anterior.

10. O sistema deve permitir a realização de adicionar comentários às avaliações feitas pelo outro, desde que tenham relacionamento de amizade.

   Esta informação permitirá que o marketing determine qual informação disparou a compra e ajudará a abordar clientes em potencial de forma mais efetiva.

11. O sistema deve permitir que o usuário possa “reagir” a avaliação do usuário através de um emoticon “joinha”.

   Isto melhorará o serviço ao cliente e reduzirá o número de chamadas ao suporte por clientes estrangeiros.
   
12. O sistema deve permitir que o usuário que reagiu a avaliação de outro usuário, possa retirar o “joinha” dado.

   Esta informação permitirá que o marketing determine qual informação disparou a compra e ajudará a abordar clientes em potencial de forma mais efetiva.

13. O sistema deve permitir que um usuário possa pedir relacionamento de amizade a outro usuário

   Isto melhorará o serviço ao cliente e reduzirá o número de chamadas ao suporte por clientes estrangeiros.
   
14. O sistema deve mostrar os amigos em comum, quando um usuário visita a página de outro.

   Esta informação permitirá que o marketing determine qual informação disparou a compra e ajudará a abordar clientes em potencial de forma mais efetiva.

15. O sistema deve sugerir amizades de usuários para o outro usuário

   Isto melhorará o serviço ao cliente e reduzirá o número de chamadas ao suporte por clientes estrangeiros.

# Objetivos não-funcionais

a. O sistema deverá estar completamente operacional pelo menos 99.99% do tempo.

b. O tempo fora do ar após uma falha não deverá exceder 0.5 hora.

c. O vendedor deverá ser capaz de utilizar o sistema em seu trabalho após um treinamento de 2 dias.

d. Um usuário que já sabe qual produto lhe interessa deve ser capaz de localizar e ver a página do produto em 20 segundos.

e. O número de páginas web pelas quais o usuário precisa navegar para acessar a informação do produto a partir da página principal não deve ser maior do que 2.

f. O sistema deverá ser capaz de suportar 1000 usuários simultâneos.

g. O tempo médio para visualizar uma página web em uma conexão de 1Mbps não deverá exceder 5 segundos.

h. O tempo médio para baixar e visualizar um *whitepaper* em uma conexão de 1Mbps não deverá exceder 10 segundos.

i. O sistema deverá oferecer acesso protegido por senha para páginas web que são acessadas somente por funcionários.

j. Os dados de transação devem ser transmitidos de forma criptografada.

k. O sistema deverá ser capaz de acomodar novos produtos e novas linhas de produto sem necessidade de alterações na sua implementação.

l. O site web do sistema deverá ser visível nos navegadores Mozilla Firefox (versão $\ge$ 75.0.0), Google Chrome (versão $\ge$ 81.0.0) e Microsoft Edge (versão $\ge$ 5.0.0).

m. O sistema deverá disponibilizar uma página web que explica como navegar pelo site. A página deverá ser customizada com base nas páginas que o usuário pode acessar. Esta página de ajuda deverá ser acessível a partir de todas as outras páginas.

o. O sistema deverá ter interface com

* Uma base de dados relacional para informações dos produtos e dos pedidos.
* O sistema atual de contabilidade da empresa.
* O sistema atual do departamento de logística.
* O tradutor (a ser adquirido).
* A engine de pesquisa (a ser adquirida).


# COTS (Commercial Off-The-Shelf)

Os softwares que serão adquiridos para compor o sistema são:

* Tradutor do português para o inglês e do português para o espanhol.

* Engine de pesquisa.


# Casos de uso


## Diagrama de casos de uso


> (em elaboração)
## Descrições dos casos de uso

1.3.1	CSU01 – Fazer Registro

Identificador	CSU01
Nome	Fazer registro
Atores	Membro
Sumário	Qualquer pessoa da empresa pode se registrar nesta rede social.
No momento do registro, o usuário deverá fornecer os seguintes dados: nome completo, username que deseja utilizar, senha que usará para acessar o sistema, data de nascimento, cidade e estado.
Complexidade	Médio
Regras de Negócio	N/D
Pré-condições	N/D
Pós-condição	É registrado no sistema o cadastro do membro
Pontos de Inclusão	Atualizar os dados do seu perfil.
Pontos de Extensão	N/D

Fluxo Principal
Ações do Ator	                                          Ações do Sistema
1. O Membro informa os dados pessoais e a senha 	
	                                                      2. O Sistema verifica se os dados e senha são válidos ( Verifica se os dados e senha pertencem a uma conta)
	                                                      3. O Sistema registra o membro. Caso de Uso é encerrado

Fluxo de Exceção 1: 3a. O Sistema não valida o membro
Ações do Ator	                                          Ações do Sistema
	                                                      1. O Sistema recusa os dados e senha do membro e exibe uma mensagem
	                                                      2. Volta ao passo 1 do Fluxo Principal.

1.3.1	CSU02 – Fazer Cadastro

Identificador	CSU02
Nome	Fazer cadastro
Atores	Membro
Sumário	Qualquer membro da rede social pode fazer o cadastro de filmes, séries e/ou livros.
Complexidade	Médio
Regras de Negócio	N/D
Pré-condições	Ser registrado na rede social
Pós-condição	N/D
Pontos de Inclusão	N/D
Pontos de Extensão	Cadastrar Filme
Cadastrar Séries
Cadastrar Livros

Fluxo Principal
Ações do Ator	                                       Ações do Sistema
1. O Membro escolhe a opção de cadastramento	
	                                                   2. O Sistema abre a página para o cadastramento
3. O membro fornece os dados específicos	
	                                                   4. O Sistema registra o cadastramento. Caso de Uso é encerrado

Fluxo Principal
Ações do Ator	                                      Ações do Sistema
1. O Membro escolhe a opção de cadastrar “Livros”	
	                                                  2. O Sistema abre a página para o cadastramento
3. O membro fornece os dados: título, autor(es), editora, país, ano de lançamento.	
	                                                  4. O Sistema registra o cadastramento. Caso de Uso é encerrado

Fluxo Principal
Ações do Ator	                                       Ações do Sistema
1. O Membro escolhe a opção de cadastrar “Filmes”	
	                                                   2. O Sistema abre a página para o cadastramento
3. O membro fornece os dados: título, diretor, elenco principal, país, ano.	
	                                                   4. O Sistema registra o cadastramento. Caso de Uso é encerrado

Fluxo Principal
Ações do Ator	                                       Ações do Sistema
1. O Membro escolhe a opção de cadastrar “Séries”	
	                                                    2. O Sistema abre a página para o cadastramento
3. O membro fornece os dados: título, diretor,
 elenco principal, país, ano, número de temporadas.	
                                                      4. O Sistema registra o cadastramento. Caso de Uso é encerrado

1.3.1	CSU03 – Fazer Avaliação

Identificador	CSU03
Nome	Fazer avaliação
Atores	Membro
Sumário	Cada membro poderá avaliar os filmes, séries e livros que desejar.
Complexidade	Médio
Regras de Negócio	N/D
Pré-condições	Para entrar uma avaliação, o membro seleciona o tipo de item (livro, filme ou série), busca pelo nome do item, atribui uma nota de 0 a 10 (somente valores inteiros) e escreve os comentários que julgar relevantes (com limite de 1024 caracteres).
Pós-condição	N/D
Pontos de Inclusão	N/D
Pontos de Extensão	Fazer Validação

Fluxo Principal
Ações do Ator	                                 Ações do Sistema
1. O Membro escolhe a opção de avaliação	
	                                             2. O sistema abre a página de validação
3. Seleciona o tipo de item(Livro, filme ou série)	
4. Busca pelo nome do item	
5. Atribui uma nota de 0 a 10	
6. Escreve os comentários que julgar relevantes	
	                                             7. O sistema registra a avaliação. O caso de uso é encerrado.

Fluxo Principal
Ações do Ator	                                 Ações do Sistema
1. O administrador verifica o cadastramento 	
	                                             2. O Sistema abre a página do cadastramento
3. Valida o cadastramento	
	                                             4. O Sistema faz a validação. Caso de uso é encerrado


Fluxo Principal
Ações do Ator                                  	Ações do Sistema
1. O administrador verifica o cadastramento 	
	                                             2. O Sistema abre a página do cadastramento
	                                             3. O sistema verifica que o item já existe 
4. Indica item	
5. Vincula a avaliação ao item já existente.	
	                                             6. O Sistema faz a validação. Caso de uso é encerrado


# Wireframes

> (em elaboração)

# Diagrama de classes de domínio

> (em elaboração)
