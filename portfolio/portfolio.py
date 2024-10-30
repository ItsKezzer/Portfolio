## Dependencies
import reflex as rx
from rxconfig import config
from portfolio.pages.index import index


## Init
app = rx.App(
    theme=rx.theme(
        appearance="inherit",
        has_background=True,
        radius="large"
    )
)
app.add_page(index, title="Kezzer.Dev")
