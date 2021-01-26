
from bs4 import BeautifulSoup
import requests

req = requests.get("http://ncov.mohw.go.kr/")

soup = BeautifulSoup(req.text, "html.parser")

time = soup.find("span", class_="livedate")
print("오늘 확진자 수 (국내 + 해외 + 총합)\n" + time.text + "\n")
local, entry = soup.find("div", class_="liveNum_today_new").find_all(
    "span", class_="data")
total = int(local.text) + int(entry.text)
print("지역 확진자: " + local.text + " 명\n\n" + "해외 입국자: " +
      entry.text + " 명\n\n" + "총합: " + str(total) + " 명\n\n")
