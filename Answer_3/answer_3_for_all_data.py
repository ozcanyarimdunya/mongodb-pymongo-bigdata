# coding=utf-8
from pymongo import MongoClient
from bson.code import Code

db = MongoClient()['newdb']

'''
    Bir user_id nin bütün location_id lerini bul
    Bu location_id lerde check-in yapmış user_id leri bul ve sayılarını karşılaştır
    En büyük sayıyı user_id ve toplam check-in i ile birlikte yaz
'''


user_entered = []
print "-"*75
user_id =input('user_id yi giriniz: ')

result = db['newcl']

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
counter = 0
for res in result.find({'user_id': user_id}).sort('location_id', -1):
    counter += 1
    db['temp'].insert({'user_id:': res['user_id'], 'location_id': res['location_id']})

temp = db['temp'].map_reduce(f_map_temp, f_reduce_temp, "temp")
for temp_d in temp.find():
    user_entered.append(temp_d['_id'])


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

new_result = db['ss'].map_reduce(function_map, function_reduce, "out_ss")
print "\n"
print "-"*75
print "\tBİLGİ: - %.f - id'li user toplam - %.f - checkin yapmıştır \t"%(user_id, counter)
print "-"*75
print "\n"
for i in new_result.find().limit(100):
    print "location_id: %.f de\t" % i['_id']['location_id'], \
          "check-in yapan user: %.f\t" % i['_id']['user_id'],\
          "toplam check-in: %.f" % i['value']

print "\n"
print "-"*75
print "BİLGİ: - %.f - id'li user toplam - %.f - checkin yapmıştır "%(user_id, counter)
print "-"*75

db['ss'].drop()
db['out_ss'].drop()
db['temp'].drop()
user_entered = []