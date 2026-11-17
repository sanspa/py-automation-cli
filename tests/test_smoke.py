"""Smoke test: aplikasi terpasang dan command 'version' bisa berjalan."""

import runpy
from unittest.mock import patch

from typer.testing import CliRunner

from taxi_cli import __version__
from taxi_cli.cli import app

runner = CliRunner()


def test_version_command_prints_version() -> None:
    """The `version` command exits cleanly and prints the version."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_module_entry_point_invokes_app() -> None:
    """The `python -m taxi_cli` entry point invokes the CLI."""
    with patch("taxi_cli.cli.app") as app_mock:
        runpy.run_module("taxi_cli.__main__", run_name="__main__")

    app_mock.assert_called_once_with()
