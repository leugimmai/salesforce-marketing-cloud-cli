import re

def match(pattern, string, group=0):
    try:
        return re.search(pattern, string).group(group)
    except:
        return None


def replace(pattern, new_value, string):
    return re.sub(pattern, new_value, string)
