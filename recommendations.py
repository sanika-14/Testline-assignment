def create_recommendations(insights):
    weak_topics = insights["weak_topics"]
    weak_difficulty = insights["weak_difficulty"]

    recommendations = {
        "suggested_topics": weak_topics,
        "suggested_difficulty": weak_difficulty,
        "actionable_steps": [
            f"Practice more questions on {', '.join(weak_topics)}.",
            f"Focus on improving your performance in {weak_difficulty} difficulty questions."
        ]
    }
    return recommendations

if __name__ == "__main__":
    insights = {
        "weak_topics": ["Math", "Physics"],
        "weak_difficulty": "Hard",
        "message": "Focus on improving in topics: Math, Physics and difficulty level: Hard."
    }

    recommendations = create_recommendations(insights)
    print("Recommendations:")
    print(recommendations)