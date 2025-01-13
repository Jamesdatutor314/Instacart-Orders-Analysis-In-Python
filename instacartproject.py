#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# This project focuses on analyzing Instacart's dataset to gain insights into customer ordering behavior. The primary goal is to clean, explore, and visualize data to identify patterns, trends, and actionable insights that could inform business decisions.
# 
# ### Datasets Utilized
# - **Orders**: Captures customer order details, such as the day of the week and time of purchase.
# - **Products**: Contains information about the items available for purchase.
# - **Aisles and Departments**: Classify products into categories for better understanding.
# - **Order Products**: Details the products ordered in each transaction.
# 
# ### Approach
# The analysis involves:
# 1. **Data Cleaning**: Handling duplicates and missing values to ensure data integrity.
# 2. **Exploratory Data Analysis (EDA)**: Identifying patterns and trends in the data.
# 3. **Visualization**: Creating graphs and charts to highlight key findings.
# 
# ### Tools
# This project utilizes Python libraries, including:
# - `pandas` for data manipulation
# - `numpy` for numerical operations
# - `matplotlib` for data visualization

# In[1]:


# import pandas library
import pandas as pd


# In[2]:


# import numpy libary
import numpy as np


# In[3]:


# import matplotlib for graphing
import matplotlib.pyplot as plt


# **1 Instacart Orders Data**

# **instacart_orders.csv: each row corresponds to one order on the Instacart app**
# 
# - **order_id**: ID number that uniquely identifies each order
# - **user_id**: ID number that uniquely identifies each customer account
# - **order_number**: the number of times this customer has placed an order
# - **order_dow**: day of the week that the order placed (which day is 0 is uncertain)
# - **order_hour_of_day**: hour of the day that the order was placed
# - **days_since_prior_order**: number of days since this customer placed their previous order

# In[4]:


# import csv
df_instacart_orders = pd.read_csv("/datasets/instacart_orders.csv",sep=';')
df_instacart_orders.head()


# **2 Products Data**

# **products.csv:** each row corresponds to a unique product that customers can buy
# 
# - **'product_id'**: ID number that uniquely identifies each product
# - **'product_name'**: name of the product
# - **'aisle_id'**: ID number that uniquely identifies each grocery aisle category
# - **'department_id'**: ID number that uniquely identifies each grocery department category

# In[5]:


# import csv
df_products = pd.read_csv("/datasets/products.csv",sep=';')
df_products.head()


# **3 Aisles Data**

# **aisles.csv**
# 
# - **'aisle_id'**: ID number that uniquely identifies each grocery aisle category
# - **'aisle'**: name of the aisle

# In[6]:


# import csv
df_aisles = pd.read_csv("/datasets/aisles.csv",sep=';')
df_aisles.head()


# **4 Departments Data**

# **departments.csv**
# 
# - **'department_id'**: ID number that uniquely identifies each grocery department category
# - **'department'**: name of the department

# In[7]:


# import csv
df_departments = pd.read_csv("/datasets/departments.csv",sep=";")
df_departments.head()


# **5 Order Products Data**

# **order_products.csv**: each row corresponds to one item placed in an order
# 
# - **'order_id'**: ID number that uniquely identifies each order
# - **'product_id'**: ID number that uniquely identifies each product
# - **'add_to_cart_order'**: the sequential order in which each item was placed in the cart
# - **'reordered'**: 0 if the customer has never ordered this product before, 1 if they have

# In[8]:


# import csv
df_order_products = pd.read_csv("/datasets/order_products.csv",sep=';')
df_order_products.head()


# ## Find and remove duplicate values (and describe why you make your choices)

# ### `orders` data frame

# In[9]:


df_instacart_orders.info()


# In[10]:


# Check for duplicated orders
dups = df_instacart_orders.duplicated().sum()
print(f"There are {dups} duplicates")


# In[11]:


print(f'Here are the {dups} rows')
df_instacart_orders[df_instacart_orders.duplicated()]


