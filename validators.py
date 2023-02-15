import re
from regex import alpha2_code_pattern

def is_valid_alpha2_code(string):
    result = re.match(alpha2_code_pattern, string)
    if result:
        return True
    else:
        return False