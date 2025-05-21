uk_countries = [57.11, 3.13, 1.91, 5.45]
provinces = [65.77, 41.88, 45.28, 61.27, 85.15]#define the list
uk_countries_sorted = sorted(uk_countries)
provinces_sorted = sorted(provinces)

print("Sorted UK countries population:", uk_countries_sorted)#title
print("Sorted Zhejiang-neighboring provinces population:", provinces_sorted)
import matplotlib.pyplot as plt#make the pie charts
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.pie(uk_countries_sorted, labels=["England", "Wales", "Northern Ireland", "Scotland"], autopct='%1.1f%%')
plt.title("UK Population Distribution")

plt.subplot(1, 2, 2)
plt.pie(provinces_sorted, labels=["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"], autopct='%1.1f%%')
plt.title("Zhejiang-Neighboring Provinces Population Distribution")

plt.show()