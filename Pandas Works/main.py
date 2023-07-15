import pandas as pnd
import seaborn as sb

# pnd.set_option("display.max_columns", None)
# df = sb.load_dataset("titanic")


# counts the number of people by gender
# print(df["sex"].value_counts())


# find the number of unique variables in columns
# print(df.nunique())


# find the number of unique variables in the pclass
# print(df["pclass"].nunique())


# finds unique variables in pclass and parch
# print(df["pclass"].unique())
# print(df["parch"].unique())


# changing the type of milk
# df['embarked']=df['embarked'].astype('category')
# names=df.dtypes
# print(names)


# embarked value only shows the information of the C ones
# print(df[df["embarked"]=="C"].head(10))


# embarked value only shows the information of non-S
# print(df[df["embarked"]!="S"].head(10))


# women younger than 30 years old show their information
# print(df[(df["age"]<30) & (df["sex"]=="female")])


# shows information for people with an age greater than 70 or a mouse value greater than 500
# print(df[(df["fare"]>500) | (df["age"]>70)])


# collects empty values in columns separately
# print(df.isnull().sum())


# delete who variable from dataframe
# df.drop("who",inplace=True,axis=1)
# print(df)


# assigns the mod value of this column to the null values of the deck column
# df["deck"].fillna(df["deck"].mode()[0], inplace=True)
# print(df)


# assigns the median value of this column to the null values of the age column
# df["age"].fillna(df["age"].median(), inplace=True)
# print(df)


# survived variable has sum, count, mean values in the breakdown of pclass and gender variables
# print(df.groupby(["pclass","sex"]).agg({"survived":["sum","count","mean"]}))



# df["age_flag"]=0
# def x(a):
#     if(a<30):
#         return 1
#     else:
#         return 0



# Write a function that gives 1 to those under 30 and 0 to those equal to 30 and above. Titanic data using the function you wrote
# creates a variable named age_flag in the set



# df["age_flag"] = df["age"].apply(x)
# print(df)



# pnd.set_option("display.max_columns", None)
# df = sb.load_dataset("tips")



# Finds the sum, min, max and average of the total_bill values according to the categories (Dinner, Lunch) of the variable Time.
# print(df.groupby("time").agg({"total_bill":["sum","min","max","mean"]}))



# Finds the sum, min, max and average of total_bill values by days and time.
# print(df.groupby(["time","day"]).agg({"total_bill":["sum","min","max","mean"]}))




# Finds the sum, min, max and average of total_bill and type values for Lunch time and female customers by day
# print(df)
# print(df[(df["sex"]=="Female")&(df["time"]=="Lunch")].groupby("day").agg({"total_bill":["sum","min","max","mean"],
#                                                                           "tip":["sum","min","max","mean"]
#                                                                           }))



# What is the average of orders with size less than 3 and total_bill greater than 10?
# print(df.loc[(df["size"]<3)&(df["total_bill"]>10),"total_bill"].mean())


# Create a new variable called total_bill_tip_sum. Give the sum of totalbill and type paid by each customer.
# df["total_bill_tip_sum"]=df["total_bill"]+df["tip"]
#  print(df)




# Sort by total_bill_tip_sum and assign the first 30 people to a new dataframe.



# df.sort_values("total_bill_tip_sum",inplace=True,ascending=False)
# df2=df.head(30)
# print(df2)