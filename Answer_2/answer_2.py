# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

#connect to database
db = MongoClient()['mydb']

#mapping func. emitting all location_ids
function_map = Code('''
    function(){
        emit(this.location_id,1);
    }
''')

#reducing func. return total value of the user_ids
function_reduce = Code('''
    function(key,values){
        var total = 0;
        for(var i in values){
        total += values[i];
        };
    return total;
    }
''')

#mycl is the collection which we are going to reduced
#save the data in reduced_location collection after map reducing
result = db['mycl'].map_reduce(function_map, function_reduce, 'reduced_location' )

"""
#This part is for printing the reduced_location collection
for doc in result.find():
    print doc
"""

