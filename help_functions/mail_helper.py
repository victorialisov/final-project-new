import re


# method for getting link from registration email
def get_link(msg: str):
    pattern = r'(http|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    result = re.search(pattern, msg)
    return result.group(0)
