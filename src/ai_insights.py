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