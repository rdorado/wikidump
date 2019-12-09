import xml.etree.ElementTree as ET
import fileinput
import re
import os

class Article:

    def __init__(self, string):
        self.raw = string
        self.xml = ET.fromstring(string)
        self.title = self.xml.find("title").text
        self.text = self.xml.find("revision/text").text

    def getAsString(self, textProcessor=None):
        return self.title

def processArticle(string):
    root = ET.fromstring(string)
    name = root.find("title")

def processdump(filename, titles=None, outputfile="output.xml", outputdirectory=".", multipleFiles=False, compression=None, outputType="xml", textProcessor=None):
    input = fileinput.FileInput(filename, openhook=fileinput.hook_compressed)

    article = None
    readArticle=False
    data = ""
    WRITE_XML_SINGLEFILE = False
    WRITE_TEXT_MULTIFILE = False

    if not os.path.isdir(outputdirectory):
        os.makedirs(outputdirectory)

    if not multipleFiles:
        if outputType is None or outputType.lower() == "xml":
            WRITE_XML_SINGLEFILE = True
    else:
        if outputType is None or outputType.lower() == "xml":
            WRITE_XML_MULTIFILE = True
        elif outputType.lower() == "text":
            WRITE_TEXT_MULTIFILE = True

    if WRITE_XML_SINGLEFILE:
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
            if WRITE_XML_SINGLEFILE:
                if titles == None or article.title in titles:
                    with open(outputfile, "a") as output:
                        output.write(article.raw)
            elif WRITE_TEXT_MULTIFILE:
                if titles == None or article.title in titles:
                    with open(outputdirectory+"/"+article.title+".txt", "w") as output:
                        if textProcessor is not None and callable(textProcessor):
                            output.write(textProcessor(article.text))
                        else:
                            output.write(article.text)
            readArticle = False
            articleBuffer = ""

    if WRITE_XML_SINGLEFILE:
        with open(outputfile, "a") as output:
            output.write("</mediawiki>")

    '''
    with bz2.open(outputfile, "wb") as f:
        f.write(data)
    '''
    pass