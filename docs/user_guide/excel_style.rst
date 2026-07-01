ExcelStyle
==========

:class:`~exceltablekit.ExcelStyle` is the high-level styling façade of
ExcelTableKit. It wraps openpyxl style objects (``PatternFill``, ``Border``,
``Side``, ``Font``, ``Alignment``) so you never have to construct them
yourself.

Every method in :class:`~exceltablekit.ExcelStyle` accepts plain Python values
(hex strings, booleans, floats) and internally converts them to the correct
openpyxl objects before delegating to
:class:`~exceltablekit.ExcelManager`.

Creating an ExcelStyle instance
--------------------------------

:class:`~exceltablekit.ExcelStyle` wraps an existing
:class:`~exceltablekit.ExcelManager`:

.. code-block:: python

   from exceltablekit import ExcelManager, ExcelStyle

   excel = ExcelManager("output.xlsx")
   excel.set_table("A1", "D10")
   excel.define_header(rows=1)

   style = ExcelStyle(excel)

.. important::

   Call ``set_table`` (and optionally ``define_header``) on the manager
   **before** creating the style instance, or before calling any style method.
   The style object does not keep its own copy of the table — it reads through
   the manager on every call.

Body styling
------------

The following methods apply styles to the **body** rows of the table (all
rows that are *not* headers).

set_background
~~~~~~~~~~~~~~

Applies a solid background fill colour to all body cells.

.. code-block:: python

   style.set_background("E8F4FD")   # light blue
   style.set_background("FFFACD")   # lemon chiffon
   style.set_background("FFFFFF")   # white

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Parameter
     - Type
     - Description
   * - ``hex_color``
     - ``str``
     - 6-character RGB hex string **without** the leading ``#``
       (e.g. ``"E8F4FD"``).

set_font
~~~~~~~~

Applies a font style to all body cells.

.. code-block:: python

   style.set_font(
       type="Calibri",
       size=11.0,
       bold=False,
       italic=False,
       hex_color="000000",
   )

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Default
     - Description
   * - ``type``
     - ``str``
     - ``"Time New Roman"``
     - Font family name.
   * - ``size``
     - ``float``
     - ``10.0``
     - Font size in points.
   * - ``bold``
     - ``bool``
     - ``False``
     - Bold text.
   * - ``italic``
     - ``bool``
     - ``False``
     - Italic text.
   * - ``hex_color``
     - ``str``
     - ``"FFFF0000"``
     - 6- or 8-character ARGB hex string for the font colour. The leading
       ``FF`` is the alpha channel (fully opaque).

.. note::

   openpyxl uses ARGB colour values for fonts (8 hex digits). If you supply
   a 6-digit value, omit the alpha prefix — openpyxl will apply it as-is.
   Use ``"FF000000"`` for opaque black or just ``"000000"`` depending on
   the openpyxl version in use.

set_alignment
~~~~~~~~~~~~~

Applies cell text alignment to all body cells.

.. code-block:: python

   style.set_alignment(
       horizontal="center",
       vertical="center",
       wrap_text=True,
   )

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Default
     - Description
   * - ``horizontal``
     - ``str``
     - ``"left"``
     - Horizontal alignment. One of: ``"left"``, ``"center"``, ``"right"``,
       ``"fill"``, ``"justify"``, ``"centerContinuous"``, ``"distributed"``.
   * - ``vertical``
     - ``str``
     - ``"center"``
     - Vertical alignment. One of: ``"top"``, ``"center"``, ``"bottom"``,
       ``"justify"``, ``"distributed"``.
   * - ``wrap_text``
     - ``bool``
     - ``False``
     - Wrap long text within the cell.

set_border
~~~~~~~~~~

Applies a border to all body cells. Each of the four edges (left, right, top,
bottom) can be enabled or disabled independently and given its own border style.

.. code-block:: python

   # All four edges, thin black border (defaults)
   style.set_border()

   # Custom: only left and right edges, medium style, grey colour
   style.set_border(
       left=True, left_style="medium",
       right=True, right_style="medium",
       top=False,
       bottom=False,
       hex_color="888888",
   )

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 50

   * - Parameter
     - Type
     - Default
     - Description
   * - ``left``
     - ``bool``
     - ``True``
     - Enable left edge border.
   * - ``left_style``
     - ``BorderStyle``
     - ``"thin"``
     - Style for the left edge.
   * - ``right``
     - ``bool``
     - ``True``
     - Enable right edge border.
   * - ``right_style``
     - ``BorderStyle``
     - ``"thin"``
     - Style for the right edge.
   * - ``top``
     - ``bool``
     - ``True``
     - Enable top edge border.
   * - ``top_style``
     - ``BorderStyle``
     - ``"thin"``
     - Style for the top edge.
   * - ``bottom``
     - ``bool``
     - ``True``
     - Enable bottom edge border.
   * - ``bottom_style``
     - ``BorderStyle``
     - ``"thin"``
     - Style for the bottom edge.
   * - ``hex_color``
     - ``str``
     - ``"000000"``
     - Border colour as a 6-character hex string.

