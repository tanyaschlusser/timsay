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
    python -m . timsay -p "/usr/bin/env python"
    ./timsay.pyz

Even without Python 3.5 you can download these files zipped
("Clone or download" → "download zip")
and then prepend the shebang.::

    # Download the zip directory
    echo "#!/usr/bin/env python" | \
        cat - timsay.zip > /tmp/out && mv /tmp/out timsay.pyz
    ./timsay.pyz


.. _`zipapp`: https://docs.python.org/3/library/zipapp.html