# ---
# # Summary For Instacart Dataframe
# #### Column Names
# - **Observation**: Column names are self-explanatory.
# - **Action**: No renaming is necessary.
# 
# #### Data Types
# - **Orders DataFrame**: 
#   - Most columns are of type `int64`, except for `days_since_prior_order`, which is `float64`.
#   - The `order_dow` (day of the week) and `order_hour_of_day` columns contain numerical data.
# - **Action**: Data types are appropriate.
# 
# #### Missing Values
# - **Orders DataFrame**:
#   - `days_since_prior_order`: Contains some missing values, which may indicate a customer's first order.
#   - Other columns have no missing values.
# - **Action**: Missing values in `days_since_prior_order` will be addressed later.
# 
# #### Duplicate Values
# - **Orders DataFrame**:
#   - Identified 15 duplicate rows.
#   - These duplicates were found to occur on the same day and at the same time, suggesting possible redundant entries.
# - **Action**: These duplicates will be handled later in the analysis.
# 
# #### Summary
# By examining the dataset's structure and content, the data aligns with expectations for this project. Identified issues, such as missing and duplicate values, have been documented and will be handled during the data cleaning process.
# 
# ---

# 

# In[12]:


# Check for all orders placed Wednesday at 2:00 AM


# In[13]:


df_instacart_orders['order_dow'].unique()


# We can assume 0=sunday, 1=monday,...,6=saturday because 0 means to start and the day of the week starts sundays.

# In[14]:


# Make a new column of the days of the week
day_of_week = {0:'sunday',
               1:'monday',
               2:'tuesday',
               3:'wednesday',
               4:'thursday',
               5:'friday',
               6:'saturday'}

df_instacart_orders['day_of_week'] = df_instacart_orders['order_dow'].replace(day_of_week)
df_instacart_orders.head()


# In[15]:


hours = sorted([i for i in df_instacart_orders['order_hour_of_day'].unique()])
print(hours)


# In[16]:


# orders placed at wednesy at 2:00 am
orders_wed_2am = df_instacart_orders.query("day_of_week == 'wednesday' & order_hour_of_day == 2")
orders_wed_2am.head()


# In[17]:


# Remove duplicate orders
df_instacart_orders = df_instacart_orders.drop_duplicates().reset_index(drop=True)
df_instacart_orders.head()


# In[18]:


# Double check for duplicate rows
dups = df_instacart_orders.duplicated().sum()
print(f"There are {dups} duplicates")


# In[19]:


# Double check for duplicate order IDs only
df_instacart_orders.shape


# In[20]:


df_instacart_orders['order_id'].nunique()


# Since number of rows match the number of unique rows for the order Id column, there is no duplicates order Id numbers.

# In[21]:


# Convert columns to correct data types
df_instacart_orders['day_of_week'] = df_instacart_orders['day_of_week'].astype('category')


# ___
# # Summary for Orders Data Frame
# 
# The `orders` data frame provides details about customer transactions, including order timing and frequency. Observations include:
# - **Duplicate Rows**: Identified 15 duplicate rows, all occurring on the same day and time. These were removed.
# - **Missing Values**: The `days_since_prior_order` column had some missing values, likely representing customers’ first orders. These were left as is it is..
# - **Data Types**: The `order_dow` and `order_hour_of_day` columns contain numerical data that fall within expected ranges (0-6 for days and 0-23 for hours). The `day_of_week` column was converted to a categorical type for optimized processing.
# ___

# 

# ### `products` data frame

# In[22]:


df_products.head()


# In[23]:


# Check for fully duplicate rows
dups = df_products.duplicated().sum()
print(f"There are {dups} full duplicated rows.")


# In[24]:


# Check for just duplicate product IDs
df_products.shape


# In[25]:


df_products['product_id'].nunique()


# The number of rows equal the number of unique values for the product id column, so no full duplicates in this columns

# In[26]:


# Check for just duplicate product names (convert names to lowercase to compare better)
def normalize_lower(col):
    if pd.isna(col):
        return col
    else:
        return col.lower()


# In[27]:


df_products["product_name_lower"] = df_products["product_name"].apply(normalize_lower)
df_products.head()


# In[28]:


# Check if there are duplicates in the product name lower column
product_lower = df_products['product_name_lower'].value_counts(ascending = False)
product_lower[product_lower>1]


# In[29]:


# Count how many duplicate product names exist among non-missing names
dups = df_products[df_products['product_name_lower'].notna()]['product_name_lower'].duplicated().sum()
print(f"There are {dups} duplicated product names among non-missing entries")

duplicate_names = df_products[df_products['product_name_lower'].notna()]['product_name_lower'].value_counts()[lambda x: x > 1]
print(f"Duplicate product names:\n{duplicate_names}")


# In[30]:


# Check for duplicate product names that aren't missing
df_products[df_products['product_name_lower'].notna()].duplicated().sum()


# In[31]:


