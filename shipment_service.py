from flask import Flask, jsonify
import random
import time
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
shipments = [
    {"id": "SHP001", "truck": "TRK001", "status": "in_transit", "origin": "Mumbai", "destination": "Delhi", "delay": False},
    {"id": "SHP002", "truck": "TRK002", "status": "delivered", "origin": "Delhi", "destination": "Pune", "delay": False},
    {"id": "SHP003", "truck": "TRK003", "status": "delayed", "origin": "Pune", "destination": "Chennai", "delay": True},
    {"id": "SHP004", "truck": "TRK004", "status": "failed", "origin": "Chennai", "destination": "Bangalore", "delay": True},
    {"id": "SHP005", "truck": "TRK005", "status": "in_transit", "origin": "Bangalore", "destination": "Mumbai", "delay": False},
]

@app.route('/shipments', methods=['GET'])
def get_shipments():
    print(f"[LOG] GET /shipments called at {time.time()}")
    return jsonify({"shipments": shipments, "total": len(shipments)})

@app.route('/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    print(f"[LOG] GET /shipments/{shipment_id} called")
    shipment = next((s for s in shipments if s["id"] == shipment_id), None)
    if not shipment:
        return jsonify({"error": "Shipment not found"}), 404
    return jsonify(shipment)

@app.route('/shipments/failed', methods=['GET'])
def get_failed():
    failed = [s for s in shipments if s["status"] == "failed"]
    return jsonify({"failed_shipments": failed, "total": len(failed)})

@app.route('/shipments/simulate-delay', methods=['GET'])
def simulate_delay():
    print(f"[LOG] Simulating shipment delay!")
    time.sleep(2)
    return jsonify({"message": "Delay simulated", "affected": "SHP003"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
