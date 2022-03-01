from flask import Flask, request, jsonify
app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "Contact": U"123456789",
        "Name": U"Mr. Ramakrishna"
    },
    {
        "id": 2,
        "Contact": U"987654321",
        "Name": U"Mr. Krishnadevraya"
    }
]

@app.route("/get-data")
def get_data():
    return jsonify({
        "data": contacts
    })

@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            'status': 'erorr',
            'message': 'Please provide the data'
        },400)
    contact = {
            "id": contacts[-1]["id"]+1,
            "Contact": request.json.get("Contact",""),
            "Name": request.json["Name"],
            }
    contacts.append(contact)
    return jsonify({
        'status': 'success',
        'message': 'Contact added successfully',
        "data": contacts
    })

if(__name__ == '__main__'):
    app.run(debug=True)