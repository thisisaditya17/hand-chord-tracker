import numpy as np
import sounddevice as sd

def finger_up(hand_landmarks, hand):
    finger_tips_ids = [4, 8, 12, 16, 20]
    fingers = []

    if hand_landmarks.landmark[finger_tips_ids[0]].x < hand_landmarks.landmark[finger_tips_ids[0] - 1].x:
        fingers.append(1)  
    else:
        fingers.append(0)  


    for id in range(1, 5):
        if hand_landmarks.landmark[finger_tips_ids[id]].y < hand_landmarks.landmark[finger_tips_ids[id] - 2].y:
            fingers.append(1)  
        else:
            fingers.append(0) 

    return fingers


def scale_chords(scale):

    if scale == "C":
        chords_dict = {1: "C", 2: "Dm", 3: "Em", 4: "F", 5: "G", 6: "Am", 7: "Bdim"}
    elif scale == "C#":
        chords_dict = {1: "C#", 2: "D#m", 3: "Fm", 4: "F#", 5: "G#", 6: "A#m", 7: "Cdim"}
    elif scale == "D":
        chords_dict = {1: "D", 2: "Em", 3: "F#m", 4: "G", 5: "A", 6: "Bm", 7: "C#dim"}
    elif scale == "D#":
        chords_dict = {1: "D#", 2: "Fm", 3: "Gm", 4: "G#", 5: "A#", 6: "Cm", 7: "Ddim"}
    elif scale == "E":
        chords_dict = {1: "E", 2: "F#m", 3: "G#m", 4: "A", 5: "B", 6: "C#m", 7: "D#dim"}
    elif scale == "F":  
        chords_dict = {1: "F", 2: "Gm", 3: "Am", 4: "A#", 5: "C", 6: "Dm", 7: "Edim"}
    elif scale == "F#":
        chords_dict = {1: "F#", 2: "G#m", 3: "A#m", 4: "B", 5: "C#", 6: "D#m", 7: "Fdim"}
    elif scale == "G":
        chords_dict = {1: "G", 2: "Am", 3: "Bm", 4: "C", 5: "D", 6: "Em", 7: "F#dim"}
    elif scale == "G#":
        chords_dict = {1: "G#", 2: "A#m", 3: "Cm", 4: "C#", 5: "D#", 6: "Fm", 7: "Gdim"}
    elif scale == "A":  
        chords_dict = {1: "A", 2: "Bm", 3: "C#m", 4: "D", 5: "E", 6: "F#m", 7: "G#dim"}
    elif scale == "A#":  
        chords_dict = {1: "A#", 2: "Cm", 3: "Dm", 4: "D#", 5: "F", 6: "Gm", 7: "Adim"}
    elif scale == "B":  
        chords_dict = {1: "B", 2: "C#m", 3: "D#m", 4: "E", 5: "F#", 6: "G#m", 7: "A#dim"}
    else:
        return None
    return chords_dict

def which_chord(fingers):
    if fingers == [0, 1, 0, 0, 0]:
        return 1  
    elif fingers == [0, 1, 1, 0, 0]:
        return 2  
    elif fingers == [0, 1, 1, 1, 0]:
        return 3  
    elif fingers == [0, 1, 1, 1, 1]:
        return 4  
    elif fingers == [1, 1, 1, 1, 1]:
        return 5  
    elif fingers == [1, 1, 0, 0, 0]:
        return 6  
    elif fingers == [0, 1, 0, 0, 1]:
        return 7  
    else:
        return 0

def get_notes_for_chords(chord):
    chords_notes = {
        # Major chords
        "C": ["C", "E", "G"],
        "C#": ["C#", "F", "G#"],  
        "D": ["D", "F#", "A"],
        "D#": ["D#", "G", "A#"],   
        "E": ["E", "G#", "B"],
        "F": ["F", "A", "C"],
        "F#": ["F#", "A#", "C#"],
        "G": ["G", "B", "D"],
        "G#": ["G#", "C", "D#"],   
        "A": ["A", "C#", "E"],
        "A#": ["A#", "D", "F"],     
        "B": ["B", "D#", "F#"],

        # Minor chords
        "Cm": ["C", "D#", "G"],
        "C#m": ["C#", "E", "G#"],
        "Dm": ["D", "F", "A"],
        "D#m": ["D#", "F#", "A#"],
        "Em": ["E", "G", "B"],
        "Fm": ["F", "G#", "C"],
        "F#m": ["F#", "A", "C#"],
        "Gm": ["G", "A#", "D"],
        "G#m": ["G#", "B", "D#"],
        "Am": ["A", "C", "E"],
        "A#m": ["A#", "C#", "F"],
        "Bm": ["B", "D", "F#"],

        # Diminished chords
        "Bdim": ["B", "D", "F"],
        "Cdim": ["C", "D#", "F#"],
        "C#dim": ["C#", "E", "G"],
        "Ddim": ["D", "F", "G#"],
        "D#dim": ["D#", "F#", "A"],
        "Edim": ["E", "G", "A#"],
        "Fdim": ["F", "G#", "B"],
        "F#dim": ["F#", "A", "C"],
        "Gdim": ["G", "A#", "C#"],
        "G#dim": ["G#", "B", "D"],
        "Adim": ["A", "C", "D#"],
        "A#dim": ["A#", "C#", "E"]
    }
    return chords_notes.get(chord, [])


def get_frequency(note):
    note_frequencies = {
        "C": 261.63,
        "C#": 277.18,
        "D": 293.66,
        "D#": 311.13,
        "E": 329.63,
        "F": 349.23,
        "F#": 369.99,
        "G": 392.00,
        "G#": 415.30,
        "A": 440.00,
        "A#": 466.16,
        "B": 493.88
    }
    return note_frequencies.get(note, 440.00)  

def generate_chord_wave(notes, duration, sample_rate, fade_ms=5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    chord = np.zeros_like(t, dtype=np.float32)
    for note in notes:
        f = get_frequency(note)
        chord += 1 * np.sin(2 * np.pi * f * t).astype(np.float32)


    fade_samples = max(1, int(sample_rate * fade_ms / 1000.0))
    if fade_samples * 2 < chord.size:
   
        fade_in = np.linspace(0.0, 1.0, fade_samples, dtype=np.float32)
        fade_out = np.linspace(1.0, 0.0, fade_samples, dtype=np.float32)
        chord[:fade_samples] *= fade_in
        chord[-fade_samples:] *= fade_out

    peak = np.max(np.abs(chord)) + 1e-12
    if peak > 1.0:
        chord /= peak

    return chord

def play_chord_async(notes, duration):
    sr = 44100
    chord = generate_chord_wave(notes, duration=duration, sample_rate=sr, fade_ms=5)
    sd.play(chord, samplerate=sr, blocking=True)






        