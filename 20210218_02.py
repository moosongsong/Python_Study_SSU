import pandas as pd

person = pd.read_csv("survey_person.csv")
site = pd.read_csv("survey_site.csv")
survey = pd.read_csv("survey_survey.csv")
visited = pd.read_csv("survey_visited.csv")

# 조인하기1
print(site)
print(visited)
result1 = visited.merge(site, left_on='site', right_on='name')
print(result1)

# 조인하기2
print(person)
print(survey)
result2 = survey.merge(person, left_on='person', right_on='ident')
print(result2)

# 조인하기3
print(visited)
print(survey)
result3 = survey.merge(visited, left_on='taken', right_on='ident')
print(result3)

