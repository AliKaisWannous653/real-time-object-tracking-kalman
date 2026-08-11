

🚀 Installation

Install the required Python packages:

pip install numpy opencv-python matplotlib

Run the project:

python main.py

Press:

q

to exit the application.

---

⚠️ Engineering Challenges

The project was developed as a practical experiment rather than only a theoretical implementation.

The main challenges were:

- Maintaining real-time FPS on limited hardware
- Designing a reliable color-segmentation pipeline
- Handling noisy centroid measurements
- Selecting appropriate Kalman Filter parameters
- Understanding the effect of P, Q, R, and dt
- Handling invalid or missing visual measurements
- Maintaining prediction during temporary object disappearance

These challenges were used as part of the experimental analysis rather than being hidden from the final results.

---

🔭 Future Work

Possible extensions include:

- Adaptive Q and R
- Improved long-term occlusion handling
- Constant-acceleration motion model
- Multi-object tracking
- SORT / DeepSORT comparison
- More robust object detection
- Camera-motion compensation

---

👤 Author

Ali Wannous

Electronic Systems Engineering — HIAST, Damascus

Incoming Master's Student in Computer Vision — VIBOT
Université Bourgogne Europe, France

This project represents a practical bridge between Electronic Systems Engineering, Control Theory, and Computer Vision.
