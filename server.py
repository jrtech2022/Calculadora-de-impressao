from flask import Flask, request, jsonify, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)
DATA_DIR = "data"

# Cria o diretório para salvar os arquivos, se não existir
os.makedirs(DATA_DIR, exist_ok=True)

# Rota para servir o arquivo HTML principal
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Rota para salvar os dados no arquivo TXT
@app.route("/finalizar", methods=["POST"])
def finalizar():
    dados = request.json
    if not dados:
        return jsonify({"message": "Nenhum dado recebido"}), 400

    # Extrai os dados
    total = dados.get("total", 0)
    serviços = {
        "Xerox P&B": dados.get("xeroxPB", 0),
        "Xerox Colorida": dados.get("xeroxCMYK", 0),
        "Impressão P&B": dados.get("impressaoPB", 0),
        "Impressão Colorida": dados.get("impressaoCMYK", 0),
        "Fotos 3x4": dados.get("fotos3x4", 0),
    }

    # Gera o conteúdo do arquivo
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    arquivo = f"{DATA_DIR}/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(arquivo, "w") as f:
        f.write(f"Data: {agora}\n")
        f.write(f"Serviços:\n")
        for nome, quantidade in serviços.items():
            f.write(f"  - {nome}: {quantidade}\n")
        f.write(f"Total: R$ {total:.2f}\n")

    return jsonify({"message": f"Total registrado: R$ {total:.2f}. Dados salvos no arquivo."})

if __name__ == "__main__":
    app.run(debug=True)
