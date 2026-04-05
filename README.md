# 🎯 Real-Time Color Detection using OpenCV

This project demonstrates a simple yet effective approach to **real-time color detection** using a webcam. It identifies a specific color in the video stream and draws a bounding box around detected regions.

---

## 🚀 Features

* Real-time video capture using OpenCV
* Color detection in HSV color space
* Dynamic masking based on selected color
* Bounding box visualization around detected regions
* Lightweight and easy to understand

---

## 🛠️ Technologies Used

* Python
* OpenCV (`cv2`)
* PIL (Python Imaging Library)

---

## 📁 Project Structure

```
ColorDetector/
│
├── main.py          # Main script for real-time detection
├── util.py          # Helper function (get_limits)
└── README.md
```

---

## ⚙️ How It Works

1. Captures video from your webcam
2. Converts each frame from **BGR → HSV color space**
3. Generates a mask for the target color
4. Finds the bounding box of detected regions
5. Draws a rectangle around detected color areas

---

## 🎨 Color Selection

```python
blue = [255, 0, 0]  # (BGR format)
```

* The color is defined in **BGR format** (not RGB)
* You can change this value to detect different colors

---

## 📌 Example Flow

* Capture frame
* Convert to HSV
* Apply color threshold
* Create mask
* Detect bounding box
* Draw rectangle

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install opencv-python pillow
```

2. Run the script:

```bash
python main.py
```

3. Press **`q`** to exit the window

---

## 🧠 Helper Function (`get_limits`)

This function (in `util.py`) converts a BGR color into a lower and upper HSV range used for masking.

---

## ⚠️ Notes

* Works best in **good lighting conditions**
* Performance may vary depending on webcam quality
* HSV color space is used because it’s more robust for color detection than RGB

---

## 🔮 Future Improvements

* Track multiple colors simultaneously
* Add object tracking (centroid tracking)
* Improve robustness using morphology operations
* Add GUI for dynamic color selection

---

## 📷 Demo

The application opens a webcam window and highlights the detected color with a green rectangle in real time.

---

## 📄 License

This project is open-source and free to use.

---

## 🙌 Acknowledgment

Built as part of learning computer vision fundamentals using OpenCV.
