ExcelManager
============

.. module:: exceltablekit.excel.manager

.. class:: ExcelManager(filepath, create_sheet=False, sheetname=None)

   Manages an Excel ``.xlsx`` file: opens or creates it, resolves the target
   worksheet, owns the :class:`~exceltablekit.table.table.Table` instance, and
   persists changes to disk after every style operation.

   :param filepath: Path to the ``.xlsx`` file. Created on disk if it does not
      exist.
   :type filepath: str
   :param create_sheet: When ``True`` and *sheetname* is provided, a new
      worksheet is inserted into the workbook.
   :type create_sheet: bool
   :param sheetname: Name of the worksheet to use. ``None`` selects the active
      sheet.
   :type sheetname: str | None
   :raises ExcelSheetMissingError: If the named sheet does not exist and
      ``create_sheet`` is ``False``.

   .. rubric:: Table setup

   .. method:: set_table(start_cell, end_cell)

      Define the rectangular table range.

      :param start_cell: Top-left cell address (e.g. ``"A1"``).
      :type start_cell: str
      :param end_cell: Bottom-right cell address (e.g. ``"D10"``).
      :type end_cell: str
      :raises InvalidCellError: If either address is malformed.
      :raises InvalidColumnValueError: If a column letter exceeds ``XFD``.
      :raises InvalidRowValueError: If a row number exceeds ``1048576``.

      **Example:**

      .. code-block:: python

         excel = ExcelManager("output.xlsx")
         excel.set_table("A1", "D10")

   .. method:: define_header(rows)

      Designate the first *rows* rows of the table as header rows.

      Must be called **after** :meth:`set_table`.

      :param rows: Number of header rows.
      :type rows: int

      **Example:**

      .. code-block:: python

         excel.set_table("A1", "F20")
         excel.define_header(rows=2)   # rows 1-2 are headers

   .. rubric:: Style application

   .. method:: apply_style_body(property, value)

      Apply an openpyxl style object to the *property* attribute of every
      **body** cell, then save the file.

      :param property: Cell attribute name (e.g. ``"fill"``, ``"font"``,
         ``"alignment"``, ``"border"``).
      :type property: str
      :param value: openpyxl style object to assign.
      :raises TableNotDefinedError: If :meth:`set_table` has not been called.

      **Example:**

      .. code-block:: python

         from openpyxl.styles import PatternFill

         fill = PatternFill(fill_type="solid", fgColor="E8F4FD")
         excel.apply_style_body("fill", fill)

   .. method:: apply_style_header(property, value)

      Apply an openpyxl style object to every **header** cell, then save.

      :param property: Cell attribute name.
      :type property: str
      :param value: openpyxl style object.
      :raises TableNotDefinedError: If :meth:`set_table` has not been called.
      :raises HeaderTableNotDefinedError: If :meth:`define_header` has not
         been called.

   .. method:: apply_style_table(property, value)

      Apply a style to **all** cells (header + body), then save.

      :param property: Cell attribute name.
      :type property: str
      :param value: openpyxl style object.
      :raises TableNotDefinedError: If :meth:`set_table` has not been called.

      **Example:**

      .. code-block:: python

         from openpyxl.styles import Alignment

         alignment = Alignment(horizontal="center", vertical="center")
         excel.apply_style_table("alignment", alignment)

   .. rubric:: Utilities

   .. method:: freeze_header()

      Freeze the worksheet pane immediately below the last header row.

      The freeze cell is ``{first_column}{first_row + total_header_rows}``.

      :raises TableNotDefinedError: If :meth:`set_table` has not been called.
      :raises HeaderTableNotDefinedError: If :meth:`define_header` has not
         been called.
      :raises HeaderTableFreezeError: If openpyxl raises an exception while
         setting the freeze pane.

      **Example:**

      .. code-block:: python

         excel.set_table("A1", "D20")
         excel.define_header(rows=1)
         excel.freeze_header()
         # Freeze pane → "A2"

   .. method:: auto_fit_columns()

      Set each column's width to ``max(len(cell value)) + 2`` across all
      cells in the table (header + body), then save.

      :raises TableNotDefinedError: If :meth:`set_table` has not been called.
      :raises TableColumnWidthError: If openpyxl raises an exception.
