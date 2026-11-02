"""Pruebas de API REST sobre JSONPlaceholder.

Validan códigos de respuesta, estructura del JSON y el comportamiento
de un POST, usando la librería requests.
"""

import pytest
import requests

from utils import config

pytestmark = pytest.mark.api

TIMEOUT = 15  # segundos máximos de espera por respuesta


def test_listar_posts():
    respuesta = requests.get(f"{config.URL_BASE_API}/posts", timeout=TIMEOUT)
    assert respuesta.status_code == 200
    # JSONPlaceholder siempre devuelve 100 posts
    assert len(respuesta.json()) == 100


def test_obtener_post_individual():
    respuesta = requests.get(f"{config.URL_BASE_API}/posts/1", timeout=TIMEOUT)
    assert respuesta.status_code == 200

    cuerpo = respuesta.json()
    # El JSON debe contener todos los campos esperados
    for campo in ("userId", "id", "title", "body"):
        assert campo in cuerpo, f"Falta el campo '{campo}' en la respuesta"
    assert cuerpo["id"] == 1


def test_crear_post():
    nuevo_post = {"title": "prueba QA", "body": "contenido de ejemplo", "userId": 1}
    respuesta = requests.post(f"{config.URL_BASE_API}/posts", json=nuevo_post, timeout=TIMEOUT)

    assert respuesta.status_code == 201  # 201 = creado
    creado = respuesta.json()
    assert creado["title"] == "prueba QA"
    assert "id" in creado  # la API devuelve el id asignado al nuevo recurso
