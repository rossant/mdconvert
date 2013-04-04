import os
import sys
from common import call_pandoc, regex_process, listfiles

def convert_to_wordpress(filename):
    """Convert from Markdown to Wordpress."""
    basename, ext = os.path.splitext(filename)
    print("Converting '{0:s}' to Wordpress HTML...".format(filename))
    filename1 = basename + ".wordpress_tmp.txt"
    call_pandoc(filename, filename1, "markdown", "html", ["--gladtex"])
    # postprocessing for wordpress and MathJax-Latex
    patterns = [("<EQ ENV=\"math\">(.*?)</EQ>", "[latex]\\1[/latex]"),
                ("<EQ ENV=\"displaymath\">(.*?)</EQ>", "<div style=\"text-align: center;\">[latex]\\1[/latex]</div>"),
                ("<pre><code>","<pre lang=\"python\">"),
                ("</code></pre>","</pre>"),
                ("&quot;", "\""),
                ("&#39;", "'"),
                ("<h1(.*?)>(.*?)</h1>\n", ""),
                ]
    filename2 = basename + ".wordpress.txt"
    regex_process(filename1, filename2, patterns)
    os.remove(filename1)
    print("Done!")

def main():
    for file in listfiles():
        convert_to_wordpress(file)

if __name__ == '__main__':
    main()
    