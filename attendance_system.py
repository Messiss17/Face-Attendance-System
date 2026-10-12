import cv2
import os
import csv
from datetime import datetime


# -----------------------------
# Face detector
# -----------------------------

face_detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)


# -----------------------------
# Face recognizer
# -----------------------------

recognizer = cv2.face.LBPHFaceRecognizer_create()


# -----------------------------
# Load training images
# -----------------------------

faces = []
labels = []
names = {}

label_id = 0

for student_name in os.listdir("known_faces"):

    student_folder = os.path.join(
        "known_faces",
        student_name
    )

    if not os.path.isdir(student_folder):
        continue

    names[label_id] = student_name

    for image_name in os.listdir(student_folder):

        image_path = os.path.join(
            student_folder,
            image_name
        )

        image = cv2.imread(
            image_path,
            cv2.IMREAD_GRAYSCALE
        )

        detected_faces = face_detector.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5
        )

        for x, y, w, h in detected_faces:

            faces.append(
                image[y:y+h, x:x+w]
            )

            labels.append(label_id)

    label_id += 1


# -----------------------------
# Train recognizer
# -----------------------------

recognizer.train(faces, 
                 __import__("numpy").array(labels))


print("Training completed!")
print("Students:", names)


# -----------------------------
# Attendance file
# -----------------------------

os.makedirs("attendance", exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")

attendance_file = os.path.join(
    "attendance",
    today + ".csv"
)


if not os.path.exists(attendance_file):

    with open(
        attendance_file,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Name", "Date", "Time"]
        )


# -----------------------------
# Attendance function
# -----------------------------

def mark_attendance(name):

    with open(
        attendance_file,
        "r",
        newline=""
    ) as file:

        rows = list(csv.reader(file))

    for row in rows:

        if row and row[0] == name:
            return

    current_time = datetime.now().strftime(
        "%H:%M:%S"
    )

    with open(
        attendance_file,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [name, today, current_time]
        )

    print("Attendance marked:", name)


# -----------------------------
# Start camera
# -----------------------------

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    detected_faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    for x, y, w, h in detected_faces:

        face = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face)

        if confidence < 70:

            name = names[label]

            mark_attendance(name)

            text = name

        else:

            text = "Unknown"


        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            text,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


    cv2.putText(
        frame,
        "Student Attendance System",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "Attendance",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()