import { useState } from "react";
import "./Admin.css";

function Admin() {
  const [lane, setLane] = useState("LANE_1");
  const [duration, setDuration] = useState(15);
  const [message, setMessage] = useState("");

  const activateEmergency = async () => {
    await fetch("http://127.0.0.1:5000/admin/force-emergency", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ lane })
    });

    setMessage(`🚨 Emergency activated on ${lane}`);
  };

  const updateDuration = async () => {
    await fetch("http://127.0.0.1:5000/admin/set-duration", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ seconds: duration })
    });

    setMessage(`⏱ Priority duration updated to ${duration} seconds`);
  };

  const resetSignals = async () => {
    await fetch("http://127.0.0.1:5000/admin/reset", {
      method: "POST"
    });

    setMessage("✅ Signals reset to normal operation");
  };

  return (
    <div className="admin-page">
      <h1 className="admin-title"> Admin Control Panel</h1>

      {/* STATUS MESSAGE */}
      {message && <div className="admin-status">{message}</div>}

      <div className="admin-grid">
        <div className="admin-card">
          <h3>Force Emergency Lane</h3>

          <select value={lane} onChange={(e) => setLane(e.target.value)}>
            <option>LANE_1</option>
            <option>LANE_2</option>
            <option>LANE_3</option>
            <option>LANE_4</option>
          </select>

          <button className="primary-btn" onClick={activateEmergency}>
            Activate Emergency
          </button>
        </div>

        <div className="admin-card">
          <h3>Priority Duration (seconds)</h3>

          <input
            type="number"
            value={duration}
            onChange={(e) => setDuration(e.target.value)}
          />

          <button className="primary-btn" onClick={updateDuration}>
            Update Duration
          </button>
        </div>

        <div className="admin-card">
          <h3>System Controls</h3>

          <button className="danger-btn" onClick={resetSignals}>
            Reset Signals
          </button>
        </div>
      </div>
    </div>
  );
}

export default Admin;
