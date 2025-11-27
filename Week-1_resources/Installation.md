## 📦 **OpenCV Installation — Windows / macOS / Linux**

Install OpenCV according to your operating system.  
After installation, run the verification script to confirm everything works.

---

### 🪟 **Windows Installation**

```bash
pip install opencv-python
pip install opencv-python-headless    
```

---

### 🍎 **macOS Installation**

#### 1. Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. Install OpenCV

```bash
brew install opencv       # System-level OpenCV
pip install opencv-python # Python OpenCV package
```

---

### 🐧 **Linux (Ubuntu/Debian) Installation**

```bash
sudo apt update
sudo apt install python3-opencv
pip install opencv-python  # Optional upgrade
```

---

## 🧪 **Verification Script**

Create a file named `test_opencv.py` and run:

```python
import cv2

print("OpenCV Version:", cv2.__version__)

# Basic display test (needs test.jpg in same directory)
img = cv2.imread("test.jpg")

if img is not None:
    cv2.imshow("OpenCV Test Window", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("\n🎉 OpenCV is working correctly!")
    print("You are ready to move on to reading resources and doing tasks 🚀")
else:
    print("\n⚠ OpenCV installed, but 'test.jpg' not found for display test.")
```

---

### ✔ Expected Success Output

```
OpenCV Version: <version_number>
🎉 OpenCV is working correctly!
You are ready to move on to reading resources and doing tasks 🚀
```

If you see this → **Congratulations! Your environment is ready.**

---
