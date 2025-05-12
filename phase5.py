from flask import Flask, render_template, request, redirect, url for
from wrkzeug.utils import secure_filename
import os
from predict import process_image, predict_degradation
from semsors.sensor_simulator import get_sensor_data
app - Flask(_nane_)
app.comfig["UPLOAD_FOLDER"] = 'static/uploads'
@app.route("/", methods-["GET', 'POST"])
def dashboard():
damge_result, forecast - None, None
sensor_data - get_semsor_data()
if request.method == "POST':
file - request.files['file']
if file:
filename = secure_filename(file.filename)
path = os.path.join(app.config["UPLO/D_FOLDER'], filemame)
file.save(path)
danage_result - process_Inage(path)
forecast = predict_degradation(sensor_data["strain'])
return render_template("dashboard.html", damage-damage_result, forecast-forecast, sensor-sensor_data)

if_name_ == "_main_":
app.run(debug-True)

import random
rom datetime import datetime
def process_image(img_path):
damage_types = ['Crack', "Rust', 'Spalling']
severity = random, choice(['Low', 'Moderate', "High'])
return {'type': random.choice(damage_types),'severity': severity,'time': datetime.now().strftime('%Y-Xm-%d XH:XM:XS")

def predict_degradation(sensor_value):
future_risk - sensor_value * random.uniform(1.1, 1.3)
return round(future_risk, 2)
<IDOCTYPE html>
<html>
<head>

<title>IBM-AI-EBPL Dashboard</title>
</head>
<body:
ch2>Upload Image for Damage Detection</h2>
<form method="post" enctype="multipart/form-data">
<input type-"file" name="file" required>

<button type="submit">Analyze</button>

</form>
(% if damage %}
<h3>Detection Result :< /h3>

<p><strong>Type :< /strong> ({ damage.type }}</p>
<p><strong>Severity :< /strong> ({ damage.severity }}</p>
<p><strong>Time :< /strong> ({ damage.time }}</p>
(% endif %)

(% if forecast %)

<h3>Predicted Degradation Risk :< /h3>
<p>{{ forecast }}</p>
(% endif %)

ch3>Sensor Data: </h3>
<ul>

<li>Strain: {{ sensor.strain }}</li>
<li>Vibration: {( sensor.vibration }]</li>
<li>Temperature: {{ sensor.temperature }}</1i>

</body>
</html>
import random
def
get_sensor_data():
return {
strain': round(random.uniform(0.3, 0.8), 2)
'vibration': round(random.uniform(0.1, 0.5), 2)
temperature': round(random.uniform(20, 45), 1)