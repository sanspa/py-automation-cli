"""Smoke test: aplikasi terpasang dan command 'version' bisa berjalan."""

from typer.testing import CliRunner

from taxi_cli import __version__
from taxi_cli.cli import app

runner = CliRunner()


def test_version_command_prints_version() -> None:
    """The `version` command exits cleanly and prints the version."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout
