import xml.etree.ElementTree as ET
import fileinput
import re
import os

class Article:

    def __init__(self, string):
        self.text = string
        self.xml = ET.fromstring(string)
        self.title = self.xml.find("title").text

def processArticle(string):
    root = ET.fromstring(string)
    name = root.find("title")

def processdump(filename, titles, outputfile="output.xml", outputdirectory=".", multipleFiles=True, compression=None, outputType="xml", textProcessor=None):
    input = fileinput.FileInput(filename, openhook=fileinput.hook_compressed)

    article = None
    readArticle=False
    data = ""

    if not os.path.isdir(outputdirectory):
        os.makedirs(outputdirectory)

    if not multipleFiles and outputType not None and outputType.lower() == "xml":
        WRITE_XML_SINGLE_FILE = True

    if WRITE_XML_SINGLE_FILE:
        with open(outputfile, "w") as output:
            output.write('<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="en">\n')

    startPageTagRE = re.compile(r"<page>")
    endPageTagRE = re.compile(r"</page>")

    nline = 0
    articleBuffer = ""
    for line in input:
        nline += 1
        line = line.decode('utf-8')
        pageSearchStartIndx = 0
        startPage = startPageTagRE.search(line, pageSearchStartIndx)

        while startPage is not None:
            readArticle=True
            pageSearchStartIndx = startPage.end()
            startPage = startPageTagRE.search(line, pageSearchStartIndx)
        endPage = endPageTagRE.search(line, pageSearchStartIndx)

        if endPage is None:
            if readArticle: articleBuffer += line.rstrip()+"\n"
        else:
            articleBuffer += line.rstrip()+"\n"
            article = Article(articleBuffer)
            if article.title in titles:
                with open(outputfile, "a") as output:
                    output.write(article.text)
            readArticle = False
            articleBuffer = ""

    if WRITE_XML_SINGLE_FILE:
        with open(outputfile, "a") as output:
            output.write("</mediawiki>")

    '''
    with bz2.open(outputfile, "wb") as f:
        f.write(data)
    '''
    pass