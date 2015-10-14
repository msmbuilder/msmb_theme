import subprocess
import os

os.chdir("notebook")

# Check for clean submodule
unclean = "Please clean up your `notebook/` submodule!"
gitout = subprocess.check_output(['git', 'clean', '-ndx'])
if gitout == b'Would remove notebook/static/components/\n':
    pass
elif gitout == b'':
    subprocess.check_call([
        'npm', 'install', '-g', 'bower', 'less', 'less-plugin-clean-css'
    ])
    subprocess.check_call(['bower', 'install'])
else:
    print(gitout)
    raise RuntimeError(unclean)

print("Calling lessc")
subprocess.check_call([
    'lessc',
    '--clean-css',
    '--include-path="./notebook/static"',
    'notebook/static/style/style.less',
    '../msmb_theme/static/css/jupyter.min.css'
])
