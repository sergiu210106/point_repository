class MyPoint:
    """
    A class representing a point in a 2D space with specific coordinates and color.

    Attributes:
        coord_x (float): The X-coordinate of the point.
        coord_y (float): The Y-coordinate of the point.
        color (str): The color of the point, limited to 'red', 'green', 'blue', 'yellow', and 'magenta'.
    """

    VALID_COLORS = {'red', 'green', 'blue', 'yellow', 'magenta'}

    def __init__(self, coord_x=0, coord_y=0, color='red'):
        """
        Initializes a MyPoint object with X and Y coordinates and a color.

        Args:
            coord_x (float, optional): The X-coordinate of the point. Defaults to 0.
            coord_y (float, optional): The Y-coordinate of the point. Defaults to 0.
            color (str, optional): The color of the point. Must be one of 'red', 'green', 'blue', 'yellow', or 'magenta'. Defaults to 'red'.

        Raises:
            ValueError: If the color is not one of the allowed values or if coord_x or coord_y is not a number.
        """
        self.__coord_x = coord_x  # Calls the coord_x setter
        self.__coord_y = coord_y  # Calls the coord_y setter
        if color not in MyPoint.VALID_COLORS:
            raise ValueError(f"Color must be one of {MyPoint.VALID_COLORS}.")
        else:
            self.__color = color  # Calls the color setter

    @property
    def coord_x(self):
        """float: Gets or sets the X-coordinate of the point."""
        return self.__coord_x

    @coord_x.setter
    def coord_x(self, value):
        """
        Sets the X-coordinate of the point.

        Args:
            value (float): The X-coordinate of the point.

        Raises:
            ValueError: If the value is not a number.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("coord_x must be a number.")
        self.__coord_x = value

    @property
    def coord_y(self):
        """float: Gets or sets the Y-coordinate of the point."""
        return self.__coord_y

    @coord_y.setter
    def coord_y(self, value):
        """
        Sets the Y-coordinate of the point.

        Args:
            value (float): The Y-coordinate of the point.

        Raises:
            ValueError: If the value is not a number.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("coord_y must be a number.")
        self.__coord_y = value

    @property
    def color(self):
        """str: Gets or sets the color of the point."""
        return self.__color

    @color.setter
    def color(self, value):
        """
        Sets the color of the point.

        Args:
            value (str): The color of the point. Must be one of 'red', 'green', 'blue', 'yellow', or 'magenta'.

        Raises:
            ValueError: If the color is not one of the allowed values.
        """
        if value not in MyPoint.VALID_COLORS:
            raise ValueError(f"Color must be one of {MyPoint.VALID_COLORS}.")
        self.__color = value


    def __str__(self):
        """
        Provides a string representation of the point.

        Returns:
            str: A string in the format "Point (coord_x, coord_y) of color color".
        """
        return f"Point ({self.__coord_x}, {self.__coord_y}) of color {self.__color}."
    def __repr__(self):
        """
        Provides a detailed string representation of the point for developers.

        Returns:
            str: A string representation generated using __str__.
        """
        return self.__str__()


    
