import re
from urllib.request import urlopen
import json
html = urlopen(
    "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
).read().decode()
res = re.findall(r'href="(.*?)"', html)
matchers = ['pressreleases/monetary']
matching = [s for s in res if any(xs in s for xs in matchers)]
K='https://www.federalreserve.gov'
matching = [K+x for x in matching]
aa=len(matching)
for i in range(0,aa):
    html = urlopen(matching[i]).read().decode('utf-8')
    res = re.findall(r"<p>(.*?)</p>", html)
    my_json_string = json.dumps(res)
    with open('FOMC', 'a+', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=4)