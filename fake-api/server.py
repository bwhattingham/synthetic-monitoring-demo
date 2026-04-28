from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/latency')
def latency():
    return jsonify({
        "region": "eu-west-1",
        "latency_ms": random.randint(120, 450)
    })

if __name__ == '__main__':
    app.run(port=5000)
