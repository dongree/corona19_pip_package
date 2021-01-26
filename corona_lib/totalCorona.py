# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

req = requests.get("http://ncov.mohw.go.kr/")
soup = BeautifulSoup(req.text, "html.parser")

all_confirmed, quarantine, patient, death = soup.find("div", class_ = "liveNum").find_all("span", class_ = "num")

ac_change, q_change, p_change, d_change = soup.find("div", class_ = "liveNum").find_all("span", class_ = "before")

date = soup.find("div", class_ = "liveNumOuter").find("span", class_ = "livedate")

def corona_case():

    print("\n누적 확진자 수 (격리 해제 + 치료 중 + 사망)")
    # 누적 확진자 수.
    print(date.text)
    print("\n누적 확진자 수: " + str(all_confirmed.text[4:]) + "명")
    print(ac_change.text)

    # 격리 해제.
    print("\n격리 해제: " + str(quarantine.text) + "명")
    print("전일대비 " + str(q_change.text))

    # 치료 중(격리 중).
    print("\n치료 중(격리 중): " + str(patient.text) + "명")
    print("전일대비 " + str(p_change.text))

    # 사망자 수.
    print("\n사망: " + str(death.text) + "명")
    print("전일대비 " + str(d_change.text))
