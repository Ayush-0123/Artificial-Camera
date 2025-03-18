import cv2
import numpy as np

def depth():
    cap = cv2.VideoCapture(0)
    
    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return
    # Alert parameters
    threshold_cm = 40  # Depth threshold in centimeters
    alert_triggered = False  # To prevent continuous beeping
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        current_alert = False  # Reset for this frame
        
        for (x, y, w, h) in faces:
            # Estimate depth based on face width
            # Assumption: the distance between eyes is roughly 1/3 of the face width
            eye_distance = w / 3  
            real_eye_distance = 6.3  # Real-world average distance between eyes in centimeters
            focal_length = 840     # Example focal length (in pixels); adjust for your camera
            depth_cm = (real_eye_distance * focal_length) / eye_distance

            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Display the estimated depth on the frame
            cv2.putText(frame, f"Depth: {depth_cm:.2f} cm", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # If the face is too close, mark it as an alert
            if depth_cm < threshold_cm:
                current_alert = True
                cv2.putText(frame, "WARNING: Too Close!", (x, y - 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
        # Trigger an audible alert only when the warning condition is met
        if current_alert and not alert_triggered:
            try:
                import winsound
                winsound.Beep(1000, 500)  # Frequency: 1000 Hz, Duration: 500 ms (Windows only)
            except ImportError:
                # On non-Windows platforms, printing the bell character may work
                print('\a')
            alert_triggered = True
        elif not current_alert:
            alert_triggered = False  # Reset the flag if condition no longer exists

        cv2.imshow("Depth Estimation", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
