import os
from common import call_pandoc, regex_process, listfiles
 
def convert_to_latex(filename):
    """
    Convert from Markdown to LaTeX.
    """
    basename, ext = os.path.splitext(filename)
    print("Converting '{0:s}' to LaTeX...".format(filename))
    filename1 = basename + ".tex"
    call_pandoc(filename, filename1, "markdown", "latex")
    print("Done!")

def main():
    for file in listfiles():
        convert_to_latex(file)

if __name__ == '__main__':
    main()
    