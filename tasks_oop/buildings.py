class Building:
    def __init__(self, south, west, width_we, width_ns, height=10):
        self.south = south
        self.west = west
        self.width_we = width_we
        self.width_ns = width_ns
        self.height = height

    @property
    def east(self):
        return self.west + self.width_we

    @property
    def north(self):
        return self.south + self.width_ns

    @property
    def corners_coordinates(self):
        """
        Returns a dictionary with the coordinates of the building corners.
        """

        return {'north-east': [self.north, self.east],
                'south-east': [self.south, self.east],
                'south-west': [self.south, self.west],
                'north-west': [self.north, self.west]}

    @property
    def area(self):
        """
        Returns the area of the building.
        """

        return abs((self.north - self.south) * (self.west - self.east))

    @property
    def volume(self):
        """
        Returns the volume of the building.
        """

        return self.area * self.height

    def __repr__(self):
        """
        This is a string representation of the Building.
        This method is used for 'print' or 'str' conversion.
        """

        return f'Building({self.south}, {self.west}, {self.width_we}, {self.width_ns}, {self.height})'

    def show_building(self):
        return (f'{self}\n'
                f'Coordinates of corners: {self.corners_coordinates}\n'
                f'Area: {self.area}\n'
                f'Volume: {self.volume}')


if __name__ == '__main__':
    b = Building(1, 2.5, 4.2, 1.25, 101)
    print(b.show_building())
