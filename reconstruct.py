import numpy as np
from custom_types import *

class Reconstructor:

    def __init__(self, photos) -> None:
        self.photos = photos
        self.walls = []

    def process_photos(self):
        self.walls = []
        frames = []
        corners_list = []
        edges_list = []
        start_collecting = False
        for photo in self.photos:
            corners = self._find_corners(photo["image"])
            edges = self._find_edges(photo["image"])
            # if two corners: init the wall
            if len(corners) == 2:
                self.walls.append({
                    "frames": [photo],
                    "corners": corners,
                    "edges": edges
                })
            # if one corner: start collecting frames
            # if the second corner: init the wall, matching the frames
            elif len(corners) == 1:
                frames.append(photo)
                corners_list.append(corners)
                edges_list.append(edges)
                if start_collecting:
                    self.walls.append({
                        "frames": frames,
                        "corners": corners_list,
                        "edges": edges_list
                    })
                    start_collecting = False
                    frames = []
                    corners_list = []
                    edges_list = []
                else:
                    start_collecting = True
        for wall_id, wall in enumerate(self.walls):
            if wall["frames"] > 1:
                self.walls[wall_id] = self._match_frames(
                    wall["frames"], wall["corners"], wall["edges"])

    def _find_corners(self, photo_id):
        pass

    def _find_edges(self, photo_id):
        pass
    
    def _match_frames(self, frames, corners, edges):
        if len(frames) < 2:
            return {
                    "frames": frames,
                    "corners": corners,
                    "edges": edges
                }
        pass

    def reconstruct(self):
        reconstructed_map = ReconstructedMap()
        prior_height = 2.5
        direction_angle_rad = 0.0
        direction = np.array([1.0, 0.0, 0.0])
        lu_coords = np.array([0.0, 0.0, 0.0])
        for wall in self.walls:
            left_corner, right_corner = wall["corners"]
            height = max(left_corner.y1 - left_corner.y0, right_corner.y1 - right_corner.y0)
            width = (left_corner.x0 + left_corner.x1 + right_corner.x0 + right_corner.x1) / 4
            # reconstruct the plane given prior height
            reconstructed_width = prior_height * float(width) / height 
            reconstructed_map.walls.append(Wall(
                prior_height, reconstructed_width, lu_coords, direction_angle_rad))
            # estimate directory change
            if right_corner.dir == 1:
                direction_angle_rad = direction_angle_rad + np.pi / 2
                # change coords right
                lu_coords = lu_coords + np.rot90(direction, 3, (0, 2)) * reconstructed_width
            else:
                direction_angle_rad = direction_angle_rad - np.pi / 2
                # change coords right
                lu_coords = lu_coords + np.rot90(direction, 1, (0, 2)) * reconstructed_width

    # visualize reconstruction
    def visualize(self):
        pass
