###Big Data Project

Bu projede elimizde bulunan veri dosyasında yaklaşık 6 milyon satırlık veri bulunmaktadır. (user_id,location_id ...)

------------------------------------------------------------------------

Burada bulmaya çalıştığımız bilgiler

    Bütün kullanıcılar herbirinin toplam kaç check-in yaptığı                                  (1)

    Bütün yerlerde toplam kaç tane check-in yapıldığı                                          (2)

    Bir kullanıcının check-in yaptığı bütün yerlerde en çok check-in yapan kişileri bulmak     (3)

İşlemlerin daha hızlı gerçekleşmesi için büyük dosyadan aldığımız demo dosya **Data_Demo** klasöründe *demo.tsv* olarak bulunmakta

Answer_1 klasöründe (1) şartı için yazılmış kodlar bulunmaktadır

Answer_2 klasöründe (2) şartı için yazılmış kodlar bulunmaktadır

**Data_Output klasöründe**

(1) şartı için export edilen tsv dosyaları ( **reduced_user_for_demo.tsv** ve **reduced_user_for_all_data.tsv** ) bulunmakta

(2) şartı için export edilen tsv dosyaları ( **reduced_location_for_demo.tsv** ve **reduced_location_for_all_data.tsv** ) bulunmakta

------------------------------------------------------------------------


##### Data aşağıdaki tablodaki gibidir

**Headerline** tabloda gösterildiği gibi  **ilk satırda** yer almaktadır

-----------------------------------------------------------------------------------------


user_id | check_in_time 	|   latitude	|  longitude	 |location_id
--------|-----------------------|---------------|----------------|-----------
0	| 2010-10-19T23:55:27Z	| 30.2359091167	| -97.7951395833 |22847
0	| 2010-10-18T22:17:43Z	| 30.2691029532	| -97.7493953705 |420315
.       |   .                   |.              |   .            |.
.       |   .                   |.              |   .            |.
.       |   .                   |.              |   .            |.



-----------------------------------------------------------------------------------------


>**NOT**

>-*- Önce Gowalla_totalCheckins.txt dosyası Gowalla_totalCheckins.tsv dosyasına dönüştürülmeli*

>-*- Bu sayede mongodb ye import edilebilir*

>-*- Gowalla_totalCheckins.tsv den aldığım 10000 satırlık bir kesiti demo.tsv olarak kaydettim*

-----------------------------------------------------------------------------------------

#####demo.tsv dosyasını mongodb ye import etmek için **terminali** açın ve aşağıdakileri yazın;
	*mongoimport -d your_db_name -c your_collection_name --file /your_tsv_file_path/demo.tsv --type tsv --headerline

-----------------------------------------------------------------------------------------

#####İmport işlemi tamamladığında yeni bir terminal açıp aşağıdakileri yazın;
	xx@xx:~$ mongo 					//mongo shell açılacaktır
	> use your_db_name
	> db.your_collection_name.find().pretty()       //pretty datayı daha düzenli gösteriyor

-----------------------------------------------------------------------------------------

#####Yukarıdaki işlemlerden sonra karşınızda şöyle bir satır örneği olmalıdır

	{
		"_id" : ObjectId("568bf2b0e792b7459fea01f9"),
		"user_id" : 0,
		"check_in_time" : "2010-10-19T23:55:27Z",
		"latitude" : 30.2359091167,
		"longitude" : -97.7951395833,
		"location_id" : 22847
	}


-----------------------------------------------------------------------------------------


#####answer_1_for_demo ve answer_2_for_demo kodlarının çalıştırılmasından sonra databasemizde iki collection olacaktır. Bunlar;
    1- reduced_user
    2- reduced_location

-----------------------------------------------------------------------------------------

#####Bu dataları export etmek (dışarı çıkarmak) için terminali açın ve aşağıdakileri yazın;

    mongoexport -d your_db_name -c reduced_user     --out /choose_a_path/reduced_user.tsv
    mongoexport -d your_db_name -c reduced_location --out /choose_a_path/reduced_location.tsv

-----------------------------------------------------------------------------------------

###Ve artık datanız hazır !

-----------------------------------------------------------------------------------------

#####   reduced_user_for_demo.tsv dosyası
    { "_id" : 0, "value" : 225 }
    { "_id" : 1, "value" : 12 }
    { "_id" : 2, "value" : 2100 }
    { "_id" : 4, "value" : 225 }
    { "_id" : 5, "value" : 50 }
    { "_id" : 7, "value" : 75 }
    { "_id" : 8, "value" : 25 }
    { "_id" : 9, "value" : 150 }
    { "_id" : 10, "value" : 100 }

-----------------------------------------------------------------------------------------


#####   reduced_location_for_demo.tsv dosyası
    { "_id" : 8904, "value" : 1 }
    { "_id" : 8938, "value" : 1 }
    { "_id" : 8947, "value" : 1 }
    { "_id" : 8964, "value" : 1 }
    { "_id" : 8977, "value" : 5 }
    { "_id" : 8994, "value" : 1 }
    { "_id" : 9002, "value" : 2 }
    { "_id" : 9063, "value" : 3 }
    { "_id" : 9064, "value" : 1 }
    { "_id" : 9071, "value" : 1 }


-----------------------------------------------------------------------------------------



#####Kullanılan araçlar

Ubuntu 14.04 LTS

Pycharm Community Edition 5.0.3

Mongodb

#####@ozcaan11 tarafında geliştirilen bir proje olarak duruyor şuan :)