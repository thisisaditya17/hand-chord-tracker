import cv2 as cv
import mediapipe as mp
import utils as ut
import sounddevice as sd
import threading

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
cap = cv.VideoCapture(1, cv.CAP_AVFOUNDATION)
audio_thread = None


if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

current_scale_index = 0
available_scales = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
selected_scale = available_scales[current_scale_index]

scale_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
scale_key_map = dict(zip(scale_keys, available_scales))

speed = 0.5
print("Press '[' to decrease speed by 0.1 seconds")
print("Press ']' to increase speed by 0.1 seconds")


print("Controls:")
for key, scale in scale_key_map.items():
    print(f"Press '{key}' for {scale} major scale")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    cv.putText(frame, f'Scale: {selected_scale} Major', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            hand = handedness.classification[0].label
            fingers = ut.finger_up(hand_landmarks, hand)
            chord = ut.which_chord(fingers)
            last_chord = 0
            if chord != 0 and chord != last_chord:
                last_chord = chord
                chords_dict = ut.scale_chords(selected_scale)
                chord_name = chords_dict[chord]
                cv.putText(frame, f'Chord: {chord_name}', (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                if audio_thread is None or not audio_thread.is_alive():
                    notes = ut.get_notes_for_chords(chord_name)
                    audio_thread = threading.Thread(target=ut.play_chord_async, args=(notes, speed))
                    audio_thread.start()
            elif chord == 0:
                last_chord = 0

    cv.imshow("Camera Feed", frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord(']'):
        speed += 0.1
        print(f"Speed increased to {speed:.1f} seconds")
    elif key == ord('['):
        speed = max(0.1, speed - 0.1)
        print(f"Speed decreased to {speed:.1f} seconds")
    else:
        key_char = chr(key) if key < 128 else None
        if key_char in scale_key_map:
            selected_scale = scale_key_map[key_char]
            current_scale_index = available_scales.index(selected_scale)
            print(f"Switched to {selected_scale} major scale")
    

cap.release()
cv.destroyAllWindows()
