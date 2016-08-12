import subprocess

import tools.myconfig
import tools.mypdfminer

class Extracter(object):

    def __init__(self):
        return None

    def applyOCR(self):
        return None

    def html(self, *args):
        return tools.mypdfminer.toHtml(*args)

    def txt(self):
        return None

    def tabula(self, infile, outfile, **kwargs):

        guess_option = {
            True: '--guess'
            , False: ''
        }.get(kwargs.get('guess', True))

        command = [
            'java', '-jar'
            , tools.myconfig.TABULA_JAR
            , '{}'.format(infile)
            , '--outfile'   , outfile
            , guess_option
            , '--format'    , kwargs.get('format', 'CSV')
            , '--pages'     , kwargs.get('pages', 'all')
            , '--password'  , kwargs.get('password', '')
        ]

        return subprocess.call(command)

    def rotate(self):
        return None
