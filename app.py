from flask import Flask, request, send_file
import subprocess
import os
import uuid

app = Flask(__name__)

@app.route("/convert", methods=["POST"])
def convert():
    if "file" not in request.files:
        return {"error": "No file provided"}, 400

    input_file = request.files["file"]
    uid = str(uuid.uuid4())

    input_path = f"/tmp/{uid}_input.mp4"
    output_path = f"/tmp/{uid}_output.mp4"

    input_file.save(input_path)

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
        output_path
    ]

    subprocess.run(cmd, check=True)

    return send_file(
        output_path,
        mimetype="video/mp4",
        as_attachment=True,
        download_name="compressed.mp4"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
