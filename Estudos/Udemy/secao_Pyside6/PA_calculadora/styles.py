#  pylint: disable=missing-docstring
#  pylint: disable=no-name-in-module
#  type: ignore
import qdarktheme
from variables import (
    PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
    ESPECIAL_PRIMARY_COLOR, ESPECIAL_DARKER_PRIMARY_COLOR,
    ESPECIAL_DARKEST_PRIMARY_COLOR)

qss = f"""
    QPushButton[cssClass="specialButtonSpace"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButtonSpace"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButtonSpace"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}

    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {ESPECIAL_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {ESPECIAL_DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {ESPECIAL_DARKEST_PRIMARY_COLOR};
    }}
"""


def setup_theme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}"
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}"
            },
        },
        additional_qss=qss
    )
