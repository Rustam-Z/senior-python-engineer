from typing import TypedDict


class MenuConfig(TypedDict):
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        cancellable: Can it be cancelled?
    """
    title: str
    body: str
    button_text: str
    cancellable: bool


def create_menu(config: MenuConfig):
    title = config["title"]
    # ...


create_menu(
    # You need to supply all the parameters
    MenuConfig(
        title="My delicious menu",
        body="A description of the various items on the menu",
        button_text="Order now!",
        cancellable=True
    )
)
