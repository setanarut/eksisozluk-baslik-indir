from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm
import sys


url = str(sys.argv[1])
dosyaismi = url.rsplit("/",1)[-1]

def get_page(url, n):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    url += "?p="
    r = requests.get(url + str(n) , headers=headers, timeout=10)
    s = BeautifulSoup(r.content, "lxml")
    return s

s = get_page(url, 1)
toplam_sayfa = int(s.find("div", {"class":"pager"}).get("data-pagecount"))

df = pd.DataFrame(columns=['entry', 'yazar', 'tarih', 'entry_id'])
for page in tqdm(range(1, toplam_sayfa+1), unit=" sayfa", desc="Sayfalar indiriliyor"):
    s = get_page(url, page)
    items = s.find_all(id="entry-item")
    #br yenisatır düzelt
    for br in s.find_all("br"):
        br.replace_with("\n")
    for i in range(len(items)):
        entry = str(items[i].find("div", {"class":"content"}).get_text())
        entry = entry.lstrip()
        entry = entry.rstrip()
        # print(entry)
        yazar = items[i].get("data-author")
        tarih = str(items[i].find("a",attrs={"class":"entry-date permalink"}).text)
        edit = "-"
        if " ~ " in tarih:
            tarih, edit = str(tarih).split(" ~ ")
        match len(tarih):
            case 10:
                tarih = datetime.strptime(tarih, '%d.%m.%Y')
            case 16:
                tarih = datetime.strptime(tarih, '%d.%m.%Y %H:%M')
        
        entry_id = items[i].get("data-id")
        new_row = {'entry': entry, 'yazar': yazar, 'tarih': tarih.date(), 'entry_id': entry_id}
        df.loc[len(df)] = new_row

dosyaismi += ".csv"
df.to_csv(dosyaismi, index=False)
print("dosya kaydedildi: ", dosyaismi)

