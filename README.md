# Acoes-Afirmativas
Projeto Integrador - IFSC

## Desenvolvimento em andamento

## Tabela de conteúdos
- Título
- Status
- Conteúdo
- Descrição
- Layout
- Pré-Requisitos
- Dependências e Libs Instaladas
- Como rodar a aplicação no seu PC
- Databases
- Solução de problemas
- Contribuintes
- Tarefas em aberto

## Descrição
Através de um trabalho que está sendo desenvolvido pela Professora Renata Pimenta sobre Ações Afirmativas concluímos a importância de ter uma base centralizada que possa disponibilizar as principais informações sobre Ações Afirmativas para a comunidade, que muitas vezes não compreende o que são essas Ações e nem que informações são necessárias para se enquadrar em um desses projetos. Esses projetos possuem o objetivo de equalizar a nossa sociedade, tentando dessa forma diminuir as desigualdades e possibilitando as mesmas oportunidades. Dessa forma desenvolvemos o nosso Projeto Integrador com o auxílio do nosso Cordenador Rômulo Beninca para unir as principais Ações afirmativas do Campus Gaspar e suas informações em um único site.


## Layoult
- Página principal
- Listagem de projetos em destaque 
- Seção de Sobre nós
- Tela sobre Ações afirmativas
- Listagem dos projetos cadastrados
- Tela de detalhes do projeto
- Tela de pesquisa
- Tela de cadastro
- Tela de login
- Tela de logout


## Pré-Requisitos
- Python 3.9.4
- Django 3.2.7
- Mysql 4.1.6 
- VSCode para edição dos códigos
- Trello para a organização
- Discord para as reunões
- Google meet para reuniões com o Coordenador do projeto



## Como rodar a aplicação no seu PC
- É necessário fazer a intalação do Python(https://www.python.org/downloads/) e do Git(https://desktop.github.com/).
- No seu terminal local você vai criar seu ambiente virtual e ativa-lo através dos seguintes comandos na ordem descrita:
  -> python -m venv (nome do seu ambiente virtual)
  -> cd (nome do ambiente virtual)
  -> Scripts/activate
  
- É necessário fazer o clone do projeto no GitHub (https://github.com/MMedeiros03/Acoes-Afirmativas). Apos acessar o link anterior do repositório do nosso grupo, clique em "clone" e copie o caminho HTTPS.                                     
- Faça o comando git "GIT CLONE" e adicione o caminho HTTPS copiado anteriormente.

- Depois de clonar o repositório por padrão o git vai estar na BRANCH "MAIN". 
                                  
- Após o ambiente virtual estar ativado, você deve fazer o download de todas a bibliotecas co projeto através do comando "pip install -r requirements.txt".
                                                                                                                                           
- Execute o comando ""python manage.py makemigratios" .

- Em seguida "python manage.py migrate" para aplicar os comandos realizados. 

- Depois de de concluir deve-se executar "python mange.py runserver"

- Com o servidor rodando, pode acessar o nosso projeto pelo seguinte link: http://127.0.0.1:8000/

## Databases

- Utilizamos o XAMPP que possui diversos servidores, mas no nosso caso utilizamos o Banco de dados MySQL

## Solução de problemas
Caso encontre algum problema em nossa aplicação ou queira conversar com os nossos colaboradores, fique a vontade para entrar em contato conosco através dos seguintes contatos:

    - amandarafaela1415@gmail.com / (47) 9 8418-9821
    - matheusmedeiros2003@gmail.com / (47) 9 9606-5225
    - davideschamps444@gmail.com / (47) 9 9248-2422
    - thiago.ads@aluno.ifsc.edu.br / (47) 9 9211-7473
    - joao.vep@aluno.ifsc.edu.br / (47) 9 8454-7116


## Contribuintes

    -Amanda Rafaela Eduardo:Responsável pela parte de documentação e conteúdo do site
    -Thiago Alves dos Santos:Desenvolvimento Front-end
    -Matheus Medeiros Oselame: Desenvolvimento Back-end
    -Davi Deschamps:Desenvolvimento Front-end
    -João Victor Pacheco:Desenvolvimento Front-end


## Tarefas em aberto
    -Página para suporte onde teria um espaço para o usuário escrever suas dúvidas ou os problemas que encontrou e seria disparado automaticamente para o e-mail dos administradores.

    -Filtro para encontrar projetos específicos.

    -A possibilidade de deixar comentários abaixo de cada projeto para que o site fique mais interativo.









