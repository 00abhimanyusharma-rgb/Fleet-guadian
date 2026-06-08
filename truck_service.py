from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

trucks = [
    {"id": "TRK001", "driver": "Ramesh", "status": "active", "location": "Mumbai"},
    {"id": "TRK002", "driver": "Suresh", "status": "idle", "location": "Delhi"},
    {"id": "TRK003", "driver": "Mahesh", "status": "active", "location": "Pune"},
    {"id": "TRK004", "driver": "Ganesh", "status": "maintenance", "location": "Chennai"},
    {"id": "TRK005", "driver": "Rajesh", "status": "active", "location": "Bangalore"},
]

@app.route('/trucks', methods=['GET'])
def get_trucks():
    print(f"[LOG] GET /trucks called at {time.time()}")
    return jsonify({"trucks": trucks, "total": len(trucks)})

@app.route('/trucks/<truck_id>', methods=['GET'])
def get_truck(truck_id):
    print(f"[LOG] GET /trucks/{truck_id} called")
    truck = next((t for t in trucks if t["id"] == truck_id), None)
    if not truck:
        return jsonify({"error": "Truck not found"}), 404
    return jsonify(truck)

@app.route('/trucks/status', methods=['GET'])
def get_status():
    active = len([t for t in trucks if t["status"] == "active"])
    return jsonify({"active": active, "total": len(trucks)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
