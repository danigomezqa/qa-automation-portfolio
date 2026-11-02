"""Configuración centralizada de las pruebas.

Mantener los datos (URLs, credenciales, etc.) en un solo lugar evita
repetirlos en cada prueba y facilita cambiarlos sin tocar los tests.
"""

# --- UI: SauceDemo (sitio público pensado para practicar automatización) ---
URL_BASE_UI = "https://www.saucedemo.com"

# Credenciales públicas que el propio SauceDemo documenta en su pantalla de login.
USUARIO_ESTANDAR = "standard_user"
USUARIO_BLOQUEADO = "locked_out_user"
CLAVE = "secret_sauce"

# Producto usado en las pruebas de carrito (atributo data-test del botón).
PRODUCTO_MOCHILA = "add-to-cart-sauce-labs-backpack"

# --- API: JSONPlaceholder (API REST pública y estable para pruebas) ---
URL_BASE_API = "https://jsonplaceholder.typicode.com"
