import unittest

import pcm


class TestPcm(unittest.TestCase):

    def setUp(self):
        pcm.clear_library()

    def test_add_entry(self):
        pcm.add_entry('scholar_1.txt')
        self.assertEqual(1, len(pcm.all_entries), 'Should be 1 entry')

    def test_delete_entry(self):
        pcm.add_entry('scholar_1.txt')
        pcm.delete_entry(pcm.all_entries[0]['uuid'])
        self.assertEqual(0, len(pcm.all_entries), 'Should be empty')

    def test_parse_bibtex_entry(self):
        bibtex = """@book{smith1994blast,
  title={Blast and ballistic loading of structures},
  author={Smith, Peter D and Hetherington, John G},
  year={1994},
  publisher={Digital Press}
}
        """
        entry = pcm.parse_bibtex_entry(bibtex)
        self.assertEqual('book', entry['bibtex_class'], 'An entry is a book')

    def test_format_entry(self):
        bibtex = """@book{smith1994blast,
  title={Blast and ballistic loading of structures},
  author={Smith, Peter D and Hetherington, John G},
  year={1994},
  publisher={Digital Press}
}
        """
        entry = pcm.parse_bibtex_entry(bibtex)
        output = pcm.format_entry(entry)
        self.assertTrue('Hetherington' in output)

    def test_format_entry2(self):
        bibtex = """@online{BlastHandbook,
  author={Madden T.},
  title={The BLAST Sequence Analysis Tool},
  year={2013}
  url={https://www.ncbi.nlm.nih.gov/books/NBK153387/},
  urldate={2018-02-14}
}"""
        entry = pcm.parse_bibtex_entry(bibtex)
        output = pcm.format_entry(entry)
        self.assertTrue('ncbi.nlm.nih.gov' in output)


if __name__ == '__main__':
    unittest.main()
