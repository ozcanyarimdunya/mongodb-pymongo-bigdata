from pymongo import MongoClient
from bson.code import Code


db = MongoClient()['mydb']


function_map = Code('''
    function(){
        emit(this.location_id,1);
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

result = db['mycl'].map_reduce(function_map, function_reduce, 'reduced_location' )
for i in result.find():
    print i

