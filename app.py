from point_repo import PointRepository
from point import MyPoint

def menu():
    print("Choose one of the following options:")
    print("1. Add a point to the repository.")
    print("2. Get all points from the repository.")
    print("3. Get a point at a given index.")
    print("4. Get all points of a given color")
    print("5. Get all points that are inside a given square(up-left corner and length given).")
    print("6. Get the minimum distance between two points.")
    print("7. Update a point at a given index.")
    print("8. Delete a point by index.")
    print("9. Delete all points inside a given square(up-left corner and length given).")
    print("10. Plot all points in a chart (using library matplotlib).")
    print("11. Delete all points that are inside a given circle")
    print("12. Get all points that are inside a given rectangle (up-left corner, length and width given).")
    print("13. Update the color of a point given its coordinates.")
    print("14. QUIT.")

if __name__ == '__main__':
    repository = PointRepository()
    repository.randomize(10)
    while True:
        menu()
        option = input("Enter your choice: ")
        match option:
            case "1":
                try:
                    coord_x = float(input("Enter the x coordinate of the point: "))
                    coord_y = float(input("Enter the y coordinate of the point: "))
                    color = input("Enter the color: ")

                    repository.add_point(coord_x, coord_y, color)
                except :
                    print("Invalid input. The coordinates must be real numbers.")
            case "2":
                print(repository.get_points())
            case "3":
                try:
                    index = int(input("Enter the index of the point: "))

                    print(repository.get_point_at_index(index))
                except:
                    print("Invalid input. The index must be an integer.")
            case "4":
                color = input("Enter the color: ")

                print(repository.get_points_by_color(color))
            case "5":
                try:
                    top_left_x = float(input("Enter the x coordinate of the top left corner: "))
                    top_left_y = float(input("Enter the y coordinate of the top left corner: "))

                    length = float(input("Enter the length of the square: "))

                    print(repository.points_in_square(top_left_x, top_left_y, length))

                except:
                    print("Invalid input. The coordinates and length must be real numbers.")

            case "6":
                print("Minimum distance between two points : ", repository.min_distance())
            case "7":
                try:
                    index = int(input("Enter the index of the point: "))
                    coord_x = float(input("Enter the x coordinate of the point: "))
                    coord_y = float(input("Enter the y coordinate of the point: "))
                    color = input("Enter the color: ")

                    repository.update_point_by_index(index, coord_x, coord_y, color)
                except:
                    print("Invalid input. The index must be an integer. The coordinates and length must be real numbers.")
            case "8":
                try:
                    index = int(input("Enter the index of the point: "))

                    repository.delete_point_by_index(index)
                except:
                    print("Invalid input. The index must be an integer.")

            case "9":
                try:
                    top_left_x = float(input("Enter the x coordinate of the top left corner: "))
                    top_left_y = float(input("Enter the y coordinate of the top left corner: "))

                    length = float(input("Enter the length of the square: "))

                    repository.delete_points_inside_square(top_left_x, top_left_y, length)

                except:
                    print("Invalid input. The coordinates and length must be real numbers.")
            case "10":
                repository.plot()
            case "11":
                try:
                    center_x = float(input("Enter the x coordinate of the center: "))
                    center_y = float(input("Enter the y coordinate of the center: "))
                    radius = float(input("Enter the radius of the circle: "))

                    repository.delete_points_inside_circle(center_x, center_y, radius)

                except:
                    print("Invalid input. The coordinates and radius must be real numbers.")

            case "12":
                try:
                    top_left_x = float(input("Enter the x coordinate of the top left corner: "))
                    top_left_y = float(input("Enter the y coordinate of the top left corner: "))

                    length = float(input("Enter the length of the rectangle: "))
                    width = float(input("Enter the width of the rectangle: "))

                    print(repository.points_inside_rectangle(top_left_x, top_left_y, length, width))

                except:
                    print("Invalid input. The coordinates, length and width must be real numbers.")
            case "13":
                try:
                    coord_x = float(input("Enter the x coordinate: "))
                    coord_y = float(input("Enter the y coordinate: "))
                    color = input("Enter the new color: ")
                    repository.update_point_by_coordinates(coord_x, coord_y, color)
                except:
                    print("Invalid input. The coordinates must be real numbers.")

            case "14":
                break