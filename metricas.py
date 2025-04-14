from pymongo import MongoClient
import pandas as pd
from collections import Counter

uri = "mongodb+srv://angelargd8:TsTwymNjqBo7MysP@cluster0.wic81.mongodb.net"
client = MongoClient(uri)
db = client["restaurante"]

#ordenes y productos
ordenes = list(db["ordenes"].find())
productos = list(db["productos"].find())
productos_dict = {p["_id"]: p["nombreProducto"] for p in productos}

df_ordenes = pd.DataFrame(ordenes)

# KPI 1 : total de ventas
total_ventas = df_ordenes["precioTotal"].sum()
print("Total de ventas: "+ str(total_ventas))

