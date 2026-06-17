"""
    Building a function that takes real analysis results and formats 
    them into a clean string for claude to read

    Claude needs 4 things. 
        * Revenue by cat 
        * Freight ration by cat 
        * Delivery vs reviews 
        * low reviews

    A function that takes all 4 analysis functions and combines them 
    into one structure text string 

    Each section should have a clear heading so claude knows what its ready 

    .to_string() 


"""

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