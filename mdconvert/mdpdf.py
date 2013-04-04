import os
from common import call_pandoc, regex_process, listfiles

def convert_to_pdf(filename):
    """
    Convert from Markdown to PDF.
    """
    basename, ext = os.path.splitext(filename)
    print("Converting '{0:s}' to PDF...".format(filename))
    filename1 = basename + ".pdf"
    call_pandoc(filename, filename1, "markdown", "pdf")
    print("Done!")

def main():
    for file in listfiles():
        convert_to_pdf(file)

if __name__ == '__main__':
    main()
    