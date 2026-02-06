import pytest
from geometry.sphere import volume_sphere


def test_volume_sphere_valid_inputs():
    """
    Test volume computation for valid sphere dimensions.
    """
    radius = 2.0
    expected = (4.0 / 3.0) * 3.141592653589793 * radius**3
    assert volume_sphere(radius) == expected


def test_volume_sphere_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    radius = -2.0
    expected = (4.0 / 3.0) * 3.141592653589793 * radius**3
    assert volume_sphere(radius) == expected


def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius = 1.1
    expected = (4.0 / 3.0) * 3.141592653589793 * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
