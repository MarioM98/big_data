
#Per eseguire lo script lanciare la seguente riga di comando:
#./spark/bin/spark-submit --master local path_to_script


import time

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession


# Returns the papers' details (id, citations, pubblication year) which contains the given entity in the abstract
# Using the filter function
def papers_by_entity(rdd, entity):
    return rdd.filter(lambda x : x[0] == entity).flatMap(lambda x: x[1]).collect()

# Returns the papers' details (id, citations, pubblication year) which contains the given entity in the abstract
# Using lookup
def papers_by_entity2(rdd, entity):
    return rdd.lookup(entity)

if __name__ == "__main__":
    
    sc = SparkContext()
    spark = SparkSession(sc)

    # Reading the json containing the papers
    df_paper = spark.read.json("computer_science_1.json")
    # Removing useless columns
    df_paper = df_paper.drop("_ignored", "_index", "_score", "_type")

    # Reading the csv containing the entities
    df_entities = spark.read.csv("entities.csv", header=True)
    # Removing useless column
    df_entities = df_entities.drop("entity_type")
    # Taking only a fraction of all the entities (needed for computation problems)
    df_entities = df_entities.limit(5000)
    # Join of the 2 df (if the paper contain the entity in its abstract)
    joined = df_entities.join(df_paper, df_paper._source.abstract.contains(df_entities.entity))     
    # Getting the RDD from the DF
    rdd = joined.rdd.map(lambda x: (x.entity, (x._id, x._source.citationcount, x._source.year)))
    # Groping by key (the key is the entity)
    rdd = rdd.groupByKey().mapValues(list)

    #List of time execution of each iteration
    time_list =[]

    #List of all keys
    keys_list = rdd.keys().collect()

    for k in keys_list:
        start_time = time.time()
        papers_by_entity(rdd, k)
        time_list.append(time.time() - start_time)

    average = 0
    for t in time_list:
        average += t

    average /= len(time_list)

    print(f'Average: {average}')

    sc.stop()