import pybullet as p
import pybullet_data
import time
import math
import numpy as np

# ==========================================
# 1. SIMULATION SETUP
# ==========================================
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)

# Load Plane
plane = p.loadURDF("src/plane.urdf")

# Load Drone at Origin
# Note: No "p.createConstraint" here. The drone is free in 3D.
startPos = [0, 0, 0.1]
drone = p.loadURDF("src/quadrotor.urdf", startPos)

# ==========================================
# 2. DEFINE SETPOINTS (WAYPOINTS)
# ==========================================
# The drone will fly to these coordinates in order.
waypoints = [
    [0, 0, 1],    # 1. Takeoff to 1m
    [1, 0, 1],    # 2. Move Right (X-axis)
    [1, 1, 1],    # 3. Move Forward (Y-axis)
    [0, 1, 2],    # 4. Move Left and Up
    [0, 0, 2]     # 5. Return Home and Hover at 2m
]

current_wp_index = 0
distance_threshold = 0.2  # Drone must get within 0.2m to switch to next point

# ==========================================
# 3. PID CONTROLLER
# ==========================================
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0
    
    def compute(self, target, current, dt):
        error = target - current
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

# --- STUDENT TUNING SECTION ---
# Tuning Tip: 
# 1. Z-axis needs enough Force to lift the 0.5kg drone (Force > 5N).
# 2. X and Y need to be snappy but not shaky.
pid_x = PIDController(kp=2.0, ki=0.0, kd=1.5)
pid_y = PIDController(kp=2.0, ki=0.0, kd=1.5)
pid_z = PIDController(kp=10.0, ki=0.0, kd=5.0) 
# ------------------------------

# ==========================================
# 4. MAIN LOOP
# ==========================================
print("Task 2: Waypoint Navigation Started...")
print(f"Current Target: {waypoints[0]}")

last_time = time.time()

while True:
    current_time = time.time()
    dt = current_time - last_time
    last_time = current_time
    if dt == 0: dt = 1./240.

    # A. Get Drone State
    pos, orn = p.getBasePositionAndOrientation(drone)
    current_x, current_y, current_z = pos

    # B. RECTIFY METHOD (Magic Gyro)
    # Forces drone upright so students only solve Position PID, not Attitude.
    p.resetBasePositionAndOrientation(drone, pos, [0, 0, 0, 1])

    # C. Waypoint Logic
    if current_wp_index < len(waypoints):
        target = waypoints[current_wp_index]
        
        # Calculate 3D distance to target
        dx = target[0] - current_x
        dy = target[1] - current_y
        dz = target[2] - current_z
        dist = math.sqrt(dx*dx + dy*dy + dz*dz)
        
        # Check if we reached the waypoint
        if dist < distance_threshold:
            print(f" >>> Reached Waypoint {current_wp_index + 1}!")
            current_wp_index += 1
            if current_wp_index < len(waypoints):
                print(f"New Target: {waypoints[current_wp_index]}")
            else:
                print("All Waypoints Complete! Hovering...")
    else:
        # Stay at the last waypoint if finished
        target = waypoints[-1]

    # D. Compute PID Output
    fx = pid_x.compute(target[0], current_x, dt)
    fy = pid_y.compute(target[1], current_y, dt)
    fz = pid_z.compute(target[2], current_z, dt)

    # E. Gravity Compensation
    # Drone Mass ~0.5kg * 10m/s^2 = 5.0 Newtons downward force.
    # We add 5.0 to Fz so the PID doesn't have to fight gravity from 0.
    fz += 5.0 

    # F. Apply Forces (World Frame)
    p.applyExternalForce(drone, -1, forceObj=[fx, fy, fz], posObj=[0,0,0], flags=p.WORLD_FRAME)

    # G. Step Simulation
    p.stepSimulation()
    time.sleep(1./240.)