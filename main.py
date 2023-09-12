from database import Database
from WriteAJson import writeAJson
from productanalyzer import ProductAnalyzer

db = Database(database="mercado", collection="produtos")
#db.resetDatabase()

#result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
#])

#writeAJson(result,"Média de gasto total")


#result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#    {"$sort": {"_id.data": 1, "total": -1}},
#    {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
#])

#writeAJson(result,"Cliente que mais comprou em cada dia")

pd = ProductAnalyzer(db)
pd.getTotalVendas()
pd.getProdutoMaisVendido()
pd.getClienteMaisGastou()
pd.getProdutos()
