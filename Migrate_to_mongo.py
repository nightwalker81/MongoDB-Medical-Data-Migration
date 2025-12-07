#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
from pymongo import MongoClient
import os


# In[2]:


data_file = pd.read_csv("healthcare_dataset.csv")


# In[13]:


# Tester l'integralitè de la base des donnèes avant la migration

def check_df(df):
    nb_ligne = df.shape[0]
    var_types = df.dtypes
    col_noms = list(df.columns)
    nb_null = int(df.isnull().sum().sum())
    nb_colonnes = df.shape[1]
    nb_doublons = int(df.duplicated().sum())

    print({"nb_lignes":nb_ligne,
          "nb_null":nb_null,
          "nb_colonnes": nb_colonnes,
          "nb_doublons":nb_doublons})
    print("_" * 50)
    print(f"This is the types of variables: \n {var_types}")
    print("_" * 50)
    print(f"This is the names of the columns:\n {col_noms}")
    


# In[14]:


check_df(data_file)


# In[15]:


# Etablir la connection de MongoDB en local
client = MongoClient(os.getenv("MONGO_URI", "mongodb://mongo:27017"))


# In[17]:


# Creation de la base de donnees
Medical_database = client["Medical_DB"]


# In[19]:


# Creation de collection de healthcare_records
collection = Medical_database["healthcare_records"]

collection.drop()
print("Old collections dropped")
# In[20]:


# Transformer la base de donnees en dictionnaire
data = data_file.to_dict(orient="records")


# In[21]:


# Migrer le jeu des donnnees vers mongodb (CRUD)----- Create
results = collection.insert_many(data)
print(f"Inserted {len(results.inserted_ids)} documents into healthcare_records")


# In[49]:


# Tester l'integralitè de la base des donnèes après la migration (CRUD) ----- READ

def check_db(collection):
    
    nb_lignes = collection.count_documents({})
    colonnes_nom = [col.keys() for col in collection.find().limit(1)]
    nb_null = 0
    for doc in collection.find():
        for val in doc.values():
            if val is None:
                nb_null = nb_null + 1
                
    duplicates = []
    seen = set()
    docs = list(collection.find({},{"_id":0}))
    
    for doc in docs:
        d_tuple = tuple(sorted(doc.items()))
        if d_tuple in seen:
            duplicates.append(d_tuple)
        else:
            seen.add(d_tuple)
    print(f"This is the columns names: \n {colonnes_nom}")
    return {"nb_ligne":nb_lignes,
           "nb_null": nb_null,
           "nb_duplicates" : len(duplicates)}


# In[51]:


# Update one document (CRUD) ----- Update
collection.update_one({"name": "Alice"}, {"$set": {"age": 30}})

# Delete one document (CRUD) ----- Delete
collection.delete_one({"name": "Bob"})

