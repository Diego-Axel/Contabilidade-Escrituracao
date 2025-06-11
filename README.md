# Sistema de Escrituração Contábil Simples

Um sistema web simples para realizar a escrituração contábil básica, permitindo o registro de lançamentos e a visualização de relatórios essenciais como Livro Diário, Livro Razão, Razonetes e Balanço Patrimonial.

## Visão Geral

Este projeto é uma ferramenta educacional e prática para demonstrar os fundamentos da escrituração contábil. A interface do usuário permite adicionar lançamentos de débito e crédito que são processados e exibidos em tempo real em diferentes seções contábeis. O sistema foi desenvolvido utilizando apenas HTML, CSS e JavaScript, sem a necessidade de frameworks ou bibliotecas externas.

## Funcionalidades

O sistema oferece as seguintes funcionalidades implementadas:

* **Formulário de Lançamentos**: Um formulário intuitivo para adicionar novos registros contábeis, incluindo data, conta, descrição, valor e o tipo de lançamento (Débito ou Crédito).
* **Livro Diário**: Exibe todos os lançamentos em ordem cronológica, detalhando cada transação.
* **Livro Razão**: Agrupa os lançamentos por conta, mostrando o histórico de movimentações e o saldo final de cada uma.
* **Razonetes (T-accounts)**: Apresenta uma visualização em formato de "T" para cada conta, separando os débitos e os créditos e exibindo o saldo.
* **Balanço Patrimonial**: Gera um balanço simplificado, separando e somando os totais de Ativo e Passivo + Patrimônio Líquido.
* **Navegação por Abas**: Interface organizada com abas para facilitar a navegação entre os diferentes relatórios contábeis.

## Como Utilizar

1.  Abra o arquivo `index.html` em seu navegador de preferência.
2.  Utilize o formulário no topo da página para inserir os dados do lançamento contábil:
    * **Data**: A data em que a transação ocorreu.
    * **Conta**: O nome da conta que está sendo movimentada (ex: Caixa, Fornecedores).
    * **Descrição**: Um breve texto sobre o lançamento.
    * **Valor**: O montante financeiro da transação.
    * **Tipo**: Selecione se o lançamento é um **DÉBITO** ou um **CRÉDITO**.
3.  Clique em "Adicionar Lançamento" para registrar a entrada.
4.  Navegue pelas abas "Livro Diário", "Livro Razão", "Razonetes" e "Balanço Patrimonial" para visualizar os resultados atualizados.

## Tecnologias Utilizadas

* **HTML5**: Estrutura principal da aplicação.
* **CSS3**: Estilização da interface, incluindo o layout do formulário, tabelas e abas.
* **JavaScript (ES6)**: Responsável por toda a lógica da aplicação, como manipulação de dados, renderização dos relatórios e interatividade da página.
