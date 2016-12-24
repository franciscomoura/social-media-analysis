// termos mais frequentes
db.tweet_terms.aggregate([
        { $group: { _id: "$termo", qtde: {$sum: 1 } } },
        { $sort: {qtde: -1}}
    ],
    {
        allowDiskUse:true,
        cursor:{}
    }
)
