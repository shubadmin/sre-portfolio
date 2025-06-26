from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "✅ Monitored Flask App"

@app.route("/health")
def health():
    return {"status": "ok"}
