## Dependencies
import reflex as rx
from reflex.components.radix.themes.color_mode import position_map
from reflex.components.radix.themes.layout.stack import hstack
from portfolio.constants import GITHUB_LINK, LINKEDIN_LINK, MADE_WITH_LOVE


## Functions
def social_link(icon_name: str, link: str) -> rx.Component:
    return rx.link(
        rx.icon(icon_name),
        href=link,
        is_external=True,
        hidden=True
    )

def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.divider(),
            rx.hstack(
                rx.text(MADE_WITH_LOVE, justify_content=["center", "center", "start",]),
                rx.hstack(
                    social_link("github", GITHUB_LINK),
                    social_link("linkedin", LINKEDIN_LINK),
                ),
                justify="between",
                align_items="center",
                flex_direction=["center", "center", "start"],
                width="100%",
            )
        ),
        margin_top="2em"
    )
