import numpy as np

class Camera:

    def __init__(self, focal_distance, height, width) -> None:
        self.f = focal_distance
        self.cx = width / 2
        self.cy = height / 2
        self.K = np.array([
            [focal_distance, 0, self.cx],
            [0, focal_distance, self.cy],
            [0, 0, 1]
        ])
        self.pos = np.zeros((3, 1))
        self.dir = np.zeros((3, 1))
        self._recalc_rotation()

    def set_pos(self, pos):
        self.pos = pos

    def set_dir(self, dir):
        self.dir = dir

    def _recalc_rotation(self):
        self.R = None

    def render(self, frame, point):
        point_hom = np.concatenate((point, np.ones((1, 1))))
        point_frame = self.K.dot(self.R).dot(point_hom)
        x = point_frame[0] / point_frame[2]
        y = point_frame[1] / point_frame[2]
        frame[y, x, :] = 255
