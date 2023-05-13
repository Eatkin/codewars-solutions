# https://www.codewars.com/kata/56a25ba95df27b7743000016
import re
def validate_code(code):
    return re.match(r"^[1-3]", str(code)) is not None