"""Página base del patrón Page Object Model.

Todas las páginas heredan de esta clase y comparten la misma referencia
a `page` (la pestaña del navegador que maneja Playwright).
"""


class BasePage:
    def __init__(self, page):
        self.page = page

    def abrir(self, ruta="/"):
        """Navega a una ruta relativa a la URL base definida en pytest.ini."""
        self.page.goto(ruta)
