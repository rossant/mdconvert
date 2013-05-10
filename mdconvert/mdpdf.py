import os
import sys
from common import call_pandoc, regex_process, listfiles

def convert_to_pdf(filename, options=[]):
    """
    Convert from Markdown to PDF.
    """
    basename, ext = os.path.splitext(filename)
    print("Converting '{0:s}' to PDF with options {1:s}...".format(
        filename, ' '.join(options)))
    filename1 = basename + ".pdf"
    call_pandoc(filename, filename1, "markdown", "pdf", 
        options=options)
    print("Done!")

def main():
    options = filter(lambda x: not(x.endswith('.md') or x.endswith('.txt')),
            sys.argv[1:])
    for file in listfiles():
        convert_to_pdf(file, options=options)

if __name__ == '__main__':
    main()
    