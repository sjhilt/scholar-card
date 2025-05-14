import requests
from bs4 import BeautifulSoup
import json

USER_ID = 'YOUR_GOOGLE_SCHOLAR_ID'
URL = f"https://scholar.google.com/citations?user={USER_ID}&hl=en"
OUTPUT_FILE = "scholar-stats.json"

headers = {
    "User-Agent": "Mozilla/5.0"
}
res = requests.get(URL, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

name = soup.find("div", id="gsc_prf_in").text
aff_tag = soup.find("div", class_="gsc_prf_il")
affiliation = aff_tag.text if aff_tag else ""

index_table = soup.find_all("td", class_="gsc_rsb_std")
citations_all = int(index_table[0].text)
citations_recent = int(index_table[1].text)
h_index_all = int(index_table[2].text)
h_index_recent = int(index_table[3].text)
i10_index_all = int(index_table[4].text)
i10_index_recent = int(index_table[5].text)

stats = {
    "name": name,
    "affiliation": affiliation,
    "citations_all": citations_all,
    "citations_recent": citations_recent,
    "h_index_all": h_index_all,
    "h_index_recent": h_index_recent,
    "i10_index_all": i10_index_all,
    "i10_index_recent": i10_index_recent
}

with open(OUTPUT_FILE, "w") as f:
    json.dump(stats, f, indent=2)

print(f"Scholar stats saved to {OUTPUT_FILE}")
