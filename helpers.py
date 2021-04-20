import string


def format_category_name(url_link): # extract all category name
    category_name = url_link.contents
    category_name = ''.join(category_name)
    category_name = category_name.strip()
    return category_name


def clean_filename(filename):  # methode de nettoyage du text de tout les carractére non pris en charge
    var = "-_.() %s%s" % (string.ascii_letters, string.digits) # recupere les caracteres(autorisé/caractere/chiffre ascii)
    return ''.join(c for c in filename if c in var) # Join le tout dans un string et return la string


def found_book_link(book): # found all book url
    link = ''.join(book.find('a')['href'])[9:]
    return link

