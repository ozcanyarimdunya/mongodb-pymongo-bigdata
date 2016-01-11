# coding=utf-8
from pymongo import MongoClient
from bson.code import Code


'''
    *---- BU KISIM 6,5 MİLYON SATIRLIK DEV DATA İÇİN ----*

    Toplam location_id bulmak için;

    >> location_id leri mapping yaptık
    >> reduce ile bunların sayısını bulduk
    >> map_reduce fonksiyonu sayesinde bu bulduğumuz verileri
       yeni bir collectiona atadık
    >> bu collectiondan _id ve value ları ekranda gösterdik
'''

# newdb ye bağlan
db = MongoClient()['newdb']

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

result = db['newcl'].map_reduce(function_map, function_reduce, 'reduced_location_all_data')

print "-"*50+"\n"

"""
# Bu kısım datayı göstermek için
"""
for doc in result.find().sort('value', -1).limit(100):
    print " location_id: %.f " % (doc['_id']), \
          "\ttoplam check-in: %.f" % (doc['value'])

print "\n"+"-"*50

db['reduced_location_all_data'].drop()