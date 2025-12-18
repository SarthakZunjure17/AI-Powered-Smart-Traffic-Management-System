# 🚦 AI-Powered Smart Traffic Management System

<div align="center">

![AI Traffic](https://img.shields.io/badge/AI-Traffic%20Management-00ff99?style=for-the-badge)
![Computer Vision](https://img.shields.io/badge/Computer-Vision-blue?style=for-the-badge)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-red?style=for-the-badge)
![Flask](https://img.shields.io/badge/Backend-Flask-black?style=for-the-badge)
![React](https://img.shields.io/badge/Frontend-React-61dafb?style=for-the-badge)

**An AI-based system for emergency vehicle detection and intelligent traffic signal prioritization**

</div>

---

## 📌 Project Overview

The **AI-Powered Smart Traffic Management System** is an academic project designed to simulate how **computer vision and intelligent control logic** can be used to improve urban traffic flow — especially during **emergency situations**.

The system detects **emergency vehicles (ambulance, police, fire brigade)** from traffic videos using **YOLOv8**, and dynamically modifies traffic signals to give **priority clearance** to the emergency lane while ensuring safe transitions using **yellow signals**.

This project focuses on **real-world practicality**, **safety**, and **clear system behavior**, making it ideal for academic evaluation and demonstrations.

---

## 🎯 Key Objectives

- Detect emergency vehicles using AI-based object detection  
- Prioritize traffic signals dynamically for emergency lanes  
- Ensure **safe signal transitions** using GREEN → YELLOW → RED logic  
- Provide a **web-based dashboard** for visualization and control  
- Simulate **admin override** functionality for traffic authorities  

---

## ✨ Features

### 🚨 Emergency Vehicle Detection
- YOLOv8-based detection of:
  - Ambulance
  - Police vehicles
  - Fire brigade
- Confidence-based detection filtering
- Visual bounding boxes on output video

### 🚦 Intelligent Traffic Signal Control
- Normal traffic cycle:
  - GREEN (10s) → YELLOW (5s) → next lane
- Emergency handling:
  - Current lane switches to **YELLOW (buffer time)**
  - Emergency lane turns **GREEN**
  - After priority duration, system safely returns to normal mode

### 🖥️ Web Dashboard (React + Flask)
- Upload traffic videos for analysis
- View processed output video
- Live traffic signal status visualization
- Emergency status display
- Admin panel for manual signal override

### 🔐 Admin Control Panel
- Force emergency on a selected lane
- Reset signals to normal mode
- Configure emergency priority duration
- Simulation-only (no real traffic hardware)

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask (REST API)
- OpenCV
- Ultralytics YOLOv8

### Frontend
- React (Vite)
- HTML / CSS
- Fetch API

### AI / Computer Vision
- YOLOv8 (object detection)
- Custom trained emergency vehicle dataset

---

## 📁 Project Structure

AI-Powered Smart Traffic Management System/
│
├── api_server.py # Flask backend API
├── emergency_core.py # YOLO-based video processing
├── signal_controller.py # Traffic signal logic (NORMAL + EMERGENCY)
├── requirements.txt # Python dependencies
│
├── frontend/
│ ├── traffic-management/ # React frontend
│ │ ├── src/
│ │ │ ├── pages/ # Home, Admin, About
│ │ │ ├── components/ # Navbar, UI components
│ │ │ ├── App.jsx
│ │ │ └── main.jsx
│
├── project/
│ └── datasets/
│ └── emergency_vehicles/ # Training dataset
│
├── uploads/ # Uploaded input videos (ignored in git)
├── output/ # Processed output videos (ignored in git)


---

## 🚀 How to Run the Project

### 1️⃣ Backend Setup
```bash
pip install -r requirements.txt
python api_server.py

Backend runs on:

http://127.0.0.1:5000

2️⃣ Frontend Setup
cd frontend/traffic-management
npm install
npm run dev


Frontend runs on:

http://localhost:5173

🧪 How It Works (Demo Flow)

Upload a traffic video via web UI

AI detects emergency vehicles frame-by-frame

Output video is generated with detection overlays

Traffic signals change dynamically:

Yellow buffer → Emergency green → Resume normal cycle

Admin panel allows manual overrides for demonstration

🎓 Academic Notes

This is a simulation-based academic project

No real traffic hardware is controlled

Designed for:

Final year project evaluation

AI + CV demonstrations

Smart city concept explanation

🔮 Future Enhancements

Integration with real CCTV feeds

Hardware-based traffic light control

Pedestrian detection

Cloud-based analytics

Smart city IoT integration

📜 License

This project is licensed under the MIT License.

<div align="center">
⭐ If you find this project useful, consider starring the repository ⭐

AI for Safer Roads • Smart Emergency Response • Academic Simulation

</div> ```