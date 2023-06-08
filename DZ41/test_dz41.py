import pytest
import random

from DZ41.main41 import Pixel


def test_pixel_value_error():
    with pytest.raises(ValueError) as exc:
        Pixel(240, 100, -1)  # if one of the integers less 0 or more 255  = passed


def test_check_str():
    pixel = Pixel(14, 128, 236)
    expected_output = "Pixel object\n\tRed: 14\n\tGreen: 128\n\tBlue: 236\n"
    assert str(pixel) == expected_output


def test_check_repr():
    pixel = Pixel(14, 128, 236)
    expected_output = "Pixel(14, 128, 236)"
    assert repr(pixel) == expected_output


def test_convert_to_byte():
    assert Pixel._convert_to_byte(-10) == 0
    assert Pixel._convert_to_byte(300) == 255
    assert Pixel._convert_to_byte(50) == 50
    assert Pixel._convert_to_byte(0) == 0
    assert Pixel._convert_to_byte(255) == 255


def test_pixel_equal():
    pixel1 = Pixel(10, 20, 30)
    pixel2 = Pixel(10, 20, 30)
    pixel3 = Pixel(40, 50, 60)
    assert pixel1 == pixel2
    assert pixel2 == pixel1
    assert pixel1 != pixel3


def test_get_pixel_near():
    pixel = Pixel(100, 100, 100)
    area = 10
    random.random()
    new_pixel = pixel.get_pixel_near(area)
    assert new_pixel.r - pixel.r <= area
    assert new_pixel.g - pixel.g <= area
    assert new_pixel.b - pixel.b <= area


def test_add():
    pixel1 = Pixel(100, 50, 75)
    pixel2 = Pixel(50, 75, 100)
    result = pixel1 + pixel2
    expected_result = Pixel(150, 125, 175)
    expected_result = Pixel._convert_to_byte(expected_result.r), Pixel._convert_to_byte(expected_result.g), Pixel._convert_to_byte(expected_result.b)
    expected_result = Pixel(*expected_result)
    assert result == expected_result


def test_sub():
    pixel1 = Pixel(100, 50, 75)
    pixel2 = Pixel(50, 75, 100)
    result = pixel1 - pixel2
    expected_result = Pixel(50, 0, 0)
    expected_result = Pixel._convert_to_byte(expected_result.r), Pixel._convert_to_byte(expected_result.g), Pixel._convert_to_byte(expected_result.b)
    expected_result = Pixel(*expected_result)
    assert result == expected_result


def test_multiplication():
    pixel = Pixel(100, 50, 75)
    result = pixel * 1.5
    assert result == Pixel(150, 75, 112.5)
    with pytest.raises(ValueError) as exc:
        pixel * 0


def test_rmul():
    pixel = Pixel(100, 50, 75)
    result = 2 * pixel
    assert result == Pixel(200, 100, 150)
