##### Data aşağıdaki tablodaki gibidir

**headerline** tabloda gösterildiği gibi  **ilk satırda** yer almaktadır

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
	mongoimport -d your_db_name -c your_collection_name --file /your_tsv_file_path/demo.tsv --type tsv --headerline

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


####@ozcaan11