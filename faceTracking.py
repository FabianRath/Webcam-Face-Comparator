import cv2
import dlib
import face_recognition
import numpy as np
import time
import os
import time
from datetime import datetime

reference_image = face_recognition.load_image_file("reference_image.jpg")
reference_face_encoding = face_recognition.face_encodings(reference_image)[0]

face_detector = dlib.get_frontal_face_detector()
def draw_rectangle(img, rect, label):
    x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

def rect_to_tuple(rect):
    left, top, right, bottom = rect.left(), rect.top(), rect.right(), rect.bottom()
    return top, right, bottom, left

def save_no_match_screenshot(frame):
    output_folder = "no_match_faces"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    current_datetime = datetime.now()
    datetime_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"{output_folder}/no_match_{datetime_string}.png"
    cv2.imwrite(output_filename, frame)

def main():
    cap = cv2.VideoCapture(0)

    last_screenshot_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = face_detector(frame, 1)
        no_match_found = False

        for face in faces:
            face_location = rect_to_tuple(face)

            face_encodings = face_recognition.face_encodings(frame, [face_location])

            if len(face_encodings) > 0:
                face_encoding = face_encodings[0]

                match = face_recognition.compare_faces([reference_face_encoding], face_encoding)

                if match[0]:
                    label = "Match"
                else:
                    label = "No Match"
                    no_match_found = True
            else:
                label = "No Encoding"

            draw_rectangle(frame, face, label)

        current_time = time.time()

        if no_match_found and (current_time - last_screenshot_time) >= 60:
            save_no_match_screenshot(frame)
            last_screenshot_time = current_time

        cv2.imshow("Face Comparison", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
