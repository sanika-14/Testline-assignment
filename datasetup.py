import pandas as pd
import requests

def load_data():
    # Fetch current quiz data
    current_quiz_url = "https://api.jsonserve.com/rJvd7g"
    current_quiz_response = requests.get(current_quiz_url)
    current_quiz_json = current_quiz_response.json()

    # Fetch historical quiz data
    historical_quiz_url = "https://www.jsonkeeper.com/b/LLQT"
    historical_quiz_response = requests.get(historical_quiz_url)
    historical_quiz_json = historical_quiz_response.json()

    # Fetch additional data from the new API endpoint
    additional_data_url = "https://api.jsonserve.com/XgAgFJ"
    additional_data_response = requests.get(additional_data_url)
    additional_data_json = additional_data_response.json()

    print("Current Quiz JSON:")
    print(current_quiz_json)
    print("\nHistorical Quiz JSON:")
    print(historical_quiz_json)
    print("\nAdditional Data JSON:")
    print(additional_data_json)

    # Convert JSON to DataFrame
    current_quiz_data = pd.json_normalize(current_quiz_json)
    historical_quiz_data = pd.json_normalize(
        historical_quiz_json["quiz"]["questions"],
        sep="_"
    )
    additional_data = pd.json_normalize(additional_data_json)

    return current_quiz_data, historical_quiz_data, additional_data

def analyze_data(current_quiz_data, historical_quiz_data, additional_data):
    if 'options' not in historical_quiz_data.columns:
        raise KeyError("The 'options' column is missing in historical_quiz_data.")

    historical_quiz_data['correct_option'] = historical_quiz_data['options'].apply(
        lambda x: next((opt['id'] for opt in x if opt['is_correct']), None)
    )

    historical_quiz_data['selected_option'] = None

    if 'selected_option' in historical_quiz_data.columns and 'correct_option' in historical_quiz_data.columns:
        historical_quiz_data['is_correct'] = historical_quiz_data['selected_option'] == historical_quiz_data['correct_option']
        topic_accuracy = historical_quiz_data.groupby('topic')['is_correct'].mean().reset_index()
    else:
        topic_accuracy = pd.DataFrame()

    if 'difficulty_level' in historical_quiz_data.columns:
        difficulty_performance = historical_quiz_data.groupby('difficulty_level')['is_correct'].mean().reset_index()
    else:
        difficulty_performance = pd.DataFrame()

    analysis_results = {
        "topic_accuracy": topic_accuracy,
        "difficulty_performance": difficulty_performance,
        "historical_quiz_data": historical_quiz_data,
        "additional_data": additional_data  
    }
    return analysis_results

if __name__ == "__main__":
    # Load data
    current_quiz_data, historical_quiz_data, additional_data = load_data()

    # Analyze data
    analysis_results = analyze_data(current_quiz_data, historical_quiz_data, additional_data)

    # Print analysis results
    print("Analysis Results:")
    print(analysis_results)