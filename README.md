`msmb_theme`
============

This applies slight modifications to `sphinx_rtd_theme`. It needs the
aforementioned theme to be installed.

Installing
----------

 - Navigate to the `notebook/` submodule.
 - `npm install -g bower`
 - `bower install`
 - lessc --include-path="./notebook/static" notebook/static/style/style.less style.css
 
 - Run `python setup.py css` to generate css from less (requires node.js)
