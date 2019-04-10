let pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  buildInputs = [
    pkgs.python35Packages.autopep8
    pkgs.python35Packages.pip
    pkgs.python35Packages.pycodestyle
    pkgs.python35Packages.pylint
    pkgs.python35Packages.pytest
    pkgs.python35Packages.pytest-virtualenv
    pkgs.python35Packages.pytestcov
    pkgs.python35Packages.pytestflakes
    pkgs.python35Packages.python
    pkgs.python35Packages.setuptools
    pkgs.python35Packages.sphinx
    pkgs.python35Packages.tox
  ];

  shellHook = ''
alias pip="PIP_PREFIX='$TEMP/_build/pip_packages' \pip"
export PYTHONPATH="$TEMP/_build/pip_packages/lib/python3.5/site-packages:$PYTHONPATH"
PATH="$TEMP/_build/pip_packages/bin:$PATH"
alias tox="TOX_TESTENV_PASSENV=\"PYTHONPATH\" \tox"
alias autopep8="autopep8 --in-place --max-line-length=80 --aggressive"
pip install pytest-pylint
pip install pytest-random
'';
}
