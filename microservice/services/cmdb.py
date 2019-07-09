from flask import Flask, jsonify, make_response

import requests
import os
import simplejson as json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print database_path

#with open("{}/database/inventory.json".format(database_path), "r") as f:
#    inv = json.load(f)

def load_inventory():
    with open("{}/database/inventory.json".format(database_path), "r") as f:
        inventory = json.load(f)
    return inventory

#@app.route("/reload", methods=['POST'])
#def reload_latest_inventory():
#    load_inventory()
#    return "reloaded inventory\n" 

@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hey! The service is up, how about doing something useful\n   IE: curl http://localhost:5000/inventory\n"

@app.route('/inventory', methods=['GET'])
def all_inventory():
    ''' Returns the list of Serials '''

    resp = make_response(json.dumps(load_inventory(), sort_keys=True, indent=4))
    resp.headers['Content-Type']="application/json"
    return resp


@app.route('/inventory/keys', methods=['GET'])
def list_keys():

    key_list = [] 
    for k in load_inventory():
        key_list.append(k)

    return jsonify(key_list)


@app.route('/inventory/<serial>/<key>', methods=['GET'])
def list_keys_value(serial, key):
    ''' Returns info about a specific serial number contents '''

    if serial not in load_inventory():
        return "Not found"

    return jsonify(load_inventory()[serial][key])


@app.route('/inventory/<serial>', methods=['GET'])
def inventory_data(serial):
    ''' Returns info about a specific serial number '''

    if serial not in load_inventory():
        return "Not found"

    return jsonify(load_inventory()[serial])

@app.route('/inventory/<sn>/lists', methods=['GET'])
def inventory_lists(sn):
    ''' Get lists based on serial number '''

    try:
        req = requests.get("http://127.0.0.1:5000/inventory/{}".format(sn))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text


if __name__ == '__main__':
    app.run(port=5000, debug=True)
