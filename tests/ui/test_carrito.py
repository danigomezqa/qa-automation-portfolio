"""Prueba end-to-end del carrito: login -> agregar producto -> verificar carrito."""

import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils import config

pytestmark = pytest.mark.ui


def test_agregar_producto_al_carrito(page):
    # 1. Iniciar sesión
    login = LoginPage(page)
    login.abrir_login()
    login.iniciar_sesion(config.USUARIO_ESTANDAR, config.CLAVE)

    # 2. Agregar un producto desde el catálogo
    inventario = InventoryPage(page)
    inventario.agregar_producto(config.PRODUCTO_MOCHILA)
    assert inventario.cantidad_en_carrito() == 1, "El contador del carrito debería ser 1"

    # 3. Verificar que el producto aparece dentro del carrito
    inventario.ir_al_carrito()
    carrito = CartPage(page)
    assert carrito.cantidad_items() == 1, "El carrito debería tener 1 producto"
