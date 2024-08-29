import pandas as pd

messages_dict = {
            "NHigh" : "Nitrogen content in soil is high!\n Consider the following fertilizers:\n -Avoid adding nitrogen-rich fertilizers. \n -Use balanced or low-nitrogen fertilizers (e.g., 10-10-10 or 5-10-10). \n Other Suggestions: \n 1.Add organic matter like compost or aged manure to the soil.\n2.Grow crops that require less nitrogen or can tolerate high levels (e.g., carrots, beets).\n3.Increase soil drainage to prevent waterlogging.\n4.Practice crop rotation to balance soil nutrients.\n5.Use green manures like clover or legumes.\n6.Monitor crop health for signs of nitrogen toxicity.\n7.Adjust irrigation practices to avoid waterlogging.",
            "NLow" : "Nitrogen content in soil is low! \nConsider the following fertilizers:\n -Apply nitrogen-rich fertilizers (e.g., 20-10-10 or 30-10-10). \n-Use organic sources of nitrogen such as compost or manure.\nOther Suggestions: \n1.Plant nitrogen-fixing cover crops like legumes (e.g., clover, beans).\n2.Ensure proper soil aeration to enhance nitrogen availability.\n3.Monitor crop growth for signs of nitrogen deficiency.\n4.Adjust irrigation practices to support nutrient uptake.\n5.Avoid over-fertilizing to prevent nutrient imbalances.",
            "PLow" : "Phosphorous content in soil is low. \n Consider the following fertilizers:\n-Identify and confirm low nitrogen levels using a soil test.\n-Apply nitrogen-rich fertilizers (e.g., 20-10-10 or 30-10-10).\nOther Suggestions:\n1.Use organic sources of nitrogen such as compost or manure.\n2.Plant nitrogen-fixing cover crops like legumes (e.g., clover, beans).\n3.Ensure proper soil aeration to enhance nitrogen availability.\n4.Monitor crop growth for signs of nitrogen deficiency.\n5.Adjust irrigation practices to support nutrient uptake.\n6.Avoid over-fertilizing to prevent nutrient imbalances. ",
            "PHigh" : "Phosphorous content in soil is high. \n Consider the following fertilizers:\n-Apply phosphorus-rich fertilizers (e.g., 10-20-10 or 0-20-20).\n-Use organic sources of phosphorus such as bone meal or rock phosphate.\nOther Suggestions:\n1.Incorporate phosphorus fertilizers into the soil before planting.\n2.Use phosphorus-fixing cover crops like legumes.\n3.Ensure proper soil pH, as phosphorus availability is affected by soil acidity.\n4.Monitor plant growth for signs of phosphorus deficiency.\n5.Avoid over-fertilizing to prevent nutrient imbalances. ",
            "KHigh" : "Potassium content in soil is high. \n Consider the following fertilizers:\n-Avoid applying potassium-rich fertilizers.\n-Use balanced fertilizers with low potassium content (e.g., 10-10-10).\nOther Suggestions:\n1.Add organic matter like compost to help balance soil nutrients.\n2.Increase soil drainage to prevent potassium build-up.\n3.Use potassium-absorbing cover crops to help reduce excess levels.\n4.Monitor plant growth for signs of nutrient imbalances.\n5.Adjust irrigation practices to avoid waterlogging and excess potassium.",
            "KLow" : "Potassium content in soil is low. \n Consider the following fertilizers:\n-Apply potassium-rich fertilizers (e.g., 0-0-60 or 10-10-20).\n-Use organic sources of potassium such as wood ash or potassium sulfate.\nOther Suggestions:\n1.Incorporate potassium fertilizers into the soil before planting.\n2.Use potassium-boosting cover crops like clover.\n3.Ensure proper soil pH, as potassium availability is affected by soil acidity.\n4.Monitor plant growth for signs of potassium deficiency.\n5.Adjust irrigation practices to support nutrient uptake and avoid waterlogging."
        }

