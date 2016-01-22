###Big Data Project

Bu projede elimizde bulunan veri dosyasında yaklaşık 6 milyon satırlık veri *Gowalla_totalCheckins.txt* bulunmaktadır.

------------------------------------------------------------------------

##### *Gowalla_totalCheckins.txt* aşağıdaki tablodaki gibidir

**Headerline** tabloda gösterildiği gibi  **ilk satırda** yer almaktadır (Normalde yoktu db'ye aktarmak için biz ekledik)

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

> - Gowalla_totalCheckins.txt den aldığım 10,000 satırlık bir kesiti demo.txt olarak kaydettim

> - demo.txt dosyasını .tsv uzantılı olarak kaydettim. Bu sayede mongodb ye import edilebilir

-----------------------------------------------------------------------------------------

#####demo.tsv dosyasını mongodb ye import etmek için **terminali** açın ve aşağıdakileri yazın;
	mongoimport -d your_db_name -c your_collection_name --file /your_tsv_file_path/demo.tsv --type tsv --headerline


İmport işlemi tamamladığında yeni bir terminal açıp aşağıdakileri yazın;
	xx@xx:~$ mongo 					//mongo shell açılacaktır
	> use your_db_name
	> db.your_collection_name.find().pretty()       //pretty datayı daha düzenli gösteriyor


Yukarıdaki işlemlerden sonra karşınızda şöyle bir satır örneği olmalıdır

	{
		"_id" : ObjectId("568bf2b0e792b7459fea01f9"),
		"user_id" : 0,
		"check_in_time" : "2010-10-19T23:55:27Z",
		"latitude" : 30.2359091167,
		"longitude" : -97.7951395833,
		"location_id" : 22847
	}


-----------------------------------------------------------------------------------------

#####Burada bulmaya çalıştığımız bilgiler

    Bütün kullanıcılar herbirinin toplam kaç check-in yaptığı                                  (1)

    Bütün yerlerde toplam kaç tane check-in yapıldığı                                          (2)

    Bir kullanıcının check-in yaptığı bütün yerlerde en çok check-in yapan kişileri bulmak     (3)

İşlemlerin daha hızlı gerçekleşmesi için büyük dosyadan aldığımız demo dosya *Data_Demo* klasöründe **demo.txt** olarak bulunmakta

**Answer_1** klasöründe (1) şartı için yazılmış kodlar bulunmaktadır.
(Çıktısı **top_100_user_checkin.txt**) olarak aynı klasörün içindedir

**Answer_2** klasöründe (2) şartı için yazılmış kodlar bulunmaktadır
(Çıktısı **top_100_location_checkin.txt**) olarak aynı klasörün içindedir

**Answer_3** klasöründe (3) şartı için yazılmış kodlar bulunmaktadır
(Çıktısı **top_100_max_checkin.txt**) olarak aynı klasörün içindedir


-----------------------------------------------------------------------------------------


#####Kullanılan araçlar

Ubuntu 14.04 LTS

Pycharm Community Edition 5.0.3

Mongodb

#####@ozcaan11 tarafında geliştirilen bir proje olarak duruyor şuan :)
