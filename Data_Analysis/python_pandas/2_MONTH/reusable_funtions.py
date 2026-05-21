import pandas as pd

# example of resuable data
def greet(name):
    return f"hello {name}"

print(greet("Abra"))




df = pd.DataFrame({
    "name":["gorge","lasa","kolo","davo"],
    "email":["gorge","laDDa","kOOlo","davo"],
    "product": ["A","B","C","D"],
    "price":[100,200,300,400]
})

#  discount - double
df["discount_price"] = df["price"] * 0.90
df["double_price"] = df["price"] * 2

# reusable function
def add_tax_column(dataframe, tax_rate):
    dataframe["price_with_tax"] = dataframe["price"] * (1 + tax_rate)
    return dataframe


new_df = add_tax_column(df, 0.07)
print(new_df)

#-------------- BETTER PRACTICES-------------------
# NO.1 AVOID MODIFYING ORIGINAL DATA
# using add_tax_column
print("practicas ")
def add_tax_column_2(dataframe, tax_rate):
    df_copy = dataframe.copy()
    
    df_copy["price_with_tax_2"] = (
        df_copy["price"] * (1 + tax_rate)
    )
    return df_copy

# NO.2 REUSABLE CLEANING FUNCTION
#df["name"] = df["name"].str.strip()
#df["email"] = df["email"].str.lower()
#df = df.dropna() # todo los vacios 


# ahora reusable
def clean_customer_data(dataframe):
    df_cleaning_copy = dataframe.copy()
    
    df_cleaning_copy["name"] = df_cleaning_copy["name"].str.strip()
    df_cleaning_copy["email"] = df_cleaning_copy["email"].str.lower()
    df_cleaning_copy = df.dropna()
    
    return df_cleaning_copy

df_limpio = clean_customer_data(df)
print("Limpieza completada:")
print(df_limpio)


# NO.3 FUNCTION WITH PARAMETERS

print("NO.3")
sales_df = pd.DataFrame({
    "product": ["A","B","C","D"],
    "cantidad":[100,200,300,400]
})

def filter_big_sales(dataframe, min_amount):
    filtered_df = dataframe[dataframe["cantidad"] >= min_amount]
    return filtered_df

def filter_small_sales(dataframe, max_amount):
    filtered_df = dataframe[dataframe["cantidad"] <= max_amount]
    return filtered_df

# pasarlas a variables
big_sales = filter_big_sales(sales_df,200)
small_sales = filter_small_sales(sales_df,300)

print("Ventas Grandes:\n",big_sales)
print("Ventas PEQUEÑAS:\n",small_sales)

# NO.4
def trasform_data(df):
    df = df.copy()
    #Transformtions
    df["new_col"] = df["old_col"] * 2
    return df 

def add_total(df):
    df = df.copy()
    df["total"] = df["price"] * df["quantity"]
    return df 

#-------------------------- CREATING DATA COLUMNS _____________----------
print("\nCREANDO DATA\n")
df2 = pd.DataFrame({
    "product":["A","B","C"],
    "price":[10,20,30],
    "quantity":[2,5,3]
    })

#sin funcion
# df2["total"] = df2[price] * df2[quantity]

def add_total_column(df):
    df = df.copy()
    
    df["total"] = df["price"] * df["quantity"]
    return df

df_final = add_total_column(df2)
print(df_final)

#----------------____GROPING DATA___---------------------
print("\npractica Agrupar\n")
sales = pd.DataFrame({
    "product":["A","A","B","B"],
    "sales":[100,200,300,400]
})

def group_sales_by_product(df):
    grouped = (
        df.groupby("product")["sales"]
        .sum()
        .reset_index()
    )
    
    return grouped
    
result = group_sales_by_product(sales)
print(result)

#-----------------_______SORTING DATA____________----------------
print("\nSORTED\n")
fd = pd.DataFrame({
    "name":["jhon","Ana","Mike"],
    "sales":[200,500,100]
})

def sort_by_sales(df, ascending= False):
    return df.sort_values(
        by="sales",
        ascending=ascending
    )
sorted_df = sort_by_sales(fd, True)# para que sea ASC
print(sorted_df)

#--------------______________REMOVING DUPLICATES__________------------------
df3 = pd.DataFrame({
    "email":[
        "a@gmail.com",
        "a@gmail.com",
        "b@gmail.com"
    ]
})

def remove_duplicate(df, column_name):
    return df.drop_duplicates(
        subset=column_name #sub set es la columna especifica sino quita todas las repetidas
    )
duplicates = remove_duplicate(df3,"email")
print(duplicates)
    
    
#-----------__________________Professional Pattern___________---------------
def some_transformation(df):
    df= df.copy()
    #modify 
    return df


#----------_________________COMBINE MULTIPLE OPERATIONS___________-------
print("\ncleaninig sort and create column")


def clean_sales_data(df):
    df = df.copy()
    #remove duplicates
    df = df.drop_duplicates()
    
    #create column
    df["total"] = df["price"] * df["quantity"]
    
    #sort
    df = df.sort_values(by="total",ascending=False)
    return df 
combine = clean_sales_data(df2)
print(combine)

    