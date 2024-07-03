import cv2
import datetime
import numpy as np
def record():
    cap = cv2.VideoCapture(0)

    if (cap.isOpened() == False):
        print("Camera is unable to open.")


    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))



    video_cod = cv2.VideoWriter_fourcc(*'XVID')
    video_output= cv2.VideoWriter('saved recording.avi',
                      video_cod,
                      10,
                      (frame_width,frame_height))

    while(True):
        ret, frame = cap.read()

        if ret == True:
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            datet = str(datetime.datetime.now())
            
            frame = cv2.putText(frame, datet, (10, 100), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
    
    
            video_output.write(frame)

      
            cv2.imshow('frame',frame)

    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

  
        else:
            break  


    cap.release()
    video_output.release()
    cv2.destroyAllWindows() 

    print("The video was successfully saved")





