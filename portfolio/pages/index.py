## Dependencies
import reflex as rx
from reflex_chakra import hstack
from portfolio.components.footer import footer
from portfolio.components.launcher import launcher, launcher_list
from portfolio.components.popup import cv_popup
from portfolio.constants import MORE_ABOUT_TEXT, PRESENTATION_TEXT, WELCOME_TEXT


## Function
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(WELCOME_TEXT, size="8"),
            rx.text(PRESENTATION_TEXT),
            rx.hstack(
                rx.text(MORE_ABOUT_TEXT),
                cv_popup(),
                spacing="1"
            ),
            launcher_list(),
            spacing="5",
            justify="center",
            min_height="35vh", # Original value: 85vh
        ),
        footer()
    )
