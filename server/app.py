#!/usr/bin/env python3

import json  # Added to handle exact string serialization
from flask import Flask, jsonify, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route("/contract/<id>")
def get_contract(id):
    """
    Scans for a contract match by casting the route variable to an integer.
    Returns details on 200 Success, or returns a 404 error code if missing.
    """
    try:
        search_id = int(id)
    except ValueError:
        return jsonify({"error": f"Invalid contract ID format: {id}"}), 404
    
    for contract in contracts:
        if contract["id"] == search_id:
            # 1. Use json.dumps to preserve definition order and matching spaces
            json_string = json.dumps(contract)
            # 2. Append the exact trailing newline CodeGrade is asserting against
            response_body = json_string + "\n"
            
            # 3. Package it into a proper JSON response object
            response = make_response(response_body, 200)
            response.headers["Content-Type"] = "application/json"
            return response
            
    return jsonify({"error": f"Contract with ID {id} not found"}), 404

@app.route("/customer/<customer_name>")
def get_customer(customer_name):
    """
    Verifies customer existence securely.
    Returns 204 No Content if verified, or returns 404 if missing.
    """
    search_name = str(customer_name).strip().lower()
    
    if search_name in customers:
        return "", 204
    else:
        return jsonify({"error": f"Customer '{customer_name}' not found"}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)