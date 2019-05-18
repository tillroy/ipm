# -*- coding: utf-8 -*-
import numpy as np

from src import transformation3d as t


def test_z_rotation():
    p = np.array([
        [1, 0, 0, 1],
        ], dtype="float32")

    expect_p = np.array([
        [0, 1, 0, 1],
        ], dtype="float32")

    new_p = t.rotate_z(p, a=90)

    assert not np.all(new_p == expect_p), "Transformation along Z axis does not correct"

