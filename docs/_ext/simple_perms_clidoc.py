from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
import simple_perms

class SimplePermsCli(Directive):
    def run(self):
        parser = simple_perms._arg_parser()  # pyright: ignore [reportPrivateUsage]  # pylint: disable=protected-access
        return [nodes.literal_block(text=parser.format_help())]

def setup(app: Sphinx):
    app.add_directive('simple_perms_clidoc', SimplePermsCli)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
