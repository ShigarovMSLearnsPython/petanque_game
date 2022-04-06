import numpy as np
import pybullet as p
import time
import pybullet_data
from setup import *

# Loads ball and its physic specs
def load_object(place, scale):
    unique_p_id = p.loadURDF("sphere2.urdf", basePosition=place, globalScaling=scale)
    p.changeDynamics(unique_p_id, linkIndex=-1, mass=BALL_MASS, restitution=BALL_BOUNCENES)
    return unique_p_id

# Loads world with horisontal plane and gravity
def load_world(current_round_field):
    physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
    print("data path: %s " % pybullet_data.getDataPath())

    p.setGravity(0, 0, -9.8)
    plane_id = p.loadURDF("plane.urdf")
    p.changeDynamics(plane_id, linkIndex=-1, restitution=PLANE_BOUNCENESS,
                     lateralFriction=PLANE_LAT_FRIC, rollingFriction=PLANE_ROL_FRIC)
    # and here it loads all ball in current_round_field dictionary
    for i in current_round_field:
        # cochonnet always has num 1 in current_round_field
        scale = COCHONNET_RADIUS if i == 1 else BALL_RADIUS
        print(f'current_round_field {current_round_field[i]}')
        load_object(current_round_field[i], scale=scale)

# Gets coordinate of balls on field
def get_field_data():
    field_data = {}
    for i in range(1, p.getNumBodies()):
        field_data.update({i: p.getBasePositionAndOrientation(i)[0]})
    print(f'field_data = {field_data}')
    return field_data

# Simulates fling and returns ditc of field data
def fling_ball_simulation(ball_id, dirrection, start_time=True):

    p.changeDynamics(ball_id, linkIndex=-1, mass=0.33, restitution=0.8)

    force = np.array(dirrection)
    p.applyExternalForce(objectUniqueId=ball_id, linkIndex=-1,
                         forceObj=force, posObj=dirrection, flags=p.LINK_FRAME)

    # MAIN simulation loop
    for i in range(DURATION):
        p.stepSimulation()

        if start_time:
            time.sleep(0.7)
            start_time = False

        # Simulations step-rate
        time.sleep(STEP_RATE / 8)

    field_data = get_field_data()

    # p.disconnect()

    return field_data, p.disconnect()
