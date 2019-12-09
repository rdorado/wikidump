import unittest
import wikidump as wd
import shutil
import filecmp
import os

def myTextProcessor(text):
    resp = ""
    splits = text.split("\n")
    for split in splits:
        resp += split.strip()+"\n"
    return resp

class TestWikiDump(unittest.TestCase):

    tmpdir = "tmp"

    def __init__(self, *args, **kwargs):
        super(TestWikiDump, self).__init__(*args, **kwargs)

        if not os.path.isdir(self.tmpdir):
            os.makedirs(self.tmpdir)
        #self.addCleanup(self.clean)

    @classmethod
    def tearDownClass(self):
        #shutil.rmtree(self.tmpdir);
        pass

    def test_defaults(self):      
        wd.processdump(r'data/test.xml.bz2')
        self.assertTrue(filecmp.cmp(r"data/results/output.xml",r"output.xml"), 'Test failed')

    def test_write_onefile_xml(self):
        articles = ["Anarchism", "Test_3"]
        wd.processdump(r'data/test.xml.bz2', articles, outputfile=r"tmp/test_write_onefile_xml.xml")
        self.assertTrue(filecmp.cmp(r"data/results/test_write_onefile_xml.xml",r"tmp/test_write_onefile_xml.xml"), 'Test failed')

    def test_write_onefile_xml_compressed(self):
        articles = ["Anarchism", "Test_3"]
        wd.processdump(r'data/test.xml.bz2', articles, outputfile=r"tmp/test_write_onefile_xml.xml", compression='bz2')
        self.assertTrue(filecmp.cmp(r"data/results/test_write_onefile_xml.xml",r"tmp/test_write_onefile_xml.xml"), 'Test failed')

    def test_write_multifile_text(self):
        articles = ["Anarchism", "Test_3"]
        wd.processdump(r'data/test.xml.bz2', multipleFiles=True, outputdirectory="tmp/test_write_multifile_text", outputType="text")

    def test_write_multifile_textprocessor(self):
        articles = ["Anarchism", "Test_3"]
        wd.processdump(r'data/test.xml.bz2', multipleFiles=True, outputdirectory="tmp/test_write_multifile_textprocessor", outputType="text",  textProcessor=myTextProcessor )

    def test_write_multifile_xml(self):
        articles = ["Anarchism", "Test_3"]
        #wd.processdump(r'data/test.xml.bz2', multiFiles=True, outputdirectory="tmp/test_write_multifile_xml")

    def test_read_bz2(self):
        #articles = ["Afghanistan", "Argentina", "Belgium", "Belize", "Bolivia", "Brazil", "Canada", "Chile", "China", "Colombia", "France", "India", "Japan", "South_Korea", "Mexico", "Peru", "Russia", "Slovakia", "Spain", "United_Kingdom", "United_States", "Venezuela", "Vietnam"]
        #articles = ["Mercury_(planet)", "Venus", "Earth", "Mars"]
        #articles = ["Afghanistan", "Argentina", "Belgium", "Belize", "Bolivia", "Brazil", "Canada", "Chile", "China", "Colombia", "France", "India", "Japan", "South_Korea", "Mexico", "Peru", "Russia", "Slovakia", "Spain", "United_Kingdom", "United_States", "Venezuela", "Vietnam", "Mercury_(planet)", "Venus", "Earth", "Mars"]
        articles = ["Anarchism", "Test_3"]
        #wd.processdump(r'C:\Users\rdsanchez\Code\wiki-ie\data\enwiki-20191120-pages-articles-multistream.xml.bz2', r'\output\test', articles)
        wd.processdump(r'C:\Users\rdsanchez\Code\wiki-ie\data\test.xml.bz2', articles, outputfile="myfile.xml", multipleFiles=True, compression='bz2', outputType="xml", textProcessor=myTextProcessor)

if __name__ == '__main__':
    unittest.main()