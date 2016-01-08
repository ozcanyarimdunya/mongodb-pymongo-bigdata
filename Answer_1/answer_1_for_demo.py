# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

'''
    *---- BU KISIM 10,000 SATIRLIK DEMO DATA İÇİN ----*

    Her bir user için toplam check_in sayılarını bulmak için;

    >> user_id leri mapping yaptık
    >> reduce ile bunların sayısını bulduk
    >> map_reduce fonksiyonu sayesinde bu bulduğumuz verileri
       yeni bir collectiona atadık
'''


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

print "-"*50
print "PLEASE WAIT ...\n"

result = db['mycl'].map_reduce(function_map, function_reduce, 'reduced_user')

print "DONE !"
print "-"*50

"""
# Bu kısım datayı göstermek için
# İsteğe bağlı
for doc in result.find():
    print doc
"""