`msmb_theme`
============

This applies slight modifications to `sphinx_rtd_theme`. It needs the
aforementioned theme to be installed.

### Modifications

 - Styling tweaks in `msmb.css`
 - Styling for Jupyter notebooks

### Jupyter CSS

Jupyter css is committed to this repository. It is slightly modified from
the upstream stylesheet. You can regenerate `jupyer.min.css`:

 - Ensure the `notebook/` submodule is initialized.
 - Apply `wrap-notebook-css.patch` to it.
 - Run `compile_jupyter_less.py` to turn the patched `less` files into
   `css`.
