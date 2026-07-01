ExcelManager
============

:class:`~exceltablekit.ExcelManager` is the core class of ExcelTableKit. It owns
the openpyxl ``Workbook`` and ``Worksheet`` objects, handles file I/O, and
exposes a low-level style-application API that higher-level facades (such as
:class:`~exceltablekit.ExcelStyle`) build on top of.

.. note::

   Most users interact with :class:`~exceltablekit.ExcelStyle` for styling and
   only use :class:`~exceltablekit.ExcelManager` directly for file/table setup
   (``set_table``, ``define_header``, etc.).

Opening and creating files
--------------------------

.. code-block:: python

   from exceltablekit import ExcelManager

   # Create a brand-new file (or overwrite the active sheet of an existing one)
   excel = ExcelManager("output.xlsx")

   # Load an existing file, target the active sheet
   excel = ExcelManager("report.xlsx")

   # Load an existing file and target a specific named sheet
   excel = ExcelManager("report.xlsx", sheetname="Q1 Data")

   # Add a new sheet to an existing file
   excel = ExcelManager("report.xlsx", create_sheet=True, sheetname="Q2 Data")

Constructor parameters
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Default
     - Description
   * - ``filepath``
     - ``str``
     - *(required)*
     - Path to the ``.xlsx`` file. The file is created if it does not exist.
   * - ``sheetname``
     - ``str | None``
     - ``None``
     - Name of the worksheet to use. When ``None``, the active sheet is used.
   * - ``create_sheet``
     - ``bool``
     - ``False``
     - When ``True`` and ``sheetname`` is provided, a new sheet with that name
       is inserted into the workbook (even if the file already exists).

.. important::

   Passing ``create_sheet=True`` without a ``sheetname`` has no effect — the
   active sheet is used instead.

Worksheet resolution logic
~~~~~~~~~~~~~~~~~~~~~~~~~~

The table below summarises which worksheet is selected depending on the
arguments supplied:

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - ``sheetname``
     - ``create_sheet``
     - File exists?
     - Result
   * - ``None``
     - any
     - any
     - Active sheet is used. Raises :class:`~exceltablekit.errors.ExcelSheetMissingError`
       if no active sheet exists.
   * - ``"Name"``
     - ``True``
     - any
     - A new sheet named ``"Name"`` is created.
   * - ``"Name"``
     - ``False``
     - Yes
     - Existing sheet ``"Name"`` is used. Raises
       :class:`~exceltablekit.errors.ExcelSheetMissingError` if it does not exist.
   * - ``"Name"``
     - ``False``
     - No
     - A new sheet named ``"Name"`` is created (file is new).

Defining the table
------------------

Before any style or display operation you must define the cell range that
represents your table.

.. code-block:: python

   excel.set_table("A1", "D10")

Both arguments follow the standard Excel cell notation (column letters +
row number, case-insensitive). The range is inclusive on both ends, so
``"A1"`` to ``"D10"`` covers columns A–D and rows 1–10 (40 cells total).

.. list-table:: ``set_table`` parameters
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Type
     - Description
   * - ``start_cell``
     - ``str``
     - Top-left cell of the table (e.g. ``"A1"``, ``"B3"``).
   * - ``end_cell``
     - ``str``
     - Bottom-right cell of the table (e.g. ``"D10"``, ``"XFD1048576"``).

Raises :class:`~exceltablekit.errors.InvalidCellError` if either address is
malformed or out of Excel bounds.

Defining header rows
--------------------

After calling ``set_table``, call ``define_header`` to designate the first
*N* rows of the range as header rows. Header and body cells are then styled
independently.

.. code-block:: python

   excel.set_table("A1", "F20")
   excel.define_header(rows=1)   # row 1 is the header
   # or
   excel.define_header(rows=2)   # rows 1 and 2 are headers

.. list-table:: ``define_header`` parameters
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Type
     - Description
   * - ``rows``
     - ``int``
     - Number of rows at the top of the table that are treated as headers.

.. note::

   ``define_header`` must be called **after** ``set_table``. Calling header
   style methods (``apply_style_header``, ``freeze_header``, etc.) without
   having called ``define_header`` raises
   :class:`~exceltablekit.errors.HeaderTableNotDefinedError`.

Low-level style application
---------------------------

These methods apply an openpyxl style object directly to a cell property.
They are intended for advanced use cases; prefer :class:`~exceltablekit.ExcelStyle`
for everyday styling.

``apply_style_body(property, value)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applies ``value`` to the ``property`` attribute of every **body** cell.

.. code-block:: python

   from openpyxl.styles import PatternFill

   fill = PatternFill(fill_type="solid", fgColor="FFFF00")
   excel.apply_style_body("fill", fill)

``apply_style_header(property, value)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Same as above but targets **header** cells only.

.. code-block:: python

   from openpyxl.styles import Font

   font = Font(bold=True, color="FFFFFF")
   excel.apply_style_header("font", font)

``apply_style_table(property, value)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applies the style to **all** cells (header + body) in a single call.

.. code-block:: python

   from openpyxl.styles import Alignment

   alignment = Alignment(horizontal="center", vertical="center")
   excel.apply_style_table("alignment", alignment)

Utility methods
---------------

``freeze_header()``
~~~~~~~~~~~~~~~~~~~

Freezes the pane immediately below the last header row so that header rows
remain visible when scrolling. Requires both ``set_table`` and
``define_header`` to have been called first.

.. code-block:: python

   excel.set_table("A1", "D20")
   excel.define_header(rows=2)
   excel.freeze_header()
   # Freeze pane is set at A3 (below the 2-row header)

The freeze cell is calculated as ``{first_column}{first_row + total_header_rows}``.
For a table starting at ``B3`` with 1 header row, the freeze pane is ``B4``.

``auto_fit_columns()``
~~~~~~~~~~~~~~~~~~~~~~

Iterates over all cells (header + body) and sets each column's width to
``max(len(cell_value)) + 2`` characters. This gives a comfortable fit for
most content.

.. code-block:: python

   excel.set_table("A1", "D10")
   excel.auto_fit_columns()

.. note::

   ``auto_fit_columns`` works on the string representation of cell values.
   For formatted numbers or dates, the visible string in Excel may differ
   from the raw value length.

Error handling
--------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Error
     - When it is raised
   * - :class:`~exceltablekit.errors.InvalidCellError`
     - Cell address is malformed or out of bounds
   * - :class:`~exceltablekit.errors.InvalidColumnValueError`
     - Column letter(s) invalid or exceed column 16384 (XFD)
   * - :class:`~exceltablekit.errors.InvalidRowValueError`
     - Row number is ≤ 0 or exceeds 1 048 576
   * - :class:`~exceltablekit.errors.ExcelSheetMissingError`
     - Named sheet does not exist in the workbook
   * - :class:`~exceltablekit.errors.TableNotDefinedError`
     - A style or utility method was called before ``set_table``
   * - :class:`~exceltablekit.errors.HeaderTableNotDefinedError`
     - A header method was called before ``define_header``
