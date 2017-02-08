#!/bin/bash
#
# Este script deverá ser executado no diretório src.
#

# Ingestão dos tweets no formato JSON para o banco de dados MongoDB
cd ../data

for file_name in $(ls -d tweets.saude.coletiva-*)
do
    mongoimport -d tweets_raw -c saude_coletiva --file $file_name
    mv $file_name "proc-$file_name"
done
