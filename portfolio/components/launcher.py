## dependencies
import reflex as rx


## Functions
def launcher(title: str, icon_name: str, link: str, color: tuple) -> rx.Component:
    return rx.link(
        rx.hover_card.root(
            rx.hover_card.trigger(
                rx.box(
                    rx.icon(
                        icon_name,
                        size=35,
                        color=rx.color(*color),
                        id="card_icon"
                    ),
                    border=f"2px solid {rx.color('gray', 12)}",
                    border_radius="8em",
                    height="8em",
                    width="8em",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    _hover={
                        "bg": rx.color(*color),
                        "#card_icon": {
                            "color": rx.color("gray", 12)
                        }
                    }
                ),
            ),
            rx.hover_card.content(
                rx.text(title),
            ),
        ),
        href=link
    )

def launcher_list() -> rx.Component:
    return rx.vstack(
        rx.tooltip(
            rx.heading("Available services:", size="3"),
            content="Services are self hosted",
        ),
        rx.flex(
            launcher("Browser", "search", "https://browser.kezzer.dev", ("blue", 8)),
            launcher("Cloud storage", "cloud", "https://cloud.kezzer.dev", ("tomato", 8)),
            launcher("Password manager", "shield", "https://passwords.kezzer.dev", ("blue", 10)),
            launcher("IT Tools", "wrench", "https://tools.kezzer.dev", ("grass", 8)),
            spacing="4",
            direction="row",
            wrap="wrap"
        ),
        spacing="4"
    )
