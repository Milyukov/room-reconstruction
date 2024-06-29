from reconstruct import *
from custom_types import *
import numpy as np

def generate_test_model():
    pass

def project_model_on_cameras(model):
    pass

def test_visuzalization():
    reconstructor = Reconstructor()
    reconstructor.walls.append(Wall(2.5, 7, np.array([0, 0, 0]), 0))
    reconstructor.walls.append(Wall(2.5, 5, np.array([7, 0, 0]), np.pi / 2))
    reconstructor.walls.append(Wall(2.5, 7, np.array([7, 0, 5]), np.pi))
    reconstructor.walls.append(Wall(2.5, 5, np.array([0, 0, 5]), 3 * np.pi / 20))
    reconstructor.visualize()

def test_reconstruction():
    frames = []
    frames.append(Frame())
    frames[-1].left_corner = Corner(0, 0, 0, 250)
    frames[-1].right_corner = Corner(700, 0, 700, 250)
    frames.append(Frame())
    frames[-1].left_corner = Corner(0, 0, 0, 250)
    frames[-1].right_corner = Corner(500, 0, 500, 250)
    frames.append(Frame())
    frames[-1].left_corner = Corner(0, 0, 0, 250)
    frames[-1].right_corner = Corner(700, 0, 700, 250)
    frames.append(Frame())
    frames[-1].left_corner = Corner(0, 0, 0, 250)
    frames[-1].right_corner = Corner(500, 0, 500, 250)

    # generate ground truth 3D model of the room
    model = generate_test_model()
    # project features on cameras (start with one frame per wall)
    features = project_model_on_cameras(model)
    # process pixel coordinates of features (test that reconstructed 3D coordinates match with ground truth)
    #reconstructed_model = 

if __name__ == '__main__':
    test_visuzalization()
    test_reconstruction()