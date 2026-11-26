"""Supreme Omni Engine web entry point.

The repository is an application foundation, not a completed AI engine.
"""
import os
from flask import Flask, jsonify

app = Flask(__name__)


def engine_status():
    return {
        "service": "Supreme Omni Engine",
        "status": "operational",
        "stage": "foundation",
        "engine_implemented": False,
        "integrations": {"gemini_api_configured": bool(os.getenv("GEMINI_API_KEY"))},
        "message": "Web foundation is running. Core AI orchestration is not yet implemented; no model execution is claimed.",
    }


@app.get("/")
def home():
    return ("<!doctype html><html lang='en'><meta charset='utf-8'>"
            "<meta name='viewport' content='width=device-width,initial-scale=1'>"
            "<title>Supreme Omni Engine</title>"
            "<style>body{font:16px system-ui;margin:3rem auto;max-width:760px;padding:0 1rem;background:#f6f8fb;color:#182230}main{background:white;padding:2rem;border-radius:16px}.muted{color:#526173}</style>"
            "<main><h1>Supreme Omni Engine</h1><p><strong>Service status: Operational</strong></p>"
            "<p>Current stage: Foundation</p><p class='muted'>The web service and health endpoints are active. AI orchestration is not yet implemented.</p>"
            "<p>Machine-readable status: /api/status</p><p>Health check: /healthz</p></main></html>")


@app.get("/healthz")
def healthz():
    return jsonify({"status": "healthy"}), 200


@app.get("/api/status")
def api_status():
    return jsonify(engine_status()), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
