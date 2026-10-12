import cv2
import os

name = input("Enter student name: ")

folder = os.path.join("known_faces", name)

os.makedirs(folder, exist_ok=True)

camera = cv2.VideoCapture(0)

count = 0

print("Look at the camera...")
print("Press Q to stop.")

while True:

    success, frame = camera.read()

    if not success:
        break

    cv2.imshow("Register Face", frame)

    if count < 30:
        file_name = os.path.join(
            folder,
            f"{count}.jpg"
        )

        cv2.imwrite(file_name, frame)

        count += 1

    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Face registration completed!")