language_popularity = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
} # PSEUDOCODE: REQUESTED_LANGUAGE_VARIABLE
import matplotlib.pyplot as plt

languages = list(language_popularity.keys())
percentages = list(language_popularity.values())

plt.bar(languages, percentages)
plt.xlabel("Programming Languages") 
plt.ylabel("Percentage of Developers")
plt.title("Programming Language Popularity")
plt.show()
