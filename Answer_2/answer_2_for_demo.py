# coding=utf-8
from pymongo import MongoClient
from bson.code import Code


'''
    *---- BU KISIM 10,000 SATIRLIK DEMO DATA İÇİN ----*

    Toplam location_id bulmak için;

    >> location_id leri mapping yaptık
    >> reduce ile bunların sayısını bulduk
    >> map_reduce fonksiyonu sayesinde bu bulduğumuz verileri
       yeni bir collectiona atadık
'''


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

result = db['mycl'].map_reduce(function_map, function_reduce, 'reduced_location')

print "-"*50+"\n"

"""
# Bu kısım datayı göstermek için
"""
for doc in result.find().sort('value',-1):
    print " location_id: %.f "%(doc['_id']), \
          "\ttoplam check-in: %.f" % (doc['value'])

print "\n"+"-"*50