# Define a normalization function for stricter cleaning
def normalize_other(col):
    '''This function will apply stricter normalization conditions'''
    if pd.isna(col):
        return col
    else:
        col = col.lower()  # Convert to lowercase
        col = col.strip()  # Remove leading/trailing whitespace
        col = " ".join(col.split())  # Remove extra spaces between words
        col = col.replace('-', '')  # Remove hyphens
        col = col.replace(' ', '')  # Remove all spaces
        return col

# Apply the normalization to create a stricter product name column
df_products["product_name_lower_2"] = df_products["product_name_lower"].apply(normalize_other)

# Check for duplicates in non-missing, normalized product names
non_missing = df_products[df_products["product_name_lower_2"].notna()]
duplicate_count = non_missing.duplicated(subset=["aisle_id", "department_id", "product_name_lower_2"]).sum()

print(f"There are {duplicate_count} more duplicated rows based on stricter normalization.")

# Optional: Print duplicate names for verification
duplicates = non_missing[non_missing.duplicated(subset=["aisle_id", "department_id", "product_name_lower_2"], keep=False)]
print("Duplicated rows based on stricter normalization:")
print(duplicates)


# In[32]:


# Ensure df_products retains all columns
df_products = df_products[["product_id", "product_name", "aisle_id", "department_id", "product_name_lower", "product_name_lower_2"]]


df_products.info()


# # Section Summary of `df_products` DataFrame
# 
# In this section, the `df_products` dataframe retains all necessary columns after cleaning and processing. Steps included:
# 
# 1. **Preserving Original and Derived Columns**:
#    - Columns like `product_id`, `product_name`, `aisle_id`, and `department_id` from the original dataframe were retained.
#    - New columns such as `product_name_lower` and `product_name_lower_2` (used for normalized product names) were kept.
# 
# 2. **Validation of Dataframe Structure**:
#    - Using `.info()` confirmed the presence of all expected columns:
#      - `product_id` (unique identifier for each product).
#      - `product_name` (original product names).
#      - `aisle_id` and `department_id` (categorization of products).
#      - `product_name_lower` and `product_name_lower_2` (processed product names for duplicate detection).

# 

# ### `departments` data frame

# In[33]:


df_departments['department'] = df_departments['department'].astype('category')


# In[34]:


df_departments.duplicated().sum()


# In[35]:


df_departments.info()


# ---
# # Section Summary For Departments Dataframe
# 
# The `departments` dataframe was analyzed to make sure the clean by checking for duplicate rows. This includes:
# - **Duplicate Rows**: No duplicate rows were found in the dataframe (`0 duplicates`).
# - **Data Structure**: The dataframe consists of 21 unique department entries and no missing values in the `department_id` or `department` columns.
# ---

# 

# ### `aisles` data frame

# In[36]:


df_aisles['aisle'] = df_aisles['aisle'].astype('category')


# In[37]:


# Check for duplicates
df_aisles['aisle'].duplicated().sum()
df_aisles.duplicated().sum()


# In[38]:


df_aisles.info()


# # Section Summary For Aisles Dataframe
# 
# The `aisles` dataframe was analyzed to make sure there are no duplicate rows and that the data is clean and ready for analysis. Key points included:
# 
# 1. **Duplicate Rows**:
#    - No duplicate rows were found in the dataframe (`0 duplicates`).
#    - Both the `aisle_id` and `aisle` columns are unique.
# 
# 2. **Data Structure**:
#    - The dataframe had 134 unique entries with no missing values in the `aisle_id` or `aisle` columns.
#    - The `aisle` column was converted to the `category` data type to optimize storage and speed.

# 

# ### `order_products` data frame

# In[39]:


df_order_products.head()


# In[40]:


# Check for fullly duplicate rows
dups = df_order_products.duplicated().sum()
print(f"The are {dups} fully duplicated rows")


# In[41]:


# Double check for any other tricky duplicates
duplicate_combinations = df_order_products.duplicated(subset=["order_id", "product_id"]).sum()
print(f"There are {duplicate_combinations} duplicate combinations of order_id and product_id.")


# In[42]:


df_order_products.info(null_counts=True)


