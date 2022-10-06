# big_data

In questa repository sono presenti due script Python: pyspark_script e time_test_script.
In pyspark_script sono presenti:
- Il preprocessing necessario per ottenere l'RDD voluto.
- Le funzioni che permettono le query sul suddetto RDD.
Per testare le funzioni:
- Inserire i file (computer_science_1.json ed entities.csv) sul sistema che si sta utilizzando (Colab, AWS EC2 ecc.)
- Aprire pyspark
- Eseguire tutta la prima parte di preprocessing (righe 1-17)
- Definire le funzioni fornite (righe 19-78)
- Chiamare la funzione desiderata e passare i parametri in input richiesti.

Per eseguire lo script di test time_test_script.py è necessario:
- Inserire i file (computer_science_1.json, entities.csv e lo script time_test_script.py) sul sistema che si sta utilizzando (Colab, AWS EC2 ecc.)
- Avviare Spark
- Lanciare il comando './spark/bin/spark-submit --master local path_to_script'
