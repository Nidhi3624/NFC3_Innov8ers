from django.shortcuts import render,redirect
import joblib
import os
import numpy as np
import pandas as pd
from .utils import get_nutrient_message
from django.conf import settings
from django.templatetags.static import static
import csv
import cohere
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import torch
from .model_util import ModelHandler
from django.http import HttpResponse


model_path = os.path.join(os.path.dirname(__file__), 'model', 'CropPrediction.pkl')
model = joblib.load(model_path)

model_handler = ModelHandler()

threshold_data = os.path.join(os.path.dirname(__file__),'media/datasets','fertilizer.csv')
data1 = pd.read_csv(threshold_data)


# Create your views here.
def HomePage(request):
    return render(request,"index.html")

def predict(request):
    
    if request.method == 'POST':
        # Get data from the form submission
        data = request.POST
        # Extract the features from the form
        nitrogen = float(data['nitrogen'])        # N
        phosphorus = float(data['phosphorus'])    # P
        potassium = float(data['potassium'])      # K
        temperature = float(data['temperature'])  # Temperature
        humidity = float(data['humidity'])        # Humidity
        ph = float(data['ph'])                    # pH
        rainfall = float(data['rainfall'])        # Rainfall

        # Prepare the features in the correct shape for the model
        features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
        message=[]
        # Make the prediction
        prediction = model.predict(features)
        crop = prediction[0]
        # print(data1.columns.tolist())
        row = data1[data1['Crop']==crop]
        print(row)
        if not row.empty:
            # Convert the row to a dictionary
            row_dict = row.iloc[0].to_dict()
            # Extract relevant thresholds
            thresholds = {
                'N': row_dict.get('N', 0),
                'P': row_dict.get('P', 0),
                'K': row_dict.get('K', 0),
                
            }
        else:
            thresholds = {}
        
        # print()
        # print(thresholds)
        message = get_nutrient_message(nitrogen,phosphorus,potassium,thresholds)
        # Render the prediction result in the template
        if isinstance(message, list):
            message = "\n".join(message)
        
        message_html = message.replace('\n', '<br>')
        # print(message)
        context = {'prediction': prediction[0],'message':message_html}
        # print(context)

        return render(request, 'prediction_result.html', context)

    # Render the input form
    return render(request, 'predict_form.html')


COHERE_API_KEY = "ckc6CNJ37YTHNoSxvkc2invpu10MDhtQqChAraz6"

client = cohere.Client(api_key=COHERE_API_KEY)

def generate_api_response(query):
    print("query")
    try:
        response = client.generate(
            prompt=query,
            max_tokens=500,
            temperature=0.5
        )
        api_response = ''.join(generation.text for generation in response.generations)
        print(api_response)
        return api_response
    except Exception as e:
        return f"Error: {str(e)}"
    

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message')
        print(user_input)
        api_response = generate_api_response(user_input)
        return JsonResponse({'response': api_response})
    return JsonResponse({'error': 'Invalid request method'}, status=400)




def disease_prediction(request):
    title = 'Harvestify - Disease Detection'
    
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return redirect(request.path)
        file = request.FILES.get('file')
        if not file:
            return render(request, 'disease.html', {'title': title})
        try:
            img = file.read()
            prediction = model_handler.predict_image(img)
            return render(request, 'disease_result.html', {'prediction': prediction, 'title': title})
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

    return render(request, 'disease.html', {'title': title})