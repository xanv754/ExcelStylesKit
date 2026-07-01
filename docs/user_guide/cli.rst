Command-Line Interface
======================

ExcelTableKit ships with a small CLI so you can apply a standard table style
to an ``.xlsx`` file without writing any Python. The entry point is
``exceltablekit``.

.. code-block:: bash

   exceltablekit [OPTIONS] COMMAND [ARGS]...

Available commands
------------------

- :ref:`cli-info` — display version information
- :ref:`cli-style` — create or style a table in an Excel file

.. _cli-info:

info
----

Prints the installed versions of ExcelTableKit and its dependencies.

.. code-block:: bash

   exceltablekit info

Example output:

.. code-block:: text

   exceltablekit version: 2.0.1
   openpyxl version:      3.1.5
   tabulate version:      0.9.0
   click version:         8.1.8

Use this command to confirm a successful installation or to record the
dependency versions for a bug report.

.. _cli-style:

style
-----

Creates (or opens) an ``.xlsx`` file, defines a table range, and applies a
background colour, header colour, and border style.

.. code-block:: bash

   exceltablekit style FILEPATH [OPTIONS]

Arguments
~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Argument
     - Description
   * - ``FILEPATH``
     - Path to the ``.xlsx`` file. The file is created if it does not exist.

Options
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Option
     - Type
     - Default
     - Description
   * - ``--start``
     - ``TEXT``
     - ``"A1"``
     - Top-left cell of the table range (e.g. ``"A1"``, ``"B3"``).
   * - ``--end``
     - ``TEXT``
     - ``"D10"``
     - Bottom-right cell of the table range (e.g. ``"D10"``, ``"F50"``).
   * - ``--header-rows``
     - ``INT``
     - ``1``
     - Number of header rows at the top of the range.
   * - ``--bg``
     - ``TEXT``
     - ``"E8F4FD"``
     - Background fill colour for body cells (6-character hex, no ``#``).
   * - ``--header-bg``
     - ``TEXT``
     - ``"1F4E79"``
     - Background fill colour for header cells (6-character hex, no ``#``).
   * - ``--border-style``
     - ``CHOICE``
     - ``"thin"``
     - Border style applied to all cells. Must be one of the 13 valid
       ``BorderStyle`` values (see below).

.. note::

   All hex colour values are supplied **without** the leading ``#`` character.

Border style choices
~~~~~~~~~~~~~~~~~~~~

The ``--border-style`` option accepts any of the following values:

``dashDot``, ``dashDotDot``, ``dashed``, ``dotted``, ``double``,
``hair``, ``medium``, ``mediumDashDot``, ``mediumDashDotDot``,
``mediumDashed``, ``slantDashDot``, ``thick``, ``thin``

Examples
--------

Create a styled table using all defaults:

.. code-block:: bash

   exceltablekit style report.xlsx

Create a table from ``A1`` to ``F50`` with 2 header rows:

.. code-block:: bash

   exceltablekit style report.xlsx \
       --start A1 \
       --end F50 \
       --header-rows 2

Apply a custom colour scheme and a thicker border:

.. code-block:: bash

   exceltablekit style report.xlsx \
       --start B2 \
       --end G30 \
       --header-bg 2E75B6 \
       --bg F2F2F2 \
       --border-style medium

Style a table in an existing file, creating the file if needed:

.. code-block:: bash

   exceltablekit style /path/to/output/sales_q2.xlsx \
       --start A1 \
       --end D100 \
       --header-rows 1 \
       --header-bg 375623 \
       --bg E2EFDA

What the style command does
---------------------------

Behind the scenes, ``exceltablekit style`` performs these steps in order:

1. ``ExcelManager(filepath)`` — opens or creates the file.
2. ``excel.set_table(start, end)`` — defines the cell range.
3. ``excel.define_header(rows)`` — marks the header rows.
4. ``ExcelStyle.set_background(bg)`` — fills body cells.
5. ``ExcelStyle.set_border(border_style)`` — applies borders to body cells.
6. ``ExcelStyle.set_header_background(header_bg)`` — fills header cells.
7. ``ExcelStyle.set_header_font(bold=True, hex_color="FFFFFF")`` — white bold
   text for the header.
8. ``ExcelStyle.set_header_border(border_style)`` — applies borders to header
   cells.
9. ``ExcelStyle.auto_fit_columns()`` — adjusts column widths to fit content.
