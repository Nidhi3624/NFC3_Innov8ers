import torch
from .models import ResNet9
import os
from django.conf import settings
from torchvision import transforms
from PIL import Image
import io


class ModelHandler:
    def __init__(self):
        # Construct the path dynamically
        model_path = os.path.join(settings.BASE_DIR, 'AgriApp', 'model', 'plant_disease_model.pth')
        self.model = ResNet9(in_channels=3, num_diseases=len(disease_classes))  # Adjust as needed
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu'), weights_only=True))
        self.model.eval()


    def predict_image(self, img):
        """
        Transforms image to tensor and predicts disease label.
        :params img: Image bytes.
        :return: prediction (string)
        """
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.ToTensor(),
        ])
        image = Image.open(io.BytesIO(img)).convert('RGB')
        img_t = transform(image)
        img_u = torch.unsqueeze(img_t, 0)

        with torch.no_grad():
            yb = self.model(img_u)
        
        _, preds = torch.max(yb, dim=1)
        prediction = disease_classes[preds[0].item()]
        return prediction
    
disease_classes = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 
                   'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
                   'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 
                   'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 
                   'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 
                   'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 
                   'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 
                   'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                   'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 
                   'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 
                   'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
