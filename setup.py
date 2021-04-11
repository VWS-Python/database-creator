"""
Setup script.
"""

from __future__ import annotations

from pathlib import Path

from setuptools import setup


def _get_dependencies(requirements_file: Path) -> list[str]:
    """
    Return requirements from a requirements file.

    This expects a requirements file with no ``--find-links`` lines.
    """
    lines = requirements_file.read_text().strip().split('\n')
    return [line for line in lines if not line.startswith('#')]


_DIRECT_REQUIRES = _get_dependencies(
    requirements_file=Path('requirements.txt'),
)

INSTALL_REQUIRES = _DIRECT_REQUIRES
DEV_REQUIRES = _get_dependencies(
    requirements_file=Path('dev-requirements.txt'),
)

setup(
    install_requires=INSTALL_REQUIRES,
    extras_require={'dev': DEV_REQUIRES},
)