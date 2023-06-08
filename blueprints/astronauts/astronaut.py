from http import HTTPStatus

import requests
from flask import Blueprint, redirect, url_for, Response

astronauts_blueprint = Blueprint("astronauts", __name__)


@astronauts_blueprint.route("/redirect-astronauts")
def redirect_astronauts():
    return redirect("http://api.open-notify.org/astros.json")


@astronauts_blueprint.route("/redirect-astronauts-local")
def redirect_astronauts_local():
    return redirect(url_for("astronauts.get_astronauts"))


@astronauts_blueprint.route("/get-astronauts")
def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    result = requests.get(url, {})

    if result.status_code not in (HTTPStatus.OK,):
        return Response("ERROR: Something went wrong", status=result.status_code)

    result: dict = result.json()
    statistics = {}
    for entry in result.get("people", {}):
        statistics[entry["craft"]] = statistics.get(entry["craft"], 0) + 1

    return statistics
