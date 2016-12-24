// Criação de índices
db.saude_coletiva.createIndex({time_stamp: 1})
db.saude_coletiva.createIndex({created_at: "text"})
db.tweet_terms.createIndex({termo: 1})
