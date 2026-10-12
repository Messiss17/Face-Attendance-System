# 🎯 FACE ATTENDANCE SYSTEM

### Automated Student Attendance Using Face Recognition

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Project-Computer%20Vision-purple" alt="Computer Vision">
</p>

## 📌 Project Overview

The **Face Attendance System** is a Python-based computer vision application that automates student attendance using webcam input and face recognition.

The system captures facial samples, identifies registered faces using a trained recognition model, and records attendance in a date-wise CSV file. It demonstrates how computer vision can be applied to reduce manual attendance work and organize attendance records.

## 💡 Why This Project?

- 📝 **Manual Work Reduction:** Reduces the need for repetitive manual attendance entry.
- ⚡ **Automation:** Supports attendance recording through face recognition.
- 🎯 **Face Identification:** Recognizes previously registered faces using a trained model.
- 📊 **Digital Records:** Stores attendance in CSV format for easy review.
- 🎓 **Practical Learning:** Demonstrates Python programming, image processing, and computer vision.

## ✨ Key Features

- 📷 **Webcam Integration:** Captures live video for face detection and recognition.
- 👤 **Face Sample Collection:** Captures facial samples for registered individuals.
- 🧠 **Face Recognition:** Uses OpenCV's LBPH face recognizer when configured in the application.
- 🔍 **Face Detection:** Uses the Haar Cascade classifier to detect faces.
- 📅 **Attendance Logging:** Saves attendance records in date-wise CSV files.
- 🧪 **Camera Testing:** Includes a separate script to verify webcam functionality.

## ⚙️ How It Works

The system follows this workflow:

1. **Camera Initialization:** Opens the webcam and captures live video.
2. **Face Detection:** Detects faces in video frames using the Haar Cascade classifier.
3. **Face Registration:** Captures and stores facial samples for known individuals.
4. **Model Training:** Trains the recognition model using the collected face samples.
5. **Face Recognition:** Compares detected faces with the registered face data.
6. **Attendance Recording:** Records recognized individuals in a date-wise CSV file.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| OpenCV | Image processing and computer vision |
| Haar Cascade | Face detection |
| LBPH Face Recognizer | Face identification |
| NumPy | Numerical and array operations |
| CSV | Attendance data storage |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
Face-Attendance-System/
│
├── attendance/
│   ├── README.md
│   └── requirements.txt
│
├── attendance_system.py
├── camera_test.py
├── capture_faces.py
├── haarcascade_frontalface_default.xml
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3
- Webcam
- Git
- Required Python libraries

### 1. Clone the Repository

```bash
git clone https://github.com/Messiss17/Face-Attendance-System.git
cd Face-Attendance-System
```

### 2. Create a Virtual Environment

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the packages required by the project:

```bash
pip install opencv-contrib-python numpy
```

The `opencv-contrib-python` package provides the OpenCV face-recognition module used by LBPH. If your code uses additional libraries, install those too.

### 4. Run the Application

**Test the webcam:**

```bash
python camera_test.py
```

**Capture face samples:**

```bash
python capture_faces.py
```

**Start the attendance system:**

```bash
python attendance_system.py
```

Follow the instructions displayed by the application. Register and train the required faces before attempting recognition.

## 📊 Output

The application is designed to provide:

- Live webcam-based face detection and recognition.
- Recognition of registered individuals.
- Date-wise attendance records in CSV format.

*Add a screenshot of your working application here to demonstrate the actual output.*

## 🔮 Future Enhancements

- 🖥️ Develop a graphical user interface.
- 📈 Generate attendance summaries and reports.
- 🗄️ Integrate a database for student information.
- 🔐 Add secure administrator access.
- 📧 Introduce attendance notifications and report exports.

## 🔒 Privacy and Security

- Do not publish personal face images or biometric training data.
- Do not upload private attendance records.
- Obtain appropriate consent before collecting or processing facial data.

## 👩‍💻 Author

**Messi Sonia**

Electronics and Communication Engineering Student

GitHub: [@Messiss17](https://github.com/Messiss17)

---

⭐ **If you find this project interesting, explore the repository and share your feedback!**