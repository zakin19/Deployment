'''
	Contoh Deloyment untuk Domain Data Science (DS)
	Orbit Future Academy - AI Mastery - KM Batch 3
	Tim Deployment
	2022
'''

# =[Modules dan Packages]========================

from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from joblib import load
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier

# =[Variabel Global]=============================

app   = Flask(__name__, static_url_path='/static')
model = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('index.html')

# [Routing untuk API]	
@app.route("/api/deteksi",methods=['POST'])
def apiDeteksi():
	# Nilai default untuk variabel input atau features (X) ke model
	input_gender = 0
	input_age = 0
	input_hypertension  = 0
	input_heart_disease = 0
	input_ever_married = 0
	input_avg_glucose_level = 0
	input_bmi = 0
	input_work_type = 0
	input_Residence_type = 0
	input_smoking_status = 0
	
	if request.method=='POST':
    
		# Set nilai untuk variabel input atau features (X) berdasarkan input dari pengguna
		input_gender = float(request.form['gender'])
		input_age = float(request.form['age'])
		input_hypertension  = float(request.form['hypertension'])
		input_heart_disease = float(request.form['heart_disease'])
		input_ever_married  = float(request.form['ever_married'])
		input_avg_glucose_level  = float(request.form['avg_glucose_level'])
		input_bmi  = float(request.form['bmi'])
		input_work_type  = float(request.form['work_type'])
		input_Residence_type  = float(request.form['Residence_type'])
		input_smoking_status  = float(request.form['smoking_status'])
		
		# Prediksi kelas atau spesies bunga iris berdasarkan data pengukuran yg diberikan pengguna
		df_test = pd.DataFrame(data={
			"gender" : [input_gender],
			"age" : [input_age],
			"hypertension"  : [input_hypertension],
			"heart_disease" : [input_heart_disease],
			"ever_married"  : [input_ever_married],
			"work_type"  : [input_work_type],
			"residence_type"  : [input_Residence_type],
			"avg_glucose_level" : [input_avg_glucose_level],
			"bmi" : [input_bmi],
			"smoking_status"  : [input_smoking_status],
		})
		
		hasil_prediksi = model.predict(df_test[0:1])[0]

		# Set Path untuk gambar hasil prediksi
		if hasil_prediksi == 0 :
			hasil_prediksi = "TIDAK TERINDIKASI STROKE"
			gambar_prediksi = '/static/images/happy.png'
		elif hasil_prediksi == 1 :
			hasil_prediksi = "TERINDIKASI STROKE"
			gambar_prediksi = '/static/images/sad.png'
		
		
		# Return hasil prediksi dengan format JSON
		return jsonify({
			"prediksi": hasil_prediksi,
			"gambar_prediksi" : gambar_prediksi
		})

# =[Main]========================================

if __name__ == '__main__':
	
	# Load model yang telah ditraining
	model = load('brain_stroke.model')

	# Run Flask di localhost 
	app.run(host="localhost", port=5000, debug=True)
	
	


