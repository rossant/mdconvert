mdconvert
=========

Convert Markdown documents in HTML, LaTeX and PDF.

Installation
------------

Put the folder in your system path.


Usage
-----

In a directory where there's a `*.md` file, type in a shell:

    $ python mdpdf.py

This will create a `*.pdf` file. Idem for `mdtex` (LaTeX document) and `mdwp`
(Wordpress HTML document). You can also specify a list of text files:

    $ python mdpdf.py text1.md text2.txt
    

Mathematical formulas
---------------------

For mathematical formulas in Markdown, use \$ ($\pi \simeq 3.14$) or double
dollars \$\$:

$$
\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}.
$$

They will be shown correctly in LaTeX and PDF, and the Wordpress HTML code
will have them work with the MathJax-LaTeX plugin. However they won't
be shown on Github.


