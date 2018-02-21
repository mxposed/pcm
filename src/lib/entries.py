class Entry:

    # TODO: This still requires plenty of boilerplate code.
    #       Consider implementing using **kwargs with superfluous argument(s) discarding base class
    #       See https://stackoverflow.com/a/8973302 for example
    def __init__(self, uuid, author, title, cite_key, is_favourite=False, notes=None, tags=None):
        self.uuid = uuid
        self.author = author
        self.title = title
        self.cite_key = cite_key
        self.is_favourite = is_favourite

    def __str__(self):
        result =  'Title: {}\n'.format(self.title)
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

    def print_fields(self):
        result =  'Year: {}\n'.format(self.year)
        result += 'Publisher: {}\n'.format(self.publisher)

        return result


class Article(Book):
    def __init__(self, uuid, author, title, cite_key, journal, volume):
        super().__init__(uuid, author, title, cite_key, journal, volume)
        self.journal = journal
        self.volume  = volume

    def print_fields(self):
        result =  'Journal: {}\n'.format(self.journal)
        result += 'Volume: {}\n'.format(self.volume)

        return result


class Online(Entry):
    def __init__(self, uuid, author, title, cite_key, url):
        super().__init__(uuid, author, title, cite_key)
        self.url = url

    def print_fields(self):
        return 'URL: {}\n'.format(self.url)
