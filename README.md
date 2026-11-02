# QA Automation Portfolio — Playwright + pytest

Proyecto de automatización de pruebas que demuestra testing de **UI** y de **API REST** con Python, aplicando el patrón **Page Object Model** y ejecución continua con **GitHub Actions**.

> Portfolio personal de **Daniela Gómez** — QA Test Analyst en transición a automatización.
> [LinkedIn](https://www.linkedin.com/in/danielagomez-qa-sap/) · [GitHub](https://github.com/danigomezqa)

---

## 🛠️ Stack

- **Lenguaje:** Python
- **UI:** Playwright (`pytest-playwright`)
- **API:** requests
- **Runner:** pytest
- **Patrón de diseño:** Page Object Model (POM)
- **CI/CD:** GitHub Actions

## ✅ Qué valida

### Pruebas de UI — [SauceDemo](https://www.saucedemo.com)
- Login exitoso con credenciales válidas.
- Mensaje de error ante credenciales inválidas.
- Bloqueo de usuario deshabilitado (`locked_out_user`).
- Flujo end-to-end: login → agregar producto → verificar carrito.

### Pruebas de API — [JSONPlaceholder](https://jsonplaceholder.typicode.com)
- Listado de recursos (código 200 y cantidad esperada).
- Consulta de un recurso individual y validación de su estructura JSON.
- Creación de un recurso vía POST (código 201).

## 📁 Estructura

```
qa-automation-portfolio/
├── pages/                  # Page Objects (un archivo por página)
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── ui/                 # Pruebas de interfaz con Playwright
│   │   ├── test_login.py
│   │   └── test_carrito.py
│   └── api/                # Pruebas de servicios REST
│       └── test_api_posts.py
├── utils/
│   └── config.py           # URLs y datos centralizados
├── .github/workflows/      # Pipeline de CI
│   └── tests.yml
├── pytest.ini
└── requirements.txt
```

## 🚀 Cómo ejecutarlo localmente

> Requiere Python 3.10 o superior.

```bash
# 1. Crear y activar un entorno virtual
py -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Instalar el navegador que usa Playwright
playwright install chromium

# 4. Ejecutar las pruebas
pytest                  # todas
pytest -m ui            # solo UI
pytest -m api           # solo API
pytest --headed         # ver el navegador en acción (UI)
```

## 🔄 Integración continua

Cada `push` o `pull request` dispara el workflow de GitHub Actions, que instala las dependencias, instala el navegador y corre toda la suite en un entorno limpio. El estado se ve en la pestaña **Actions** del repositorio.

## 📌 Próximas mejoras

- Reportes HTML de resultados.
- Capturas automáticas ante fallos.
- Más cobertura del flujo de checkout.
