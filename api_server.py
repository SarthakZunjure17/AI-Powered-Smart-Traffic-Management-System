from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from emergency_core import analyze_video
from signal_controller import controller

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------- VIDEO ANALYSIS ----------------

@app.route("/analyze", methods=["POST"])
def analyze():
    if "video" not in request.files:
        return jsonify({"error": "No video uploaded"}), 400

    video = request.files["video"]
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    result = analyze_video(video_path)

    # 🚨 THIS WAS MISSING
    if result["emergency"]:
        controller.trigger_emergency("LANE_1")

    return jsonify(result)


@app.route("/output/<filename>")
def get_output_video(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


# ---------------- SIGNAL API ----------------

@app.route("/signal-status", methods=["GET"])
def signal_status():
    return jsonify(controller.get_status())


# ---------------- ADMIN API ----------------

@app.route("/admin/force-emergency", methods=["POST"])
def force_emergency():
    data = request.json
    lane = data.get("lane", "LANE_1")
    controller.trigger_emergency(lane)
    return jsonify({"status": "EMERGENCY ACTIVATED", "lane": lane})


@app.route("/admin/reset", methods=["POST"])
def reset_signal():
    controller.reset()
    return jsonify({"status": "RESET TO NORMAL"})


@app.route("/admin/set-duration", methods=["POST"])
def set_duration():
    data = request.json
    seconds = int(data.get("seconds", 15))
    controller.set_duration(seconds)
    return jsonify({"priority_duration": seconds})


@app.route("/admin/toggle-priority", methods=["POST"])
def toggle_priority():
    data = request.json
    enabled = bool(data.get("enabled", True))
    controller.toggle_priority(enabled)
    return jsonify({"priority_enabled": enabled})


if __name__ == "__main__":
    app.run(debug=True)
