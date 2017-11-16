Timsay - Cowsay, but with ASCII Tim Peters!
===========================================

::

	.___________________________
	< Now is better than never. >
	 ---------------------------
	      \        ///||\\\\
	       \      / __  __,\\
	        \    |  o'  o'  +‖
	            (|    C     |)
	             |   /¨¨\   |ľ
	              \  `¨>'  /  ľ
	               \______/"w"w`
	            .4###|__|###.
	            #############2.


Why?
----

Demonstrate the use of Python 3.5's new `zipapp`_ to make an executable zipfile
that can run on any computer that has Python installed; including with bundled
libraries.::

    git clone https://github.com/tanyaschlusser/timsay.git
    cd timsay
    python -m zipapp timsay -p "/usr/bin/env python"
    ./timsay.pyz

Even without Python 3.5 you can just use the plain zip utility
and prepend the shebang (`#!`).::

    git clone https://github.com/tanyaschlusser/timsay.git
    cd timsay
    cd timsay; zip -r ../tmp.pyz .; cd ..
    ## Remember to use single quotes!
    echo '#!/usr/bin/env python' | \
      cat - tmp.pyz > /tmp/out && mv /tmp/out timsay.pyz
    rm tmp.pyz
    chmod u+x timsay.pyz 
    ./timsay.pyz 'Hello world'


Usage
-----

There are text colors (to demonstrate that the executable zipfile can include
bundled libraries) which you can change on the command line.::

    ./timsay.pyz 'I am not an AI' --red

And you can pipe a file,::

    cat __main__.py | ./timsay.pyz --stdin

Or read a file.::

    ./timsay.pyz -f README.rst

Use help if you want for the rest.::

    ./timsay.pyz --help


.. _`zipapp`: https://docs.python.org/3/library/zipapp.html
