from pymongo import MongoClient

conexao = 'mongodb+srv://desafioSquad:3K3s6pYlnp9AXwev@projeto-mongo.a2fumrt.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(conexao)

def ajustar_estoque(sku, estoque, collection):
    client[collection].update_one({"sku": sku}, {"$set": {"estoque": estoque}})

