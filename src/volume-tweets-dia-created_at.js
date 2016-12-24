// volume por dia: atributo created_at, sem índice
db.saude_coletiva.aggregate([
    {
        $match: {
            $or: [
                {"created_at" : {$in : [/Nov/]}},
                {"created_at" : {$in : [/Dec/]}}
            ]
        }
    },
    {
        $group: {
            _id: {
                ano : { $substr : ["$created_at", 26, 4 ] },   
                mes : { $substr : ["$created_at", 4, 3 ] },                                      
                dia : { $substr : ["$created_at", 8, 2 ] }
            },
            total: { $sum: 1 }
        }
    },
    {
        $sort: {_id: -1}
    }
])