# # Section Summary For Order-Products Dataframe
# 
# The `order_products` dataframe was analyzed for duplicates to make sure data is clean.
# 
# 1. **Fully Duplicated Rows**:
#    - No fully duplicated rows were found (`0 fully duplicated rows`).
# 
# 2. **Duplicate Combinations of `order_id` and `product_id`**:
#    - No duplicate combinations of `order_id` and `product_id` were found (`0 duplicate combinations`).
#    - This confirms that each product is uniquely associated with an order.
# 
# 3. **Data Structure**:
#    - The dataframe contains 4,545,007 entries with the following columns:
#      - `order_id`: Unique identifier for each order.
#      - `product_id`: Unique identifier for each product in an order.
#      - `add_to_cart_order`: Position of the product in the cart.
#      - `reordered`: Indicator of whether the product was previously ordered.

# 

# ## Find and remove missing values
# 

# ### `products` data frame

# In[43]:


df_products.info()


# In[44]:


df_products.isna().sum()


# In[45]:


# Are all of the missing product names associated with aisle ID 100?
df_products[df_products['product_name'].isna()]


# In[46]:


df_products[df_products['product_name'].isna()]['aisle_id'].value_counts()


# All of the missing product names are associated with aisle ID 100

# In[47]:


# Are all of the missing product names associated with department ID 21?
df_products[df_products['product_name'].isna()]['department_id'].value_counts()


# All of the missing product names are associated with department 21

# In[48]:


# What is this ailse and department?
df_aisles.query('aisle_id == 100')


# In[49]:


df_departments.query('department_id==21')


# The aisle and department is missing

# In[50]:


# Fill missing product names with 'Unknown'
df_products['product_name'] = df_products['product_name'].fillna('Unknown')


# In[51]:


df_products.info()


# # Section Summary: Missing Value Handling for Products Dataframe
# 
# The `products` dataframe was analyzed for missing values. Key points and actions include:
# 
# 1. **Missing Values**:
#    - A total of 1,258 rows had missing `product_name` values.
#    - All missing rows were associated with:
#      - `aisle_id = 100` (identified as "missing" in the aisles dataframe).
#      - `department_id = 21` (identified as "missing" in the departments dataframe).
# 
# 2. **Action Taken**:
#    - Missing `product_name` values were replaced with `"Unknown"`.
# 3. **Final Validation**:
#    - Verified that there are no remaining missing values in the dataframe.

# 

# ### `orders` data frame

# In[52]:


print("Missing values in each column:")
print(df_instacart_orders.isna().sum())


missing_days = df_instacart_orders[df_instacart_orders['days_since_prior_order'].isna()]
print("Rows with missing 'days_since_prior_order':")
missing_days


# In[53]:


# Are there any missing values where it's not a customer's first order?
print("Checking missing values where it is not a customer 1st order")
df_instacart_orders.query("order_number != 1").isna().sum()


# In[54]:


#missing values where it is a  customer's first order
print("Checking missing values where it is a customer 1st order")
df_instacart_orders.query("order_number == 1").isna().sum()


# # Section Summary:  Missing Values Handling For Instacart Orders Dataframe
# 
# The `orders` dataframe was analyzed to investigate missing values in the `days_since_prior_order` column. The results of the analysis shows:
# 
# 1. **Non-First Orders (`order_number != 1`)**:
#    - There are no missing values in the `days_since_prior_order` column for non-first orders.
# 2. **First Orders (`order_number == 1`)**:
#    - All rows for first orders have missing values in the `days_since_prior_order` column. This is expected behavior because first orders do not have prior days.
# 
# **Conclusion**:
# - The missing values in the `days_since_prior_order` column are consistent.
# - No  action was required to address these missing values because if replace with -1, that would affect the statisics.

# 

# ### `order_products` data frame

# In[55]:


df_order_products.info(null_counts=True)


# In[56]:


df_order_products.head()


# In[57]:


# What are the min and max values in this column?
col = "add_to_cart_order"
min1 = df_order_products['add_to_cart_order'].min()
max1 = df_order_products['add_to_cart_order'].max()
print(f"The min value for the {col} column is {min1}.)")
print(f"The max value for the {col} column is {max1}.)")


# In[58]:


# Save all order IDs with at least one missing value in 'add_to_cart_order'
order_ids = list(df_order_products.query("@pd.isna(add_to_cart_order)")['order_id'].unique())
df = df_order_products.query("order_id in @order_ids")
df.head()


# In[59]:


df.query("@pd.isna(add_to_cart_order)")


# In[60]:


df.query("add_to_cart_order==64")


# In[61]:


# Do all orders with missing values have more than 64 products?
df.groupby('order_id').count()


# In[62]:


df.groupby('order_id').size()


# In[63]:


