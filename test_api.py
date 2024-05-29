from flask import Flask, request, jsonify
from controller import admission_controller

def test_index_route():
    response = admission_controller.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello'