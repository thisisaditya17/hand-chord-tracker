# 🎵 Hand Chord Tracker

A real-time computer vision musical instrument that transforms hand gestures into musical chords. Built with MediaPipe hand tracking, OpenCV, and real-time audio synthesis for an intuitive gesture-controlled music experience.

## 📂 Demo Video
*Coming soon - Record your demo and add link here*

### Key Features

- **Real-time hand tracking** with 21-point finger detection
- **7 chord mappings** per scale (i, ii, iii, iv, v, vi, vii)
- **12 musical scales** with instant switching (C, C#, D, D#, E, F, F#, G, G#, A, A#, B)
- **Threaded audio processing** for smooth video performance
- **Visual feedback** with chord names and scale display
- **Harmonic synthesis** combining multiple sine waves for rich chord sounds

## 📦 Download Standalone Application

**No Python installation required!** Download the pre-built executable for your operating system:

### For Mac/Linux Users
- **[Download HandChordTracker](https://github.com/thisisaditya17/hand-chord-tracker/releases/latest/download/HandChordTracker)** 
- Make executable: `chmod +x HandChordTracker`
- Run: `./HandChordTracker`
- Or just open the executable in the terminal

## 🚀 Quick Start

### Option 1: Download Executable (Recommended)
1. Download the appropriate file for your OS from the links above
2. Grant camera permissions when prompted
3. Start playing immediately!

### Option 2: Run from Source

#### Prerequisites
- Python 3.12
- Webcam
- Audio output device (speakers/headphones)

#### Installation

1. **Clone the repository**
```bash
git clone https://github.com/thisisaditya17/hand-chord-tracker
cd hand-chord-tracker
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python chord_tracker.py
```

4. **Start playing!**
- Position your hand in front of the camera
- Raise different finger combinations to play chords
- Use keyboard shortcuts to change scales

## 🎹 Finger Mappings

| Gesture | Chord Type | Example (C Major Scale) |
|---------|------------|-------------------------|
| Index finger | i (Tonic) | C Major |
| Peace sign (Index + Middle) | ii (Supertonic) | D Minor |
| Three fingers (Index + Middle + Ring) | iii (Mediant) | E Minor |
| Four fingers (All except thumb) | iv (Subdominant) | F Major |
| All five fingers | v (Dominant) | G Major |
| Thumb + Index Finger | vi (Submediant) | A Minor |
| Index + Pinky Finger | vii (Leading tone) | B Diminished |

## ⌨️ Controls

**Scale Selection:**
- `1-9`, `0`, `-`, `=` - Direct scale selection
- `q` - Quit application

**Visual Indicators:**
- Current scale displayed on screen
- Active chord name when playing
- Real-time hand landmark visualization

## 🏗️ Architecture

```
├── chord_tracker.py        # Main application with MediaPipe integration
├── utils.py               # Audio synthesis and music theory functions
└── README.md
```

## 🛠️ Technologies Used

**Computer Vision**
- MediaPipe - Google's ML framework for hand tracking
- OpenCV - Image processing and camera interface
- NumPy - Efficient numerical computations

**Audio Processing**
- SoundDevice - Real-time audio I/O
- Threading - Asynchronous audio playback
- NumPy - Audio waveform generation

**Music Theory**
- Custom chord mapping system
- Circle of fifths implementation
- Diatonic harmony rules

## 🎵 Musical Theory Background

The system implements traditional Western diatonic harmony:
- **Major Scale Pattern**: W-W-H-W-W-W-H (whole/half steps)
- **Chord Qualities**: Major (I, IV, V), Minor (ii, iii, vi), Diminished (vii)
- **Voice Leading**: Smooth harmonic progressions between finger changes

## 👨‍💻 Author

**Aditya Joshi**
- GitHub: [@thisisaditya17](https://github.com/thisisaditya17)
- LinkedIn: [thisisaditya17](https://linkedin.com/in/thisisaditya17)

## 🙏 Acknowledgments

- Google MediaPipe team for robust hand tracking
- OpenCV community for computer vision tools
- Music theory inspired by traditional Western harmony
- SoundDevice developers for real-time audio capabilities
