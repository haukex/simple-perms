Changelog for simple-perms
==========================

1.0.0 - 2024-10-06
------------------

- Package `simple_perms` now has a `__main__.py` so you can invoke the CLI tool with `python3 -m simple_perms` as well

(Note this version was accidentally released as 0.9.2 as well)

0.9.1 - 2024-03-30
------------------

`commit 26c08cb979bb170f1eb3d4d816edb78e180b86bd`

- Fix incorrect Readme filename in `pyproject.toml`

0.9.0 - 2024-03-30
------------------

`commit 88e4a13b335621d097ea2f5eb7d90095191fbf7e`

- Initial release, based on the `simple-perms` that was part of
  <https://pypi.org/project/igbpyutils/> up until its v0.4.1.
  - **WARNING:** There are at least two incompatible changes:
  - This version of `simple-perms` does not recurse into directories by default,
    you will now need to use the `-r`/`--recurse` option. This option did not exist
    in the previous version
  - The option previously named `--umask` was renamed to `--mask` (short form options
    are unchanged), and a new `--umask`/`-k` option with a different meaning was introduced.
