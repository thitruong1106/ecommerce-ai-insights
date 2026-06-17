from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv() 

client = Anthropic()

def generate_insights(analysis_results: str): 
    """
        Send analysis results to Claude and return plain english business insights. 

        Args: 
            analysis_results (str) : The analysis result to explain 

        Returns: 
            str: plain-english business insights from claude 
    """

    #sending a message 

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024, 
        system="you are a business intelligence analyst. You receive e-commerce data analysis results, and explain them in plain english for a small business owner who has no data skillls. ",
        messages=[
            {'role': 'user', 'content': analysis_results}
        ]
    )

    return response.content[0].text

def format_analysis_for_ai(revenue, freight, delivery, low_reviews): 
    summary = "=== REVENUE BY CATEGORY === \n"
    summary += revenue.head(10).to_string()
    summary += "\n\n"

    summary += "=== FREIGHT COST ANALYSIS ===\n"
    summary += freight.head(10).to_string()
    summary += "\n\n"

    summary += "=== DELIVERY VS REVIEW ANALYSIS ===\n"
    summary += str(delivery)
    summary += "\n\n"

    summary += "=== LOW REVIEW ANALYSIS ===\n"
    summary += low_reviews.head(10).to_string()
    summary += "\n\n"

    return summary