order_sizes = df.groupby('order_id').size()
min_size = order_sizes.min()

print(f"The minimum size of orders is {min_size}.")
print("All orders with missing values contain more than 64 items.")


# In[64]:


# Replace missing values with 999 and convert column to integer type
df_order_products['add_to_cart_order'] = df_order_products['add_to_cart_order'].fillna(999)
df_order_products['add_to_cart_order'] = df_order_products['add_to_cart_order'].astype('int')
df_order_products.info()


# ---
# # Section Summary: Missing Values Handling For Order Products Dataframe
# 
# ### Overview
# The `order_products` dataframe was analyzed to handle missing values in the `add_to_cart_order` column. The column was checked for missing values.
# 
# 
# 
# ### Steps Taken
# 
# 1. **Basic Exploration**
#    - **Min and Max Values:**
#      - The minimum value of the `add_to_cart_order` column: **1.0**.
#      - The maximum value of the `add_to_cart_order` column: **64.0**.
# 
# 2. **Identifying Missing Values**
#    - Missing values in `add_to_cart_order` were identified using `pd.isna()`. 
#    - **Number of rows with missing values:** **836 rows**.
# 
# 3. **Special Case Check**
#    - Verified all orders with missing values to confirm that they contain more than **64 items**.
# 
# 4. **Handling Missing Values**
#    - Replaced missing values in the `add_to_cart_order` column with `999`.
#    - Converted the column to an integer type for consistent data handling.
# 
# 5. **Validation**
#    - Verified that all missing values were replaced and the column type.
# 
# ---

# 

# # [A] Easy (must complete all to pass)

# ### [A1] Verify that the `'order_hour_of_day'` and `'order_dow'` values in the `orders` tables are sensible (i.e. `'order_hour_of_day'` ranges from 0 to 23 and `'order_dow'` ranges from 0 to 6)

# In[65]:


order_hour_of_day = sorted(list(df_instacart_orders['order_hour_of_day'].unique()))
order_hour_of_day


# In[66]:


order_dow = sorted(list(df_instacart_orders['order_dow'].unique()))
order_dow


# ### [A2] What time of day do people shop for groceries?

# In[67]:


df_instacart_orders["order_hour_of_day"].value_counts().plot(kind="bar",
                                                             rot=0,
                                                             xlabel="Hour Of Day",
                                                             ylabel="Fequency",
                                                             title="Time Of Day People Grocery Shop",
                                                             figsize=[10,5],
                                                             grid=True,
                                                             color='purple')
plt.show()


# # The bar chart indicates that the most popular time for grocery shopping is between 10 a.m and 4 p.m. Shopping frequency decreases in the evening and early morning hours, with the lowest activity observed between 1 a.m. and 6 a.m. This suggests that the majority of people prefer shopping during late mornings and early afternoons.

# ### [A3] What day of the week do people shop for groceries?

# In[68]:


df_instacart_orders["day_of_week"].value_counts().plot(kind="bar",
                                                             rot=0,
                                                             xlabel="Day Of Week",
                                                             ylabel="Fequency",
                                                             title="Day Of Week People Grocery Shop",
                                                             figsize=[10,5],
                                                             grid=True,
                                                             color='red')
plt.show()


# In[69]:


df_instacart_orders["day_of_week"].value_counts().plot(kind="pie",
                                                       autopct="%1.1f%%",
                                                       figsize=[70,8],
                                                       title="Percent Day Of Week People Grocery Shop",
                                                       ylabel='',
                                                       colors=['silver','red','yellow','pink','green','teal','gold'])
                                                       

plt.show()


# # Conclusion for Weekly Shopping Patterns
# 
# # The bar chart and pie chart shows that most grocery shopping happens on Sunday (17.6%) and Monday (17.2%), making them the most popular days. The remaining days are relatively consistent, with Thursday (12.5%) and Wednesday (12.7%) being the least common shopping days. This suggests people prefer to shop on Instacart at the start of the week.

# ### [A4] How long do people wait until placing another order?

# In[70]:


df_instacart_orders['days_since_prior_order'].value_counts(ascending=False).plot(kind='bar',
                                                                                figsize=[12,8],
                                                                                ylabel = 'Frequency',
                                                                                xlabel = "Days",
                                                                                title = "Days Before Next Order",
                                                                                grid = True,
                                                                                rot=45)
plt.xlabel('Frequency')
plt.ylabel('Days')
plt.show()


# # Conclusion:
# 
# # Most frequent days are 30 days and 7 day for placing the next order. Many customers tend to order weekly or monthly.

