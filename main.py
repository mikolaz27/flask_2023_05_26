import pprint
import random
import string



import requests

from http import HTTPStatus

from flask import Flask, request, Response
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

from blueprints.customers.customers import customers_blueprint
from blueprints.astronauts.astronaut import astronauts_blueprint

app = Flask(__name__, template_folder='templates/')

app.register_blueprint(astronauts_blueprint, url_prefix='/astronauts')
app.register_blueprint(customers_blueprint)


@app.route("/<int:counter>/")
def hello_world(counter):
    return [str(i) for i in range(int(counter))]


@app.route("/")
def hello_world_with_args():
    my_args = request.args.get('a')
    return 'my_args'


# MyFirstName - camel
# my_first_name - snake
# my-first-name - kebab

@app.route("/generate-password")
@use_kwargs(
    {
        "password_length": fields.Int(
            missing=15,
            validate=[validate.Range(min=8, max=100)]
        ),
    },
    location="query"
)
def generate_password(password_length: int):
    # password_length = 10
    # request.args.get('length', '15')

    # if not password_length.isdigit():
    #     return "ERROR: should be a digit"
    # password_length = int(password_length)
    #
    # if not 8 <= password_length <= 100:
    #     return "ERROR: should be in range [8, 100]"

    return "".join(
        random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
                       k=password_length))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
