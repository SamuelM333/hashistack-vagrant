import os
import json

import hvac
from flask import Flask

client = hvac.Client(
    url='http://localhost:8200',
    token=os.environ['VAULT_TOKEN'],
)

client.secrets.kv.v2.configure(
    max_versions=20,
    mount_point='secret',
)

app = Flask("hashistack-python")
app.secret_key = "123"

@app.route('/', methods=['GET'])
def index():
    return "working\n"

@app.route('/secret', methods=['GET'])
def secret():
    secret_data = client.secrets.kv.v2.read_secret(path='test')

    return "shhh, the secret is {}\n".format(json.dumps(secret_data["data"]["data"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)