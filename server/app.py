#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response, jsonify

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
        # If the input cannot be cast to an integer, it cannot match our data matrix
        return jsonify({"error": f"Invalid contract ID format: {id}"}), 404
    
    # Iterate through the contracts list array to find a matching ID
    for contract in contracts:
        if contract["id"] == search_id:
            return jsonify(contract), 200
            
    # Fallback response if contract ID doesn't exist
    return jsonify({"error": f"Contract with ID {id} not found"}), 404

@app.route("/customer/<customer_name>")
def get_customer(customer_name):
    """
    Verifies customer existence securely.
    Returns 204 No Content if verified, or returns 404 if missing.
    """
    # Clean the input parameter string for flexible lookup comparisons
    search_name = str(customer_name).strip().lower()
    
    # Check if the cleaned search name exists directly in the customers array list
    if search_name in customers:
        # Success, but sensitive data: Return completely blank payload with a 204 code
        return "", 204
    else:
        # Not found fallback code route
        return jsonify({"error": f"Customer '{customer_name}' not found"}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)