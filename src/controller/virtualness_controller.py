# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

from src.service import journey_service as service

# creating a Flask app
app = Flask(__name__)


# On the terminal type: curl http://127.0.0.1:5000/

# Captures input cards provided via input.
@app.route('/input', methods=['POST'])
def store_input_cards():
    try:
        data = request.get_json()

        # Extract all cards in list
        journey_cards_input = data["entry_list"]
        service.store_journey_cards(journey_cards_input)

        return jsonify({"Success": "Input is received"}), 200

    except Exception as ex:
        return jsonify({'error': 'An error occurred', 'details': str(ex)}), 500


# Returns sorted output of end-to-end journey.
@app.route('/output', methods=['GET'])
def get_journey_end_to_end():
    output = service.get_sorted_end_to_end_journey_details()
    return jsonify({"output": output})


if __name__ == '__main__':
    app.run(debug=True)
