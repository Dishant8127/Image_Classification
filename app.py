import os

from flask import Flask, render_template, request, send_from_directory

from predict import predict

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")

def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])

def upload():

    file = request.files["image"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    label, confidence = predict(filepath)

    confidence = round(confidence * 100,2)

    return render_template(
        "index.html",
        image=file.filename,
        prediction=label,
        confidence=confidence
    )

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":

    app.run(debug=True)