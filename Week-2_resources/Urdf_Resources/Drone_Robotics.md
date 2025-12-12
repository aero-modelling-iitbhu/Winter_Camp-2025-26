# 🚁 Drone Robotics: Movement and Computation

A drone is more than just a flying machine; it is an aerial robot that transcends simple remote control. It combines the ability to **compute** (via Flight Controllers) with the capability of **3D movement**.

Unlike ground robots which rely on kinematic chains of limbs, a drone's movement is achieved through aerodynamics and precise variation of motor speeds.

### 🔗 The Structure: Links (The Frame)
In the context of drone mechanics and modeling (like URDF), we still view the robot as a collection of links:

* **Base Link (Fuselage):** The foundation or "central hub" that houses the flight controller, battery, and sensors. It acts as the anchor for the entire system.
* **Child Links (Arms & Landing Gear):** Rigid segments connected to the base. They provide the structural integrity to hold the motors far enough from the center to generate torque (yaw).

> **Note:** Ideally, a drone frame is rigid. We want minimum vibration and flexing in these links to ensure stable flight.

---

### ⚙️ Joints and Rotors
Now that we understand the frame, let’s look at how things move. In standard ground robots, joints like elbows and wrists are key. In drones, the concept is slightly different but just as critical for simulation and modeling.

#### 1. The "Virtual" Joint
* **Floating Joint:** Unlike a robot arm bolted to a table, a drone isn't attached to the ground. In simulation (like Gazebo/ROS), we often define a "Floating Joint" (6 degrees of freedom) connecting the drone's `base_link` to the `world`. This allows it to move freely in x, y, z, roll, pitch, and yaw.

#### 2. Physical Joints
* **Continuous Joints (Propellers):** The connection between the motor bell and the frame is modeled as a continuous joint. It rotates infinitely around one axis (the Z-axis of the motor) to generate thrust.
* **Revolute Joints (Gimbals):** If your drone has a camera, it likely uses a 2-axis or 3-axis gimbal. These are standard revolute joints that rotate to keep the camera steady while the drone tilts.

---

### ⚡ Actuators: The Power of Flight
We've explored the structure, but how does the drone actually defy gravity? That's where **Actuators** come in. In the drone world, these are almost exclusively electrical.

* **Brushless DC Motors (BLDC):** The absolute workhorses of modern drones. They are efficient, powerful, and durable. By changing the speed of these motors, the drone changes its orientation:
    * *Speed up all motors:* Ascend.
    * *Speed up one side:* Roll/Pitch.
    * *Spin diagonals faster:* Yaw (Rotation).
* **Electronic Speed Controllers (ESCs):** While not a "moving" part, the ESC is the bridge between the computer and the motor. It acts as the driver, translating digital commands from the flight controller into precise electrical pulses for the motors.
* **Servo Motors:** Often used for tilting mechanisms (in VTOL planes) or camera gimbals.

---

### 🚀 Next Steps
Now that you've covered the basics of aerial mechanics, it's time to explore **URDF (Unified Robot Description Format)** to define your drone's geometry and begin coding your flight algorithms!