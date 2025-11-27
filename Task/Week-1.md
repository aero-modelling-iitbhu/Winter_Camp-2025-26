# Task 1: ArUco Marker Detection

## Objective
Detect ArUco markers in a given image, identify each marker, and visualize the detection.

For each detected marker, you should:
- Draw a bounding box around the marker.
- Display the ArUco marker ID on the image.
- (Optional but recommended) Print the marker ID and its center coordinates in the console.

---

## Instructions

### Image File
- Download the image from this link:  
  **[Download ArUco Image](ImageRef/Task-1.png)**  
  The image will contain **6 ArUco markers**.

### Requirements
- Use **OpenCV** in Python.
- Use the **ArUco module** (e.g., `cv2.aruco`) for marker detection.
- For each detected marker:
  - Draw a **bounding box** around it.
  - Write the **marker ID** near the box.
- The final annotated image should clearly show:
  - Each ArUco marker
  - Its bounding box
  - Its ID

### Submission
Submit a **compressed ZIP file** containing:

1. **Python Script**  
   - `task1_aruco_detection.py`

2. **Output Image**  
   - Annotated image showing bounding boxes and IDs  
   - Example filename: `task1_output_aruco_annotated.png`

3. **Video (Short Demo)**  
   - A short screen recording or camera recording (≈ 10–20 seconds) showing your script running and detection working.  
   - Example filename: `task1_demo_video.mp4`

4. **Screenshot(s)**  
   - At least one screenshot of the annotated output image.  
   - Example filename: `task1_screenshot.png`

---

# Task 2: Contour Detection and Centroid Identification

## Objective
Detect polygons/objects in a given image using **contours**, identify their centroids, and print:

- The name of the polygon (e.g., triangle, rectangle, pentagon, circle-like)  
- The centroid coordinates of each detected shape  

---

## Instructions

### Image File
- Download the image from this link:  
  **[Download Contour Image](ImageRef/Task-2.png)**

### Requirements
- Use **OpenCV’s contour functions** (e.g., `cv2.findContours`).
- Detect the shapes in the image using contour approximation.
- For each polygon:
  - Determine its **type** (triangle, quadrilateral, etc.).
  - Calculate its **centroid** using image moments (`cv2.moments`).
- Print for each detected shape:
  - Polygon name  
  - Centroid coordinates  
- **Save the output** (polygon name + centroid coordinates) to a text file using Python file handling.

### Submission
Submit a **compressed ZIP file** containing:

1. **Python Script**  
   - `task2_contour_centroid.py`

2. **Output Text File**  
   - Contains the polygon names and centroid coordinates.  
   - Example format:  
     ```
     Triangle  → Centroid: (x1, y1)
     Rectangle → Centroid: (x2, y2)
     Circle    → Centroid: (x3, y3)
     ```  
   - Example filename: `task2_output_centroids.txt`

3. **Output Image (Optional but Recommended)**  
   - Image with contours drawn and centroids marked.  
   - Example filename: `task2_output_contours.png`

---

# Task 3: Plant Arena Analysis with ArUco & Color Detection

## Objective
Given an image of an **arena**:
- The arena has several **plants**: some are **yellow**, and the rest are **green**.
- There are **ArUco markers at the 4 corners** of the arena.

You must:
1. Detect the ArUco markers and define the arena boundary as a box.
2. Detect and highlight all **yellow plants** inside the arena.
3. Provide your **approach/explanation** in a text file.

---

## Instructions

### Image File
- Download the arena image from this link:  
  **[Download Arena Image](ImageRef/Task3.png)**

### Requirements

1. **ArUco Marker Detection**
   - Use OpenCV’s ArUco functions to:
     - Detect the **4 corner markers**.
     - Draw a **bounding box** (or outline) representing the arena using these markers.

2. **Yellow Plant Detection**
   - Use **color detection** (recommended: convert to HSV and use masking).
   - Detect and highlight **yellow plants** (e.g., draw circles, bounding boxes, or contours).
   - Green plants may remain unmarked (focus on yellow ones).
   - (Optional) Count and print the number of yellow plants detected.

3. **Output Visualization**
   - Final output image should show:
     - The arena box (based on ArUco markers).
     - All **yellow plants highlighted/marked**.

4. **Approach Description**
   - Create a short text file explaining:
     - How you detected the arena using ArUco markers.
     - How you detected yellow plants (e.g., HSV ranges, masking, contours).
     - Any challenges or assumptions.

---

## Submission

Submit a **compressed ZIP file** containing:

1. **Python Script**  
   - `task3_arena_plants_detection.py`

2. **Output Image**
   - Annotated arena image with:
     - Arena boundary drawn
     - Yellow plants marked  
   - Example filename: `task3_output_arena_plants.png`

3. **Screenshot(s)**
   - At least one screenshot of your output or code running.  
   - Example filename: `task3_screenshot.png`

4. **Approach Text File**
   - A brief explanation of your method.  
   - Example filename: `task3_approach.txt`

---

## 📤 Submission Link

Please upload your ZIP files for all tasks here:

👉 **[Submission Portal](ADD_SUBMISSION_LINK_HERE)**
