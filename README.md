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

The **AI-Powered Smart Traffic Management System** is an **academic simulation project** that demonstrates how **computer vision and intelligent control logic** can improve traffic flow at road intersections — especially during **emergency situations**.

The system uses **YOLOv8 object detection** to identify emergency vehicles such as **ambulances, police vehicles, and fire brigades** from traffic videos.  
Once an emergency vehicle is detected, the system dynamically **prioritizes the corresponding traffic lane** while maintaining **safe signal transitions** using a **YELLOW buffer phase**.

This project focuses on:
- Practical traffic logic
- Safety-aware signal transitions
- Clear and explainable system behavior  
making it suitable for **final-year project evaluation and live demonstrations**.

---

## 🎯 Key Objectives

- Detect emergency vehicles using AI-based object detection  
- Dynamically prioritize traffic signals for emergency lanes  
- Ensure **safe GREEN → YELLOW → RED transitions**  
- Provide a **web-based dashboard** for monitoring and control  
- Simulate **admin override functionality** for traffic authorities  

---

## ✨ Features

### 🚨 Emergency Vehicle Detection
- YOLOv8-based detection of:
  - Ambulance
  - Police vehicles
  - Fire brigade
- Confidence-based filtering
- Bounding boxes drawn on output video

### 🚦 Intelligent Traffic Signal Control
- **Normal mode**
  - GREEN (10s) → YELLOW (5s) → next lane
- **Emergency mode**
  - Current lane switches to **YELLOW (buffer time)**
  - Emergency lane turns **GREEN**
  - After priority duration, system safely returns to normal mode

### 🖥️ Web Dashboard (React + Flask)
- Upload traffic videos for analysis
- View processed output video
- Live traffic signal status visualization
- Emergency detection status display
- Simple and clean UI for demonstration

### 🔐 Admin Control Panel
- Force emergency on a selected lane
- Reset traffic signals to normal mode
- Configure emergency priority duration
- **Simulation only** (no real traffic hardware involved)

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
- YOLOv8 object detection
- Custom emergency vehicle dataset

---

## 📁 Project Structure

AI-Powered Smart Traffic Management System/
│
├── api_server.py # Flask backend API
├── emergency_core.py # YOLO-based video processing
├── signal_controller.py # Traffic signal logic
├── requirements.txt # Python dependencies
│
├── frontend/
│ └── traffic-management/ # React frontend
│ └── src/
│ ├── pages/ # Home, Admin, About, Login
│ ├── components/ # Navbar, ProtectedRoute
│ ├── App.jsx
│ └── main.jsx
│
├── project/
│ └── datasets/
│ └── emergency_vehicles # Training dataset
│
├── uploads/ # Uploaded input videos (git ignored)
├── output/ # Processed output videos (git ignored)


---

## 🚀 How to Run the Project

### 1️⃣ Backend Setup
```bash
pip install -r requirements.txt
python api_server.py

Backend runs at:

http://127.0.0.1:5000

2️⃣ Frontend Setup
cd frontend/traffic-management
npm install
npm run dev


Frontend runs at:

http://localhost:5173

🧪 System Flow (Demo)

User opens the web application

Login page appears (admin authentication)

User uploads a traffic video

AI processes video frame-by-frame

Emergency vehicle is detected (if present)

Traffic signals change dynamically:

Yellow buffer → Emergency green → Normal cycle

Admin panel allows manual override for demonstration

🔐 Authentication Flow

Login page appears on first load

Valid credentials enable access to:

Home

Admin

About pages

Protected routes implemented using React Router

Authentication state stored using localStorage

Demo Credentials

Username: admin
Password: admin123

🎓 Academic Notes

This is a simulation-based academic project

No real traffic lights or CCTV systems are controlled

Designed for:

Final-year project evaluation

AI & Computer Vision demonstrations

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