import string
from random import choice

from app.base.config import get_settings


def create_random_url():
    short_url = "".join(
        (
            choice(string.digits + string.ascii_letters)
            for _ in range(get_settings().num_url_chars)
        )
    )

    return f"{get_settings().base_url}/{short_url}"

