import cv2
import numpy as np
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hand
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    # Read frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Get frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame using MediaPipe
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the tip of the index finger
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Convert landmark coordinates to screen coordinates
            x = int(index_finger_tip.x * frame_width)
            y = int(index_finger_tip.y * frame_height)

            # Map the coordinates to the screen size
            screen_x = np.interp(x, [0, frame_width], [0, screen_width])
            screen_y = np.interp(y, [0, frame_height], [0, screen_height])

            # Move the mouse
            pyautogui.moveTo(screen_x, screen_y)

            # Add a visual marker for the cursor
            cv2.circle(frame, (x, y), 10, (255, 0, 255), -1)

            # Detect gestures (example: thumb and index pinch for click)
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)

            # Calculate distance between thumb and index finger
            distance = np.hypot(thumb_x - x, thumb_y - y)
            if distance < 30:
                pyautogui.click()

    # Display the frame
    cv2.imshow("Virtual Mouse", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# import cv2
# import htmodule as htm
# import mediapipe as mp
# import pyautogui as pag
# cap = cv2.VideoCapture(0)
# det = htm.Handdetection(max_hands=1)
# s_w,s_h = pag.size()
# while True:
#     success, img = cap.read()
#     h, w, c = img.shape
#     img = det.findhands(img)
#     lmlist = det.handpos(img,draw = False)
#
#     if len(lmlist) != 0:
#         x1, y1 = lmlist[8][1:]
#
#         cv2.circle(img, (x1, y1), 15, (0, 0, 0), 3)
#         i_x = s_w/w*x1
#         i_y = s_h/h*y1
#         if abs(i_y-s_h/h*lmlist[12][2]) < 60:
#             pag.moveTo((i_x, i_y))
#         if abs((s_h / h * lmlist[12][2]) - (s_h/h*lmlist[11][2]))< 30:
#             print("click")
#             pag.click()
#             pag.sleep(1)
#
#     cv2.imshow('Image', img)
#     cv2.waitKey(1)
