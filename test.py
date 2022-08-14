#!/usr/bin/env python3

from jsonschema_to_sqlalchemy_flask.src import convert_to_sqlalchemy_flask
from jsonschema_to_sqlalchemy_flask.src import convert_to_json_loader
from jsonschema_to_sqlalchemy_flask.src import convert_to_json_dump
from jsonschema_to_sqlalchemy_flask.src import convert_to_unique_name_list_getter
from jsonschema_to_sqlalchemy_flask.src.get_order import get_order
from jsonschema_to_sqlalchemy_flask.src.convert_from_json_schema import convert_flask_admin

schema_filename_list = ["test1.schema.json", "test2.schema.json"]
flask_filename_without_extension = "flask_main_file"
flask_filename = "test_js2sf/flask_main_file.py"

data = convert_flask_admin(schema_filename_list, flask_filename_without_extension)

flask_file = convert_to_sqlalchemy_flask.insert_in_template(data)
with open(flask_filename, "w") as fh:
    fh.write(flask_file)

json_load_file = convert_to_json_loader.insert_in_template(data)
json_dump_from_database_file = convert_to_json_dump.insert_in_template(data)
unique_name_list_file = convert_to_unique_name_list_getter.insert_in_template(data)
order_list = get_order(data)

with open("test_js2sf/json_load.py","w") as fh:
    fh.write(json_load_file)

with open("test_js2sf/json_dump.py","w") as fh:
    fh.write(json_dump_from_database_file)

with open("test_js2sf/name_list.py","w") as fh:
    fh.write(unique_name_list_file)

print(order_list)