See :ref:`border-styles` for the full list of accepted ``BorderStyle`` values.

Header styling
--------------

Every body method has a ``set_header_*`` counterpart that targets **header**
rows only. Their signatures are identical to their body equivalents.

``define_header`` must have been called on the manager before these methods
are used, otherwise :class:`~exceltablekit.errors.HeaderTableNotDefinedError`
is raised.

set_header_background
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   style.set_header_background("1F4E79")   # dark blue
   style.set_header_background("2E75B6")   # medium blue

set_header_font
~~~~~~~~~~~~~~~

.. code-block:: python

   style.set_header_font(
       type="Calibri",
       size=12.0,
       bold=True,
       hex_color="FFFFFF",   # white text
   )

set_header_alignment
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   style.set_header_alignment(
       horizontal="center",
       vertical="center",
   )

set_header_border
~~~~~~~~~~~~~~~~~

.. code-block:: python

   style.set_header_border(bottom_style="medium")   # emphasise the header bottom

freeze_header
~~~~~~~~~~~~~

Freezes the worksheet pane immediately below the last header row.

.. code-block:: python

   excel.set_table("A1", "D20")
   excel.define_header(rows=2)

   style = ExcelStyle(excel)
   style.freeze_header()
   # Freeze pane is set at A3

The freeze cell is ``{first_column}{first_row + total_header_rows}``. For a
table starting at ``B3`` with 1 header row the freeze pane is ``B4``.

Column auto-fit
---------------

auto_fit_columns
~~~~~~~~~~~~~~~~

Adjusts each column's width to fit the longest cell value in that column
(plus 2 characters of padding).

.. code-block:: python

   style.auto_fit_columns()

This iterates over all cells (header + body) so even header text influences
the final width.

.. _border-styles:

Available border styles
-----------------------

The ``BorderStyle`` type is a ``Literal`` union of the following 13 values:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Value
     - Visual result
   * - ``"thin"``
     - Thin solid line *(default)*
   * - ``"medium"``
     - Medium-weight solid line
   * - ``"thick"``
     - Thick solid line
   * - ``"double"``
     - Double solid line
   * - ``"hair"``
     - Hairline (thinnest possible)
   * - ``"dashed"``
     - Short dashes
   * - ``"dotted"``
     - Dots
   * - ``"dashDot"``
     - Alternating dash–dot
   * - ``"dashDotDot"``
     - Alternating dash–dot–dot
   * - ``"mediumDashed"``
     - Medium-weight dashes
   * - ``"mediumDashDot"``
     - Medium-weight dash–dot
   * - ``"mediumDashDotDot"``
     - Medium-weight dash–dot–dot
   * - ``"slantDashDot"``
     - Slanted dash–dot

Error handling
--------------

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Error
     - When it is raised
   * - :class:`~exceltablekit.errors.TableNotDefinedError`
     - ``set_table`` was not called before a body or table style method
   * - :class:`~exceltablekit.errors.HeaderTableNotDefinedError`
     - ``define_header`` was not called before a header style method
   * - :class:`~exceltablekit.errors.TableBackgroundError`
     - Background fill failed on the body
   * - :class:`~exceltablekit.errors.TableFontError`
     - Font style failed on the body
   * - :class:`~exceltablekit.errors.TableAlignmentError`
     - Alignment failed on the body
   * - :class:`~exceltablekit.errors.TableBorderError`
     - Border failed on the body
   * - :class:`~exceltablekit.errors.HeaderTableBackgroundError`
     - Background fill failed on the header
   * - :class:`~exceltablekit.errors.HeaderTableFontError`
     - Font style failed on the header
   * - :class:`~exceltablekit.errors.HeaderTableAlignmentError`
     - Alignment failed on the header
   * - :class:`~exceltablekit.errors.HeaderTableBorderError`
     - Border failed on the header
   * - :class:`~exceltablekit.errors.HeaderTableFreezeError`
     - Freeze panes failed
   * - :class:`~exceltablekit.errors.TableColumnWidthError`
     - Auto-fit column widths failed
