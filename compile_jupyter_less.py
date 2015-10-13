import subprocess
import os

os.chdir("notebook")

# Check for clean submodule
unclean = "Please clean up your `notebook/` submodule!"
assert subprocess.check_output(['git', 'clean', '-ndx']) == b'', unclean

subprocess.check_call(['npm', 'install', '-g', 'bower'])
subprocess.check_call(['bower', 'install'])
subprocess.check_call([
    'lessc',
    '--include-path="./notebook/static"',
    'notebook/static/style/style.less',
    '../msmb_theme/static/css/jupyter.css'
])
