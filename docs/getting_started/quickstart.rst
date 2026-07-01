Quickstart
==========

This page walks you through the most common use cases in five minutes.

Basic workflow
--------------

Every ExcelTableKit session follows the same three-step pattern:

1. **Open or create** a ``.xlsx`` file with :class:`~exceltablekit.ExcelManager`.
2. **Define the table** range and, optionally, which rows are headers.
3. **Apply styles** through :class:`~exceltablekit.ExcelStyle`.

.. code-block:: python

   from exceltablekit import ExcelManager, ExcelStyle

   # 1. Open (or create) the file
   excel = ExcelManager("output.xlsx")

   # 2. Define the table range A1:D10, with 1 header row
   excel.set_table("A1", "D10")
   excel.define_header(rows=1)

   # 3. Apply styles
   style = ExcelStyle(excel)
   style.set_header_background("1F4E79")      # dark-blue header
   style.set_header_font(bold=True, hex_color="FFFFFF")  # white bold text
   style.set_background("E8F4FD")             # light-blue body
   style.set_border()                          # thin black borders everywhere
   style.auto_fit_columns()                   # column widths fit content

The file is saved automatically after every style method call.

Styling the body
----------------

Use :class:`~exceltablekit.ExcelStyle` methods prefixed with ``set_`` (without
``header_``) to target only the body rows.

.. code-block:: python

   style.set_background("FFFACD")            # lemon chiffon background
   style.set_font(
       type="Calibri",
       size=11.0,
       bold=False,
       italic=False,
       hex_color="000000",
   )
   style.set_alignment(horizontal="center", vertical="center")
   style.set_border(
       left=True, left_style="thin",
       right=True, right_style="thin",
       top=True, top_style="thin",
       bottom=True, bottom_style="thin",
       hex_color="AAAAAA",
   )

Styling the header
------------------

Mirror methods with the ``header_`` prefix target only the designated header rows.

.. code-block:: python

   excel.set_table("A1", "F20")
   excel.define_header(rows=2)       # rows 1 and 2 are headers

   style = ExcelStyle(excel)
   style.set_header_background("2E75B6")
   style.set_header_font(bold=True, size=12.0, hex_color="FFFFFF")
   style.set_header_alignment(horizontal="center")
   style.set_header_border()
   style.freeze_header()              # freeze rows 1-2 while scrolling

Working with an existing file and a specific sheet
---------------------------------------------------

.. code-block:: python

   # Load an existing file and target the sheet named "Sales"
   excel = ExcelManager("report.xlsx", sheetname="Sales")
   excel.set_table("B2", "G50")
   excel.define_header(rows=1)

   style = ExcelStyle(excel)
   style.set_background("F2F2F2")
   style.set_border()

Creating a new sheet inside an existing file
--------------------------------------------

.. code-block:: python

   excel = ExcelManager(
       "report.xlsx",
       create_sheet=True,
       sheetname="Q2 Results",
   )

If the file does not exist yet it is created on the fly. If the sheet already
exists inside the file, the existing one is reused.

Applying a style to the whole table at once
-------------------------------------------

Use ``apply_style_table`` on the manager directly when you want the same openpyxl
style object to hit every cell (header + body) without constructing an
:class:`~exceltablekit.ExcelStyle` instance.

.. code-block:: python

   from openpyxl.styles import Alignment

   excel = ExcelManager("output.xlsx")
   excel.set_table("A1", "D10")
   excel.define_header(rows=1)
   excel.apply_style_table("alignment", Alignment(horizontal="center"))

Using the CLI
-------------

ExcelTableKit ships with a small command-line interface so you can apply a
standard style without writing any Python:

.. code-block:: bash

   exceltablekit style output.xlsx \
       --start A1 \
       --end D10 \
       --header-rows 1 \
       --header-bg 1F4E79 \
       --bg E8F4FD \
       --border-style thin

See :doc:`../user_guide/cli` for the full CLI reference.

.. note::

   All hex color values are passed **without** the leading ``#`` character.
   For example, use ``"1F4E79"`` rather than ``"#1F4E79"``.