# 

# # [B] Medium (must complete all to pass)

# ### [B1] Is there a difference in `'order_hour_of_day'` distributions on Wednesdays and Saturdays? Plot the histograms for both days and describe the differences that you see.

# In[71]:


def histogram_info(data, bin_size=10, minx = None,r=None ):
    '''
    r = rounding for width
    minx = custum min value
    bin_size = bin size
    data = data as a series
    '''
    print('will return bins,midpoints, and labels for intervals')
    
    # find min and max
    if minx == None:
        minx = min(data)
    else:
        pass
    maxy = max(data)
    n = len(data)
    width = np.ceil( (maxy - minx) / bin_size)
    if r == None:
        pass
    else:
        width = round( (maxy - minx) / bin_size,r)
    bins = [i for i in np.arange(minx,maxy+1,width)]
    
    while max(bins) < maxy:
        bins.append(max(bins)+width)
        
    midpoints = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)]
    labels = [ f"[{bins[i]},{bins[i+1]})" for i in range(len(bins)-1)]
    labels[-1] = labels[-1][:-1] + "]"
    

    print(f'size:{n}')
    print(f'min:{minx}')
    print(f'max:{maxy}')
    print(f'bin size:{bin_size}')
    print(f'width:{width}')
    return bins,midpoints,labels    


# In[72]:


# distrubtion for saturday
saturdays = df_instacart_orders.query("day_of_week=='saturday'")['order_hour_of_day']
# distrubtion for wednesday
wednesdays = df_instacart_orders.query("day_of_week=='wednesday'")['order_hour_of_day']


# In[73]:


bins,midpoints,labels =histogram_info(saturdays)
labels = [i.replace('.0','') for i in labels] # remove decimals


# In[74]:


saturdays.plot(kind="hist",
               grid=True,
               xlabel='Hour Of Day',
               title='Distrubtions Of Hour Of Day Of The Week',
               figsize=[10,8],
               edgecolor='black',
               bins = bins)
plt.xticks(midpoints,labels)

wednesdays.plot(kind="hist",
                alpha=0.65,
                edgecolor='black',
                bins = bins)

plt.legend(['Saturday','Wednesday'])
plt.grid(True)
plt.show()


# # Conclustion:
# 
# # The distributions of the order hours on Wednesday and Saturday appear similar overall, but there is a  difference between 12:00 and 15:00. During this time, Saturday shows a higher frequency of orders compared to Wednesday. This indicates that more people prefer shopping during these hours on Saturdays.
# 

# ### [B2] What's the distribution for the number of orders per customer?

# In[75]:


bins,midpoints,labels = histogram_info(df_instacart_orders.groupby('user_id')['order_number'].max(),bin_size=10)
labels = [i.replace('.0','') for i in labels] # remove decimals


# In[76]:


df_instacart_orders.groupby('user_id')['order_number'].max().plot(kind='hist',
                                                                  edgecolor='black',
                                                                 figsize = [10,5],
                                                                 title='Distribution For Number Of Orders Per Customer',
                                                                 xlabel = 'Number Of Orders',
                                                                  grid = True,
                                                                  bins=bins)


plt.xticks(midpoints,labels)
plt.show()


# # Conclusion:
# 
# # The distribution of the number of orders per customer shows that most customers place between 1 and 10 orders, with the frequency declining as the number of orders increases. This indicates that a huge portion of Instacart’s customer base consists of low frequency shoppers, while high frequency shoppers are relatively rare.

# ### [B3] What are the top 20 popular products (display their id and name)?

# In[77]:


df_products.head()


# In[78]:


df_instacart_orders.head()


# In[79]:


df_order_products.head()


# In[80]:


df_merge1 = df_instacart_orders.merge(df_order_products,on='order_id',how='inner')
df_merge1.head()


# In[81]:


df_merge2 = df_merge1.merge(df_products,on='product_id',how='inner')
cols = ['order_id','user_id','product_name','product_id']
df_clean = df_merge2[cols]
df_clean.head()


# In[82]:


df_clean_grouped = df_clean.groupby(['product_name','product_id']).agg(freq=('user_id','count')).sort_values(by='freq',ascending=False)
df_clean_grouped.head(20).plot(kind='barh',
                               figsize=[8,12],
                               grid=True,
                               ylabel ='Product Name & ID',
                               title = 'Top 20 Popular Products',
                               legend = False)

