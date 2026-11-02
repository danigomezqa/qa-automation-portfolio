"""Página de inventario (catálogo de productos) de SauceDemo."""

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITULO = ".title"
    BADGE_CARRITO = ".shopping_cart_badge"
    ENLACE_CARRITO = ".shopping_cart_link"

    def esta_visible(self):
        """Devuelve True si el catálogo se cargó (indica login exitoso).

        Esperamos primero la navegación a /inventory.html; de lo contrario
        is_visible() se evaluaría antes de que la página nueva cargue.
        """
        self.page.wait_for_url("**/inventory.html")
        return self.page.locator(self.TITULO).is_visible()

    def agregar_producto(self, data_test):
        """Agrega un producto al carrito usando su atributo data-test."""
        self.page.click(f"[data-test='{data_test}']")

    def cantidad_en_carrito(self):
        """Lee el número que muestra el ícono del carrito (0 si está vacío)."""
        badge = self.page.locator(self.BADGE_CARRITO)
        if badge.count() == 0:
            return 0
        return int(badge.inner_text())

    def ir_al_carrito(self):
        self.page.click(self.ENLACE_CARRITO)
