ExcelStyle
==========

.. module:: exceltablekit.excel.styles

.. class:: ExcelStyle(excel)

   High-level styling façade over :class:`~exceltablekit.ExcelManager`.
   Constructs openpyxl style objects from plain Python values and delegates
   to the manager for application and file persistence.

   :param excel: A configured :class:`~exceltablekit.ExcelManager` instance
      with a table already defined via :meth:`~exceltablekit.ExcelManager.set_table`.
   :type excel: ExcelManager

   .. rubric:: Body styling

   .. method:: set_background(hex_color)

      Apply a solid background fill to all **body** cells.

      :param hex_color: 6-character RGB hex string without ``#``
         (e.g. ``"E8F4FD"``).
      :type hex_color: str
      :raises TableNotDefinedError: If the table is not defined.
      :raises TableBackgroundError: If openpyxl fails to apply the fill.

      **Example:**

      .. code-block:: python

         style.set_background("E8F4FD")

   .. method:: set_font(type="Time New Roman", size=10.0, bold=False, italic=False, hex_color="FFFF0000")

      Apply a font style to all **body** cells.

      :param type: Font family name.
      :type type: str
      :param size: Font size in points.
      :type size: float
      :param bold: Bold text.
      :type bold: bool
      :param italic: Italic text.
      :type italic: bool
      :param hex_color: 8-character ARGB or 6-character RGB hex string for
         the font colour.
      :type hex_color: str
      :raises TableNotDefinedError: If the table is not defined.
      :raises TableFontError: If openpyxl fails to apply the font.

      **Example:**

      .. code-block:: python

         style.set_font(type="Calibri", size=11.0, bold=True, hex_color="000000")

   .. method:: set_alignment(horizontal="left", vertical="center", wrap_text=False)

      Apply text alignment to all **body** cells.

      :param horizontal: Horizontal alignment.
         One of: ``"left"``, ``"center"``, ``"right"``, ``"fill"``,
         ``"justify"``, ``"centerContinuous"``, ``"distributed"``.
      :type horizontal: str
      :param vertical: Vertical alignment.
         One of: ``"top"``, ``"center"``, ``"bottom"``, ``"justify"``,
         ``"distributed"``.
      :type vertical: str
      :param wrap_text: Wrap text within the cell.
      :type wrap_text: bool
      :raises TableNotDefinedError: If the table is not defined.
      :raises TableAlignmentError: If openpyxl fails to apply the alignment.

      **Example:**

      .. code-block:: python

         style.set_alignment(horizontal="center", vertical="center")

   .. method:: set_border(left=True, left_style="thin", right=True, right_style="thin", top=True, top_style="thin", bottom=True, bottom_style="thin", hex_color="000000")

      Apply a border to all **body** cells.

      :param left: Enable left edge.
      :type left: bool
      :param left_style: Style for the left edge.
      :type left_style: BorderStyle
      :param right: Enable right edge.
      :type right: bool
      :param right_style: Style for the right edge.
      :type right_style: BorderStyle
      :param top: Enable top edge.
      :type top: bool
      :param top_style: Style for the top edge.
      :type top_style: BorderStyle
      :param bottom: Enable bottom edge.
      :type bottom: bool
      :param bottom_style: Style for the bottom edge.
      :type bottom_style: BorderStyle
      :param hex_color: 6-character RGB hex colour for all border edges.
      :type hex_color: str
      :raises TableNotDefinedError: If the table is not defined.
      :raises TableBorderError: If openpyxl fails to apply the border.

      **Example:**

      .. code-block:: python

         style.set_border(bottom_style="medium", hex_color="444444")

   .. method:: auto_fit_columns()

      Adjust column widths to fit the longest cell value (header + body)
      plus 2 characters of padding.

      :raises TableNotDefinedError: If the table is not defined.
      :raises TableColumnWidthError: If openpyxl fails to set column widths.

   .. rubric:: Header styling

   .. method:: set_header_background(hex_color)

      Apply a solid background fill to all **header** cells.

      :param hex_color: 6-character RGB hex string without ``#``.
      :type hex_color: str
      :raises TableNotDefinedError: If the table is not defined.
      :raises HeaderTableNotDefinedError: If no header rows have been defined.
      :raises HeaderTableBackgroundError: If openpyxl fails to apply the fill.

      **Example:**

      .. code-block:: python

         style.set_header_background("1F4E79")

   .. method:: set_header_font(type="Time New Roman", size=10.0, bold=False, italic=False, hex_color="FFFF0000")

      Apply a font style to all **header** cells.

      :param type: Font family name.
      :type type: str
      :param size: Font size in points.
      :type size: float
      :param bold: Bold text.
      :type bold: bool
      :param italic: Italic text.
      :type italic: bool
      :param hex_color: 8-character ARGB or 6-character RGB hex string.
      :type hex_color: str
      :raises TableNotDefinedError: If the table is not defined.
      :raises HeaderTableNotDefinedError: If no header rows have been defined.
      :raises HeaderTableFontError: If openpyxl fails to apply the font.

      **Example:**

      .. code-block:: python

         style.set_header_font(bold=True, size=12.0, hex_color="FFFFFF")

   .. method:: set_header_alignment(horizontal="left", vertical="center", wrap_text=False)

      Apply text alignment to all **header** cells.

      :param horizontal: Horizontal alignment.
      :type horizontal: str
      :param vertical: Vertical alignment.
      :type vertical: str
      :param wrap_text: Wrap text within the cell.
      :type wrap_text: bool
      :raises TableNotDefinedError: If the table is not defined.
      :raises HeaderTableNotDefinedError: If no header rows have been defined.
      :raises HeaderTableAlignmentError: If openpyxl fails to apply the
         alignment.

   .. method:: set_header_border(left=True, left_style="thin", right=True, right_style="thin", top=True, top_style="thin", bottom=True, bottom_style="thin", hex_color="000000")

      Apply a border to all **header** cells. Same parameters as
      :meth:`set_border`.

      :raises TableNotDefinedError: If the table is not defined.
      :raises HeaderTableNotDefinedError: If no header rows have been defined.
      :raises HeaderTableBorderError: If openpyxl fails to apply the border.

   .. method:: freeze_header()

      Freeze the pane below the last header row.

      :raises TableNotDefinedError: If the table is not defined.
      :raises HeaderTableNotDefinedError: If no header rows have been defined.
      :raises HeaderTableFreezeError: If openpyxl fails to set the freeze
         pane.

      **Example:**

      .. code-block:: python

         excel.set_table("A1", "D20")
         excel.define_header(rows=2)
         style = ExcelStyle(excel)
         style.freeze_header()
         # Freeze pane is set at "A3"
