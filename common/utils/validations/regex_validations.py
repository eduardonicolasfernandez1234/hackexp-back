import re


class RegexValidations:

    @staticmethod
    def has_lowercase_character(value: str):
        return re.search(r'[a-z]', value)

    @staticmethod
    def has_uppercase_character(value: str):
        return re.search(r'[A-Z]', value)

    @staticmethod
    def has_special_character(value: str):
        return re.search(r'[!@#$%^&*(),.?":{}|<>]', value)

    @staticmethod
    def generate_slug(value: str) -> str:
        return re.sub(r'[^\w]+', '-', value.lower().strip())
