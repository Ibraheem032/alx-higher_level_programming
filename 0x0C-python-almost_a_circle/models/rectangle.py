#!/usr/bin/python3
"""
Contains class "Base"
"""


class Base:
    """
    Creating the class.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
class Rectangle(Base):
    """Creating a subclass of class "Base".
    """
    def display(self):
        try:
            for j in range(self.__height):
                print("#" * self.__width)
        except Exception:
            pass

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")		
        self.__x = x

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        l1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
        l2 = f"- {self.__width}/{self.__height}"
        return (l1 + l2)

    def update(self, *args, **kwargs):
        try:
            if args:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            else:
                for key in kwargs:
                    if key == 'id':
                        self.id = kwargs[key]
                    elif key == 'width':
                        self.__width = kwargs[key]
                    elif key == 'height':
                        self.__height = kwargs[key]
                    elif key == 'x':
                        self.__x = kwargs[key]
                    elif key == 'y':
                        self.__y = kwargs[key]
        except Exception:
            pass
