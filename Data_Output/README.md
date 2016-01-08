#####answer_1_for_demo ve answer_2_for_demo kodlarının çalıştırılmasından sonra databasemizde iki collection olacaktır. Bunlar;
    1- reduced_user_for_demo
    2- reduced_location_for_demo

-----------------------------------------------------------------------------------------

#####Bu dataları export etmek (dışarı çıkarmak) için terminali açın ve aşağıdakileri yazın;

    mongoexport -d your_db_name -c reduced_user     --out /choose_a_path/reduced_user.tsv
    mongoexport -d your_db_name -c reduced_location --out /choose_a_path/reduced_location.tsv

-----------------------------------------------------------------------------------------

###Ve artık datanız hazır !

-----------------------------------------------------------------------------------------

@ozcaan11