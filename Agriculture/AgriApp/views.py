from django.shortcuts import render,redirect
import joblib
import os
import numpy as np
import pandas as pd
from .utils import get_nutrient_message,getdata
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
import requests
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


model_path = os.path.join(os.path.dirname(__file__), 'model', 'CropPrediction.pkl')
model = joblib.load(model_path)

model_handler = ModelHandler()

threshold_data = os.path.join(os.path.dirname(__file__),'media/datasets','fertilizer.csv')
data1 = pd.read_csv(threshold_data)


# Create your views here.
def HomePage(request):
    return render(request,"index.html")

# crop prediction
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

# chatbot
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



# Image processing work
def disease_prediction(request):
    title = 'Detecting Disease'
    
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return redirect(request.path)
        file = request.FILES.get('file')
        if not file:
            return render(request, 'disease.html', {'title': title})
        try:
            img = file.read()
            prediction = model_handler.predict_image(img)
            message = getdata(prediction)
            if isinstance(message, list):
                message = "\n".join(message)
        
            message_html = message.replace('\n', '<br>')
            return render(request, 'disease_result.html', {'prediction': prediction, 'title': title, 'message':message_html})
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

    return render(request, 'disease.html', {'title': title})

# weather forecast
def weather_fetch(city_name):
    """
    Fetch and return agriculture-relevant weather data of a city.
    """
    api_key = "244fe839ef361642af1d35a0f5dc8042"  # Replace this with your valid API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if "main" in x:
        weather_data = {}

        # Temperature in Celsius
        weather_data["temperature"] = round((x["main"]["temp"] - 273.15), 2)
        
        # Humidity percentage
        weather_data["humidity"] = x["main"]["humidity"]
        
        # Weather description
        weather_data["description"] = x["weather"][0]["description"]
        
        # Wind speed in meters/second
        weather_data["wind_speed"] = x["wind"]["speed"]
        
        # Wind direction in degrees
        weather_data["wind_direction"] = x["wind"]["deg"]
        
        # Atmospheric pressure in hPa
        weather_data["pressure"] = x["main"]["pressure"]
        
        # Cloudiness percentage
        weather_data["cloudiness"] = x["clouds"]["all"]

        return weather_data
    else:
        return None

def weather_dashboard(request):
    city_name = "Mumbai"  # You can dynamically set this or get it from request parameters
    weather = weather_fetch(city_name)
    if weather:
        return render(request, 'weather/dashboard.html', {'weather': weather})
    else:
        return HttpResponse("Could not retrieve weather data.")
    


 # fertilizer
def predict12(request):
    
    if request.method == 'POST':
        # Get data from the form submission
        data = request.POST
        fruit = str(data['fruit'])
        # Extract the features from the form
        nitrogen = float(data['nitrogen'])        # N
        phosphorus = float(data['phosphorus'])    # P
        potassium = float(data['potassium'])      # K
       # Rainfall

        # Prepare the features in the correct shape for the model
        features = np.array([[fruit,nitrogen, phosphorus, potassium]])
        print(features)
        message=[]
        # Make the prediction
        
        # print(data1.columns.tolist())
        row = data1[data1['Crop']==fruit]
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
        context = {'message':message_html}
        # print(context)

        return render(request, 'fertilizer_result.html', context)

    # Render the input form
    return render(request, 'fertilizer.html')


# chatbot
def chat12(request):
    return render(request,'index2.html')


# signup
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Additional user profile creation could happen here
            # For example, saving phone, address, etc., to a custom user profile model

            # Automatically log the user in after signup
            login(request, user)
            return redirect('dash1')  # Redirect to a home page or another page
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            print("successfull")
            return redirect('dash1')  # Replace 'home' with your desired redirect page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


# main dashboard
@login_required
def dashboard1(request):
    return render(request,'dashboard_main.html')