from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

# FUNCTIONS

def parse(path, password=''):
    with open(path, 'rb') as fp:
        return PDFDocument(PDFParser(fp), password)

def is_extractable(document):
    return document.is_extractable

def process(document):
    # Create a PDF resource manager object that stores shared resources.
    rsrcmgr = PDFResourceManager()
    # Create a PDF device object.
    device = PDFDevice(rsrcmgr)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)

# HTML PARSING

from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams

codec = 'utf-8'
scale = 1
layoutmode = 'normal'
laparams = LAParams()
imagewriter = None
debug = 0

maxpages = 0,
password = '',
caching = True,
check_extractable = True

rsrcmgr = PDFResourceManager(caching = caching)

def toHtml(path_pdf, path_html, rotation = 0, pagenos = set()):

    with open(path_html, 'w') as outfp:

        device = HTMLConverter(
            rsrcmgr
            , outfp
            , codec = codec
            , scale = scale
            , layoutmode = layoutmode
            , laparams = laparams
            , imagewriter = imagewriter
            # , debug = debug
        )

        interpreter = PDFPageInterpreter(rsrcmgr, device)

        with open(path_pdf, 'rb') as fp:

            pages = PDFPage.get_pages(
                fp,
                pagenos,
                maxpages = maxpages,
                password = password,
                caching = caching,
                check_extractable = check_extractable
            )

            for page in pages:
                page.rotate = (page.rotate + rotation) % 360
                interpreter.process_page(page)
