from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from test import process_img

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "hello World"


@app.route("/img", methods=["POST"])
def img():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image provided in the request"}), 400

        image = request.files["image"]
        print(image)

        common_prefix = process_img(image)

        return jsonify({"common_prefix": common_prefix}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
