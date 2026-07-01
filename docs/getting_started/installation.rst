Installation
============

Requirements
------------

- **Python** 3.10 or higher
- **openpyxl** 3.1.5 or higher (installed automatically)

ExcelTableKit is available on PyPI and can be installed with ``pip``.

Install from PyPI
-----------------

.. code-block:: bash

   pip install exceltablekit

This will also install the required dependencies:

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Package
     - Minimum version
     - Purpose
   * - ``openpyxl``
     - 3.1.5
     - Core Excel file read/write engine
   * - ``click``
     - 8.0.0
     - Powers the CLI interface
   * - ``tabulate``
     - 0.10.0
     - Terminal table display (``display_cells()``)
   * - ``et-xmlfile``
     - 1.1.0
     - XML streaming required by openpyxl

Verify the installation
-----------------------

After installing, you can verify everything is working by running:

.. code-block:: bash

   exceltablekit info

Expected output:

.. code-block:: text

   exceltablekit version: 2.0.1
   openpyxl version:      3.1.x
   tabulate version:      0.x.x
   click version:         8.x.x

Install for development
-----------------------

To contribute or run the tests locally, clone the repository and install in
editable mode:

.. code-block:: bash

   git clone https://github.com/xanv754/ExcelTableKit.git
   cd ExcelTableKit
   pip install -e .

Running the test suite:

.. code-block:: bash

   python -m unittest discover -s tests -v
