# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

"""
#    *---- BU KISIM 6,5 MİLYON SATIRLIK DEV DATA İÇİN ----*
#
#    Her bir user için toplam check_in sayılarını bulmak için;
#
#    >> user_id leri mapping yaptık
#    >> reduce ile bunların sayısını bulduk
#    >> map_reduce fonksiyonu sayesinde bu bulduğumuz verileri
#       yeni bir collectiona atadık (_id,value)
#    >> bu collectiondan _id ve value ları ekranda gösterdik



#    mongoimport --db newdb --collection newcl --file /home/../Gowalla_totalCheckins.tsv --type tsv --headerline
#    mongodb' ye Gowalla_totalCheckins.tsv dosyasındaki
#    verileri newdb olarak import ettik

"""

# newdb database ne bağlan
db = MongoClient()['newdb']

# mapping user_id
function_map = Code('''
    function(){
        emit(this.user_id,1);
    }
''')

# toplam değeri döndür
function_reduce = Code('''
    function(key,values){
        var total = 0;
        for(var i in values){
        total += values[i];
        };
    return total;
    }
''')

# newcl collectionundan user_id leri ve sayısını reduce_user_all_data collectionuna at
result = db['newcl'].map_reduce(function_map, function_reduce, 'reduced_user_all_data')

print "-"*50+"\n"

"""
# Bu kısım datayı göstermek için
# sort() ile value ları büyükten küçüğe doğru sırala
# limit() ile ilk 100 satırı al
"""
for doc in result.find().sort('value', -1).limit(100):
    print " user_id: %.f\t\t" % (doc['_id']), \
          "toplam check-in: %.f" % (doc['value'])

print "\n"+"-"*50

# collectionu sil
# sürekli üzerine yeni veri yazılmaması için
db['reduced_user_all_data'].drop()
