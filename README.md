

![mongoDB](http://www.bit-forge.com/wp-content/uploads/2015/06/mongodb-logo-large.png)

----------

 - [Büyük Veri İşlemesi](#b%C3%BCy%C3%BCk-veri-%C4%B0%C5%9Flemesi)
	 - [Açıklama](#a%C3%A7%C4%B1klama)
	 - [Nasıl Yapılır ?](#nas%C4%B1l-yap%C4%B1l%C4%B1r-)
	 - [İsterler](#%C4%B0sterler)
	 - [Kullanılan Araçlar](#kullan%C4%B1lan-ara%C3%A7lar)
	 - [Projenin scala dilinde kodları (Fatih Metin)](#extra)

----------


#Büyük Veri İşlemesi

##Açıklama

Bu projede elimizde bulunan veri dosyasında yaklaşık 6 milyon satırlık veri *Gowalla_totalCheckins.txt* bulunmaktadır.

*Gowalla_totalCheckins.txt* aşağıdaki tablodaki gibidir

**Headerline** tabloda gösterildiği gibi  *ilk satırda* yer almaktadır (Normalde yoktu database' ye aktarmak için biz ekledik)



user_id | check_in_time 	|   latitude	|  longitude	 |location_id
--------|-----------------------|---------------|----------------|-----------
0	| 2010-10-19T23:55:27Z	| 30.2359091167	| -97.7951395833 |22847
0	| 2010-10-18T22:17:43Z	| 30.2691029532	| -97.7493953705 |420315
.       |   .                   |.              |   .            |.
.       |   .                   |.              |   .            |.
.       |   .                   |.              |   .            |.





**NOT**

> - Uygulamayı Windowsta yapmadım. Ubuntu 14.04 LTS de yaptım. O yüzden aşağıda yapılacak işlemlerin Windowsta ne sonuçlar vereceğini bilmiyorum.

> - Gowalla_totalCheckins.txt den aldığım 10,000 satırlık bir kesiti [***demo.txt***](Data_Demo/demo.txt) olarak kaydettim

> - demo.txt dosyasını ***.tsv*** uzantılı olarak kaydettim. Bu sayede mongodb ye import edilebilir


----------


##Nasıl Yapılır ?

 1. [**demo.tsv**](Data_Demo/demo.tsv) dosyasını mongodb ye import etmek için terminali açın ve aşağıdakileri yazın;

		mongoimport -d your_db_name -c your_collection_name --file /your_tsv_file_path/demo.tsv --type tsv --headerline

 2. İmport işlemi tamamladığında yeni bir terminal açıp aşağıdakileri
    yazın;

		  mongo 					//mongo shell açılacaktır
		> use your_db_name
		> db.your_collection_name.find().pretty()       //pretty datayı daha düzenli gösteriyor


Yukarıdaki işlemlerden sonra karşınızda şöyle bir satır örneği olmalıdır.

	{
		"_id" : ObjectId("568bf2b0e792b7459fea01f9"),
		"user_id" : 0,
		"check_in_time" : "2010-10-19T23:55:27Z",
		"latitude" : 30.2359091167,
		"longitude" : -97.7951395833,
		"location_id" : 22847
	}

 3. Pymongo  modülünü pip üzerinde kurmak için terminali açın ve sırasıyla
	1. pip kurmak için ;
		
			sudo apt-get install python-pip
	2. pymongo modülünü kurmak için ; 
				
			sudo pip install pymongo
		
		

---------



##İsterler

Burada bulmaya çalıştığımız bilgiler

 1. Bütün kullanıcılar herbirinin toplam kaç check-in yaptığı,
 2. Bütün yerlerde toplam kaç tane check-in yapıldığı,
 3. Bir kullanıcının check-in yaptığı bütün yerlerde en çok check-in
    yapan kişileri bulmak.

Sonuç olarak;

 - [*Answer_1*](Answer_1) klasöründe **(1)** şartı için yazılmış kodlar bulunmaktadır. Çıktı  [**top_100_user_checkin.txt**](Answer_1/top_100_user_checkin.txt) olarak aynı
   klasörün içindedir
 - [*Answer_2*](Answer_2) klasöründe **(2)** şartı için yazılmış kodlar bulunmaktadır. Çıktı  [**top_100_location_checkin.txt**](Answer_2/top_100_locations_checkin.txt)  olarak aynı
   klasörün içindedir
 - [*Answer_3*](Answer_3) klasöründe **(3)** şartı için yazılmış kodlar bulunmaktadır. Çıktı  [**top_100_max_checkin.txt**](Answer_3/top_100_max_checkin.txt)  olarak aynı
   klasörün içindedir

----------

##Extra
Projenin scala dilinde yazılmış haline [buradan](https://github.com/teaddict/bigdata-project) ulaşabilirsiniz.

Proje [Fatih Metin](https://github.com/teaddict) tarafından yazılmıştır.


----------

##Kullanılan Araçlar

| 1. [Ubuntu 14.04 LTS](http://www.ubuntu.com/download/desktop)
----------
 
| 2. [Pycharm Community Edition 5.0.3](https://www.jetbrains.com/pycharm/download/)
----------
 
| 3. [Mongodb](https://www.mongodb.org/)
----------  


----------


| [@ozcaan11](https://github.com/ozcaan11) tarafında geliştirilecek bir proje olarak duruyor şuan :)
----------
