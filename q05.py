from pymongo import MongoClient

def get_collection(url_conexao, colecao):
    db = MongoClient(url_conexao)
    collection = db[colecao]
    return collection
