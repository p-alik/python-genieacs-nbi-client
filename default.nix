let pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  buildInputs = [
    pkgs.python27Packages.autopep8
    pkgs.python27Packages.pip
  ];

  shellHook = ''
alias pip="PIP_PREFIX='$TEMP/_build/pip_packages' \pip"
export PYTHONPATH="$TEMP/_build/pip_packages/lib/python2.7/site-packages:$PYTHONPATH"
PATH="$TEMP/_build/pip_packages/bin:$PATH"
alias tox="TOX_TESTENV_PASSENV=\"PYTHONPATH\" \tox"
alias autopep8="autopep8 --in-place --max-line-length=80 --aggressive"
pip install sphinx
pip install tox
'';
}
