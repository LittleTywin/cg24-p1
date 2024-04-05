import unittest
import numpy as np
import tripaint as tp

class TestFShading(unittest.TestCase):

    def testThreeSamePoints(self):
        vertices = np.array([
            [10,10],
            [10,10],
            [10,10]
        ])
        vcolors = np.zeros((3,3))
        img = np.ones((20,20,3))
        shaded_img = tp.f_shading(img,vertices,vcolors)
        expected_img = img
        expected_img[10,10]=vcolors[0]
        self.assertTrue((shaded_img == expected_img).all())

if __name__ == "__main__":
    unittest.main()