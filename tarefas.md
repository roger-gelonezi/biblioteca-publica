# Tarefas pendentes

## Melhorias na documentação

### Preencher todos autores no ReadME.md

Inserir dados atualizados do GitHub, LinkedIn, Gmail e RA da UNIVESP daqueles que ainda não possuem estes dados.

### Referenciar o Trello no ReadME.md

Inserir um bloco que leve ao painel público do nosso Trello.

## Melhorias na página inicial

### Inserir informações da biblioteca Malatrasi no cabeçalho

Analisar a melhor forma de informar o usuário de que ele está navegando no acervo da biblioteca Malatrasi.

Futuramente esta informação será carregada dinamicamente de acordo com a biblioteca ativa, mas neste momento manteremos chumbado a Malatrasi.

### Implementar paginação da lista de livros

Os livros deverão ser carregados dinamicamente para o usuário.

Em um cenário ideal, os livros serão carregados conforme rolagem, sei que é uma feature de fácil implementação em React.

Caso não seja possível carregar via rolagem da lista, criaremos então uma paginação estática de 10 em 10.

### Implementar navegação por categorias

Através de um menu lateral no estilo de "gaveta", deve ser possível aplicar filtro por categoria.

### Implementar o campo de busca de livros

Esta busca deverá executar procura nos campos a seguir "title", "authors" e "isbns".

## Novas páginas

### Criar página para adicionar/editar livros

Uma página que possibilite ao usuário adicionar um novo livro ou editar os dados de um livro existente.

### Criar uma página que de Sobre

Adicionar informações do projeto, para quem ele é destinado, informações de contato, etc.

### Criar página de cadastro de usuário

Possibilitar o cadastro de usuários.

Neste momento todos usuários deverão passar por aprovação de um administrador para ter seu usuário ativado, pois a única Role existente é de Bibliotecário.

### Criar página de login

### Implementar recuperação de senhas via e-mail

## Refatoração de funcionalidade html

### Melhorar a página de importação de livros

Permitir enviar apenas um código de barra por vez.

Imediatamente após o envio, informar sucesso ou falha na importação. Informar o título do livro importado na mensagem de sucesso.

### Escanear o código de barras através da câmera do celular

Permitir a abertura da câmera do celular do usuário e escaneamento do código de barras.

### Escanear o código de barras através de foto enviada

Permitir ao usuário realizar o upload de uma foto para escaneamento do código de barras.

## Refatoração de Código

### Criar campo com link para download do livro

Adicionar campo para download do livro de nome "download_link".

Nós não hospedaremos o arquivo, este link deve ser um download direto.

### Tratar imagem antes do upload

Quando feito o upload da imagem da capa de livro, o arquivo deve ser tratado para ter 

- max-width de 200px.
- max-heith de 300px.
- max-size de 200kb.

### Replanejar a camada google_books_service.py

Extrair esta classe para uma camada de serviços, deixar mais robusto seu funcionamento e dividir melhor as competências de cada método.

## Fonte de arquivos

### Implementar repositório arquivos estáticos local

### Implementar chaveamento para arquivos estáticos MinIO

## Pesquisar novos serviços de metadados de livros

## Implementar camada de Testes de Unidade
