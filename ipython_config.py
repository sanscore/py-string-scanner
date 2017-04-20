# IPython configuration
# tox -econsole
# pylint: disable=all

c.InteractiveShellApp.exec_lines = [
    'import inspect',
    'from strscan import StringScanner',
]

c.InteractiveShell.banner2 = 'StringScanner Console\n======================\n\n%s\n' % '\n'.join(c.InteractiveShellApp.exec_lines)
