## Dependencies
import reflex as rx
from reflex_chakra.components import divider
from portfolio.constants import CV_EN, CV_FR


## Functions
def cv_card(flag: str, title: str, link: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.heading(flag, size="9"),
                rx.divider(),
                rx.text(title)
            ),
            border=f"1px solid {rx.color('gray', 8)}",
            border_radius="0.313em",
            height="8em",
            width="12em",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        href=link,
        underline="none",
        is_external=True
    )

def cv_popup() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.link("my CV")),
        rx.dialog.content(
            rx.dialog.title("Choose a CV"),
            rx.hstack(
                cv_card("🇫🇷", "Francais", CV_FR),
                cv_card("🇬🇧", "English", CV_EN),
                spacing="8",
                display="flex",
                align_items="center",
                justify_content="center"
            ),
            rx.dialog.close(
                rx.center(rx.button("Close", size="3", margin_top="16px"))
            ),
        ),
    )
