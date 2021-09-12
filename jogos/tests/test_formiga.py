from unittest import TestCase

import numpy as np

from jogos.formiga import Formiga


class TestFormiga(TestCase):

    def setUp(self):
        self.formiga = Formiga()

    def test_init(self):
        expected_vector = (2, 2)
        expected_direction = (2 / np.sqrt(8), 2 / np.sqrt(8))
        expected_loc = [0, 0]
        self.assertEqual(
            expected_vector, self.formiga.vector
        )
        self.assertEqual(
            expected_direction, self.formiga.direction
        )
        self.assertEqual(
            expected_loc, self.formiga.rect[:2]
        )

    def test_reverse(self):
        expected_vector = (-2, -2)
        expected_direction = (-2 / np.sqrt(8), -2 / np.sqrt(8))
        self.formiga.reverse()
        self.assertEqual(
            expected_vector, self.formiga.vector
        )
        self.assertEqual(
            expected_direction, self.formiga.direction
        )

    def test_speed_up(self):
        expected_vector = (3, 3)
        expected_direction = (3 / np.sqrt(18), 3 / np.sqrt(18))
        self.formiga.speed_up()
        self.assertEqual(
            expected_vector, self.formiga.vector
        )
        self.assertEqual(
            expected_direction, self.formiga.direction
        )

    def test_slow_down(self):
        expected_vector = (1, 1)
        expected_direction = (1 / np.sqrt(2), 1 / np.sqrt(2))
        self.formiga.slow_down()
        self.assertEqual(
            expected_vector, self.formiga.vector
        )
        self.assertEqual(
            expected_direction, self.formiga.direction
        )

    def test_update(self):
        expected_vector = (2, 2)
        expected_direction = (2 / np.sqrt(8), 2 / np.sqrt(8))
        expected_loc = [2, 2]
        self.formiga.update()
        self.assertEqual(
            expected_vector, self.formiga.vector
        )
        self.assertEqual(
            expected_direction, self.formiga.direction
        )
        self.assertEqual(
            expected_loc, self.formiga.rect[:2]
        )
