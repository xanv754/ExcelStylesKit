import click

from exceltablekit import __version__
from exceltablekit.constants import BorderStyle


@click.group()
@click.version_option(version=__version__, prog_name="exceltablekit")
def cli() -> None:
    """ExcelTableKit — declarative Excel table styling built on top of openpyxl."""


@cli.command()
def info() -> None:
    """Display package version and core dependencies."""
    import importlib.metadata as meta

    click.echo(f"exceltablekit  {__version__}")
    for dep in ("openpyxl", "tabulate", "click"):
        try:
            ver = meta.version(dep)
        except meta.PackageNotFoundError:
            ver = "not installed"
        click.echo(f"  {dep:<12} {ver}")


@cli.command()
@click.argument("filepath")
@click.option("--start", default="A1", show_default=True, help="Start cell (e.g. A1).")
@click.option("--end", default="D10", show_default=True, help="End cell (e.g. D10).")
@click.option(
    "--header-rows", default=1, show_default=True, help="Number of header rows."
)
@click.option(
    "--bg", default="E8F4FD", show_default=True, help="Body background hex color."
)
@click.option(
    "--header-bg",
    default="1F4E79",
    show_default=True,
    help="Header background hex color.",
)
@click.option(
    "--border-style",
    default="thin",
    show_default=True,
    type=click.Choice(list(BorderStyle.__args__)),
    help="Border style for all cells.",
)
def style(
    filepath: str,
    start: str,
    end: str,
    header_rows: int,
    bg: str,
    header_bg: str,
    border_style: str,
) -> None:
    """Apply default styling to an Excel file table range.

    FILEPATH is the path to the target .xlsx file (created if it does not exist).
    """
    from exceltablekit.excel.manager import ExcelManager
    from exceltablekit.excel.styles import ExcelStyle

    excel = ExcelManager(filepath)
    excel.set_table(start, end)

    if header_rows > 0:
        excel.define_header(rows=header_rows)

    styles = ExcelStyle(excel)
    styles.set_background(bg)
    styles.set_border(border_style=border_style)

    if header_rows > 0:
        styles.set_header_background(header_bg)
        styles.set_header_font(bold=True, hex_color="FFFFFFFF")
        styles.set_header_border(border_style=border_style)

    styles.auto_fit_columns()
    click.echo(f"Styled {filepath} — table {start}:{end}, {header_rows} header row(s).")


if __name__ == "__main__":
    cli()
