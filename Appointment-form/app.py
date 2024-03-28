from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for locations
locations = ["Hospital A", "Clinic B", "Office C"]

@app.route('/recommend_location', methods=['POST'])
def recommend_location():
    user_input = request.json.get('input_location', '').lower()

    # Filter locations based on user input
    recommended_locations = [loc for loc in locations if user_input in loc.lower()]

    return jsonify({"recommended_locations": recommended_locations})

if __name__ == '__main__':
    app.run(debug=True)
