"""Página del carrito de compras de SauceDemo."""

from pages.base_page import BasePage


class CartPage(BasePage):
    CONTENEDOR = ".cart_list"
    ITEMS = ".cart_item"

    def cantidad_items(self):
        """Cuenta cuántos productos hay listados en el carrito.

        Esperamos la navegación a /cart.html y que el contenedor del carrito
        esté presente antes de contar, para no leer un DOM a medio cargar.
        """
        self.page.wait_for_url("**/cart.html")
        self.page.locator(self.CONTENEDOR).wait_for()
        return self.page.locator(self.ITEMS).count()
