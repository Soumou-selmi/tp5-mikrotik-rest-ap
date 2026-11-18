from flask import Flask, request, jsonify
import itertools

app = Flask(__name__)
USER, PASSWORD = "api-user", "motdepasse"
counter = itertools.count(2)

DB = {
    "ip/address": {
        "*1": {".id": "*1", "address": "192.168.88.1/24",
               "network": "192.168.88.0", "interface": "ether1",
               "disabled": "false"}
    },
    "ip/route": {},
}

@app.before_request
def check_auth():
    a = request.authorization
    if not a or a.username != USER or a.password != PASSWORD:
        return jsonify({"error": 401, "message": "Unauthorized"}), 401

@app.route("/rest/<path:path>", methods=["GET", "POST", "PATCH", "DELETE"])
def rest(path):
    parts = path.split("/")
    collection = "/".join(parts[:2])
    item_id = parts[2] if len(parts) > 2 else None

    if collection not in DB:
        return jsonify({"error": 404, "message": "no such command"}), 404
    table = DB[collection]

    if request.method == "GET":
        if item_id:
            if item_id not in table:
                return jsonify({"error": 404, "message": "not found"}), 404
            return jsonify(table[item_id])
        return jsonify(list(table.values()))

    if request.method == "POST":
        new_id = f"*{next(counter):X}"
        obj = {".id": new_id, "disabled": "false", **request.get_json()}
        table[new_id] = obj
        return jsonify(obj), 200

    if request.method == "PATCH":
        if item_id not in table:
            return jsonify({"error": 404, "message": "not found"}), 404
        table[item_id].update(request.get_json())
        return jsonify(table[item_id])

    if request.method == "DELETE":
        if item_id not in table:
            return jsonify({"error": 404, "message": "not found"}), 404
        del table[item_id]
        return "", 204

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)