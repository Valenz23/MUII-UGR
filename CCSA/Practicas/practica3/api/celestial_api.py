from flask import Flask, request, jsonify
from pyspark.ml import PipelineModel
from pyspark.ml.classification import DecisionTreeClassificationModel, RandomForestClassificationModel, GBTClassificationModel  
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, FloatType
import os
import time

# Crear una sesión de Spark
spark = SparkSession.builder.appName('MLModelPrediction').getOrCreate()

# Ruta al modelo MLlib
MODEL_DT_PATH = "/opt/spark-output/celestial/dt"
MODEL_RF_PATH = "/opt/spark-output/celestial/rf"
MODEL_GB_PATH = "/opt/spark-output/celestial/gb"
PIPELINE_PATH = "/opt/spark-output/celestial/pipeline"

# Crear la aplicación Flask
app = Flask(__name__)

# Función para cargar los modelos y el pipeline
def load_models_and_pipeline():
    global pre_pipeline, model_dt, model_rf, model_gb
    while True:
        if os.path.exists(MODEL_DT_PATH) and os.path.exists(MODEL_RF_PATH) and os.path.exists(MODEL_GB_PATH) and os.path.exists(PIPELINE_PATH):
            pre_pipeline = PipelineModel.load(PIPELINE_PATH)
            model_dt = DecisionTreeClassificationModel.load(MODEL_DT_PATH)
            model_rf = RandomForestClassificationModel.load(MODEL_RF_PATH)
            model_gb = GBTClassificationModel.load(MODEL_GB_PATH)
            break
        else:
            print("Models or pipeline not found. Waiting for them to become available...")
            time.sleep(30)  # Espera 30 segundos antes de volver a verificar

# Cargar los modelos y el pipeline al iniciar la aplicación
load_models_and_pipeline()

@app.route('/')
def home():
    spark = SparkSession.builder.appName("example").getOrCreate()
    return "Spark session created successfully!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos del request
        data = request.get_json()
        
        # Definir el esquema de los datos esperados
        schema = StructType([
            StructField("expAB_z", FloatType(), True),
            StructField("i", FloatType(), True),
            StructField("q_r", FloatType(), True),
            StructField("modelFlux_r", FloatType(), True),
            StructField("expAB_i", FloatType(), True),
            StructField("expRad_u", FloatType(), True),
            StructField("q_g", FloatType(), True),
            StructField("psfMag_z", FloatType(), True),
            StructField("dec", FloatType(), True),
            StructField("psfMag_r", FloatType(), True)
        ])
        
        # Crear un DataFrame de Spark con los datos recibidos
        input_data = spark.createDataFrame([data], schema)
        
        prep_data = pre_pipeline.transform(input_data)

        # Hacer la predicción
        predictions_dt = model_dt.transform(prep_data)
        predictions_rf = model_rf.transform(prep_data)
        predictions_gb = model_gb.transform(prep_data)
        
        # Seleccionar las columnas de predicción y probabilidad para cada modelo
        prediction_dt = predictions_dt.select("prediction").collect()[0][0]
        probabilities_dt = predictions_dt.select("probability").collect()[0][0]
        
        prediction_rf = predictions_rf.select("prediction").collect()[0][0]
        probabilities_rf = predictions_rf.select("probability").collect()[0][0]
        
        prediction_gb = predictions_gb.select("prediction").collect()[0][0]
        probabilities_gb = predictions_gb.select("probability").collect()[0][0]
        
        # Devolver los resultados como JSON
        result_dt = {'model': 'Decision Tree', 'prediction': 'Es una galaxia' if prediction_dt == 0 else 'Es una estrella', 'probability': round(probabilities_dt[0] * 100, 2)}
        result_rf = {'model': 'Random Forest', 'prediction': 'Es una galaxia' if prediction_rf == 0 else 'Es una estrella', 'probability': round(probabilities_rf[0] * 100, 2)}
        result_gb = {'model': 'Gradient Boosting', 'prediction': 'Es una galaxia' if prediction_gb == 0 else 'Es una estrella', 'probability': round(probabilities_gb[0] * 100, 2)}
        
        return jsonify({'results': [result_dt, result_rf, result_gb]})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)