from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, SRE/DevOps World! This is CI/CD Demo on AWS EC2 🚀"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
