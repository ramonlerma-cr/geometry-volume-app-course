import pytest
from geometry.cone import volume_cone


def test_volume_cone_valid_inputs():
    """
    Test volume computation for valid cone dimensions.
    """
    radius, height = 2.0, 3.0
    expected = (1.0 / 3.0) * 3.141592653589793 * radius * radius * height
    assert volume_cone(radius, height) == expected


def test_volume_cone_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    radius, height = -2.0, 3.0
    expected = (1.0 / 3.0) * 3.141592653589793 * radius * radius * height
    assert volume_cone(radius, height) == expected


def test_volume_cone_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius, height = 1.1, 2.2
    expected = (1.0 / 3.0) * 3.141592653589793 * radius * radius * height
    assert volume_cone(radius, height) == pytest.approx(expected, rel=1e-6)
