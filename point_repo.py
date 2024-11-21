from matplotlib import pyplot as plt

from point import MyPoint

import random

class PointRepository:
    def __init__(self):
        '''
        Constructor for the point repository

        Attributes:
            __points - list[MyPoint] - the array of points in the repository
            __size - int - the number of points in the repository
        '''
        self.__points = []
        self.__size = 0

    def add_point(self, coord_x, coord_y, color): # 1
        '''
        Adds a point to the point repository.
        Args:
            coord_x: int|float - the x coordinate of the point
            coord_y: int|float - the y coordinate of the point
            color: str - the color of the point
        '''
        new_point = MyPoint(coord_x, coord_y, color)
        self.__points.append(new_point)
        self.__size += 1

    def get_points(self): # 2
        '''
        Gets the points in the repository.
        Returns:
            list[MyPoint]: The points in the repository.
        '''
        return self.__points
    def get_point_at_index(self, index): # 3
        '''
        Gets the point at a given index in the repository.
        Args:
            index: int

        Returns:
            MyPoint: The point at the given index in the repository.
        '''
        return self.__points[index]

    def get_points_by_color(self, color): # 4
        '''
        Gets the points in the repository with a specific color.
        Args:
            color: str - the color of the point
        Returns:
            list[MyPoint]: Points with the specified color.
        '''
        return [point for point in self.__points if point.color == color]

    def points_in_square(self, top_left_x, top_left_y, length): # 5
        '''
        Gets the points in the repository within a square.
        Args:
            top_left_x: float|int - the x coordinate of the top left corner of the square
            top_left_y: float|int - the y coordinate of the top left corner of the square
            length: the length of the square
        Returns:
            list[MyPoint]: The points inside the square.
        '''
        return [
            point for point in self.__points
            if top_left_x <= point.coord_x <= top_left_x + length and
               top_left_y <= point.coord_y <= top_left_y + length
        ]

    def distance(self, point_a, point_b):
        '''
        Calculates the distance between two points.
        Args:
            point_a: MyPoint - the first point
            point_b: MyPoint - the second point
        Returns:
            float: The distance between two points.
        '''
        return ((point_a.coord_x - point_b.coord_x) ** 2 +
                (point_a.coord_y - point_b.coord_y) ** 2) ** 0.5

    def min_distance(self): # 6
        '''
        Calculates the minimum distance between any two points.
        Returns:
            float: The minimum distance between any two points, or None if less than two points exist.
        '''
        if self.__size < 2:
            return None

        min_dist = float('inf')
        for i, point_1 in enumerate(self.__points):
            for point_2 in self.__points[i + 1:]:
                dist = self.distance(point_1, point_2)
                if dist < min_dist:
                    min_dist = dist
        return min_dist

    def update_point_by_index(self, index, coord_x, coord_y, color): # 7
        '''
        Updates a point by its index.
        Args:
            index (int): The index of the point to update.
            coord_x (int|float): New x coordinate.
            coord_y (int|float): New y coordinate.
            color (str): New color.
        '''
        if 0 <= index < self.__size:
            self.__points[index].coord_x = coord_x
            self.__points[index].coord_y = coord_y
            self.__points[index].color = color

    def delete_point_by_index(self, index): # 8
        '''
        Deletes a point by its index.
        Args:
            index: int - the index of the point
        Returns:
            list[MyPoint]: The updated list of points.
        '''
        if 0 <= index < self.__size:
            del self.__points[index]
            self.__size -= 1
        return self.__points

    def delete_points_inside_square(self, top_left_x, top_left_y, length): # 9
        '''
        Deletes points in the repository within a square.
        Args:
            top_left_x: int|float - the x coordinate of the top left corner of the square
            top_left_y: int|float - the y coordinate of the top left corner of the square
            length: the length of the square
        Returns:
            list[MyPoint]: The updated list of points after deletion.
        '''
        self.__points = [
            point for point in self.__points
            if not (top_left_x <= point.coord_x <= top_left_x + length and
                    top_left_y <= point.coord_y <= top_left_y + length)
        ]
        self.__size = len(self.__points)
        return self.__points

    def plot(self): # 10
        '''
        Plots the points in the repository.
        '''
        x = [point.coord_x for point in self.__points]
        y = [point.coord_y for point in self.__points]
        col = [point.color for point in self.__points]

        plt.scatter(x, y, c=col)
        plt.show()

    def randomize(self, size):
        '''
        function that adds "size" random points to the repository.
        Args:
            size: int - the number of points to be added.

        Returns:
            list[MyPoint]: The updated list of points after randomization.

        '''

        for _ in range(size):
            random_value_x = random.randint(1, 10)
            random_value_y = random.randint(1, 10)

            color = random.choice(['red', 'green', 'blue', 'yellow', 'magenta'])

            self.add_point(random_value_x, random_value_y, color)

        return self.__points

    def delete_points_inside_circle(self, circle_x, circle_y, radius): # 19
        '''
        function that deletes points inside a given circle.
        Args:
            circle_x: int|float - the x coordinate of the center of the circle.
            circle_y: int|float - the y coordinate of the center of the circle.
            radius: int|float - the radius of the circle

        Returns: list[MyPoint]: The updated list of points after deletion.

        '''
        center_of_circle = MyPoint(circle_x, circle_y)
        self.__points = [point for point in self.__points if self.distance(point, center_of_circle) > radius]

        return self.__points

    def points_inside_rectangle(self, top_left_x, top_left_y, length, width): # 12
        '''
        function that gets all points inside a rectangle.
        Args:
            top_left_x: int|float - the x coordinate of the top left corner of the rectangle.
            top_left_y: int|float - the y coordinate of the top left corner of the rectangle.
            length: int|float - the length of the rectangle.
            width: int|float - the width of the rectangle.

        Returns:
            list[MyPoint]: the list of points inside the rectangle.

        '''

        return [
            point for point in self.__points
            if top_left_x <= point.coord_x <= top_left_x + length and
               top_left_y <= point.coord_y <= top_left_y + width
        ]

    def update_point_by_coordinates(self, coord_x, coord_y, color): # 15
        '''
        function that updates the color of a point by its coordinates.
        Args:
            coord_x: int|float - the x coordinate of the point.
            coord_y:int|float - the y coordinate of the point.
            color: new color of the point.

        Returns:
            list[MyPoint]: The updated list of points after updating.

        '''

        for point in self.__points:
            if point.coord_x == coord_x and point.coord_y == coord_y:
                point.color = color

        return self.__points