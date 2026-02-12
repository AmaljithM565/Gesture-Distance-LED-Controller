# Gesture-Distance-LED-Controller
Control 4 LEDs on an ESP32 using real-time thumb–index distance detection via Python, OpenCV, and MediaPipe.


# ESP32 Gesture Distance LED Controller

This project demonstrates a real-time hand gesture control system using an ESP32 and computer vision.

A Python script (OpenCV + MediaPipe) detects the distance between the thumb tip and index finger tip using a laptop webcam. Based on this distance, a level value (0–4) is sent to the ESP32 over Serial communication.

The ESP32 then turns ON a corresponding number of LEDs, creating a gesture-controlled LED bar indicator.

## Features

- Thumb–index proximity detection using MediaPipe Hands
- Distance mapped to LED levels (0–4)
- Real-time Serial communication with ESP32
- LEDs remain ON until the gesture level changes
- Simple and expandable for more outputs or devices

## Hardware Required

- ESP32 DevKit V1
- 4 LEDs
- 4 × 220Ω resistors
- Breadboard + jumper wires
- Laptop/PC webcam

## Software Used

- PlatformIO (VS Code)
- Python 3
- OpenCV
- MediaPipe
- PySerial

## How It Works

- Fingers touching → All LEDs OFF  
- Fingers slightly apart → 1 LED ON  
- Increasing distance → More LEDs ON  
- Maximum distance → All 4 LEDs ON  

## Applications

- Gesture-based smart lighting control
- Touchless human-computer interaction
- IoT + Computer Vision projects
