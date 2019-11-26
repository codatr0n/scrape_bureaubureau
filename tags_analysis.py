import json

agencies = json.loads(open('digital_agencies.json', 'r').read())

tags = dict()
for agency, values in agencies.items():
    # print(agency, values['tags'])
    # print()
    for tag in list(set(values['tags'])):
        if tag in tags:
            tags[tag] += 1
        else:
            tags[tag] = 1

print(('=' * 30) + '\n' + 'Tags analyse - Top10' + '\n' + '=' * 30)
tags_sorted = sorted(tags.items(), key=lambda kv: -kv[1])
for i in range(10):
    print('{tag}: {count}'.format(tag=tags_sorted[i][0],
                                  count=tags_sorted[i][1]))
