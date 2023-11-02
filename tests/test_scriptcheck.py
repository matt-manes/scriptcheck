import pytest

from scriptcheck import scriptcheck


def test__get_scripts():
    print()
    scripts = scriptcheck.get_scripts()
    assert isinstance(scripts, list)
    assert len(scripts) > 0
    print(*scripts, sep="\n")