plt.xlabel('Frequency')
plt.show()


# # Conclusion:
# 
# # The most frequently purchased products include a mix of organic fruits, vegetables, and other products. Bananas and bags of organic bananas are the top items, with much higher frequencies compared to the rest. Other highly popular items include organic strawberries, organic baby spinach, organic avocados, and limes. This distribution highlights a preference for organic and fresh produce among customers. Retailers can focus on stocking these items to meet consumers demand.

# # [C] Hard (must complete at least two to pass)

# ### [C1] How many items do people typically buy in one order? What does the distribution look like?

# In[83]:


df_clean = df_order_products.groupby('order_id').agg(freq=('product_id','count'))
df_clean.head()


# In[84]:


bins,midpoints,labels = histogram_info(df_clean['freq'],bin_size=20)
labels = [i.replace('.0','') for i in labels] # remove decimals


# In[86]:


df_clean['freq'].plot(kind='hist',
                      edgecolor='black',
                      figsize = [12,5],
                      title='Distribution For Number Of Items Per Order',
                      xlabel = 'Number Of Orders',
                      grid = True,
                      bins=bins,
                      color='green',
                      rot=40)

plt.xticks(midpoints,labels)
plt.xlabel('Number Of Orders')
plt.show()


# The distribution for number of items per order is highly skewd to the left. The majority of customers make purchase between 1 to 13 items per order.

# # Conclusion:
# 
# # The distribution of items per order is highly skewed to the right, with most orders between 1 to 14 items. The frequency greatly decreases as the number of items in an order increases. This indicates that customers tend to make smaller and more frequent purchases rather than placing large orders. 

# ### [C2] What are the top 20 items that are reordered most frequently (display their names and product IDs)?

# In[91]:


df_reordered = df_order_products.query("reordered ==1")
df_reordered.head()


# In[92]:


# Indices of the top 20  most reordered items in order
index_top20 = list(df_reordered['product_id'].value_counts(ascending = False).head(20).index)


# In[93]:


cols = ['product_name','product_id']
# make sure its in order
top20 = df_products.query("product_id in @index_top20")[cols].set_index("product_id").loc[index_top20].reset_index()
print('Top 20 items that are reordered most frequently ')
top20


# # Conclusion:
# # The top 20 most frequently reordered items include organic and fresh produce, like  bananas, organic strawberries, organic avocados, and organic baby spinach. This suggests that customers frequently reorder healthy food items.

# ### [C3] For each product, what proportion of its orders are reorders?

# In[98]:


proportion_product_reorder = df_order_products.groupby('product_id').agg(proportion_product_reorders = ('reordered','mean'))*100
proportion_product_reorder.head()


# In[99]:


# Merge the products df with the new proportion df to get the names and 
proportion_product_reorder = proportion_product_reorder.merge(df_products,how="inner",on="product_id")

# Get the most important columns 
cols = ['product_id','product_name','proportion_product_reorders']
proportion_product_reorder = proportion_product_reorder[cols]
proportion_product_reorder.head()


# In[100]:


# clean the proportion_product_reorders column
proportion_product_reorder['proportion_product_reorders'] = proportion_product_reorder['proportion_product_reorders'].apply(lambda x: str(round(x,2))+"%" )
proportion_product_reorder.sort_values(by='proportion_product_reorders',ascending=False).head(10)


# In[101]:


proportion_product_reorder.sort_values(by='proportion_product_reorders',ascending=False).tail(10)


# # Conclusion:
# 
# # The analysis shows the proportion of orders that are reorders for each product. The products with the highest reorder proportions like Fragrance Free Clay with Natural Odor Eliminator (95.24%) and Tequila Reposado (94.74%).However, products like XXXtra Hot Chile Habanero Sauce and Grape Super Drink, with 0% reorder rates indicate a lack of repeat demand.

# ### [C4] For each customer, what proportion of their products ordered are reorders?

# In[107]:


df_order_products.head()


# In[108]:


df_instacart_orders.head()


# In[109]:


df_merge = df_order_products.merge(df_instacart_orders,on="order_id",how="inner")
df_merge.head()


# In[110]:


proportion_users_reorder = df_merge.groupby('user_id').agg(proportion_user_reorders = ('reordered','mean'))*100
proportion_users_reorder.head()


# In[111]:


# clean the proportion user reorders col
proportion_users_reorder['proportion_user_reorders'] = proportion_users_reorder['proportion_user_reorders'].apply(lambda x: str(round(x,2))+"%")
proportion_users_reorder.sort_values(by='proportion_user_reorders').head(10)


