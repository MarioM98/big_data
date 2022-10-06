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

#------------------------------------------------------------------------------------------------------------------------------------------#
# # Returns the ids of papers which contains the given entity
# Not need to be collected
def id_papers_by_entity(rdd, entity):
    return rdd.filter(lambda x : x[0] == entity).flatMap(lambda x: x[1]).map(lambda x: x[0]).collect()

# Returns the papers' details (id, citations, pubblication year) which contains the given entity in the abstract
# Using the filter function
# Need to be collected
def papers_by_entity(rdd, entity):
    return rdd.filter(lambda x : x[0] == entity).flatMap(lambda x: x[1])

# Returns the papers' details (id, citations, pubblication year) which contains the given entity in the abstract
# Using lookup
def papers_by_entity2(rdd, entity):
    return rdd.lookup(entity)

#------------------------------------------------------------------------------------------------------------------------------------------#
# Returns the papers' details (id, citations, publication year) of papers which contain both given entities
# Need to be collected
def papers_co_occurences(rdd, entita_x, entita_y):
    return rdd.filter(lambda x : x[0] == entita_x).flatMap(lambda x: x[1]).intersection(rdd.filter(lambda x: x[0] == entita_y).flatMap(lambda x: x[1]))

# Returns the IDs of papers which contain both given entities
# Need to be collected
def id_papers_co_occurences(rdd, entita_x, entita_y):
    return rdd.filter(lambda x : x[0] == entita_x).flatMap(lambda x: x[1]).intersection(rdd.filter(lambda x: x[0] == entita_y).flatMap(lambda x: x[1])).map(lambda x: x[0])

#------------------------------------------------------------------------------------------------------------------------------------------#
# Returns the papers' details (id, citations, pubblication year) of the papers which contains both given entities and that have a number of citation greater than or equal to the given threshold
# Need to be collected
def co_occurences_with_threshold(rdd, entity_x, entity_y, threshold):
    return rdd.filter(lambda x : x[0] == entity_x).flatMap(lambda x: x[1]).intersection(rdd.filter(lambda x: x[0] == entity_y).flatMap(lambda x: x[1])).filter(lambda x: x[1] >= threshold)

#------------------------------------------------------------------------------------------------------------------------------------------#
# Returns the papers' details (id, citations, publication year) of papers which contain the given entity and that have a number of citations greater or equal to a given threshold
def papers_with_threshold(rdd, entity, threshold):
    return rdd.filter(lambda x: x[0] == entity).flatMap(lambda x: x[1]).filter(lambda x: x[1] >= threshold)

# Returns the IDs of the papers which contain the given entity and that have a number of citations greater or equal to a given threshold
# Need to be collected
def id_papers_with_threshold(rdd, entity, threshold):
    return rdd.filter(lambda x: x[0] == entity).flatMap(lambda x: x[1]).filter(lambda x: x[1] >= threshold).map(lambda x: x[0])

#------------------------------------------------------------------------------------------------------------------------------------------#
# Returns the total number of citations of papers published in a given year of all papers which contain the given entity
# No need to be collected
def year_citation_by_entity(rdd, entity, year):
    return papers_by_entity(rdd, entity).filter(lambda x : x[2][:4] == year).map(lambda x : x[1]).reduce(lambda x,y : x+y)

#------------------------------------------------------------------------------------------------------------------------------------------#
# Return the papers' details (id, citations, publication year) of papers which contain the given entity and published in a given year
# Need to be collected
def papers_with_year(rdd, entity, year):
    return papers_by_entity(rdd, entity).filter(lambda x : x[2][:4] == year)

# Returns the IDs of the papers which contain the given entity and published in a given year
# Need to be collected
def id_papers_with_year(rdd, entity, year):
    return papers_by_entity(rdd, entity).filter(lambda x : x[2][:4] == year).map(lambda x: x[0])


