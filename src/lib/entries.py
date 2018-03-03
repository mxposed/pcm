import datetime


class Tag:
    def __init__(self, name, entries=None):
        self.name = name
        if not entries:
            entries = []
        self.entries = entries

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Tag):
            return False
        return self.name == o.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return '<Tag: {}>'.format(self.name)

    def __reduce__(self) -> tuple:
        """
        This override is needed for pickle to handle sets of tags correctly
        """
        return Tag, (self.name, self.entries)

    def add_entry(self, entry):
        self.entries.append(entry)


class Entry:

    # TODO: This still requires plenty of boilerplate code.
    #       Consider implementing using **kwargs with superfluous argument(s) discarding base class
    #       See https://stackoverflow.com/a/8973302 for example
    def __init__(self, uuid, author, title, cite_key, is_favourite=False, notes=None, tags=None):
        if not notes:
            notes = []
        if not tags:
            tags = set()

        self.uuid = uuid
        self.author = author
        self.title = title
        self.cite_key = cite_key
        self.is_favourite = is_favourite
        self.notes = notes
        self.tags = tags

        self.creation_date = datetime.datetime.now()

    def __str__(self):
        result =  'Title: {}\n'.format(self.title)
        result += 'Author: {}\n'.format(self.author)
        result += self.print_fields()
        result += '-----\n'
        result += 'BibTeX Class: {}\n'.format(self.__class__.__name__.lower())
        result += 'UUID: {}\n'.format(self.uuid)
        result += 'Created on: {}\n'.format(self.creation_date)
        result += 'Tags: {}\n'.format(', '.join(map(lambda x: x.name, self.tags)))
        return result

    def print_fields(self):
        return ''

    def add_tag(self, tag: Tag):
        """

        :param tag:
        :type tag: Tag
        :return:
        """
        self.tags.add(tag)
        tag.add_entry(self)


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
