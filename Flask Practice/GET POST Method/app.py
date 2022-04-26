from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores =[
    {
        "name":"My Wonderful Store",
        "items":
        [
            {
                "name":"My Items",
                "price":15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST -> used to receive the data
# GET -> used to send the data

# POST /store data: {name:}
@app.route('/store', methods = ["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data["name"],
    'items':[]
    }
    stores.append(new_store)

    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate the store till it matches and return it.
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    # If None matches, return an error message
    return jsonify({'message':"Store Not Found"})
    

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({"store":stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    # If None matches, return an error message
    return jsonify({'message':"Store Not Found"})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    # Iterate the store till it matches and return it.
    for store in stores:
        if(store['name'] == name):
            return jsonify({'items':store['items']})
    # If None matches, return an error message
    return jsonify({'message':"Store Not Found"})

if __name__ == "__main__":
    app.run()