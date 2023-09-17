def generate_insights(compliance_breaches):
    insights = []

    for breach in compliance_breaches:
     
        insight = f"Compliance breach detected: {breach['description']}. Recommendation: {breach['recommendation']}"
        insights.append(insight)

    return insights
