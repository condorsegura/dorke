from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, Docker com Python no Windows 10!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
