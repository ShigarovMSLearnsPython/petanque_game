
import pybullet as p
import time
import pybullet_data
from setup import *


# Loads ball and its physic specs
def create_ball(place, scale):
    unique_p_id = p.loadURDF("sphere2.urdf", basePosition=place, globalScaling=scale)
    p.changeDynamics(unique_p_id, linkIndex=-1, mass=BALL_MASS, restitution=BALL_BOUNCENES)
    return unique_p_id


# Loads world with horisontal plane and gravity
def load_world():
    physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
    print("data path: %s " % pybullet_data.getDataPath())

    p.setGravity(0, 0, -9.8)
    # load the plane
    plane_id = p.loadURDF("plane.urdf")
    p.changeDynamics(plane_id, linkIndex=-1, restitution=PLANE_BOUNCENESS,
                     lateralFriction=PLANE_LAT_FRIC, rollingFriction=PLANE_ROL_FRIC)


# Gets coordinate of balls on field
def get_field_data() -> dict[int, tuple[float, float, float]]:
    field_data = {}
    for i in range(1, p.getNumBodies()):
        field_data.update({i: p.getBasePositionAndOrientation(i)[0]})
    print(f'field_data = {field_data}')
    return field_data


def disconnect():
    p.disconnect()


# resets simulation, loads graviry and plane again for next round
def clean_balls():
    p.resetSimulation()
    p.setGravity(0, 0, -9.8)
    plane_id = p.loadURDF("plane.urdf")
    p.changeDynamics(plane_id, linkIndex=-1, restitution=PLANE_BOUNCENESS,
                     lateralFriction=PLANE_LAT_FRIC, rollingFriction=PLANE_ROL_FRIC)


# Simulates fling and returns ditc of field data
def fling_ball_simulation(ball_id, direction: tuple[float, float, float], start_time=True):

    p.resetBaseVelocity(objectUniqueId=ball_id, linearVelocity=direction, angularVelocity=[300, 300, 0])

    # MAIN simulation loop
    for i in range(DURATION):
        p.stepSimulation()

        # wait a while before fling - only for debugging
        if start_time:
            time.sleep(TIME_BEFORE_FLING)
            start_time = False

        # Simulations step-rate
        time.sleep(STEP_RATE / 8)

    # field_data = get_field_data()

    return get_field_data()
