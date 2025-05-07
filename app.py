<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Conexión a MongoDB Atlas
client = MongoClient("mongodb+srv://Nayeli:PASSWORD@cluster0.6ylalqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["sensor_data"]         # Nombre de tu base de datos
collection = db["lecturas"]        # Nombre de la colección

@app.route('/datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    datos['fecha'] = datetime.now()  # Agrega timestamp
    collection.insert_one(datos)
    return jsonify({"mensaje": "Datos guardados correctamente"}), 200

@app.route("/ver")
def ver_datos():
    datos = list(collection.find().sort("_id", -1).limit(10))  # Los 10 datos más recientes
    return render_template("datos.html", datos=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
=======
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Conexión a MongoDB Atlas
client = MongoClient("mongodb+srv://Nayeli:PASSWORD@cluster0.6ylalqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["sensor_data"]         # Nombre de tu base de datos
collection = db["lecturas"]        # Nombre de la colección

@app.route('/datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()
    datos['fecha'] = datetime.now()  # Agrega timestamp
    collection.insert_one(datos)
    return jsonify({"mensaje": "Datos guardados correctamente"}), 200

@app.route("/ver")
def ver_datos():
    datos = list(collection.find().sort("_id", -1).limit(10))  # Los 10 datos más recientes
    return render_template("datos.html", datos=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
>>>>>>> 082fce6499796121941bc666695526e58b59db51
