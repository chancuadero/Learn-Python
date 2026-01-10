from collections import defaultdict

words = ['apple','ant','banana','bat','carrot']
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
print(grouped)

#defaultdict using list
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print(d)


applications = [("Google","Remote"), ("Atlassian", "Australia"),
                ("Canva","Australia"),("Xero","New Zealand"),
                ("Revolut","United Kingdom"),("Spotify", "Remote")]

category_tracker = defaultdict(list)
for company,category in applications:
    category_tracker[category].append(company)

for category,company in category_tracker.items():
    print(f"{category}: {", ".join(company)}")

#namedtuple
from collections import namedtuple
Job = namedtuple('Job', ['company','location','status','salary'])

my_apps = [Job("Google","Remote","Sent",150000),Job("Canva","Australia","Interview",130000),
           Job("Xero","New Zealand","Rejected",110000)]

for app in my_apps:
    print(f"{app.company} - {app.location} | Status: {app.status}")