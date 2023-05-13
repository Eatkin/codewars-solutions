# https://www.codewars.com/kata/514a024011ea4fb54200004b
import re
def domain_name(url):
    pattern = r"(?:https?://)?(?:www\.)?([\w-]+)(?:\.\w+)?"
    return re.search(pattern, url).group(1)