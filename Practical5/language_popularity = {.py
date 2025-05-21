language_popularity = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}#give the varieable
import matplotlib.pyplot as plt#make the chart

languages = list(language_popularity.keys())
percentages = list(language_popularity.values())

plt.bar(languages, percentages)
plt.xlabel("Programming Languages") 
plt.ylabel("Percentage of Developers")
plt.title("Programming Language Popularity")#name the x,y,give title
plt.show() 
requested_language = "Python" # if request language, give the number
if requested_language in language_popularity:
    print(f"The percentage of developers who use {requested_language} is {language_popularity[requested_language]}%")
else:
    print("Language not found in the list.")