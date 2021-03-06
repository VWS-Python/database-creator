"""
Tests for the VWS CLI help.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from click.testing import CliRunner

from vws_web_tools import vws_web_tools_group

_SUBCOMMANDS = [[item] for item in vws_web_tools_group.commands.keys()]
_BASE_COMMAND: list[list[str]] = [[]]
_COMMANDS = _BASE_COMMAND + _SUBCOMMANDS


@pytest.mark.parametrize(
    'command',
    _COMMANDS,
    ids=[str(cmd) for cmd in _COMMANDS],
)
def test_vws_command_help(command: list[str]) -> None:
    """
    Expected help text is shown for ``vws`` commands.

    This help text is defined in files.
    To update these files, run the command ``bash admin/update_cli_tests.sh``.
    """
    runner = CliRunner()
    arguments = command + ['--help']
    group = vws_web_tools_group
    result = runner.invoke(group, arguments, catch_exceptions=False)
    assert result.exit_code == 0
    help_output_filename = '-'.join(['vws'] + command) + '.txt'
    help_outputs_dir = Path(__file__).parent / 'help_outputs'
    expected_help_file = help_outputs_dir / help_output_filename
    try:
        expected_help = expected_help_file.read_text()
        assert result.output == expected_help
    except (AssertionError, FileNotFoundError):  # pragma: no cover
        if os.getenv('FIX_CLI_TESTS') == '1':
            help_outputs_dir.mkdir(exist_ok=True)
            expected_help_file.touch()
            expected_help_file.write_text(result.output)
        else:
            raise
