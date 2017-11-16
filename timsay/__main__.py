"""A Tim-Petersified version of cowsay."""
import argparse
import contextlib
import random
import sys

from textcolors import bright, dim

tim = """
\        ///||\\\\\\\\
 \      / __  __,\\\\
  \    |  o'  o'  +‖
      (|    C     |)
       |   /¨¨\   |ľ
        \  `¨>'  /  ľ
         \______/"w"w`
      .4###|__|###.
      #############2.
"""

@contextlib.contextmanager
def suppress_stdout():
    import os
    saved = sys.stdout, sys.stderr
    try:
        sys.stdout = sys.stderr = open(os.devnull, 'w')
        yield
    finally:
        sys.stdout, sys.stderr = saved

def get_width(statement):
    return max([len(x) for x in statement.split('\n')])

def get_zen():
    with suppress_stdout():
        import this
    # The text of the zen is encoded in `this.s` so we must decode:
    lookup = this.d
    return ''.join(ch if not ch in lookup else lookup[ch] for ch in this.s)

def bubble(statement, color='blue'):
    highlight = bright[color] if color in bright else bright['blue']
    width = get_width(statement)
    rows = ['{: <{w}}'.format(s, w=width) for s in statement.split('\n')]
    if len(rows) == 1:
        bubbled_statement = '< {} >'.format(highlight(rows[0]))
    elif len(rows) == 2:
        bubbled_statement = '/ {} \\\n\\ {} /'.format(*[highlight(r) for r in rows])
    else:  # 3 or more rows
        middle = '| {} |'.format(' |\n| '.join(highlight(r) for r in rows[1:-1]))
        bubbled_statement = '/ {} \\\n{}\n\\ {} /'.format(
            highlight(rows[0]), middle, highlight(rows[-1]))
    top_bottom = '\n _{}_\n{{}}\n -{}-\n'.format('_' * width, '-' * width)
    sys.stdout.write(top_bottom.format(bubbled_statement))

def timsay(saying=None, color='blue'):
    if not saying:
        zen = get_zen()
        zens = zen.split('\n\n')[-1].split('\n')
        saying = random.choice(zens)
    bubble(saying, color=color)
    indent = ' ' * max(0, get_width(saying) - 30)
    highlight = dim[color] if color in dim else dim['blue']
    for row in highlight(tim).split('\n'):
        sys.stdout.write(indent + row + '\n')

def make_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('message', type=str, nargs='*', default=None,
                        help='Your own message')
    parser.add_argument('-f', '--file', dest='fname', help='Use a file.')
    parser.add_argument('-s', '--stdin', dest='use_stdin', action='store_true',
                        help='Use a piped message.')
    for color in bright.keys():
        ch = '-k' if color == 'black' else '-' + color[0]
        parser.add_argument(ch, '--' + color, dest='color', action='store_const',
                            const=color, default='blue',
                            help='Make the text {}.'.format(color))
    return parser


if __name__ == '__main__':
    import sys
    options = make_parser().parse_args()
    if options.message:
        message = ' '.join(options.message)
    elif options.fname:
        try:
            message = open(options.fname).read()
        except FileNotFoundError:
            err_message = "Couldn't find {}.\nUsing a random saying...\n\n"
            sys.stdout.write(err_message.format(options.fname))
            message = None
    elif options.use_stdin:
        message = sys.stdin.read()
    else:
        message = None
    timsay(saying=message, color=options.color)
