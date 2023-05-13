# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
import re
def validate_pin(pin):
    return bool(re.match(r"^(?:\d{4})(?# I just found out you can write regex comments, pretty cool)(?:\d{2})?(?![\n\r])(?# This is all really obvious so no need to explain it)$", pin))