import numpy as np
import pybullet as p
import time
import pybullet_data

# Hit phase simulation
STEP_RATE = 1/240.  # one spep lenght in seconds
DURATION = 5000     # steps of simulation with given STEP_RATE
HIT_POWER = 15000

physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
print("data path: %s " % pybullet_data.getDataPath())
# p.setGravity(0, 0, -10) gravity turns on after aiming stage
planeId = p.loadURDF("plane.urdf")
# Ball to be hit
ballStartPos = [0, 0, 0.5]
# ballStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
ballId = p.loadURDF("sphere2.urdf", ballStartPos, useFixedBase=1)
# Aiming pointer, that disappears with HIT button pressed
pointStartPos = [1, -1, 0.5]
pointerId = p.loadURDF("sphere2.urdf", pointStartPos, useFixedBase=0, globalScaling=0.1)
# Ball that hits
hammerId = p.loadURDF("sphere2.urdf", [5, -5, 0.5])

ballPos, ballOrn = p.getBasePositionAndOrientation(ballId)
hammPos, hammOrn = p.getBasePositionAndOrientation(hammerId)

hit_done = False

# MAIN simulation loop
for i in range(DURATION):
    p.stepSimulation()

    # Phase of aiming
    if hit_done == False:
        # Current position of aiming pointer (x,y,z)
        pointPos = p.getBasePositionAndOrientation(pointerId)[0]
        # Aims gravity to ball
        ball_gravity = 350 * (np.array(ballPos) - np.array(pointPos))
        p.applyExternalForce(objectUniqueId=pointerId, linkIndex=-1,
                             forceObj=ball_gravity, posObj=ballPos, flags=p.WORLD_FRAME)
        # Aims gravity to hammer-ball
        gem_gravity = 10 * (np.array(hammPos) - np.array(pointPos))
        p.applyExternalForce(objectUniqueId=pointerId, linkIndex=-1,
                             forceObj=gem_gravity, posObj=hammPos, flags=p.WORLD_FRAME)
    # Simulations step-rate
    time.sleep(STEP_RATE)

    # Keyboard input
    qKey = ord('q') # to quit
    spaceKey = ord(' ') # to hit

    # to move aiming pointer
    leftKey = p.B3G_LEFT_ARROW
    rightKey = p.B3G_RIGHT_ARROW
    upKey = p.B3G_UP_ARROW
    downKey = p.B3G_DOWN_ARROW

    keys = p.getKeyboardEvents()

    # QUIT KEY
    if qKey in keys and keys[qKey] & p.KEY_WAS_TRIGGERED:
        p.disconnect()
        quit()
    # HIT KEY
    if spaceKey in keys and keys[spaceKey] & p.KEY_WAS_TRIGGERED:
        # Replace unmovable ball from aiming phase by exactly the same movable for hit simulation
        p.removeBody(ballId)
        ballId = p.loadURDF("sphere2.urdf", ballStartPos, useFixedBase=0)
        # Calculating vector parameters for hit
        hammPos, hammOrn = p.getBasePositionAndOrientation(hammerId)
        pointPos, pointOrn = p.getBasePositionAndOrientation(pointerId)
        force = HIT_POWER * (np.array(pointPos) - np.array(hammPos))
        # We don't need aim anymore
        p.removeBody(pointerId)
        hit_done = True # it says aim's pointer not to be calculated

        # Gravity, hit, go!
        p.setGravity(0, 0, -9.8)
        p.applyExternalForce(objectUniqueId=hammerId, linkIndex=-1,
                             forceObj=force, posObj=pointPos, flags=p.WORLD_FRAME)

    # B3G_LEFT_ARROW
    if leftKey in keys and keys[leftKey] & p.KEY_IS_DOWN:
        posObj = (pointPos[0] - 10, pointPos[1] - 10, pointPos[2])
        p.applyExternalForce(objectUniqueId=pointerId, linkIndex=-1,
                             forceObj=[-100., -100., 0.], posObj=posObj, flags=p.WORLD_FRAME)
    # B3G_RIGHT_ARROW
    if rightKey in keys and keys[rightKey] & p.KEY_IS_DOWN:
        posObj = (pointPos[0] + 10, pointPos[1] + 10, pointPos[2])
        p.applyExternalForce(objectUniqueId=pointerId, linkIndex=-1,
                             forceObj=[100., 100., 0.], posObj=posObj, flags=p.WORLD_FRAME)
    # B3G_UP_ARROW
    if upKey in keys and keys[upKey] & p.KEY_IS_DOWN:
        posObj = (pointPos[0], pointPos[1], pointPos[2] + 10)
        p.applyExternalForce(objectUniqueId=pointerId, linkIndex=-1,
                             forceObj=[0., 0., 100.], posObj=posObj, flags=p.WORLD_FRAME)
    # B3G_DOWN_ARROW
    if downKey in keys and keys[downKey] & p.KEY_IS_DOWN:
        posObj = (pointPos[0], pointPos[1], pointPos[2] - 10)
        p.applyExternalForce(objectUniqueId=pointerId, linkIndex=-1,
                             forceObj=[0., 0., -100.], posObj=posObj, flags=p.WORLD_FRAME)

p.disconnect()
