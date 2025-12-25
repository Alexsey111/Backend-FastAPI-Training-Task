import secrets
import string

ALPHABET = string.ascii_letters + string.digits
ID_LENGTH = 6


def generate_short_id() -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(ID_LENGTH))
