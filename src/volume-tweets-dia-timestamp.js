// volume por dia: atributo time_stamp
db.saude_coletiva.aggregate([
    {
        $group: {
            _id: {
                time_stamp: {
                    ano: {$year: "$time_stamp"},
                    mes: {$month: "$time_stamp"},
                    dia: {$dayOfMonth: "$time_stamp"}
                }
            },
            qtde: {$sum: 1}            
        }
    },
    {$sort: {_id: 1}}
])
