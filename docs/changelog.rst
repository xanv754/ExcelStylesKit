Changelog
=========

All notable changes to ExcelTableKit are documented here.

----

.. _v2.0.1:

2.0.1 — 2026-07-01
-------------------

Changed
~~~~~~~

- Updated README documentation.
- Updated CI configuration.
- Fixed repository name in badges.

----

.. _v2.0.0:

2.0.0 — 2026-07-01
-------------------

This release is a full architectural overhaul of the library. The public API
has been redesigned around :class:`~exceltablekit.ExcelManager` and
:class:`~exceltablekit.ExcelStyle`, replacing the previous low-level cell
iteration model.

Added
~~~~~

- :class:`~exceltablekit.ExcelManager` — manages Excel file I/O, sheet
  resolution, and style dispatch.
- Header style support: :meth:`~exceltablekit.ExcelStyle.set_header_background`,
  :meth:`~exceltablekit.ExcelStyle.set_header_font`,
  :meth:`~exceltablekit.ExcelStyle.set_header_alignment`,
  :meth:`~exceltablekit.ExcelStyle.set_header_border`,
  :meth:`~exceltablekit.ExcelStyle.freeze_header`.
- :meth:`~exceltablekit.Table.display_cells` — renders the table grid in the
  terminal using ``tabulate``.
- Styling methods: font, border, alignment, background colour, and column
  width auto-fit.
- CLI entry point ``exceltablekit`` with ``info`` and ``style`` sub-commands.
- Cell validation with comprehensive unit tests covering boundary conditions.
- GitHub Actions workflows: CI (multi-version), Black formatter, and PyPI
  trusted publishing.
- Pull request template.

Changed
~~~~~~~

- Package renamed from the original name to ``exceltablekit``.
- :class:`~exceltablekit.Cell` and :class:`~exceltablekit.Table` refactored
  for clarity and consistency.
- Validation logic moved to a dedicated :class:`~exceltablekit.utils.validation.Validation`
  utility class.
- Renamed attributes and methods for PEP 8 compliance.
- Private attributes use single underscore convention (``_attr``).

Fixed
~~~~~

- Tests excluded from the distributed package build.

----

.. _v0.0.3:

0.0.3 — 2025-02-05
-------------------

Added
~~~~~

- First public release available via ``pip install exceltablekit``.
