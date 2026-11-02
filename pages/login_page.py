"""Página de login de SauceDemo."""

from pages.base_page import BasePage


class LoginPage(BasePage):
    # Localizadores (selectores) de los elementos de la pantalla de login
    CAMPO_USUARIO = "#user-name"
    CAMPO_CLAVE = "#password"
    BOTON_LOGIN = "#login-button"
    MENSAJE_ERROR = "[data-test='error']"

    def abrir_login(self):
        self.abrir("/")

    def iniciar_sesion(self, usuario, clave):
        self.page.fill(self.CAMPO_USUARIO, usuario)
        self.page.fill(self.CAMPO_CLAVE, clave)
        self.page.click(self.BOTON_LOGIN)

    def obtener_mensaje_error(self):
        return self.page.locator(self.MENSAJE_ERROR).inner_text()
