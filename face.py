import cv2
import time
import datetime

def face():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open video device")
        return

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

    recording = False
    detection_start_time = None
    SECONDS_TO_RECORD_AFTER_DETECTION = 5
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = None

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = body_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0 or len(bodies) > 0:
            if not recording:
                recording = True
                detection_start_time = time.time()
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
                print("Started Recording!")
        else:
            if recording:
                if time.time() - detection_start_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                    recording = False
                    out.release()
                    print('Stop Recording!')

        if recording:
            out.write(frame)
            for (x, y, width, height) in faces:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
            for (x, y, width, height) in bodies:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 3)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage:
# face()
