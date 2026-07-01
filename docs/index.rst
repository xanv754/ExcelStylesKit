ExcelTableKit Documentation
============================

.. image:: https://img.shields.io/pypi/v/exceltablekit
   :target: https://pypi.org/project/exceltablekit/
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/exceltablekit
   :target: https://pypi.org/project/exceltablekit/
   :alt: Python versions

.. image:: https://img.shields.io/github/license/xanv754/ExcelTableKit
   :target: https://github.com/xanv754/ExcelTableKit/blob/main/LICENSE
   :alt: License

**ExcelTableKit** is a Python library that acts as a high-level abstraction layer
over `openpyxl <https://openpyxl.readthedocs.io/>`_ for styling tables in ``.xlsx`` files.

Instead of dealing directly with openpyxl internals like ``PatternFill``, ``Border``,
``Side``, ``Font``, and ``Alignment``, ExcelTableKit lets you define a cell range as a
table object and apply styles to it declaratively in just a few lines of code.

.. code-block:: python

   from exceltablekit import ExcelManager, ExcelStyle

   excel = ExcelManager("report.xlsx")
   excel.set_table("A1", "D10")
   excel.define_header(rows=1)

   style = ExcelStyle(excel)
   style.set_header_background("1F4E79")
   style.set_header_font(bold=True, hex_color="FFFFFF")
   style.set_background("E8F4FD")
   style.set_border()
   style.auto_fit_columns()

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting_started/installation
   getting_started/quickstart

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user_guide/excel_manager
   user_guide/excel_style
   user_guide/tables
   user_guide/cli

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api_reference/index

.. toctree::
   :maxdepth: 1
   :caption: Project

   changelog
