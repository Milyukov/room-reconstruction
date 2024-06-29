class Frame:

    def __init__(self) -> None:
        self.left_corner = Corner()
        self.right_corner = Corner()



class Wall:

    def __init__(self, height, width, lu_coords, direction) -> None:
        self.height = height
        self.width = width
        self.lu_coords = lu_coords
        self.direction = direction

class ReconstructedMap:
    
    def __init__(self) -> None:
        self.walls = []

class Corner:

    def __init__(self, x0=0, y0=0, z0=0, x1=0, y1=0, z1=0) -> None:
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

