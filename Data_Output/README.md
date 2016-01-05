#####After operation we have two *db*
    -1-reduced_user

    -2-reduced_location

-----------------------------------------------------------------------------------------

#####To export this db open terminal and write;

    mongoexport -d your_db_name -c reduced_user     --out /choose_a_path/reduced_user.tsv
    mongoexport -d your_db_name -c reduced_location --out /choose_a_path/reduced_location.tsv

-----------------------------------------------------------------------------------------

###And now your file is ready !

-----------------------------------------------------------------------------------------

@ozcaan11
