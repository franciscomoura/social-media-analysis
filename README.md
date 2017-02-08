# Social Media data Analysis - Análise de dados de mídia social

*Practical work on collecting data from twitter, text-processing and some term frequencies analysis*.

Autor: Francisco M. Moura

Github: [Social Media Analysis](https://github.com/franciscomoura/social-media-analysis)

Gitbook: [Análise de dados da rede social Twitter](https://www.gitbook.com/book/franciscomoura/analise-de-dados-da-rede-social-twitter/details) 

E-mail: franciscomoura@gmail.com



## Conteúdo do repositório
Os diretórios são utilizados para organizar o contéudo no ambiente do projeto.
A seguir, é especificado cada diretório e seu objetivo.

- **data/**
Contém os arquivos, no formato JSON, com todos os tweets coletados e utilizados na elaboração da análise.
    
- **doc/**
Documento contendo narrativa sobre o desenvolvimento do trabalho e uso dos dados.
Pode ser utilizado como guia para reprodução da análise em seu ambiente.

- **src/**
Contém o código-fonte utilizado para produzir as análise e resultados.
Foram utilizadas as linguagens de programação `Python`, `JavaScript` e `Bash` para produzir os artefatos necessários para realizar a computação dos dados.
    - ***crawler\_tweets\_saude\_publica.py***: coleta twewts na Streaming API do Twitter. 
    - ***twitter\_credentials.py***: armazena as credenciais de acesso à API do Twitter.
    - ***mongoimport.sh***: importa os dados em formato json para o banco MongoDB.
    - ***otimizar-colecao.js***: converte data string em ISODate e cria atributo auxiliar na coleção.
    - ***criar-indices.js***: cria os índices necessários.
    - ***termos-mais-frequentes.js***: contabiliza a ocorrência de cada termo no conjunto de dados.
    - ***termos_frequencia.py***: contabiliza a ocorrência de termos parametrizados no conjunto de dados.
    - ***volume-tweets-dia-created_at.js***: informação da quantidade de tweets coletados por dia, usando data string.
    - ***volume-tweets-dia-timestamp.js***: informação da quantidade de tweets coletados por dia, usando data ISODate.
    - ***volume-tweets-hora-dia-timestamp.js***: informação da quantidade de tweets coletados por hora do dia 
