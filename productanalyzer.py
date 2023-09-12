from database import Database
from WriteAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database : Database):
        self.db = Database(database = "mercado", collection = "produtos")

    def getTotalVendas(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"produtos": "$produtos.descricao", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}},
            {"$group": {"_id": "$_id.data", "produto": {"$first": "$produtos.descricao"}, "total": {"$first": "$total"}}}
        ])
        writeAJson(result,"Total de vendas por dia")

    def getProdutoMaisVendido(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(result,"Produto mais vendido")

    def getClienteMaisGastou(self):
        result = self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"_id.data": 1, "total": -1}},
        {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
        ])
        writeAJson(result,"Cliente que mais comprou")

    def getProdutos(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "$produtos.quantidade": {"$gt": 1}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(result,"Produtos que foram vendidos mais de uma vez")
