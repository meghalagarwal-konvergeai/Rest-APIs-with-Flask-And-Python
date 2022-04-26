from flask import Flask

app = Flask(__name__)

# POST -> used to receive the data
# GET -> used to send the data

# POST /store data: {name:}
@app.route('/store', methods = ["POST"])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    pass

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', method=['POST'])
def create_items_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

if __name__ == "__main__":
    app.run(debug=True)