def get_nutrient_message(nitrogen, phosphorus, potassium, thresholds):
    messages = []

    # Check Nitrogen
    if nitrogen > thresholds['N']:
        messages.append(messages_dict.get('NHigh'))
    elif nitrogen < thresholds['N']:
        messages.append(messages_dict.get('NLow'))

    # Check Phosphorus
    if phosphorus > thresholds['P']:
        messages.append(messages_dict.get('PHigh'))
    elif phosphorus < thresholds['P']:
        messages.append(messages_dict.get('PLow'))

    # Check Potassium
    if potassium > thresholds['K']:
        messages.append(messages_dict.get('KHigh'))
    elif potassium < thresholds['K']:
        messages.append(messages_dict.get('KLow'))

    return messages




disease_dict = {
    "Apple___Apple_scab": (
        "Apple Scab\n"
        "Cause of the disease: Caused by the fungus Venturia inaequalis, leading to dark, sunken lesions on leaves and fruit.\n"
        "Solution:\n"
        "1. Remove and destroy infected leaves and fruit.\n"
        "2. Apply fungicides as a preventive measure.\n"
        "3. Ensure good air circulation around the plant."
    ),
    "Apple___Black_rot": (
        "Apple Black Rot\n"
        "Cause of the disease: Caused by the fungus Diplodia seriata, leading to black, sunken lesions on fruit and leaves.\n"
        "Solution:\n"
        "1. Prune and remove infected plant parts.\n"
        "2. Apply fungicides to protect healthy fruit.\n"
        "3. Practice crop rotation to reduce pathogen load."
    ),
    "Apple___Cedar_apple_rust": (
        "Cedar Apple Rust\n"
        "Cause of the disease: Caused by the fungus Gymnosporangium juniperi-virginianae, affecting apple and cedar trees.\n"
        "Solution:\n"
        "1. Remove cedar trees within 1 mile of apple trees.\n"
        "2. Apply fungicides during the growing season.\n"
        "3. Prune affected branches to improve airflow."
    ),
    "Apple___healthy": (
        "Healthy Apple\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and fertilization."
    ),
    "Blueberry___healthy": (
        "Healthy Blueberry\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and fertilization."
    ),
    "Cherry_(including_sour)_Powdery_mildew": (
        "Cherry Powdery Mildew\n"
        "Cause of the disease: Caused by the fungus Podosphaera clandestina, leading to white, powdery spots on leaves and fruit.\n"
        "Solution:\n"
        "1. Apply fungicides as soon as symptoms appear.\n"
        "2. Remove and destroy infected plant parts.\n"
        "3. Ensure good air circulation around plants."
    ),
    "Cherry_(including_sour)_healthy": (
        "Healthy Cherry\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and fertilization."
    ),
    "Corn_(maize)_Cercospora_leaf_spot_Gray_leaf_spot": (
        "Corn Cercospora Leaf Spot / Gray Leaf Spot\n"
        "Cause of the disease: Caused by the fungus Cercospora zeae-maydis, leading to grayish lesions on leaves.\n"
        "Solution:\n"
        "1. Use resistant corn varieties.\n"
        "2. Apply fungicides if necessary.\n"
        "3. Practice crop rotation to reduce pathogen load."
    ),
    "Corn_(maize)Common_rust": (
        "Corn Common Rust\n"
        "Cause of the disease: Caused by the fungus Puccinia sorghi, leading to reddish-brown pustules on leaves.\n"
        "Solution:\n"
        "1. Use rust-resistant corn varieties.\n"
        "2. Apply fungicides if necessary.\n"
        "3. Practice good field sanitation."
    ),
    "Corn_(maize)_Northern_Leaf_Blight": (
        "Corn Northern Leaf Blight\n"
        "Cause of the disease: Caused by the fungus Exserohilum turcicum, leading to large, grayish lesions on leaves.\n"
        "Solution:\n"
        "1. Use resistant corn varieties.\n"
        "2. Apply fungicides if necessary.\n"
        "3. Practice crop rotation and field sanitation."
    ),
    "Corn_(maize)_healthy": (
        "Healthy Corn\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, fertilization, and pest control."
    ),
    "Grape___Black_rot": (
        "Grape Black Rot\n"
        "Cause of the disease: Caused by the fungus Guignardia bidwellii, leading to dark, sunken lesions on fruit and leaves.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply fungicides during the growing season.\n"
        "3. Practice good vineyard sanitation."
    ),
    "Grape__Esca(Black_Measles)": (
        "Grape Esca (Black Measles)\n"
        "Cause of the disease: Caused by multiple fungi, leading to dark, necrotic areas on leaves and wood.\n"
        "Solution:\n"
        "1. Remove and destroy infected wood.\n"
        "2. Avoid excessive pruning wounds.\n"
        "3. Apply fungicides if necessary."
    ),
    "Grape__Leaf_blight(Isariopsis_Leaf_Spot)": (
        "Grape Leaf Blight (Isariopsis Leaf Spot)\n"
        "Cause of the disease: Caused by the fungus Isariopsis griseola, leading to dark spots and lesions on leaves.\n"
        "Solution:\n"
        "1. Remove and destroy infected leaves.\n"
        "2. Apply fungicides to protect healthy foliage.\n"
        "3. Practice good vineyard sanitation."
    ),
    "Grape___healthy": (
        "Healthy Grape\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and pest control."
    ),
    "Orange__Haunglongbing(Citrus_greening)": (
        "Orange Huanglongbing (Citrus Greening)\n"
        "Cause of the disease: Caused by the bacterium Candidatus Liberibacter spp., leading to yellowing and fruit drop.\n"
        "Solution:\n"
        "1. Remove and destroy infected trees.\n"
        "2. Apply systemic insecticides to control vectors.\n"
        "3. Use disease-free planting material."
    ),
    "Peach___Bacterial_spot": (
        "Peach Bacterial Spot\n"
        "Cause of the disease: Caused by the bacterium Xanthomonas campestris pv. pruni, leading to lesions on leaves and fruit.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply copper-based bactericides.\n"
        "3. Practice good orchard sanitation."
    ),
    "Peach___healthy": (
        "Healthy Peach\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and pest control."
    ),
    "Pepper,bell__Bacterial_spot": (
        "Pepper Bell Bacterial Spot\n"
        "Cause of the disease: Caused by the bacterium Xanthomonas campestris pv. vesicatoria, leading to dark, water-soaked spots on leaves and fruit.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply copper-based bactericides.\n"
        "3. Practice good field sanitation and crop rotation."
    ),
    "Pepper,bell__healthy": (
        "Healthy Pepper Bell\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and pest control."
    ),
    "Potato___Early_blight": (
        "Potato Early Blight\n"
        "Cause of the disease: Caused by the fungus Alternaria solani, leading to dark, concentric spots on leaves.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply fungicides to protect healthy foliage.\n"
        "3. Practice crop rotation and good field sanitation."
    ),
    "Potato___Late_blight": (
        "Potato Late Blight\n"
        "Cause of the disease: Caused by the fungus Phytophthora infestans, leading to rapid decay of leaves and tubers.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply fungicides promptly.\n"
        "3. Ensure proper spacing and ventilation."
    ),
    "Potato___healthy": (
        "Healthy Potato\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, fertilization, and pest control."
    ),
    "Raspberry___healthy": (
        "Healthy Raspberry\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and pest control."
    ),
    "Soybean___healthy": (
        "Healthy Soybean\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, fertilization, and pest control."
    ),
    "Squash___Powdery_mildew": (
        "Squash Powdery Mildew\n"
        "Cause of the disease: Caused by the fungus Podosphaera xanthii, leading to white, powdery patches on leaves.\n"
        "Solution:\n"
        "1. Apply fungicides as soon as symptoms appear.\n"
        "2. Remove and destroy infected plant parts.\n"
        "3. Ensure good air circulation around plants."
    ),
    "Strawberry___Leaf_scorch": (
        "Strawberry Leaf Scorch\n"
        "Cause of the disease: Caused by environmental stress or pathogens, leading to brown, scorched leaves.\n"
        "Solution:\n"
        "1. Improve watering practices and avoid water stress.\n"
        "2. Remove and destroy affected leaves.\n"
        "3. Apply appropriate fungicides if necessary."
    ),
    "Strawberry___healthy": (
        "Healthy Strawberry\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and pest control."
    ),
    "Tomato___Bacterial_spot": (
        "Tomato Bacterial Spot\n"
        "Cause of the disease: Caused by the bacterium Xanthomonas campestris pv. vesicatoria, leading to dark, water-soaked spots on leaves and fruit.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply copper-based bactericides.\n"
        "3. Practice good field sanitation."
    ),
    "Tomato___Early_blight": (
        "Tomato Early Blight\n"
        "Cause of the disease: Caused by the fungus Alternaria solani, leading to dark, concentric spots on leaves and stems.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply fungicides as needed.\n"
        "3. Practice crop rotation and good field sanitation."
    ),
    "Tomato___Late_blight": (
        "Tomato Late Blight\n"
        "Cause of the disease: Caused by the fungus Phytophthora infestans, leading to rapid decay of leaves and fruit.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply fungicides promptly.\n"
        "3. Ensure proper spacing and ventilation."
    ),
    "Tomato___Leaf_Mold": (
        "Tomato Leaf Mold\n"
        "Cause of the disease: Caused by the fungus Cladosporium fulvum, leading to gray mold on leaves.\n"
        "Solution:\n"
        "1. Remove and destroy infected leaves.\n"
        "2. Apply fungicides to control the spread.\n"
        "3. Improve air circulation around plants."
    ),
    "Tomato___Septoria_leaf_spot": (
        "Tomato Septoria Leaf Spot\n"
        "Cause of the disease: Caused by the fungus Septoria lycopersici, leading to small, dark spots with concentric rings on leaves.\n"
        "Solution:\n"
        "1. Remove and destroy infected leaves.\n"
        "2. Apply fungicides as needed.\n"
        "3. Practice crop rotation and good field sanitation."
    ),
    "Tomato___Spider_mites_Two-spotted_spider_mite": (
        "Tomato Spider Mites (Two-spotted Spider Mite)\n"
        "Cause of the disease: Caused by Tetranychus urticae, leading to stippling and webbing on leaves.\n"
        "Solution:\n"
        "1. Apply miticides to control spider mites.\n"
        "2. Increase humidity to reduce mite activity.\n"
        "3. Remove heavily infested leaves."
    ),
    "Tomato___Target_Spot": (
        "Tomato Target Spot\n"
        "Cause of the disease: Caused by the fungus Corynespora cassiicola, leading to dark spots with concentric rings on leaves.\n"
        "Solution:\n"
        "1. Remove and destroy infected plant parts.\n"
        "2. Apply fungicides as needed.\n"
        "3. Ensure proper plant spacing and air circulation."
    ),
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": (
        "Tomato Yellow Leaf Curl Virus\n"
        "Cause of the disease: Caused by a virus transmitted by whiteflies, leading to yellowing and curling of leaves.\n"
        "Solution:\n"
        "1. Remove and destroy infected plants.\n"
        "2. Control whitefly populations with insecticides.\n"
        "3. Use virus-resistant tomato varieties."
    ),
    "Tomato___Tomato_mosaic_virus": (
        "Tomato Mosaic Virus\n"
        "Cause of the disease: Caused by a virus leading to mottling and discoloration of leaves and fruit.\n"
        "Solution:\n"
        "1. Remove and destroy infected plants.\n"
        "2. Use virus-free seeds and resistant varieties.\n"
        "3. Practice good hygiene to prevent virus spread."
    ),
    "Tomato___healthy": (
        "Healthy Tomato\n"
        "Cause of the disease: No disease present.\n"
        "Solution:\n"
        "1. Continue regular maintenance and care.\n"
        "2. Ensure proper watering, pruning, and pest control."
    )
}


def getdata(title):
    message = []
    message.append(disease_dict.get(title))
    return message