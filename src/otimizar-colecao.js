/**
* Otimização da coleção: 
* - conversão do valor string para ISODate da data de criação do tweet
*/
db.saude_coletiva.find().forEach(function(doc){
    //save the time string in Unix time.
    doc.time_stamp = new Date(Date.parse(doc.created_at));

    //save our modifications
    db.saude_coletiva.save(doc);
});

// Comando para executar o código deste arquivo diretamente no shell do MongoDB
// load("/Users/francisco/dev/github-repositories/pos-graduacao/social-media-analysis-git/src/02-otimizar-colecao.js")