# In[112]:


proportion_users_reorder.sort_values(by='proportion_user_reorders').tail(10)


# In[114]:


proportion_users_reorder = df_merge.groupby('user_id').agg(proportion_user_reorders = ('reordered','mean'))*100
proportion_users_reorder['proportion_user_reorders'] = proportion_users_reorder['proportion_user_reorders'].apply(lambda x: round(x,2))
proportion_users_reorder.head()


# In[127]:


bins,midpoints,labels = histogram_info(proportion_users_reorder['proportion_user_reorders'],bin_size=15)


# In[128]:


proportion_users_reorder['proportion_user_reorders'].plot(kind='hist',
                                                          edgecolor='black',
                                                          figsize = [12,5],
                                                          title='Distribution Of Proportion of Users Reorders',
                                                          xlabel = 'Number Of Orders',
                                                          grid = True,
                                                          bins=bins,
                                                          color='green',
                                                          rot=40)

plt.xticks(midpoints,labels)
plt.xlabel('Proportion %')
plt.show()


# # Conclusion
# 
# # The histogram of the proportion of reordered products for each customer shows a diverse range of reorder behaviors. The distribution appears multimodal, with a large number of customers having very low reorder percentages (close to 0-6%), a peak at the 49-55%, and another peak at high reorder percentages (above 98%). 

# ### [C5] What are the top 20 items that people put in their carts first? 

# In[129]:


df_order_products.head()


# In[130]:


df_products.head()


# In[131]:


# Filter only products that are 1st
df_first = df_order_products.query("add_to_cart_order==1")

top20_1st_products = df_first['product_id'].value_counts().head(20).reset_index().rename(columns = {'index':'product_id','product_id':'Freq'})
top20_1st_products.head()


# In[132]:


top20_1st_products_merge = top20_1st_products.merge(df_products,on='product_id')[['product_name','Freq']].set_index('product_name').sort_values('Freq')

# Plot
top20_1st_products_merge.plot(kind='barh',
                              xlabel = 'Product Name',
                              ylabel = 'Frequency',
                              title = 'Top 20 Products Put In Carts First',
                              figsize=[12,6],
                              legend=False,
                              grid = True)


plt.xlabel('Frequency')
plt.show()


# # Conclusion:
# 
# # The analysis of the top 20 products first added to carts shows patterns regarding initial selections in their shopping experience. Bananas rank as the most frequently added item, followed by the "Bag of Organic Bananas" and "Organic Whole Milk." This implies that produce items dominate customers' initial cart choices. Organic products also dominates the list.

# # Instacart Dataset Analysis: Key Insights 
# 
# ## Key Insights
# 
# ### 1. Popular Items
# - **Bananas** are the most frequently purchased and the most commonly added first to shopping carts on Instachart users, showing their importance as a grocery product.
# - **Organic products** dominate both the frequently reordered and first added items, showing a strong preference for fresh and organic produce among customers.
# 
# ### 2. Shopping Patterns
# - **Time of Day:** Customers primarily shop between **10 a.m. and 4 p.m.**, with minimal activity during the early morning hours (1 a.m.–6 a.m.).
# - **Day of the Week:** Sundays and Mondays are the most popular shopping days.
# - **Order Frequency:** Weekly (7 days) and monthly (30 days) orders are the most common.
# 
# ### 3. Reordering Trends
# - Customers show a strong interest to reorder organic fruits and vegetables.
# 
# ### 4. Order Size Distribution
# - The majority of orders contain between **1 and 14 items**, indicating a preference for smaller, more frequent shopping trips rather than bulk purchasing.
# 
# ### 5. Customer Segmentation
# - A **multimodal distribution** in reorder percentages across customers suggests diverse purchasing behaviors. Some customers reorder very frequently (above 98%), while others rarely reorder.
# 
# ---
# 
# ## Recommendations
# 
# ### 1. Stocking and Inventory
# - Focus on showing the availability of high demand organic produce like bananas, spinach, and avocados.
# 
# ### 2. Optimized Delivery Slots
# - Make delivery options with peak shopping hours (**10 a.m.–4 p.m.**) and popular days (**Sunday and Monday**) to increase customer satisfaction.
# 
# ### 3. Customer 
# - Tailor loyalty programs for high frequency customers.
# - Better advitising to convert low frequency shoppers into regular customers.
# 
# ---
