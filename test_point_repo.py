import unittest
from point import MyPoint
from point_repo import PointRepository
import random

class TestPointRepository(unittest.TestCase):

    def setUp(self):
        """Set up a PointRepository instance before each test."""
        self.repo = PointRepository()

    def test_add_point(self): # 1
        """Test adding a point to the repository."""
        self.repo.add_point(1.0, 2.0, 'red')
        points = self.repo.get_points()
        self.assertEqual(len(points), 1)
        self.assertEqual(points[0].coord_x, 1.0)
        self.assertEqual(points[0].coord_y, 2.0)
        self.assertEqual(points[0].color, 'red')

    def test_get_points(self): # 2
        """
        Test the `get_points` function to ensure all points in the repository are retrieved.
        """
        self.repo = PointRepository()

        self.repo.add_point(1, 1, 'red')
        self.repo.add_point(2, 2, 'green')
        self.repo.add_point(3, 3, 'blue')
        points = self.repo.get_points()

        # Check if the number of points matches
        self.assertEqual(len(points), 3)

        # Verify attributes of each point
        self.assertEqual(points[0].coord_x, 1)
        self.assertEqual(points[0].coord_y, 1)
        self.assertEqual(points[0].color, 'red')

        self.assertEqual(points[1].coord_x, 2)
        self.assertEqual(points[1].coord_y, 2)
        self.assertEqual(points[1].color, 'green')

        self.assertEqual(points[2].coord_x, 3)
        self.assertEqual(points[2].coord_y, 3)
        self.assertEqual(points[2].color, 'blue')

    def test_get_point_at_index(self): # 3
        """
        Test the `get_point_at_index` function to ensure specific points are retrieved by index.
        """
        self.repo = PointRepository()

        self.repo.add_point(1, 1, 'red')
        self.repo.add_point(2, 2, 'green')
        self.repo.add_point(3, 3, 'blue')
        # Retrieve and validate each point by index
        point = self.repo.get_point_at_index(0)
        self.assertEqual(point.coord_x, 1)
        self.assertEqual(point.coord_y, 1)
        self.assertEqual(point.color, 'red')

        point = self.repo.get_point_at_index(1)
        self.assertEqual(point.coord_x, 2)
        self.assertEqual(point.coord_y, 2)
        self.assertEqual(point.color, 'green')

        point = self.repo.get_point_at_index(2)
        self.assertEqual(point.coord_x, 3)
        self.assertEqual(point.coord_y, 3)
        self.assertEqual(point.color, 'blue')

    def test_get_points_by_color(self): # 4
        """Test retrieving points by a specific color."""
        self.repo.add_point(1.0, 2.0, 'red')
        self.repo.add_point(3.0, 4.0, 'blue')
        red_points = self.repo.get_points_by_color('red')
        self.assertEqual(len(red_points), 1)
        self.assertEqual(red_points[0].color, 'red')

    def test_points_in_square(self): # 5
        """Test retrieving points within a specified square."""
        self.repo.add_point(1, 1, 'red')
        self.repo.add_point(3, 3, 'blue')
        self.repo.add_point(6, 6, 'green')
        square_points = self.repo.points_in_square(0, 0, 5)
        self.assertEqual(len(square_points), 2)  # Only points (1,1) and (3,3) are within the square

    def test_distance(self):
        """Test calculating the distance between two points."""
        point_a = MyPoint(0, 0, 'red')
        point_b = MyPoint(3, 4, 'blue')
        dist = self.repo.distance(point_a, point_b)
        self.assertEqual(dist, 5.0)  # 3-4-5 triangle

    def test_min_distance(self): # 6
        """Test finding the minimum distance between points in the repository."""
        self.repo.add_point(0, 0, 'red')
        self.repo.add_point(3, 4, 'blue')
        self.repo.add_point(6, 8, 'green')
        min_dist = self.repo.min_distance()
        self.assertEqual(min_dist, 5.0)  # Minimum distance is between (0,0) and (3,4)

    def test_update_point_by_index(self): # 7
        """Test updating a point by its index."""
        self.repo.add_point(1.0, 2.0, 'red')
        self.repo.update_point_by_index(0, 10.0, 20.0, 'green')
        updated_point = self.repo.get_points()[0]
        self.assertEqual(updated_point.coord_x, 10.0)
        self.assertEqual(updated_point.coord_y, 20.0)
        self.assertEqual(updated_point.color, 'green')

    def test_delete_point_by_index(self): # 8
        """Test deleting a point by its index."""
        self.repo.add_point(1.0, 2.0, 'red')
        self.repo.add_point(3.0, 4.0, 'blue')
        self.repo.delete_point_by_index(0)
        points = self.repo.get_points()
        self.assertEqual(len(points), 1)
        self.assertEqual(points[0].color, 'blue')

    def test_delete_points_inside_square(self): # 9
        """Test deleting points within a specified square."""
        self.repo.add_point(1, 1, 'red')
        self.repo.add_point(3, 3, 'blue')
        self.repo.add_point(6, 6, 'green')
        self.repo.delete_points_inside_square(0, 0, 5)
        remaining_points = self.repo.get_points()
        self.assertEqual(len(remaining_points), 1)  # Only point (6,6) should remain

    def test_randomize(self):
        """Test adding random points to the repository."""
        random.seed(0)  # Set seed for reproducibility
        self.repo.randomize(5)
        points = self.repo.get_points()
        self.assertEqual(len(points), 5)
        # Validate some random points - coordinates and colors should match expected values given the seed
        self.assertIn(points[0].color, MyPoint.VALID_COLORS)
        self.assertIn(points[1].color, MyPoint.VALID_COLORS)

    def test_delete_points_inside_circle(self): # 19
        """Test deleting points inside a given circle."""
        # Add points inside and outside the circle
        self.repo.add_point(1, 1, 'red')  # Inside the circle
        self.repo.add_point(10, 10, 'blue')  # Outside the circle
        self.repo.add_point(3, 3, 'green')  # Inside the circle

        # Delete points inside the circle with center (0, 0) and radius 5
        self.repo.delete_points_inside_circle(0, 0, 5)
        remaining_points = self.repo.get_points()

        # Only the point outside the circle should remain
        self.assertEqual(len(remaining_points), 1)
        self.assertEqual(remaining_points[0].coord_x, 10)
        self.assertEqual(remaining_points[0].coord_y, 10)
        self.assertEqual(remaining_points[0].color, 'blue')

    def test_points_inside_rectangle(self): # 12
        """Test retrieving points inside a given rectangle."""
        # Add points inside and outside the rectangle
        self.repo.add_point(1, 1, 'red')  # Inside the rectangle
        self.repo.add_point(10, 10, 'blue')  # Outside the rectangle
        self.repo.add_point(4, 4, 'green')  # Inside the rectangle

        # Get points inside the rectangle with top-left corner at (0, 0), length 5, and width 5
        points_in_rectangle = self.repo.points_inside_rectangle(0, 0, 5, 5)

        # Check that only points inside the rectangle are retrieved
        self.assertEqual(len(points_in_rectangle), 2)
        self.assertTrue(any(p.coord_x == 1 and p.coord_y == 1 for p in points_in_rectangle))
        self.assertTrue(any(p.coord_x == 4 and p.coord_y == 4 for p in points_in_rectangle))

    def test_update_point_by_coordinates(self): # 15
        """Test updating the color of a point by its coordinates."""
        # Add a point to be updated
        self.repo.add_point(2, 2, 'red')
        self.repo.add_point(5, 5, 'blue')

        # Update the color of the point at coordinates (2, 2)
        self.repo.update_point_by_coordinates(2, 2, 'green')
        updated_point = self.repo.get_points()[0]  # Get the first point

        # Check that the color was updated correctly
        self.assertEqual(updated_point.coord_x, 2)
        self.assertEqual(updated_point.coord_y, 2)
        self.assertEqual(updated_point.color, 'green')

        # Verify that the color of other points remains unchanged
        other_point = self.repo.get_points()[1]
        self.assertEqual(other_point.color, 'blue')
if __name__ == '__main__':
    unittest.main()
