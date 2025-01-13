# Instacart Dataset Analysis  
By James Weaver

## Introduction  
This project focuses on analyzing Instacart's dataset to gain insights into customer ordering behavior. The primary goal is to clean, explore, and visualize data to identify patterns, trends, and actionable insights that can inform business decisions.  

## Files  
1. **instacart_analysis.ipynb**  
   The main Jupyter Notebook containing the code for data cleaning, analysis, and visualizations.  
2. **instacart_orders.csv**  
   Dataset with details about customer orders, including day and time of purchase.  
3. **products.csv**  
   Metadata about products, including names, aisles, and departments.  
4. **aisles.csv**  
   Categorizes products into grocery aisles.  
5. **departments.csv**  
   Groups products into larger department categories.  
6. **order_products.csv**  
   Links orders to products, showing details like cart order and reorder status.  
7. **README.md**  
   Overview of the project, methodology, and key findings.

## Approach  
1. **Data Cleaning**  
   - Removed duplicates and handled missing values.  
   - Normalized product names for consistency.  
2. **Exploratory Data Analysis (EDA)**  
   - Investigated ordering trends by time and day of the week.  
   - Analyzed popular products, reorder behavior, and order sizes.  
3. **Visualization**  
   - Created bar charts, histograms, and pie charts to highlight key insights.

## Tools Used  
- **Python**: Data manipulation and analysis.  
- **Pandas**: Data cleaning and preprocessing.  
- **NumPy**: Numerical computations.  
- **Matplotlib**: Visualization of shopping patterns and trends.

## Key Findings  
1. **Popular Items**  
   - Bananas are the most frequently purchased and first-added item.  
   - Organic products dominate frequently reordered and first-added items, reflecting customer preference for fresh and organic produce.  
2. **Shopping Patterns**  
   - Peak shopping hours: 10 a.m. to 4 p.m.  
   - Most popular shopping days: Sunday and Monday.  
   - Common order frequencies: Weekly (7 days) and monthly (30 days).  
3. **Reordering Trends**  
   - High reorder rates for organic fruits and vegetables.  
4. **Order Size Distribution**  
   - Most orders contain 1–14 items, indicating smaller, frequent shopping trips.  
5. **Customer Segmentation**  
   - Diverse reorder percentages, with some customers reordering frequently (above 98%) and others rarely reordering.

## Visuals  
### Time of Day People Grocery Shop  
![Time of Day Shopping](timeofhourpeopleshop.png)

### Day of the Week Shopping Patterns  
![Day of the Week](dayofweekpeopleshopmost.png)

### Top 20 Most Popular Products  
![Top Products](top20itemsfirst.png)

## Recommendations  
1. **Stocking and Inventory**  
   - Focus on high-demand organic produce like bananas, spinach, and avocados.  
2. **Optimized Delivery Slots**  
   - Prioritize delivery options during peak hours (10 a.m.–4 p.m.) on popular days (Sunday and Monday).  
3. **Customer Engagement**  
   - Introduce loyalty programs for high-frequency customers.  
   - Improve advertising strategies to convert low-frequency shoppers into regular customers.

## Future Improvements  
- Analyze product pairings within single orders.  
- Segment shopping patterns based on customer demographics.  
- Compare Instacart order behavior with other grocery delivery services.

