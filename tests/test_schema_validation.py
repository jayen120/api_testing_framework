import requests
import json
from jsonschema import validate

def test_user_schema():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    schema = json.load(open("schemas/user_schema.json"))
    validate(instance=data, schema=schema)