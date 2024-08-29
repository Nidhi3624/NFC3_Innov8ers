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




