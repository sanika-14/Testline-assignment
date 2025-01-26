import pandas as pd
import matplotlib.pyplot as plt

def generate_insights(analysis_results):
    topic_accuracy = analysis_results["topic_accuracy"]
    difficulty_performance = analysis_results["difficulty_performance"]

    weak_topics = topic_accuracy[topic_accuracy['is_correct'] < 0.5]['topic'].tolist()

    if not difficulty_performance.empty:
        weak_difficulty = difficulty_performance.loc[difficulty_performance['is_correct'].idxmin(), 'difficulty_level']
    else:
        weak_difficulty = None

    insights = {
        "weak_topics": weak_topics,
        "weak_difficulty": weak_difficulty,
        "message": f"Focus on improving in topics: {', '.join(weak_topics)} and difficulty level: {weak_difficulty}."
    }

    # Visualizations
    if not topic_accuracy.empty:
        plt.figure(figsize=(10, 5))
        plt.bar(topic_accuracy['topic'], topic_accuracy['is_correct'], color='skyblue')
        plt.axhline(y=0.5, color='red', linestyle='--', label='50% Accuracy Threshold')
        plt.xlabel('Topics')
        plt.ylabel('Accuracy')
        plt.title('Topic Accuracy')
        plt.legend()
        plt.show()

    if not difficulty_performance.empty:
        plt.figure(figsize=(10, 5))
        plt.bar(difficulty_performance['difficulty_level'], difficulty_performance['is_correct'], color='lightgreen')
        plt.xlabel('Difficulty Level')
        plt.ylabel('Accuracy')
        plt.title('Performance by Difficulty Level')
        plt.show()

    return insights

if __name__ == "__main__":
    analysis_results = {
        "topic_accuracy": pd.DataFrame({'topic': ['Math', 'Physics', 'Chemistry'], 'is_correct': [0.4, 0.6, 0.7]}),
        "difficulty_performance": pd.DataFrame({'difficulty_level': ['Easy', 'Medium', 'Hard'], 'is_correct': [0.8, 0.6, 0.5]})
    }

    insights = generate_insights(analysis_results)
    print("Insights:")
    print(insights)