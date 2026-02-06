import pytest
from geometry.cylinder import volume_cylinder


def test_volume_cylinder_valid_inputs():
    """
    Test volume computation for valid cylinder dimensions.
    """
    radius, height = 2.0, 3.0
    expected = 3.141592653589793 * radius * radius * height
    assert volume_cylinder(radius, height) == expected


def test_volume_cylinder_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    radius, height = -2.0, 3.0
    expected = 3.141592653589793 * radius * radius * height
    assert volume_cylinder(radius, height) == expected


def test_volume_cylinder_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius, height = 1.1, 2.2
    expected = 3.141592653589793 * radius * radius * height
    assert volume_cylinder(radius, height) == pytest.approx(expected, rel=1e-6)
