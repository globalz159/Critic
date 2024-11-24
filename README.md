





ShopNow
Plataforma de e-commerce













NOMES DOS INTEGRANTES DO GRUPO
●	David Silva
●	Hugo Novaes
●	Rafael Araujo Reis de Souza
●	Marcos Vinicius Cerqueira Souto





URL DE ACESSO AO REPOSITÓRIO DE CÓDIGO-FONTE DO GRUPO
●	https://github.com/Rafael-Reis75/shopnow-project
URL DE ACESSO AO QUADRO DE ACOMPANHAMENTO DO PROJETO DO GRUPO
●	https://trello.com/invite/b/66f494cc67d0c8038c38d727/ATTI733e07ee50b33598ca96068e4283e659159BAD9F/shop-now
________________________________________
Sumário
1.	Introdução
2.	Interessados
3.	Objetivos Funcionais
4.	Objetivos Não Funcionais
5.	Diagrama de Casos de Uso
6.	Protótipos de tela
7.	Modelo de Domínio
8.	Diagrama de classes de projeto
9.	Diagrama de sequência de projeto
10.	
11.	Descrição Detalhada dos Casos de Uso Principais
12.	Conclusão
13.	Referências
________________________________________
Lista de Figuras
●	Figura 1: Diagrama de Casos de Uso da Plataforma ShopNow
________________________________________

Lista de Tabelas
●	Tabela 1: Principais Casos de Uso da Plataforma ShopNow
________________________________________


1. Introdução
O projeto ShopNow consiste no desenvolvimento de uma plataforma de e-commerce que visa oferecer aos usuários uma experiência de compra ágil e intuitiva. A plataforma permitirá que os usuários busquem produtos, adicionem ao carrinho, realizem pagamentos e acompanhem suas compras. O foco deste projeto é desenvolver um ambiente seguro e escalável que atenda às necessidades dos consumidores e vendedores.
A plataforma será implementada utilizando tecnologias modernas como React para o frontend, Node.js para o backend, e um banco de dados MySQL para armazenar as informações. Este documento apresenta os objetivos funcionais e não funcionais, diagrama de casos de uso, e a descrição detalhada dos principais casos de uso.
________________________________________
2. Interessados
Os principais interessados no projeto ShopNow incluem:
●	Usuários finais: consumidores que realizarão compras na plataforma.
●	Vendedores: empresas ou indivíduos que venderão produtos através da plataforma.
●	Equipe de Desenvolvimento: responsáveis pela criação e manutenção do sistema.
●	Equipe de Marketing: encarregados de promover a plataforma.
●	Gerentes de Projeto: supervisionam o progresso do desenvolvimento.
●	Equipe de Suporte: oferece assistência aos usuários e vendedores.
________________________________________
3. Objetivos Funcionais
Os objetivos funcionais do sistema ShopNow são:
●	Login e Cadastro: Permitir que os usuários criem contas e façam login de maneira segura.
●	Busca de Produtos: Oferecer um mecanismo de busca que permita aos usuários encontrar produtos por nome, categoria ou preço.
●	Carrinho de Compras: Implementar uma área onde os usuários podem adicionar, remover e revisar produtos antes da compra.
●	Pagamento Online: Integrar a plataforma com gateways de pagamento para que os usuários possam pagar por produtos utilizando diversos métodos (cartão de crédito, boleto, etc.).
●	Acompanhamento de Pedidos: Permitir que os usuários acompanhem o status de suas compras e recebam notificações sobre o envio.
________________________________________



