Constants and Types
===================

.. module:: exceltablekit.constants

ExcelTableKit exposes a small set of constants and type aliases that are used
throughout the library. They are importable directly from
``exceltablekit.constants``.

.. code-block:: python

   from exceltablekit.constants import BorderStyle, COLUMN_MAX, ROW_MAX

BorderStyle
-----------

.. data:: BorderStyle

   A ``Literal`` type alias listing the 13 border styles supported by Excel
   (and openpyxl). Used as the type for all ``*_style`` parameters in
   :meth:`~exceltablekit.ExcelStyle.set_border` and
   :meth:`~exceltablekit.ExcelStyle.set_header_border`.

   .. code-block:: python

      from exceltablekit.constants import BorderStyle

   **Accepted values:**

   .. list-table::
      :header-rows: 1
      :widths: 35 65

      * - Value
        - Description
      * - ``"thin"``
        - Thin solid line *(default for all border methods)*
      * - ``"medium"``
        - Medium-weight solid line
      * - ``"thick"``
        - Thick solid line
      * - ``"double"``
        - Two parallel thin lines
      * - ``"hair"``
        - Hairline — thinnest visible line
      * - ``"dashed"``
        - Short dashes
      * - ``"dotted"``
        - Dots
      * - ``"dashDot"``
        - Alternating dash–dot pattern
      * - ``"dashDotDot"``
        - Alternating dash–dot–dot pattern
      * - ``"mediumDashed"``
        - Medium-weight dashes
      * - ``"mediumDashDot"``
        - Medium-weight dash–dot
      * - ``"mediumDashDotDot"``
        - Medium-weight dash–dot–dot
      * - ``"slantDashDot"``
        - Slanted dash–dot pattern

Excel grid limits
-----------------

.. data:: COLUMN_MAX

   :type: int
   :value: 16384

   Maximum column index in Excel, corresponding to column ``XFD``. Column
   values that exceed this limit raise
   :class:`~exceltablekit.errors.ColumnOutOfBoundsError`.

.. data:: ROW_MAX

   :type: int
   :value: 1048576

   Maximum row index in Excel. Row values that exceed this limit raise
   :class:`~exceltablekit.errors.InvalidRowValueError`.

Alphabet lookup tables
----------------------

These dictionaries are used internally by the
:class:`~exceltablekit.alphabet.alphabet.Alphabet` utility and are exported
for completeness. Direct use is rarely needed.

.. data:: STRING_ALPHABET

   :type: dict[str, int]

   Maps each uppercase letter ``"A"``–``"Z"`` to its 1-based column index
   (``1``–``26``).

   .. code-block:: python

      from exceltablekit.constants import STRING_ALPHABET

      STRING_ALPHABET["A"]  # 1
      STRING_ALPHABET["Z"]  # 26

.. data:: NUMBER_ALPHABET

   :type: dict[int, str]

   Inverse of ``STRING_ALPHABET``. Maps each integer ``1``–``26`` to its
   uppercase letter ``"A"``–``"Z"``.

   .. code-block:: python

      from exceltablekit.constants import NUMBER_ALPHABET

      NUMBER_ALPHABET[1]   # "A"
      NUMBER_ALPHABET[26]  # "Z"
