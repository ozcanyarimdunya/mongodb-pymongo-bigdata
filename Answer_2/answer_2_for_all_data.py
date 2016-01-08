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
'''


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

print "-"*50
print "PLEASE WAIT ...\n"

result = db['newcl'].map_reduce(function_map, function_reduce, 'reduced_location_all_data')

print "DONE !"
print "-"*50+"\n"

"""
# Bu kısım datayı göstermek için
# İsteğe bağlı
for doc in result.find():
    print doc
"""

"""
# Bu kısımda en çok check-in yapılan yeri
# ve check-in yapan user_id yi bulduk
# İsteğe bağlı

g = {}

for res in results.find():
    g.__setitem__(res['_id'], res['value'])

maximum = max(g, key=g.get)
print 'location_id :', maximum, '\ttotal_check_in :', g[maximum]

"""

