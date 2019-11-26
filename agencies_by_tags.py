import json

# ==============================
# Tags analyse - Top10
# ==============================
# Effektmåling / ROI: 34
# Strategi: 30
# Lead generering: 29
# Konverteringsoptimering: 29
# Online marketing: 28
# Webdesign & Banner: 28
# SEO: 27
# Kampagner: 27
# Konceptudvikling & kampagner: 27
# Social media & Mobile & Apps: 27

agencies = json.loads(open('web_agencies.json', 'r').read())


def display_agency(agency):
    print(agency)
    print(agencies[agency]['web url'])
    print('https://www.proff.dk/branchesøg?q=' + agency.replace(' ', '+'))
    print(', '.join(agencies[agency]['tags']), end='\n\n')


search_for = [
    'Webdesign & Banner', 'Website / HTML / CSS', 'CMS & webudvikling', 'PHP',
    '.Net', 'Webshop', 'Programmering', 'Webudvikling', 'Laravel'
]

for agency, values in agencies.items():
    tags = list(set(values['tags']))
    for tag in tags:
        if tag in search_for:
            display_agency(agency)
            break
