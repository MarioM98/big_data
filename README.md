# How to execute the scripts

## Test per ottenere il tempo medio di esecuzione

Passi da seguire per eseguire lo script di test (tempo medio per trovare un entità):

-   Inserire i file (**_computer_science_1.json_**, **_entities.csv_** e lo script **_time_test_script.py_**) sul sistema che si sta utilizzando (**_Colab_**, **_AWS EC2_** ecc.)
-   Avviare Spark
-   Lanciare il comando `./spark/bin/spark-submit --master local `**_path_to_script_**

## Esecuzione delle query

Passi da eseguire per ottenere l'RDD ideato ed eseguire le query richieste aprire il file **_pyspark_script.py_** in cui è presente:

-   Il preprocessing necessario per ottenere l'RDD.
-   Le funzioni che permettono le query sul suddetto RDD.

Per testare le funzioni (eseguire le query):

-   Inserire i file (**_computer_science_1.json_** ed **_entities.csv_**) sul sistema che si sta utilizzando (**_Colab_**, **_AWS EC2_** ecc.)
-   Aprire pyspark lanciando il comando `pyspark`
-   Eseguire tutta la prima parte di preprocessing **_righe 1-17_**
-   Definire le funzioni fornite **_righe 19-78_**
-   Chiamare la funzione desiderata e passare i parametri in input richiesti.
