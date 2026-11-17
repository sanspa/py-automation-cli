"""Command line interface for taxi-report."""

import typer

from taxi_cli import __version__

app = typer.Typer(help="Laporan analitik dataset NYC TLC Yellow Taxi.")


@app.callback()
def _root() -> None:
    """Root command group."""


@app.command()
def version() -> None:
    """Tampilkan versi aplikasi."""
    typer.echo(f"taxi-report v{__version__}")
