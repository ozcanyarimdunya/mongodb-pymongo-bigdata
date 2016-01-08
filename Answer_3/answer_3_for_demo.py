# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

# connect to database
db = MongoClient()['mydb']

# mapping func. emitting all user_ids
function_map = Code('''
    function(){
        emit(this.location_id,1);
    }
''')

# reducing func. return total value of the user_ids
function_reduce = Code('''
    function(key,values){
        var total = 0;
        for(var i in values){
        total += values[i];
        };
    return total;
    }
''')

# mycl is the collection which we are going to reduced
# save the data in reduced_user collection after map reducing
results = db['mycl'].map_reduce(function_map, function_reduce, 'max_check-in')

g = {}

# This part is for printing the reduced_user collection
for res in results.find().sort('value', -1):
    g.__setitem__(res['_id'], res['value'])

# en fazla check-in nerede yapılmış
maximum = max(g, key=g.get)
print 'location_id :', maximum, '\ttotal_check_in :', g[maximum]
