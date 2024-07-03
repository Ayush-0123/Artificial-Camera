import cv2
import numpy as np

def depth():
    # OpenCV VideoCapture
    cap = cv2.VideoCapture(0)

    # Load pre-trained face detection cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Calculate depth for each face detected
        for (x, y, w, h) in faces:
            # Calculate the distance between eyes (assumption: eyes are 1/3 of the face width apart)
            eye_distance = w / 3

            # Set known parameters
            real_eye_distance = 6.3  # Real-world distance between eyes in centimeters
            focal_length = 840  # Focal length of the camera in pixels

            # Calculate depth using similar triangles
            depth = (real_eye_distance * focal_length) / eye_distance

            # Display depth information on the frame
            cv2.putText(frame, f"Depth: {depth:.2f} cm", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the processed frame
        cv2.imshow('Depth Estimation', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

   
