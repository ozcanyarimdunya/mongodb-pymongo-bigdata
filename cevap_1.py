from pymongo import MongoClient
from bson.code import Code


db = MongoClient()['mydb']

function_map = Code('''
    function(){
        emit(this.user_id,1);
    }
''')
function_reduce = Code('''
    function(key,values){
        var total = 0;
        for(var i in values){
        total += values[i];
        };
    return total;
    }
''')

result = db['mycl'].map_reduce(function_map, function_reduce, 'reduced_user')
for doc in result.find():
    print doc