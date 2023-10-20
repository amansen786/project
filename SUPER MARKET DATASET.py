import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('supermarket_sales - Sheet1.csv')

var_head=df.head(1000)
print(var_head)
print()

#*****************************************************************************************************************************************
#//////////////////////////////////////// SUPERMARKET DATASET ANALYSIS PROJECT///////////////////////////////////////////////////////////
#-----------------------------------------------------------------------------------------------------------------------------------------




df2=var_head['Payment']= var_head["Payment"].replace(["Cash","Ewallet","Credit card"],["upi","paytm","phonpe"]) #I REPLACE ALL THE VALUES IN "PAYMENT COLUMN" 

df3=var_head["City"] = var_head["City"].replace(["Yangon","Naypyitaw","Mandalay"],["Indore","Bhopal","CHHATARPUR"]) #I REPLACE ALL THE VALUES IN "CITY COLUMN" 

df3 = var_head.drop(['gross margin percentage','Invoice ID', 'Date', 'Time'], axis = 1)    # I REMOVED UNNECESSARY COLUMNS HERE

df4= var_head['Gender'].value_counts()   #In this operation we saw what was the total number of men and women.

df5 = pd.DataFrame(var_head['Payment'].value_counts())    # in this operation we saw total number's of payments have done.

df6=var_head.describe() # 
print()
#_____________________________________________________________________________________________
products_male = var_head.where(var_head['Gender'] == "Male")  # In this operation we saw which products was using by MALE.
out_male = products_male.groupby('Product line')
print(out_male.describe()) 
print()
#___________________________________________________________________________________________________________________

products_female = var_head.where(var_head['Gender'] == "Female")    # In this operation we saw which products was using by WOMEN.

out_female = products_female.groupby('Product line')

print(out_female.describe()) 
#the Describe() Methods used for calcultating some statistical data like percentile,mean,min,max and numerical values of the series or data frame.

print()
#____________________________________________________________________________________________________________________________
print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
print()

#_____________________________________________________________________________________________________________________________________________
#/////////////////////////////////////////////////////////// DATA VISUALISATION ///////////////////////////////////////////////////////////////
#________________________________________________________________________________________________________________________________________________

x= var_head['Product line']
y= var_head['City'] 
plt.figure(figsize=(12,4))
plt.xlabel('Product line')   # in this Graph we saw which prouct's were purchased from which cities.
plt.ylabel('City')
plt.title("WHICH CITY BUY HIGH PRODUCT", fontsize=15)
plt.bar(x,y)
plt.show()

#_____________________________________________________________________________________________________________________

x= var_head['Product line']
y= var_head['gross income'] 
plt.figure(figsize=(12,6))
plt.xlabel('Product line')      # We saw in this graph total amount before taxes or other deductions.
plt.ylabel('gross income')
plt.title("GROSS INCOME IN PRUDUCT'S", fontsize=15)
plt.bar(x,y)
plt.show()
#_________________________________________________________________________________________________________________________

x= var_head['Product line']
y= var_head['Rating'] 
plt.figure(figsize=(12,6))
plt.xlabel('Product line')  # WE SAW IN THIS Graph WHICH PRODUCT RATING IS Good.
plt.ylabel('Rating')
plt.title("HIGHEST RATING PRODUCT", fontsize=15)
plt.bar(x,y)
plt.show()
#________________________________________________________________________________________________________________________

x= var_head['Product line']
y= var_head['Total'] 
plt.figure(figsize=(12,6))    
plt.xlabel('Product line')      # WE SAW IN THIS Graph TOTAL PROFIT IN WHICH PRODUCT.
plt.ylabel('Total')
plt.title("HIGHEST PROFIT PRODUCT", fontsize=15)
plt.bar(x,y)
plt.show()
#________________________________________________________________________________________________________________________





