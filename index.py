from flask import Flask, request, send_from_directory
from Generate import Generate
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Pricefy</h1>"

@app.route("/pricefy", methods=["POST"])
def pricefy():
    arquivo = request.files.get("meuArquivo")
    arquivo.save(os.path.join('/tmp/', arquivo.filename))
    filePath = (os.path.join('/tmp/', arquivo.filename))

    title = request.form.get('title')
    price = request.form.get('price')

    imagem = Generate(filePath, title, 'R$' + price)
    imagem.textfy()

    return send_from_directory('/tmp/', 'newImage.jpg', as_attachment=True)