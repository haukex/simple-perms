Simplify \*NIX Permissions
==========================

This package primarily provides a command-line script, ``simple-perms``, which suggests and can optionally apply
permission bits from a small set of "simple" permissions (0o444, 0o555, 0o644, 0o755, 0o664, 0o775) based on
the original file's permissions and type, as follows.

1. The basic suggested permission bits are 0o444.
2. If the file is a directory, or it has its user execute bit set, the suggested permissions are 0o555.
3. If the file has its user write bit set, then the suggested permissions are 0o644 or 0o755.
4. If the file has its user write bit set, then the suggested group write permissions (0o664 or 0o775) depend on the options:

   - No option or ``--ignore-group-write``: The suggestion is based on the original group write bit.
   - ``--group-write``: The suggestion always has the group write bit set.
   - ``--no-group-write``: The suggestion never has the group write bit set.

5. Additionally, the command-line interface allows the setting and masking of permission bits.

No changes are ever suggested for symbolic links.

Command-Line Interface
----------------------

.. simple_perms_clidoc::

Functions
---------

.. autofunction:: simple_perms.suggest_perms

Author, Copyright, and License
------------------------------

Copyright (c) 2022-2024 Hauke Dämpfling (haukex@zero-g.net)
at the Leibniz Institute of Freshwater Ecology and Inland Fisheries (IGB),
Berlin, Germany, https://www.igb-berlin.de/

This library is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This library is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
details.

You should have received a copy of the GNU Lesser General Public License
along with this program. If not, see https://www.gnu.org/licenses/
