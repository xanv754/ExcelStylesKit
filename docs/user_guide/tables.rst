Tables, Cells, and Ranges
=========================

This page explains the internal data model that ExcelTableKit uses to
represent an Excel cell range, and shows how to interact with it directly.

Overview
--------

ExcelTableKit models a styled region of an Excel worksheet as a
:class:`~exceltablekit.Table` object that owns two lists of
:class:`~exceltablekit.Cell` objects:

- **Header cells** — created when ``define_header(rows=N)`` is called.
- **Body cells** — all remaining cells in the range.

Most users never need to create :class:`~exceltablekit.Table` or
:class:`~exceltablekit.Cell` objects directly; :class:`~exceltablekit.ExcelManager`
does that automatically. The classes are documented here for advanced use cases
and for developers who want to extend the library.

Cell
----

A :class:`~exceltablekit.Cell` represents a single Excel cell identified by a
column letter (or letters) and a row number.

.. code-block:: python

   from exceltablekit import Cell

   cell = Cell(column="B", row=3)
   print(cell.get_cell())    # "B3"
   print(cell.get_column())  # "B"
   print(cell.get_row())     # 3

Constructor
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Type
     - Description
   * - ``column``
     - ``str``
     - Excel column letter(s), case-insensitive (e.g. ``"A"``, ``"AA"``,
       ``"XFD"``). Validated against the maximum column of 16 384.
   * - ``row``
     - ``int``
     - 1-based row number. Must be between 1 and 1 048 576 inclusive.

Raises :class:`~exceltablekit.errors.InvalidColumnValueError` or
:class:`~exceltablekit.errors.InvalidRowValueError` if the values are out of
range.

Applying a style to a single cell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from openpyxl import Workbook
   from openpyxl.styles import PatternFill
   from exceltablekit import Cell

   wb = Workbook()
   ws = wb.active

   cell = Cell("C", 5)
   fill = PatternFill(fill_type="solid", fgColor="FF0000")
   cell.set_property(ws, "fill", fill)

   wb.save("output.xlsx")

Table
-----

A :class:`~exceltablekit.Table` represents a rectangular range of cells. It
is created with the four boundary values of the range and automatically
instantiates all ``Cell`` objects inside it.

.. code-block:: python

   from openpyxl import Workbook
   from exceltablekit import Table

   wb = Workbook()
   ws = wb.active

   # Table from A1 to D3 — 4 columns × 3 rows = 12 cells
   table = Table(
       worksheet=ws,
       first_column="A",
       first_row=1,
       last_column="D",
       last_row=3,
   )

Constructor parameters
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Type
     - Description
   * - ``worksheet``
     - ``Worksheet``
     - An openpyxl ``Worksheet`` object.
   * - ``first_column``
     - ``str``
     - Top-left column letter(s).
   * - ``first_row``
     - ``int``
     - Top-left row number.
   * - ``last_column``
     - ``str``
     - Bottom-right column letter(s).
   * - ``last_row``
     - ``int``
     - Bottom-right row number.

Defining headers
~~~~~~~~~~~~~~~~

After creating the table, call ``set_header`` to split the body into header
and body sections:

.. code-block:: python

   table.set_header(total_row_header=1)

   print(len(table.get_header()))  # 4  (row 1: columns A–D)
   print(len(table.get_body()))    # 8  (rows 2–3: columns A–D)

.. warning::

   Calling ``set_header`` a second time resets the split. The previous header
   cells are discarded and the table is rebuilt from scratch.

Applying styles
~~~~~~~~~~~~~~~

.. code-block:: python

   from openpyxl.styles import Font

   bold_font = Font(bold=True, color="FFFFFF")

   table.set_style_header("font", bold_font)  # header rows
   table.set_style_body("font", Font(size=10))  # body rows

Retrieving cells by row
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all body cells in row 2
   row_cells = table.get_cells_by_row(num_row=2)
   for cell in row_cells:
       print(cell.get_cell())   # "A2", "B2", "C2", "D2"

.. note::

   ``get_cells_by_row`` searches only **body** cells. After ``set_header``,
   header cells are no longer in the body list and will not be returned.

Visualising the table in the terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``display_cells()`` to print a grid of all cells (header + body) to
standard output. This is useful for debugging:

.. code-block:: python

   table.display_cells()

Example output for a 4 × 3 table with 1 header row::

   ┌──────┬──────┬──────┬──────┐
   │ A1   │ B1   │ C1   │ D1   │  ← header row
   ├──────┼──────┼──────┼──────┤
   │ A2   │ B2   │ C2   │ D2   │
   │ A3   │ B3   │ C3   │ D3   │
   └──────┴──────┴──────┴──────┘

Column and row limits
---------------------

Excel imposes hard limits on the grid size. ExcelTableKit enforces the same
limits on all cell and table construction:

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Limit
     - Value
     - Notes
   * - Maximum column
     - 16 384 (``XFD``)
     - Enforced via :class:`~exceltablekit.errors.ColumnOutOfBoundsError`
   * - Maximum row
     - 1 048 576
     - Enforced via :class:`~exceltablekit.errors.InvalidRowValueError`

Column letter ↔ number conversion
----------------------------------

The :class:`~exceltablekit.alphabet.Alphabet` utility class converts between
Excel column letters and 1-based column numbers:

.. code-block:: python

   from exceltablekit.alphabet.alphabet import Alphabet

   Alphabet.get_string_column_by_number(1)     # "A"
   Alphabet.get_string_column_by_number(27)    # "AA"
   Alphabet.get_string_column_by_number(16384) # "XFD"

   Alphabet.get_number_column_by_string("A")   # 1
   Alphabet.get_number_column_by_string("AA")  # 27
   Alphabet.get_number_column_by_string("XFD") # 16384
