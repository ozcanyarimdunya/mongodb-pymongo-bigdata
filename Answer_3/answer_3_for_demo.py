# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

db = MongoClient()['mydb']

"""
                *-- AMAÇ --*

    Bir user_id nin bütün location_id lerini bul
    Bu location_id lerde check-in yapmış user_id leri bul ve sayılarını karşılaştır
    En büyük sayıyı user_id ve toplam check-in i ile birlikte yaz
"""

print "\n", "*"*75
user_id =input('user_id yi giriniz: ')

# mycl collectionun üzerinden arama yap --> ana collection : mycl
result = db['mycl']

f_map_temp = Code('''
    function(){
        emit(this.location_id,{count:1});
        }
''')

f_reduce_temp = Code('''
    function(key,values){
        var total = 0;
        values.forEach(
            function(v){
                total += v['count']
            });
        return total;}
''')

# (isteğe bağlı) kullanıcının kaç tane check-in yaptığını hesaplamak için
counter = 0

# kullanıcının check-in yaptığı tüm yerleri bulduk
# temp adında yeni bir collectiona user_id si ile birlikte ekledik
for res in result.find({'user_id': user_id}).sort('location_id', -1):
    counter += 1
    db['temp'].insert({'user_id:': res['user_id'], 'location_id': res['location_id']})

"""
# kullanıcının bu yerlerin herbirinde toplamda
# kaç check-in yaptığını bulduk
# kullanıcı farklı zamanlarda aynı yerde check-in yapmışsa eğer
# map_reduce işlemi ile aynı yerlerin sayısını bul
# burda amaç temp collectionunda farklı object_id ile bulunan
# aynı location_id leri tek satırda toplayıp bir diziye atmak
"""
temp = db['temp'].map_reduce(f_map_temp, f_reduce_temp, "temp_t")

# bütün location_id leri diziye ekledik
user_entered = []
for temp_d in temp.find():
    user_entered.append(temp_d['_id'])

# dizide bulunan location_id lere göre arama yaparak
# bu yerlerde checkin yapmış bütün kullanıcıları
# ss adında yeni bir collectionuna ekle
for loc in user_entered:
    for res in result.find({'location_id': loc}):
        db['ss'].insert({'user_id': res['user_id'],
                          'location_id': res['location_id']
                         })

function_map = Code('''
    function(){

        emit({location_id: this.location_id, user_id: this.user_id},1);
    }
''')

function_reduce = Code('''
    function(key,values){
        var total = 0;
        for(var i in values){
            total += 1;
        };
    return total;
    }
''')

"""
# ss collectionunda girdiğimiz kullanıcının check-in yaptığı her bir yerde
# check-in yapmış bütün kullanıcılar bulunmakta
# bir kullanıcı aynı yerde birkaç defa check-in yaptığı için
# bunların toplam sayısını bulmamız gerekiyor
# map_reduce ile bunun sayısını bulduk
# yani 5 idli kullanıcı 10 idli yerde 3 check-in yapıştır gibi
# ve en sonunda bunları ekrana yazdırdık
# ancak bunların sayıları arasında karşılaştırma yapıp
# en çok check-in yapanı bulamadım :(
"""
new_result = db['ss'].map_reduce(function_map, function_reduce, "out_ss")

print "\n"
print "-"*75
print "\tBİLGİ: - %.f - id'li user toplam - %.f - checkin yapmıştır \t"%(user_id, counter),\
    "\n\n\tbu yerlerde bütün kullanıcılar toplam - %.f - checkin yapmıştır\t"%(new_result.count())
print "-"*75
print "\n"
for i in new_result.find():
    print "location_id: %.f da\t" % i['_id']['location_id'], \
          "check-in yapan user: %.f\t" % i['_id']['user_id'],\
          "\ttoplam check-in: %.f" % i['value']

print "\n"


# en sonda dbleri sil ve diziyi temizle
db['ss'].drop()
db['out_ss'].drop()
db['temp'].drop()
db['temp_t'].drop()
user_entered = []