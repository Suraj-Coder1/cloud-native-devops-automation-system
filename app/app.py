from flask import Flask, jsonify, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "project": "Cloud Native DevOps Automation System",
        "status": "Application is running",
        "message": "Cloud-native application deployed successfully"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
