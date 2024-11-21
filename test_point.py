import unittest
from point import MyPoint

class TestMyPoint(unittest.TestCase):

    def test_default_initialization(self):
        """Test initializing a point with default values."""
        point = MyPoint()
        self.assertEqual(point.coord_x, 0)
        self.assertEqual(point.coord_y, 0)
        self.assertEqual(point.color, 'red')

    def test_custom_initialization(self):
        """Test initializing a point with specific values."""
        point = MyPoint(5.5, -3.2, 'blue')
        self.assertEqual(point.coord_x, 5.5)
        self.assertEqual(point.coord_y, -3.2)
        self.assertEqual(point.color, 'blue')

    def test_invalid_color_initialization(self):
        """Test initializing a point with an invalid color."""
        with self.assertRaises(ValueError) as context:
            MyPoint(0, 0, 'orange')
        self.assertIn("Color must be one of", str(context.exception))

    def test_invalid_coord_x_initialization(self):
        """Test initializing a point with a non-numeric x-coordinate."""
        with self.assertRaises(ValueError) as context:
            MyPoint("not a number", 0, 'red')
        self.assertIn("coord_x must be a number", str(context.exception))

    def test_invalid_coord_y_initialization(self):
        """Test initializing a point with a non-numeric y-coordinate."""
        with self.assertRaises(ValueError) as context:
            MyPoint(0, "not a number", 'green')
        self.assertIn("coord_y must be a number", str(context.exception))

    def test_set_coord_x(self):
        """Test setting a new x-coordinate."""
        point = MyPoint()
        point.coord_x = 10.1
        self.assertEqual(point.coord_x, 10.1)

    def test_set_invalid_coord_x(self):
        """Test setting a non-numeric x-coordinate raises ValueError."""
        point = MyPoint()
        with self.assertRaises(ValueError) as context:
            point.coord_x = "invalid"
        self.assertIn("coord_x must be a number", str(context.exception))

    def test_set_coord_y(self):
        """Test setting a new y-coordinate."""
        point = MyPoint()
        point.coord_y = -7.3
        self.assertEqual(point.coord_y, -7.3)

    def test_set_invalid_coord_y(self):
        """Test setting a non-numeric y-coordinate raises ValueError."""
        point = MyPoint()
        with self.assertRaises(ValueError) as context:
            point.coord_y = None
        self.assertIn("coord_y must be a number", str(context.exception))

    def test_set_color(self):
        """Test setting a valid color."""
        point = MyPoint()
        point.color = 'green'
        self.assertEqual(point.color, 'green')

    def test_set_invalid_color(self):
        """Test setting an invalid color raises ValueError."""
        point = MyPoint()
        with self.assertRaises(ValueError) as context:
            point.color = 'purple'
        self.assertIn("Color must be one of", str(context.exception))

    def test_string_representation(self):
        """Test the string representation of the point."""
        point = MyPoint(3.5, 4.5, 'yellow')
        self.assertEqual(str(point), "Point (3.5, 4.5) of color yellow")

if __name__ == '__main__':
    unittest.main()
