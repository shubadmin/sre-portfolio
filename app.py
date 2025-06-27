@@ -1,10 +1,13 @@
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, SRE/DevOps World! This is CI/CD Demo on AWS EC2 🚀"
    return "🚀 Hello from Flask via NGINX!"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
    app.run()
