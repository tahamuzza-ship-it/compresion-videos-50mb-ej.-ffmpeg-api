import os
from flask import Flask, request, send_file
import subprocess
import uuid

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return {"status": "ok"}, 200

@app.route("/convert", methods=["POST"])
def convert():
    if "file" not in request.files:
        return {"error": "No file provided"}, 400

    input_file = request.files["file"]
    uid = str(uuid.uuid4())

    input_path = f"/tmp/{uid}_input.mp4"
    output_path = f"/tmp/{uid}_output.mp4"

    input_file.save(input_path)

    if not os.path.exists(input_path):
        return {"error": "Input file not saved"}, 500

    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-vf", "scale=1280:-2",
        "-r", "30",
        "-c:v", "libx264",
        "-b:v", "2500k",
        "-maxrate", "2500k",
        "-bufsize", "5000k",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        "-f", "mp4",
        output_path
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        return {"error": "ffmpeg_failed", "details": result.stderr}, 500

    return send_file(output_path, mimetype="video/mp4", as_attachment=True)
