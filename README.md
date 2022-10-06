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

## Descrizione funzioni per effettuare le query

-   `id_papers_by_entity(rdd, entity)`
    La fuzione prende in input l'RDD su cui effettuare la query e l'entità da ricercare nel RDD.
    Restituisce la lista di id dei papers che contengono l'entità data in input.

-   `papers_by_entity(rdd, entity)`
    Utilizza la funzione **_filter_**.
    La fuzione prende in input l'RDD su cui effettuare la query e l'entità da ricercare nel RDD.
    Restituisce l'RDD contenente i dettagli dei papers (id, numero di citazioni e anno di pubblicazione) che contengono l'entità passata come parametro.

-   `papers_by_enity2(rdd, entity)`
    Utilizza la funzione **_lookup_**
    La fuzione prende in input l'RDD su cui effettuare la query e l'entità da ricercare nel RDD.
    Restituisce la lista contenente i dettagli dei papers (id, numero di citazioni e anno di pubblicazione) che contengono l'entità passata come parametro.

-   `papers_co_occurencies(rdd, entity_x, entity_y)`
    La fuzione prende in input l'RDD su cui effettuare la query e le entità da ricercare nel RDD.
    Restituisce l'RDD contenente i dettagli dei papers (id, numero di citazioni e anno di pubblicazione) che contengono entrambe le entità passate come parametro.

-   `id_papers_co_occurencies(rdd, entity_x, entity_y)`
    La fuzione prende in input l'RDD su cui effettuare la query e le entità da ricercare nel RDD.
    Restituisce l'RDD contenente gli ID dei papers che contengono entrambe le entità passate come parametro.

-   `co_occurencies_with_threshold(rdd, entity_x, entity_y, threshold)`
    La fuzione prende in input l'RDD su cui effettuare la query e le entità da ricercare nel RDD e la soglia minima di citazioni che devono avere i papers.
    Restituisce l'RDD contenente i dettagli dei papers (id, numero di citazioni e anno di pubblicazione) che contengono entrambe le entità passate come parametro e che hanno un numero di citazioni maggiore o uguale alla soglia data.

-   `papers_with_threshold(rdd, entity, threshold)`
    La fuzione prende in input l'RDD su cui effettuare la query e l'entità da ricercare nel RDD e la soglia minima di citazioni che devono avere i papers.
    Restituisce l'RDD contenente i dettagli dei papers (id, numero di citazioni e anno di pubblicazione) che contengono l'entità passata come parametro e che hanno un numero di citazioni maggiore o uguale alla soglia data.

-   `id_papers_with_threshold(rdd, entity, threshold)`
    La fuzione prende in input l'RDD su cui effettuare la query e l'entità da ricercare nel RDD e la soglia minima di citazioni che devono avere i papers.
    Restituisce l'RDD contenente gli ID dei papers che contengono l'entità passata come parametro e che hanno un numero di citazioni maggiore o uguale alla soglia data.

-   `year_citaions_by_entity(rdd, entity, year)`
    La fuzione prende in input l'RDD su cui effettuare la query e l'entità da ricercare nel RDD e l'anno di pubblicazione dei papers richiesti.
    Restituisce il numero totale di citazioni dei papers pubblicati in un determinato anno, dei papers che contengono l'entità data.

-   `papers_with_year(rdd, entity, year)`
    La fuzione prende in input l'RDD su cui effettuare la query e l'entità da ricercare nel RDD e l'anno di pubblicazione dei papers richiesti.
    Restituisce l'RDD contenente i dettagli dei papers (id, numero di citazioni e anno di pubblicazione) che contengono l'entità passata come parametro e che sono stati pubblicati nell'anno passato come parametro

-   `id_papers_with_year(rdd, entity, year)`
    La fuzione prende in input l'RDD su cui effettuare la query e l'entità da ricercare nel RDD e l'anno di pubblicazione dei papers richiesti.
    Restituisce l'RDD contenente gli ID dei papers che contengono l'entità passata come parametro e che sono stati pubblicati nell'anno passato come parametro
