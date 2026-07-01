# ExcelTableKit

[![PyPI version](https://img.shields.io/pypi/v/exceltablekit?color=blue)](https://pypi.org/project/exceltablekit/)
[![Python versions](https://img.shields.io/pypi/pyversions/exceltablekit)](https://pypi.org/project/exceltablekit/)
[![License: MIT](https://img.shields.io/github/license/xanv754/ExcelStylesKit)](https://github.com/xanv754/ExcelStylesKit/blob/main/LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/xanv754/ExcelStylesKit/ci.yml?branch=main&label=CI)](https://github.com/xanv754/ExcelStylesKit/actions/workflows/ci.yml)
[![PyPI downloads](https://img.shields.io/pypi/dm/exceltablekit)](https://pypi.org/project/exceltablekit/)

A declarative abstraction layer over [openpyxl](https://openpyxl.readthedocs.io/) that simplifies styling Excel tables in `.xlsx` files. Define cell ranges as table objects and apply colors, fonts, borders, and alignment without touching `PatternFill`, `Border`, `Side`, or any other low-level openpyxl construct directly.

## Installation

```bash
pip install exceltablekit
```

**Requirements:** Python >= 3.10

## Quick start

### Python

```python
from exceltablekit.excel import ExcelManager, ExcelStyle

excel = ExcelManager("report.xlsx")
excel.set_table("A1", "D10")
excel.define_header(rows=1)

styles = ExcelStyle(excel)
styles.set_background("E8F4FD")
styles.set_font(type="Arial", size=11)
styles.set_alignment(horizontal="center", vertical="center")
styles.set_border()

styles.set_header_background("1F4E79")
styles.set_header_font(bold=True, hex_color="FFFFFFFF")
styles.set_header_border()
styles.auto_fit_columns()
```

### CLI

```bash
# Apply default styling to a table range
exceltablekit style report.xlsx --start A1 --end D10 --header-rows 1

# Custom colors and border style
exceltablekit style report.xlsx --start A1 --end D10 \
  --bg "E8F4FD" --header-bg "1F4E79" --border-style thin

# Show installed versions
exceltablekit info
```

## Documentation

Full API reference and guides at [exceltablekit.readthedocs.io](https://exceltablekit.readthedocs.io) *(coming soon)*.

## License

MIT — [Angyee Marin](mailto:angyeemarin.dev@gmail.com)
