import matplotlib.pyplot as plt
from src.analyser import revenue_by_category,freight_ratio_by_category,delivery_vs_reviews,low_review_categories

def plot_revenue_by_category(product_table): 
    revenue = revenue_by_category(product_table)
    top_10 = revenue.head(10)
    top_10 = top_10.sort_values(ascending = True)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(top_10.index, top_10.values)

    ax.set_title("Revenue by Category")
    ax.set_xlabel("Total Revenue")
    ax.set_ylabel("Category")

    plt.tight_layout()
    plt.savefig('docs/revenue_by_category.png', bbox_inches='tight', dpi=150)
    plt.show()


def plot_freight_ratio(product_table): 
    freight_ratio = freight_ratio_by_category(product_table)
    top_10 = freight_ratio.head(10)
    top_10 = top_10.sort_values('percentage', ascending=True)


    fig, ax = plt.subplots(figsize=(10,6))

    ax.barh(top_10.index, top_10['percentage'])

    ax.set_title("Frieght ratio by category")
    ax.set_xlabel("Freight")
    ax.set_ylabel("Category")

    plt.tight_layout() 
    plt.savefig('docs/freight_ratio.png', bbox_inches='tight', dpi=150)
    plt.show() 

def plot_delivery_vs_review(master_table):
    summary = delivery_vs_reviews(master_table)

    late_score = summary['late_orders']['avg_review_score']
    early_score = summary['early_or_ontime_orders']['avg_review_early_or_on_time']

    labels = ['Late orders', 'Early / on-time orders']
    scores = [late_score, early_score]

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.barh(labels, scores)

    ax.set_title("Average Review Score: Late vs On-Time Delivery")
    ax.set_xlabel("Average Review Score")
    ax.set_ylabel("Delivery Status")

    plt.tight_layout()
    plt.savefig('docs/delivery_vs_review.png', bbox_inches='tight', dpi=150)
    plt.show()

def plot_low_reviews_cat(product_table): 
    summary = low_review_categories(product_table)

    #show 10 worst categories 
    summary = summary.head(10).sort_values('avg_review_score', ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(
        summary['product_category_name_english'],
        summary['avg_review_score']
    )

    ax.set_title("Lowest Average Review Score by Category")
    ax.set_xlabel("Average Review Score")
    ax.set_ylabel("Product Category")
    ax.set_xlim(3.0, 4.2) #zoom into speicfic range


    plt.tight_layout()
    plt.savefig('docs/low_review_categories.png', bbox_inches='tight', dpi=150)
    plt.show()