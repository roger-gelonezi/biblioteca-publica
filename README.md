# Biblioteca Pública

Este é um projeto Open Source desenvolvido pelos alunos da UNIVESP com o objetivo de criar uma plataforma online para disponibilizar o acervo de uma biblioteca pública. A ideia é facilitar o acesso dos associados a livros, artigos e outros materiais de forma prática e conveniente.

## Sobre o Projeto

A Biblioteca Pública visa proporcionar uma experiência amigável e eficiente para os usuários, permitindo que eles:

- Pesquisem e encontrem obras disponíveis no acervo.
- Visualizem detalhes sobre cada obra, como autor, resumo e disponibilidade.
- Realizem empréstimos e reservas diretamente pela plataforma.
- Acessem materiais digitais, quando disponíveis.

## Funcionalidades

- **Cadastro Facilitado:** Os metadados das obras terão cadastro facilitado através de integração com o Google Books API.
- **Pesquisa Avançada:** Os usuários podem buscar por título, autor, categoria e outros critérios.
- **Detalhes das Obras:** Cada obra possui uma página com informações detalhadas.
- **Empréstimos e Reservas:** Os associados podem verificar disponibilidade, solicitar empréstimos e realizar reservas online.
- **Notificações:** Receba alertas sobre datas de devolução e disponibilidade de obras.

## Tecnologias Utilizadas

- **Frontend:** Python e Django
- **Backend:** Python e Django
- **Banco de Dados:** MySQL
- **Autenticação:** JWT (JSON Web Tokens)
- **Publicação Web:** Amazon Web Services EC2
- **Repositório de Imagens:** Amazon Web Services S3
- **Publicação de Banco de Dados:** Amazon Web Services RDS

## Executando o Projeto

Para completo aproveitamento do projeto é necessário conhecimento prévio em Docker, Docker Compose, Python, Django e MySQL.

### Variáveis de Ambiente

O primeiro passo é criar um arquivo de nome .env na raiz do projeto, configurando as seguintes variáveis de ambiente

| Variável                | Possíveis Valores                                   |
|-------------------------|-----------------------------------------------------|
| SECRET_KEY              | "s3cr3tK3y123"                                      |
| DEBUG                   | boolean                                             |
| ALLOWED_HOSTS           | "*, localhost, bibliotecapublica.online"            |
| AWS_ACCESS_KEY_ID       | string                                              |
| AWS_SECRET_ACCESS_KEY   | string                                              |
| AWS_STORAGE_BUCKET_NAME | string                                              |
| AWS_S3_REGION_NAME      | string                                              |
| MYSQL_DATABASE          | "bibliotecapublica"                                 |
| MYSQL_USER              | "admin"                                             |
| MYSQL_PORT              | "3306"                                              |
| MYSQL_HOST              | "localhost" / "mysql"                               |
| MYSQL_PASSWORD          | "2s6GZzk%wmY7qs!JzTxu"                              |

Nota: É possível configurar o repositório de arquivos estáticos e mídias apenas na AWS S3. Futuramente será implementado opções de repositórios na pasta do projeto ou via MinIO.

### Docker Compose

Agora escolha o ambiente que deseja erguer na pasta docker compose. Para o primeiro contato recomendamos o ambiente de testes em docker-compose-atdd.yml.

### Execução via Python

Este projeto utiliza o Python 3.12.16 e você pode executá-lo seguindo as boas práticas do framework Django através da pasta ./src.

## Autores

### Adailton Pereira de Brito

---

### Anthony Camilo Costa

---

### Leandro Rebelatto

[![GitHub Badge](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=GitHub&logoColor=white)](https://github.com/leandro2206)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/leandro-roberto-r-24389852/)

---

### Leonardo Silva

[![GitHub Badge](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=GitHub&logoColor=white)](https://github.com/leonardo16silva12)
[![Linkedin Badge](https://img.shields.io/badge/-Leonardo-blue?style=flat-square&logo=Linkedin&logoColor=white)](<https://www.linkedin.com/in/leonardo16silva12/>)

---

### Márcio Diniz Pinto

---

### Mauro Leão

[![GitHub Badge](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=GitHub&logoColor=white)](https://github.com/Mauroleao)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/mauro-s%C3%A9rgio-bouwman-le%C3%A3o-b62b41260/)
[![Gmail Badge](https://img.shields.io/badge/-bouwmanleao@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white)](mailto:bouwmanleao@gmail.com)

---

### Rodrigo Pasquarella

[![GitHub Badge](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=GitHub&logoColor=white)](https://github.com/rodrigopasquarella)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/rodrigo-pasquarella-134127201/)

---

### Roger Gelonezi

[![GitHub Badge](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=GitHub&logoColor=white)](https://github.com/roger-gelonezi)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/rogeriogelonezi/)
[![Gmail Badge](https://img.shields.io/badge/-rogeriogelonezi@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white)](mailto:rogeriogelonezi@gmail.com)

## UNIVESP - Universidade Virtual do Estado de São Paulo

### Turma DRP05-PJI240-SALA-003GRUPO-010
