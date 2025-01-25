from pymilvus import connections, utility, FieldSchema, CollectionSchema, DataType, Collection
import random

# Connexion à Milvus
connections.connect("default", host="127.0.0.1", port="19530")

# Créer une collection
collection_name = "example_collection"

def create_collection():
    if utility.has_collection(collection_name):
        print(f"Collection '{collection_name}' existe déjà.")
        return

    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128),
    ]
    schema = CollectionSchema(fields, description="Exemple de collection Milvus")

    collection = Collection(name=collection_name, schema=schema)
    print(f"Collection '{collection_name}' créée avec succès.")

# Insérer des données dans la collection
def insert_data():
    collection = Collection(collection_name)

    # Générer des vecteurs aléatoires
    vectors = [[random.random() for _ in range(128)] for _ in range(10)]
    data = [
        vectors
    ]

    ids = collection.insert(data)
    print(f"Données insérées avec les IDs : {ids.primary_keys}")

# Effectuer une recherche dans la collection
def search_data():
    collection = Collection(collection_name)
    collection.load()

    # Exemple de vecteur de requête
    query_vector = [[random.random() for _ in range(128)]]

    search_params = {"metric_type": "L2", "params": {"ef": 20}}
    results = collection.search(query_vector, "vector", param=search_params, limit=5, output_fields=["id"])

    print("Résultats de la recherche :")
    for result in results:
        for hit in result:
            print(f"ID: {hit.id}, Distance: {hit.distance}")

if __name__ == "__main__":
    create_collection()
    insert_data()
    search_data()
