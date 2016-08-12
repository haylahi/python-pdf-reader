from os import path

#############
# VARIABLES #
#############

ABS_CONFIG = path.realpath(__file__)
ROOT = path.dirname(path.dirname(path.dirname(ABS_CONFIG)))

REL_TABULA_JAR_DIR = 'target'
TABULA_JAR_NAME  = 'tabula-0.9.0-jar-with-dependencies.jar'

REL_TABULA_JAR = path.join(REL_TABULA_JAR_DIR, TABULA_JAR_NAME)
TABULA_JAR = path.join(ROOT, REL_TABULA_JAR)

REL_DATA_DIR = 'data'
DATA_DIR = path.join(ROOT, REL_DATA_DIR)

PDF_DIR_NAME = 'pdf'
PDF_DIR = path.join(DATA_DIR, PDF_DIR_NAME)

CSV_DIR_NAME = 'csv'
CSV_DIR = path.join(DATA_DIR, CSV_DIR_NAME)
