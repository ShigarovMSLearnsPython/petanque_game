import numpy as np
import pybullet as p
import time
import pybullet_data

# import game
class Ball:
    def __init__(self, x, y, z, team, scale):
        self.place = (x, y, z)
        self.team = team
        self.scale = scale


STEP_RATE = 1/240.  # one spep lenght in seconds
DURATION = 5000     # steps of simulation with given STEP_RATE
HIT_POWER = 20000

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
print("data path: %s " % pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
plane_id = p.loadURDF("plane.urdf")
p.changeDynamics(plane_id, linkIndex=-1, restitution=0.3, lateralFriction=0.6, rollingFriction=0)


def load_object(ball: Ball):
    # ball.id = p.loadURDF("sphere2.urdf", ball.place, globalScaling=ball.scale)
    return p.loadURDF("sphere2.urdf", ball.place, globalScaling=ball.scale)


def load_world(a):
    for ball in a:
        load_object(ball)


def get_fling_results():
    pass


def fling_ball_simulation(ball: Ball, dirrection, power):

    # STEP_RATE = 1 / 120.  # one spep lenght in seconds
    # DURATION = 1000  # steps of simulation with given STEP_RATE
    #
    # physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
    # p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
    # print("data path: %s " % pybullet_data.getDataPath())
    # p.setGravity(0, 0, -9.8)
    # plane_id = p.loadURDF("plane.urdf", basePosition=(0, 0, 0), useFixedBase=1)
    # p.changeDynamics(plane_id, linkIndex=-1, restitution=0.3, lateralFriction=0.6, rollingFriction=0)


    # load_world(round.field)
    ball_id = load_object(ball)
    p.changeDynamics(ball_id, linkIndex=-1, mass=0.33, restitution=1.5)
    force = power * np.array(dirrection)
    return p.applyExternalForce(objectUniqueId=ball_id, linkIndex=-1,
                         forceObj=force, posObj=dirrection, flags=p.LINK_FRAME)



    # return get_fling_results()

dirrection = (-1, 0, 1.4)
power = 380

ball_1 = Ball(0,0,0.3, 1, 0.2)

fling_ball_simulation(ball_1, dirrection, power)

# MAIN simulation loop
for i in range(DURATION):
    p.stepSimulation()
    # Simulations step-rate
    time.sleep(STEP_RATE/8)

