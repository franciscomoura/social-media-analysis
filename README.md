# Social Media data Analysis - Análise de dados de média social

Practical work on collecting data from twitter, text-processing and some term frequencies analysis.

Autor: Francisco M. Moura

Github: [Social Media Analysis](https://github.com/franciscomoura/social-media-analysis)

Gitbook: [Análise de dados da rede social Twitter](https://www.gitbook.com/book/franciscomoura/analise-de-dados-da-rede-social-twitter/details) 



## Conteúdo do repositório
* data/

    Contém arquivos formato JSON com todos os tweets coletados e utilizados na elaboração da análise.
    
* doc/
    
    O documento PDF do artigo sobre o desenvolvimento do trabalho, uso dados e reproduço em seu ambiente.

* src/

    Contém código-fonte utilizado para produzir as análise e resultados.
   
    - src/crawler_tweets_saude_publica.py: coleta twewts na Streaming API do Twitter. 
    - sr/twitter_credentials.py: armazena as credenciais de acesso à API do Twitter.
    - src/mongoimport.sh: importa os dados em formato json para o banco MongoDB
    - src/otimizar-colecao.js: converte data string em ISODate e cria atributo auxiliar na coleção
    - src/criar-indices.js:cria os índices necessários
    - src/termos-mais-frequentes.js: contabiliza a ocorrência de cada termo no conjunto de dados
    - src/termos_frequencia.py: contabiliza a ocorrência de termos parametrizados no conjunto de dados.
