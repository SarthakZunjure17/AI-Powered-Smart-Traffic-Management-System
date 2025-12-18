import { useEffect, useState } from "react";

function TrafficLight({ color }) {
  return (
    <div className="traffic-light">
      <div className={`light red ${color === "RED" ? "on" : ""}`}></div>
      <div className={`light yellow ${color === "YELLOW" ? "on" : ""}`}></div>
      <div className={`light green ${color === "GREEN" ? "on" : ""}`}></div>
    </div>
  );
}

export default function Home() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  // ✅ DEFAULT SIGNAL STATE (NO EMPTY RENDER)
  const [signals, setSignals] = useState({
    LANE_1: "GREEN",
    LANE_2: "RED",
    LANE_3: "RED",
    LANE_4: "RED",
  });

  const [mode, setMode] = useState("NORMAL");

  // 🔁 Poll signal status (faster + smoother)
  useEffect(() => {
    const fetchSignals = () => {
      fetch("http://127.0.0.1:5000/signal-status")
        .then(res => res.json())
        .then(data => {
          setSignals(prev => ({ ...prev, ...data.signals }));
          setMode(data.mode);
        })
        .catch(() => {});
    };

    fetchSignals(); // 🔥 immediate first fetch
    const interval = setInterval(fetchSignals, 1500);

    return () => clearInterval(interval);
  }, []);

  const analyzeVideo = async () => {
    if (!file) {
      alert("Please select a video first");
      return;
    }

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("video", file);

    try {
      const res = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data);
    } catch {
      alert("Backend not reachable");
    }

    setLoading(false);
  };

  return (
    <>
      {/* UPLOAD CARD */}
      <div className="upload-card">
        <h2>Upload Traffic Video</h2>
        <p className="subtitle">MP4 / AVI (20–30 sec)</p>

        <input type="file" onChange={(e) => setFile(e.target.files[0])} />

        <button className="analyze-btn" onClick={analyzeVideo} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Video"}
        </button>
      </div>

      {/* 🚥 SIGNAL DASHBOARD */}
      <div className="signal-dashboard fade-in">
        <h2>🚦 Live Traffic Signals ({mode})</h2>

        <div className="signal-grid">
          {Object.entries(signals).map(([lane, color]) => (
            <div key={lane} className="lane-card">
              <h3>{lane}</h3>
              <TrafficLight color={color} />
            </div>
          ))}
        </div>
      </div>

      {/* RESULT */}
      {result && (
        <div className="result-card fade-in">
          <h2>Analysis Result</h2>
          <p><b>Emergency Detected:</b> {result.emergency ? "YES" : "NO"}</p>
          <p><b>Vehicle Type:</b> Emergency Vehicle</p>
          <p><b>Confidence:</b> {result.confidence}</p>

          <div className="signal">{result.signal}</div>

          {result.output_video && (
            <video
              src={`http://127.0.0.1:5000${result.output_video}`}
              controls
            />
          )}
        </div>
      )}
    </>
  );
}
