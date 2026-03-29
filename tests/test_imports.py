"""Basic smoke tests verifying that all required dependencies are importable."""

import importlib


def test_requests_importable():
    mod = importlib.import_module("requests")
    assert mod is not None


def test_yaml_importable():
    mod = importlib.import_module("yaml")
    assert mod is not None


def test_mysql_connector_importable():
    mod = importlib.import_module("mysql.connector")
    assert mod is not None


def test_yaml_parse():
    import yaml

    data = yaml.safe_load("key: value\nnumber: 42")
    assert data == {"key": "value", "number": 42}


def test_requests_session():
    import requests

    session = requests.Session()
    assert session is not None
    assert hasattr(session, "get")
    assert hasattr(session, "post")
