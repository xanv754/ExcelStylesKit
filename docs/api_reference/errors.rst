Errors
======

.. module:: exceltablekit.errors

All exceptions raised by ExcelTableKit inherit from the base class
:class:`ExcelTableKitError` and are importable from ``exceltablekit.errors``.

.. code-block:: python

   from exceltablekit.errors import (
       TableNotDefinedError,
       HeaderTableNotDefinedError,
       InvalidCellError,
       ExcelSheetMissingError,
       # ... etc.
   )

Base exception
--------------

.. exception:: ExcelTableKitError

   Base class for all exceptions in ExcelTableKit. Inherits from the built-in
   ``Exception``.

   .. code-block:: python

      from exceltablekit.errors import ExcelTableKitError

      try:
          excel.set_table("ZZZ1", "A1")
      except ExcelTableKitError as e:
          print(f"ExcelTableKit error: {e}")

Cell validation errors
----------------------

Raised when a cell address, column, or row value fails validation.

.. exception:: InvalidCellError(value)

   The cell address string is malformed (does not match the pattern
   ``[A-Za-z]+[0-9]+``, is longer than 10 characters, or the embedded column
   / row values are out of bounds).

   :param value: The invalid cell value that was supplied.

   **Raised by:** :meth:`~exceltablekit.ExcelManager.set_table`,
   :class:`~exceltablekit.utils.validation.Validation`.

   .. code-block:: python

      from exceltablekit import ExcelManager
      from exceltablekit.errors import InvalidCellError

      excel = ExcelManager("output.xlsx")
      try:
          excel.set_table("!1", "D10")    # invalid column character
      except InvalidCellError as e:
          print(e)

.. exception:: InvalidColumnValueError(value, reason)

   The column value is not a non-empty alphabetic string, or the resulting
   column number exceeds ``COLUMN_MAX`` (16 384 / ``XFD``).

   :param value: The invalid value supplied.
   :param reason: Human-readable explanation of why the value was rejected.

   **Raised by:** :class:`~exceltablekit.table.cell.Cell`,
   :class:`~exceltablekit.utils.validation.Validation`.

.. exception:: ColumnOutOfBoundsError(value)

   The integer column index exceeds ``COLUMN_MAX`` (16 384).

   :param value: The out-of-range integer.

   **Raised by:** :class:`~exceltablekit.alphabet.alphabet.Alphabet`.

.. exception:: InvalidRowValueError(value, reason)

   The row value is not a positive integer, or exceeds ``ROW_MAX``
   (1 048 576).

   :param value: The invalid value supplied.
   :param reason: Human-readable explanation.

   **Raised by:** :class:`~exceltablekit.table.cell.Cell`,
   :class:`~exceltablekit.utils.validation.Validation`.

File errors
-----------

.. exception:: ExcelSheetMissingError(sheetname)

   The named worksheet does not exist in the workbook, and ``create_sheet``
   was not set to ``True``.

   :param sheetname: The sheet name that was looked up.

   **Raised by:** :class:`~exceltablekit.ExcelManager`.

   .. code-block:: python

      from exceltablekit import ExcelManager
      from exceltablekit.errors import ExcelSheetMissingError

      try:
          excel = ExcelManager("report.xlsx", sheetname="NonExistentSheet")
      except ExcelSheetMissingError as e:
          print(e)

Table state errors
------------------

These are precondition errors raised when methods are called in the wrong
order.

.. exception:: TableNotDefinedError()

   A style or utility method was called before
   :meth:`~exceltablekit.ExcelManager.set_table`.

   .. code-block:: python

      from exceltablekit import ExcelManager, ExcelStyle
      from exceltablekit.errors import TableNotDefinedError

      excel = ExcelManager("output.xlsx")
      style = ExcelStyle(excel)
      try:
          style.set_background("E8F4FD")   # set_table was not called
      except TableNotDefinedError:
          print("Call set_table() first.")

.. exception:: HeaderTableNotDefinedError()

   A header style method was called before
   :meth:`~exceltablekit.ExcelManager.define_header`.

   .. code-block:: python

      from exceltablekit.errors import HeaderTableNotDefinedError

      excel.set_table("A1", "D10")
      # define_header not called
      try:
          style.set_header_background("1F4E79")
      except HeaderTableNotDefinedError:
          print("Call define_header() first.")

Style application errors
------------------------

These are raised when openpyxl raises an exception internally during a style
operation. They wrap the original exception.

**Body style errors:**

.. exception:: TableBackgroundError(error)

   Background fill failed on body cells.

.. exception:: TableFontError(error)

   Font style failed on body cells.

.. exception:: TableAlignmentError(error)

   Alignment failed on body cells.

.. exception:: TableBorderError(error)

   Border failed on body cells.

**Header style errors:**

.. exception:: HeaderTableBackgroundError(error)

   Background fill failed on header cells.

.. exception:: HeaderTableFontError(error)

   Font style failed on header cells.

.. exception:: HeaderTableAlignmentError(error)

   Alignment failed on header cells.

.. exception:: HeaderTableBorderError(error)

   Border failed on header cells.

.. exception:: HeaderTableFreezeError(error)

   Freeze panes operation failed.

**Utility errors:**

.. exception:: TableColumnWidthError(error)

   Auto-fit column widths failed.

Error hierarchy
---------------

.. code-block:: text

   Exception
   └── ExcelTableKitError
       ├── InvalidCellError
       ├── InvalidColumnValueError
       ├── ColumnOutOfBoundsError
       ├── InvalidRowValueError
       ├── ExcelSheetMissingError
       ├── TableNotDefinedError
       ├── HeaderTableNotDefinedError
       ├── TableBackgroundError
       ├── TableFontError
       ├── TableAlignmentError
       ├── TableBorderError
       ├── HeaderTableBackgroundError
       ├── HeaderTableFontError
       ├── HeaderTableAlignmentError
       ├── HeaderTableBorderError
       ├── HeaderTableFreezeError
       └── TableColumnWidthError
