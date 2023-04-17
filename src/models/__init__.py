class GameObject:
    """
    This class represents an object in the game.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tile = None  # the tile on which the object is placed

    def move(self, dx, dy):
        """
        Moves the object by (dx, dy) tiles.
        """
        self.x += dx
        self.y += dy

class Tile:
    """
    This class represents a tile on the game map.
    """
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type  # can be "wall", "empty", or "target"

class Box(GameObject):
    """
    This class represents a box in the game.
    """
    def __init__(self, x, y):
        super().__init__(x, y)

class Player(GameObject):
    """
    This class represents the player in the game.
    """
    def __init__(self, x, y):
        super().__init__(x, y)

class GameMap:
    """
    This class represents the game map.
    """
    def __init__(self, width, height, tiles):
        self.width = width
        self.height = height
        self.tiles = tiles  # a list of lists of tiles

    def get_tile(self, x, y):
        """
        Returns the tile at position (x, y).
        """
        return self.tiles[y][x]

    def set_tile(self, x, y, tile):
        """
        Modifies the tile at position (x, y).
        """
        self.tiles[y][x] = tile

    def is_valid_position(self, x, y):
        """
        Checks if position (x, y) is valid (i.e., it does not go out of the map boundaries and it is not a wall).
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return self.get_tile(x, y).type != "wall"

class Game:
    """
    This class represents the game itself.
    """
    def __init__(self, map):
        self.map = map
        self.player = None  # the player
        self.boxes = []  # a list of boxes

    def set_player(self, player):
        """
        Sets the initial position of the player.
        """
        self.player = player
        player.tile = self.map.get_tile(player.x, player.y)

    def add_box(self, box):
        """
        Adds a box to the map.
        """
        self.boxes.append(box)
        box.tile = self.map.get_tile(box.x, box.y)

    def remove_box(self, box):
        """
        Removes a box from the map.
        """
        self.boxes.remove(box)
        box.tile = None

    def is_box_at(self, x, y):
        """
        Checks if a box is present at position (x, y).
        """
        for box in self.boxes:
            if box.x == x and box.y == y:
                return True
        return False

    def is_completed(self):
        """
        Checks if all the boxes are placed on a target tile.
        """
        for box in self.boxes:
            if self.map.get_tile(box.x, box.y).type != "target":
                return False
        return True
