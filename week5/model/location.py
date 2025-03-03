class Location:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def set_x(self, new_x: int) -> None:
        self.__x = new_x

    def set_y(self, new_y: int) -> None:
        self.__y = new_y

    def equals(self, other_location) -> bool:
        return self.__x == other_location.get_x() and self.__y == other_location.get_y()

    def __str__(self) -> str:
        return f"Location(x={self.__x}, y={self.__y})"