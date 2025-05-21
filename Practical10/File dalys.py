import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\ASUS\Desktop\ZJE\IBI1\IBI1_2024-25\Practical10") 
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print("\nthe first 10 rows of the third column (year):")
print(dalys_data.iloc[0:10, 2]) 
print("10th year of Afghanistan:", dalys_data.iloc[9, 2])
print("\n1990-DALYs:")
print(dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"])

uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]

# Calculate the mean DALYs for the UK and France
mean_uk_dalys = uk["DALYs"].mean()
mean_france_dalys = france["DALYs"].mean()

# Print the mean DALYs for the UK and France
print("\nAverage DALYs for the UK:", mean_uk_dalys)
print("Average DALYs for France:", mean_france_dalys)

#The average DALYs for the UK is greater than France.
plt.figure(figsize=(10, 6))
plt.plot(uk["Year"], uk["DALYs"], 'b+-', label="United Kingdom")
plt.title("DALYs over Time in the UK")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(rotation=45)
plt.legend()
plt.show()
# Answer the question: Are the trends of DALYs in China and the UK similar over time?
china = dalys_data[dalys_data["Entity"] == "China"]
plt.figure(figsize=(10, 6))
plt.plot(uk["Year"], uk["DALYs"], 'b+-', label="United Kingdom")
plt.plot(china["Year"], china["DALYs"], 'r+-', label="China")
plt.title("DALYs over Time in the UK and China")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(rotation=45)
plt.legend()
plt.show()
