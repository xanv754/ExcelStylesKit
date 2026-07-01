Cell
====

.. module:: exceltablekit.table.cell

.. class:: Cell(column, row)

   Represents a single Excel cell identified by a column letter string and a
   1-based integer row number.

   :class:`Cell` instances are created automatically by
   :class:`~exceltablekit.table.table.Table`. You rarely need to instantiate
   them directly unless you are extending the library.

   :param column: Excel column letter(s), case-insensitive
      (e.g. ``"A"``, ``"AB"``, ``"XFD"``). Must not exceed column 16 384.
   :type column: str
   :param row: 1-based row number. Must be between 1 and 1 048 576 inclusive.
   :type row: int
   :raises InvalidColumnValueError: If *column* is not a non-empty alphabetic
      string, or the resulting column number exceeds 16 384.
   :raises InvalidRowValueError: If *row* is not a positive integer, or
      exceeds 1 048 576.

   **Example:**

   .. code-block:: python

      from exceltablekit import Cell

      cell = Cell("B", 5)
      print(cell.get_cell())    # "B5"
      print(cell.get_column())  # "B"
      print(cell.get_row())     # 5

   .. rubric:: Methods

   .. method:: get_cell()

      Return the cell address in ``"A1"`` notation.

      :returns: Cell address string (e.g. ``"B5"``).
      :rtype: str

   .. method:: get_column()

      Return the column letter(s).

      :returns: Column string, always uppercase (e.g. ``"B"``).
      :rtype: str

   .. method:: get_row()

      Return the row number.

      :returns: 1-based row integer.
      :rtype: int

   .. method:: set_property(worksheet, property, value)

      Set a style attribute on the underlying openpyxl cell object.

      :param worksheet: The openpyxl ``Worksheet`` that contains this cell.
      :type worksheet: openpyxl.worksheet.worksheet.Worksheet
      :param property: The cell attribute to set (e.g. ``"fill"``, ``"font"``,
         ``"alignment"``, ``"border"``).
      :type property: str
      :param value: The value to assign — typically an openpyxl style object.

      **Example:**

      .. code-block:: python

         from openpyxl import Workbook
         from openpyxl.styles import PatternFill
         from exceltablekit import Cell

         wb = Workbook()
         ws = wb.active

         cell = Cell("C", 3)
         fill = PatternFill(fill_type="solid", fgColor="FFFF00")
         cell.set_property(ws, "fill", fill)

         wb.save("output.xlsx")
