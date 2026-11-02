"""Pruebas de login sobre SauceDemo.

El fixture `page` lo provee pytest-playwright: es una pestaña nueva del
navegador para cada prueba, ya configurada con la base_url de pytest.ini.
"""

import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils import config

pytestmark = pytest.mark.ui


def test_login_exitoso(page):
    login = LoginPage(page)
    login.abrir_login()
    login.iniciar_sesion(config.USUARIO_ESTANDAR, config.CLAVE)

    inventario = InventoryPage(page)
    assert inventario.esta_visible(), "No se cargó el catálogo tras iniciar sesión"
    assert "inventory" in page.url


def test_login_credenciales_invalidas(page):
    login = LoginPage(page)
    login.abrir_login()
    login.iniciar_sesion("usuario_inexistente", "clave_incorrecta")

    assert "Username and password do not match" in login.obtener_mensaje_error()


def test_login_usuario_bloqueado(page):
    login = LoginPage(page)
    login.abrir_login()
    login.iniciar_sesion(config.USUARIO_BLOQUEADO, config.CLAVE)

    assert "locked out" in login.obtener_mensaje_error()
