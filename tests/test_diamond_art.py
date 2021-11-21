#!/usr/bin/env python

"""Tests for `diamond_art` package."""

from importlib import resources

import numpy as np  # type: ignore
import pytest  # type: ignore
from PIL import Image  # type: ignore

from diamond_art import DiamondArt

from . import images


@pytest.fixture()
def test_images():
    """Pair of test image and expected result (within images package)"""
    return [("1px.png", "1px_canvas.png")]


def test_end_to_end(test_images):
    for input_file, expected_file in test_images:
        with resources.path(images, input_file) as input_path:
            img = DiamondArt(input_path).get_image()
            with resources.path(images, expected_file) as expected_path:
                expected_img = Image.open(expected_path)
                assert np.all(np.asarray(img) == np.asarray(expected_img))
