###Big Data Project

In this project we have about **6 million** data which show users check-in times,location ...

------------------------------------------------------------------------

All we want to know *all users total check-in*

and *all locations total user* (explain it widely)

The data files demo stored at **Data_Demo** file

Answer_1 python file looks for all users total check-in and its file saved in Data_Output file as **reduced_user**

Answer_2 python file looks for all locations total user and its file saved in Data_Output file as **reduced_location**

------------------------------------------------------------------------


##### Our data looks like below table

The **headerline** shown as in the **first line**

-----------------------------------------------------------------------------------------


user_id | check_in_time 	|   latitude	|  longitude	 |location_id
--------|-----------------------|---------------|----------------|-----------
0	| 2010-10-19T23:55:27Z	| 30.2359091167	| -97.7951395833 |22847
0	| 2010-10-18T22:17:43Z	| 30.2691029532	| -97.7493953705 |420315
.       |   .                   |.              |   .            |.
.       |   .                   |.              |   .            |.
.       |   .                   |.              |   .            |.



-----------------------------------------------------------------------------------------


>**NOTE**

>-*- First i have to save Gowalla_totalCheckins.txt as demo.tsv*

>-*- So i can import it into mongodb*

-----------------------------------------------------------------------------------------

#####To import demo.tsv file into our mongodb  open **terminal** and write;
	*mongoimport -d your_db_name -c your_collection_name --file /your_tsv_file_path/demo.tsv --type tsv --headerline

-----------------------------------------------------------------------------------------

#####When import process done write;
	xx@xx:~$ mongo 					//mongo shell will open
	> use your_db_name
	> db.your_collection_name.find().pretty()       //pretty make it pretty good :D

-----------------------------------------------------------------------------------------

#####Your result must be like below

	{
		"_id" : ObjectId("568bf2b0e792b7459fea01f9"),
		"user_id" : 0,
		"check_in_time" : "2010-10-19T23:55:27Z",
		"latitude" : 30.2359091167,
		"longitude" : -97.7951395833,
		"location_id" : 22847
	}


-----------------------------------------------------------------------------------------


#####After operation we have two collections
    1- reduced_user
    2- reduced_location

-----------------------------------------------------------------------------------------

#####To export these collections open terminal and write;

    mongoexport -d your_db_name -c reduced_user     --out /choose_a_path/reduced_user.tsv
    mongoexport -d your_db_name -c reduced_location --out /choose_a_path/reduced_location.tsv

-----------------------------------------------------------------------------------------

###And now your file is ready !

#####   reduced_user
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


#####   reduced_location
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




####Resources

#####Pycharm Community Edition 5.0.3

#####@ozcaan11