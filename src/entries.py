

class Entry:

    def __init__(self, uuid, author, title, cite_key):
        self.uuid = uuid
        self.author = author
        self.title = title
        self.cite_key = cite_key

    def __str__(self):
        result = 'Title: {}\n'.format(self.title)
        result += 'Author: {}\n'.format(self.author)
        result += self.print_fields()
        result += '-----\n'
        result += 'BibTeX Class: {}\n'.format(self.__class__.__name__.lower())
        result += 'UUID: {}\n'.format(self.uuid)
        return result

    def print_fields(self):
        return ''


class Book(Entry):

    def __init__(self, uuid, author, title, cite_key, year, publisher):
        super().__init__(uuid, author, title, cite_key)
        self.year = year
        self.publisher = publisher


class Article(Book):
    def __init__(self, uuid, author, title, cite_key, year, publisher):
        super().__init__(uuid, author, title, cite_key, year, publisher)
        self.journal = None
        self.volume = None


class Online(Entry):
    def __init__(self, uuid, author, title, cite_key, url):
        super().__init__(uuid, author, title, cite_key)
        self.url = url

    def print_fields(self):
        return 'URL: {}\n'.format(self.url)

