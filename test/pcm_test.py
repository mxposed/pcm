import unittest

import pcm


class TestPcm(unittest.TestCase):

    def test_add_entry(self):
        pcm.add_entry('scholar_1.txt')
        self.assertEqual(1, len(pcm.all_entries), 'Should be 1 entry')

    def test_delete_entry(self):
        pcm.add_entry('scholar_1.txt')
        pcm.delete_entry(pcm.all_entries[0]['uuid'])
        self.assertEqual(0, len(pcm.all_entries), 'Should be empty')

    def test_parse_bibtex_file(self):
        entry = pcm.parse_bibtex_file('scholar_1.txt')
        self.assertEqual('book', entry['bibtex_class'], 'An entry is a book')



if __name__ == '__main__':
    unittest.main()