4. Objetivos Não Funcionais
Os objetivos não funcionais incluem:
●	Segurança: Todas as transações e informações dos usuários deverão ser criptografadas.
●	Desempenho: O sistema deve ser capaz de suportar até 1000 usuários simultâneos, mantendo um tempo de resposta de até 2 segundos.
●	Escalabilidade: O sistema deve ser escalável para que novos módulos e funcionalidades possam ser adicionados no futuro.
●	Compatibilidade: A plataforma deve ser responsiva, oferecendo uma experiência otimizada tanto para desktops quanto para dispositivos móveis.
________________________________________
5. Diagrama de Casos de Uso

 
Figura 1: Diagrama de Casos de Uso da Plataforma ShopNow
________________________________________
6. Protótipos de Tela
Os protótipos de tela mostram a interface que os usuários verão e interagirão no sistema. Para uma plataforma de e-commerce como o "ShopNow", os principais protótipos de tela podem incluir:
●	Tela de Login/Cadastro:
○	Campos de entrada para e-mail, senha, e botões para fazer login ou criar uma nova conta.
●	Tela de Busca de Produtos:
○	Barra de pesquisa para buscar produtos por nome ou categoria, lista de produtos filtrados.
●	Tela de Carrinho de Compras:
○	Lista de produtos adicionados ao carrinho, com botões para remover itens ou alterar a quantidade.
●	Tela de Pagamento:
○	Exibição de produtos selecionados, campos para inserir informações de pagamento, e um botão para finalizar a compra.
7. Modelo de Domínio
O modelo de domínio descreve as entidades principais do sistema e suas relações. Para a plataforma "ShopNow", o modelo de domínio pode incluir:
●	Usuário
○	Atributos: ID, Nome, Email, Senha
○	Associações: Usuário tem Carrinho, Pedido
●	Produto
○	Atributos: ID, Nome, Preço, Quantidade em Estoque
○	Associações: Produto está em Carrinho, Produto está em Pedido
●	Carrinho
○	Atributos: ID, Lista de Produtos
○	Associações: Carrinho contém Produtos, Carrinho pertence a Usuário
●	Pedido
○	Atributos: ID, Status, Data de Criação, Total
○	Associações: Pedido contém Produtos, Pedido está associado a Pagamento
●	Pagamento
○	Atributos: ID, Valor, Método de Pagamento, Status
○	Associações: Pagamento está associado a Pedido
8. Diagrama de Classes de Projeto
O diagrama de classes de projeto detalha como o sistema será implementado, mostrando as classes, atributos, métodos e suas interações. Para "ShopNow", o diagrama pode incluir:
●	Usuário
○	Métodos: login(), registrar(), adicionarProdutoAoCarrinho(), finalizarCompra()
●	Produto
○	Métodos: getInformacoesProduto(), atualizarEstoque(), definirPreco()
●	Carrinho
○	Métodos: adicionarProduto(), removerProduto(), calcularTotal()
●	Pedido
○	Métodos: gerarPedido(), atualizarStatus(), calcularTotal()
●	Pagamento
○	Métodos: processarPagamento(), confirmarPagamento()
9. Diagramas de Sequência de Projeto
Os diagramas de sequência de projeto mostram a interação temporal entre as classes do sistema para um caso de uso específico. Os diagramas que poderiam ser criados incluem:
●	Sequência para Login
○	O Usuário envia as credenciais para a classe Sistema, que valida as informações no Banco de Dados e retorna uma resposta.
●	Sequência para Busca de Produtos
○	O Usuário envia uma solicitação de busca à classe Produto, que acessa o Banco de Dados e retorna uma lista de produtos correspondentes.
●	Sequência para Finalizar Compra
○	O Usuário envia um pedido de compra à classe Carrinho, que gera um Pedido e processa o Pagamento através da classe Pagamento.


10. Descrição Detalhada dos Casos de Uso Principais
Caso de Uso 1: Login e Cadastro
●	Ator Principal: Usuário
●	Descrição: O usuário acessa a página inicial do site e pode se cadastrar como um novo cliente ou fazer login caso já tenha uma conta.
●	Fluxo Principal:
1.	O usuário acessa a página de login.
2.	O sistema exibe o formulário de login/cadastro.
3.	O usuário insere suas informações de login (e-mail e senha) ou se cadastra preenchendo um formulário.
4.	O sistema valida as informações e concede acesso à plataforma.
Caso de Uso 2: Busca de Produtos
●	Ator Principal: Usuário
●	Descrição: O usuário pesquisa por produtos utilizando palavras-chave ou categorias.
●	Fluxo Principal:
1.	O usuário insere o nome do produto ou categoria na barra de busca.
2.	O sistema retorna os produtos que correspondem à pesquisa.
3.	O usuário visualiza a lista de produtos e pode acessar as informações detalhadas de cada um.
Caso de Uso 3: Pagamento
●	Ator Principal: Usuário
●	Descrição: O usuário realiza o pagamento dos produtos adicionados ao carrinho utilizando métodos de pagamento disponíveis.
●	Fluxo Principal:
1.	O usuário finaliza a compra no carrinho.
2.	O sistema redireciona o usuário para a página de pagamento.
3.	O usuário seleciona o método de pagamento (cartão de crédito, boleto, etc.).
4.	O sistema processa o pagamento e confirma a compra.
________________________________________
Wireframes
                                          

                                   

11. Conclusão
O projeto ShopNow é uma solução de e-commerce robusta, projetada para oferecer uma experiência de compra eficiente e segura aos usuários. A arquitetura modular da plataforma permite sua escalabilidade e a fácil integração de novas funcionalidades no futuro. Com a implementação dos objetivos funcionais e não funcionais definidos, espera-se que a plataforma atenda às necessidades tanto dos consumidores quanto dos vendedores, tornando-se uma ferramenta essencial no ambiente de comércio eletrônico.
________________________________________
12. Referências
●	Sommerville, Ian. Software Engineering. Pearson, 2016.
●	Gamma, Erich, et al. Design Patterns: Elements of Reusable Object-Oriented Software. Addison-Wesley, 1994.
