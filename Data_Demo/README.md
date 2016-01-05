### Our data looks like below table
-----------------------------------


user_id | check_in_time 	|   latitude	|  longitude	 |location_id
--------|-----------------------|---------------|----------------|-----------
0	| 2010-10-19T23:55:27Z	| 30.2359091167	| -97.7951395833 |22847
0	| 2010-10-18T22:17:43Z	| 30.2691029532	| -97.7493953705 |420315
.       |   .                   |.              |   .            |.
.       |   .                   |.              |   .            |.
.       |   .                   |.              |   .            |.


The **headerline** shown as in the first line

*NOTE*

*- First i have to save Gowalla_totalCheckins.txt as demo.tsv*

*- So i can import it into mongodb*

#####To import demo.tsv file into our mongodb  open **terminal** and write;
	*mongoimport -d your_db_name -c your_collection_name --file /your_tsv_file_path/demo.tsv --type tsv --headerline


#####When import process done write;
	xx@xx:~$ mongo 		//mongo shell will open
	> use your_db_name
	> db.your_collection_name.find().pretty()       //pretty make it pretty good :D

#####Your result must be like below

	{
		"_id" : ObjectId("568bf2b0e792b7459fea01f9"),
		"user_id" : 0,
		"check_in_time" : "2010-10-19T23:55:27Z",
		"latitude" : 30.2359091167,
		"longitude" : -97.7951395833,
		"location_id" : 22847
	}



####@ozcaan11
