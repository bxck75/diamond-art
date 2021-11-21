#!/usr/bin/env python

"""Tests for `gem_painting` package."""

import pytest
from gem_painting import GemPainting
from gem_painting import cli

from . import images
from importlib import resources
from PIL import Image
import numpy as np

@pytest.fixture()
def test_images():
    """Pair of test image and expected result (within images package)"""
    return [("1px.png", "1px_painting.png")]

def test_end_to_end(test_images):
    for input_file, expected_file in test_images:
        with resources.path(images, input_file) as input_path:
            img = GemPainting(input_path).get_image()
            with resources.path(images, expected_file) as expected_path:
                expected_img = Image.open(expected_path)
                assert np.all(np.asarray(img) == np.asarray(expected_img))
