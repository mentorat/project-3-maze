"""Pytest tests map."""

from maze import settings as constants

from maze.models.map import Map
from maze.models.position import Position


MAP = Map(constants.MAP_LEVEL_1)


def test_01_map_returns_a_valid_path():
    """Test the map returns a valid path."""
    assert Position(0, 0) in MAP


def test_02_map_returns_wrong_path():
    """Ensure the map returns a wrong path."""
    assert Position(-1, 0) not in MAP


def test_03():
    """Ensure the map returns a wrong path."""
    assert Position(-1, 0) in MAP
