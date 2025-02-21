
def is_valid_url(url):
    """
    Checks if the given parameter is a valid URL based on basic rules.
    :param url: The input string to check.
    :return: True if it's a valid URL, False otherwise.
    """
    if not (url.startswith("http://") or url.startswith("https://") or url.startswith("www.")):
        return False
    if "." not in url:
        return False
    if " " in url:
        return False
    return True
print(is_valid_url("https://www.youtube.com/"))
print(is_valid_url("https:// site.com"))