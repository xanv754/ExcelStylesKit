Table
=====

.. module:: exceltablekit.table.table

.. class:: Table(worksheet, first_column, first_row, last_column, last_row)

   Represents a rectangular range of cells in an Excel worksheet. The range
   is modelled as two lists of :class:`~exceltablekit.table.cell.Cell` objects:
   header cells and body cells.

   :class:`Table` objects are created internally by
   :class:`~exceltablekit.ExcelManager` when you call
   :meth:`~exceltablekit.ExcelManager.set_table`. You rarely need to
   instantiate this class directly.

   :param worksheet: The openpyxl ``Worksheet`` that owns this table.
   :type worksheet: openpyxl.worksheet.worksheet.Worksheet
   :param first_column: Top-left column letter(s) (e.g. ``"A"``).
   :type first_column: str
   :param first_row: Top-left row number.
   :type first_row: int
   :param last_column: Bottom-right column letter(s) (e.g. ``"D"``).
   :type last_column: str
   :param last_row: Bottom-right row number.
   :type last_row: int
   :raises InvalidColumnValueError: If a column letter is invalid or exceeds
      ``XFD``.
   :raises InvalidRowValueError: If a row number is ≤ 0 or exceeds
      1 048 576.

   On construction, all ``Cell`` objects for the range are created and stored
   in ``_body``. Column iteration is inner (A → D), row iteration is outer
   (1 → N).

   **Example:**

   .. code-block:: python

      from openpyxl import Workbook
      from exceltablekit import Table

      wb = Workbook()
      ws = wb.active

      table = Table(ws, "A", 1, "D", 3)  # 4 cols × 3 rows = 12 cells
      print(len(table.get_body()))        # 12

   .. rubric:: Header setup

   .. method:: set_header(total_row_header)

      Split the cell range into header and body sections.

      The first *total_row_header* rows of the current body list are moved
      into the header list. The remaining rows form the new body list.

      :param total_row_header: Number of rows to designate as headers.
      :type total_row_header: int

      **Example:**

      .. code-block:: python

         table.set_header(1)
         print(len(table.get_header()))  # 4  (row 1, columns A–D)
         print(len(table.get_body()))    # 8  (rows 2–3)

   .. rubric:: Style application

   .. method:: set_style_header(property, value)

      Apply a style property to all header cells.

      :param property: Cell attribute name (e.g. ``"fill"``, ``"font"``).
      :type property: str
      :param value: The openpyxl style object to assign.

   .. method:: set_style_body(property, value)

      Apply a style property to all body cells.

      :param property: Cell attribute name.
      :type property: str
      :param value: The openpyxl style object to assign.

   .. rubric:: Accessors

   .. method:: get_body()

      Return the list of body cells.

      :returns: All non-header cells in the table.
      :rtype: list[Cell]

   .. method:: get_header()

      Return the list of header cells.

      :returns: Header cells, or an empty list if :meth:`set_header` has not
         been called.
      :rtype: list[Cell]

   .. method:: get_first_column()

      Return the first column letter.

      :returns: Top-left column string (e.g. ``"A"``).
      :rtype: str

   .. method:: get_first_row()

      Return the first row number.

      :returns: Top-left row integer.
      :rtype: int

   .. method:: get_total_row_headers()

      Return the number of header rows.

      :returns: ``0`` if :meth:`set_header` has not been called.
      :rtype: int

   .. method:: get_cells_by_row(num_row)

      Return all **body** cells in a given row number.

      :param num_row: The absolute row number to look up (1-based).
      :type num_row: int
      :returns: All body cells whose row equals *num_row*.
      :rtype: list[Cell]
      :raises ValueError: If *num_row* exceeds the table's last row.

      .. note::

         Only body cells are searched. After :meth:`set_header`, header cells
         are no longer in the body list and will not be returned.

      **Example:**

      .. code-block:: python

         table = Table(ws, "A", 1, "D", 3)
         table.set_header(1)
         cells = table.get_cells_by_row(2)
         # Returns [Cell("A",2), Cell("B",2), Cell("C",2), Cell("D",2)]

   .. rubric:: Display

   .. method:: display_cells()

      Print a ``tabulate`` grid of all cells (header + body) to standard
      output, organised by row. Useful for debugging.

      **Example output** for a 4 × 3 table with 1 header row::

         ┌──────┬──────┬──────┬──────┐
         │ A1   │ B1   │ C1   │ D1   │
         ├──────┼──────┼──────┼──────┤
         │ A2   │ B2   │ C2   │ D2   │
         │ A3   │ B3   │ C3   │ D3   │
         └──────┴──────┴──────┴──────┘
