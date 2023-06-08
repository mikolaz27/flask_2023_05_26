import requests
from flask import Blueprint, redirect, url_for, Response
from webargs import fields
from webargs.flaskparser import use_kwargs

from utils.database_handler import execute_query
from utils.formatter import format_records

customers_blueprint = Blueprint("customers", __name__)


@customers_blueprint.route("/get-customers")
@use_kwargs(
    {
        "first_name": fields.Str(
            required=True
            # missing=None
        ),
        "last_name": fields.Str(
            # required=True
            missing=None
        )
    },
    location='query'
)
def get_all_customers(first_name, last_name):
    query = "SELECT FirstName, LastName FROM customers"

    fields = {}

    if first_name:
        fields["FirstName"] = first_name
    if last_name:
        fields["LastName"] = last_name

    if fields:
        query += " WHERE " + " AND ".join(
            f"{key}=?" for key in fields
        )
    print(query)

    records = execute_query(query=query, args=tuple(fields.values()))
    return format_records(records)
