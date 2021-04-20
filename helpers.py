def format_category_name(url_link):
    category_name = url_link.contents
    category_name = ''.join(category_name)
    category_name = category_name.strip()
    return category_name