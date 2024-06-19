Development Notes
=================

Note this is currently referenced by:
- <https://github.com/haukex/unzipwalk/blob/main/dev/DevNotes.md>

Development Environment
-----------------------

- [ ] Development on Linux
- [ ] In order to run full tests locally, install multiple Python versions with `python3.X`
  aliases, e.g as per <https://github.com/haukex/toolshed/blob/main/notes/Python.md>,
  and use the lowest supported version for normal development to catch any backcompat issues
- [ ] `python3.9 -m venv .venv3.9` and `. .venv3.9/bin/activate`
- [ ] `make installdeps` - set up dev env
- [ ] Installing Pyright (if you don't have Node/Pyright already):
  - [ ] Install Node as per <https://github.com/haukex/toolshed/blob/main/notes/JavaScript.md>
  - [ ] `npm install -g pyright`
- [ ] `pip install --upgrade build twine` - for making releases

Testing
-------

- [ ] `make` - tests incl. lint & coverage
- [ ] `dev/local-actions.sh` - tests on all Python versions

Release Preparation
-------------------

- [ ] Check:
  - [ ] `make tasklist`
  - [ ] GitHub Issues
  - [ ] Git stash
  - [ ] Whether the Python versions in `dev/local-actions.sh` and the GitHub Actions Workflows need updating
- [ ] Spellcheck documentation in `simple_perms/__init__.py` and `docs/index.rst`
- [ ] `make README.md` - generate `README.md` (`make -B` to force) and check formatting
- [ ] Bump version number in `pyproject.toml`
- [ ] Update `CHANGELOG.md`

Releasing
---------

**These steps should be done on Linux!**

- [ ] `git commit` and `git push` if needed
- [ ] `git tag vX.X.X`
- [ ] `git push --tags`
- [ ] watch GitHub Actions
- [ ] `python3 -m build`
- [ ] `twine check dist/simple-perms-*.tar.gz`
- [ ] `tar tzvf dist/simple-perms-*.tar.gz` to inspect the package
- [ ] `dev/isolated-dist-test.sh dist/simple-perms-*.tar.gz`
- [ ] `twine upload dist/simple-perms-*.tar.gz`
- [ ] New GitHub Release: Title "simple-perms vX.X.X", body from the changelog, link to PyPI (specific version); attach `.tar.gz` to release
- [ ] `pip3 install --upgrade simple-perms` and `simple-perms -h`
- [ ] `git clean -dxf dist *.egg-info`
- [ ] Add placeholder for next version to `CHANGELOG.md`
