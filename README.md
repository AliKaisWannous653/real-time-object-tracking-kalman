Real-Time Color-Based Object Tracking with Kalman Filter

A real-time computer vision project for detecting and tracking a colored object using OpenCV, contour analysis, and a Kalman Filter.

The project was developed as a practical study of the connection between computer vision, image processing, and state estimation.

🎥 Demo

A short video demonstrating the complete tracking system, including object detection, centroid tracking, Kalman prediction, and temporary object occlusion.

"Watch the Demo" (https://www.youtube.com/watch?v=tAHP9uk7Mbc)

📊 Project Presentation

The presentation explains the complete project in more detail, including:

- Image segmentation pipeline
- Contour analysis
- Centroid extraction
- Kalman Filter mathematical model
- Q, R, P, and dt
- Experimental parameter selection
- Trajectory and error analysis
- FPS and computational limitations
- Experimental results

"View the Presentation" (https://www.youtube.com/watch?v=x6IYB1JJDP8)

 Pipeline

Camera
  ↓
HSV Color Segmentation
  ↓
Binary Mask
  ↓
Contour Detection
  ↓
Centroid Measurement
  ↓
Kalman Filter
  ↓
Prediction / Estimation

⚙️ Main Technologies

- Python
- OpenCV
- NumPy
- Matplotlib
- HSV color segmentation
- Contour analysis
- Kalman Filtering
- Real-time camera processing

📈 Results

The system was tested in real time and achieved approximately 35 FPS under normal conditions on the development computer.

The experiments included:

- Raw centroid measurements
- Kalman-filtered estimates
- Object trajectory visualization
- Temporary object disappearance
- Prediction without measurements
- Measurement–estimate difference analysis

«The reported measurement–estimate difference is not a ground-truth tracking error because no independent ground-truth position was available.»

💻 Development Hardware

Component| Specification
CPU| Intel processor — 2 physical / 4 logical CPUs
RAM| 3.88 GB
OS| Windows 8.1
Python| 3.8.10
Camera| 640 × 480

The project was developed on limited computational resources, making real-time performance an important practical challenge.

📁 Project Structure

project/
│
├── main.py
├── config.py
├── TIME.py
├── visualization.py
│
├── vision/
│   ├── segmentation.py
│   └── contour.py
│
├── tracker/
│   └── KalmanTracker.py
│
├── docs/
│   └── presentation.pdf
│
└── README.md

🚀 Installation

pip install numpy opencv-python matplotlib

Run the project with:

python main.py

Press "q" to exit.

⚠️ Challenges

The main practical challenges were:

- Limited CPU and RAM resources
- Maintaining real-time FPS
- Color-segmentation sensitivity
- Temporary object occlusion
- Choosing suitable Kalman Filter parameters
- Handling invalid measurements and prolonged object disappearance

🔭 Future Work

Possible extensions include:

- Adaptive Q and R
- Better long-term occlusion handling
- Multi-object tracking
- Constant-acceleration models
- SORT / DeepSORT comparison
- More robust object detection

👤 Author

Ali Wannous
Electronic Systems Engineering — HIAST, Damascus

Incoming Master's Student in Computer Vision — VIBOT
Université Bourgogne Europe, France
