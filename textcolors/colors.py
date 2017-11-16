"""Text colors.

Really to confirm that included libraries can be bundled in a zip app.
"""
def make_colorizer(i):
    """Use 3-bit terminal colors."""
    pattern =  u'\u001b[3{}m{{}}\u001b[0m'.format(i)
    def colorizer(message):
        return pattern.format(message)
    return colorizer

colors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
dim = dict((c, make_colorizer(i)) for i, c in enumerate(colors))
bright = dict((c, make_colorizer('{};1'.format(i))) for i, c in enumerate(colors))
