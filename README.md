# E-Commerce AI Insights

E-Commerce AI Insights is a Python dashboard that looks into e-commerce sales data and turns it into plain English business insights. It was built to help business owners understand what is selling well, where money may be lost, and what can be improved — using the Brazilian E-Commerce dataset from [Olist on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

## What It Does

- Loads and joins e-commerce orders, products, payments, customer, and reviews data
- Shows total revenue, total orders, and average review scores
- Finds the product categories with the most revenue and the highest freight costs
- Compares late deliveries with customer review scores
- Uses Claude AI to turn the analysis into simple business recommendations

## Key Findings

- **Health & Beauty** was the highest revenue category, followed by Watches & Gifts, then Bed, Bath & Table. These three categories alone are carrying the business. If the business is not already focusing promotions on those areas, it should be considered a top priority.

- Some categories have very high freight costs compared to revenue. For example, Home Comfort 2 — 54 cents of every dollar earned goes back into freight. That is very unsustainable for the business and is a problem that needs to be addressed. Categories such as Flowers and Furniture (Mattress & Upholstery) also had high freight costs, reducing profits and potentially taking up valuable inventory space.

- Delivery speed has a direct impact on customer satisfaction. Late orders averaged **2.3 star reviews** compared to **4.3 stars** for on-time orders. This was validated with a t-test showing the difference is statistically significant (p < 0.001).

## Tech Stack

- Python
- pandas
- Streamlit
- Matplotlib
- SciPy
- Anthropic Claude API

## Project Structure

```
ecommerce-ai-insights/
├── data/               # raw dataset (not included — download from Kaggle)
├── docs/               # charts and write-ups
├── notebooks/          # exploratory analysis
├── src/
│   ├── __init__.py
│   ├── loader.py       # data loading functions
│   ├── transformer.py  # data joining and transformation
│   ├── analyser.py     # business analysis functions
│   ├── visualiser.py   # chart generation
│   └── ai_insights.py  # Claude API integration
├── app.py              # Streamlit dashboard
├── main.py             # command line entry point
├── .gitignore
└── README.md
```

## How To Run

1. Clone the repo
```bash
git clone https://github.com/thitruong1106/ecommerce-ai-insights.git
cd ecommerce-ai-insights
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate    # Git Bash on Windows
```

3. Install the required packages
```bash
pip install pandas streamlit matplotlib scipy anthropic python-dotenv
```

4. Download the [Olist E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and place the CSV files inside a folder called `data/`

5. Create a `.env` file in the project root with your Anthropic API key
```
ANTHROPIC_API_KEY=your_key_here
```

6. Run the Streamlit dashboard
```bash
streamlit run app.py
```

## What I Learned

Building this project helped me practice working with multiple CSV files and joining them into useful tables for analysis. I learned how to use pandas to find business insights, Matplotlib to create charts, and then putting it all together — I used Streamlit to turn a Python project into a dashboard that is easily navigable for new users. It outputs results in a way anyone can understand while still highlighting what matters to the business.
