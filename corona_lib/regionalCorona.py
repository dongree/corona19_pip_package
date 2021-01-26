import requests
from bs4 import BeautifulSoup


def regionalCorona():
    req = requests.get(
        "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=")
    req2 = requests.get(
        "http://ncov.mohw.go.kr/"
    )

    soup = BeautifulSoup(req.text, "html.parser")
    soup2 = BeautifulSoup(req2.text, "html.parser")

    합계, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 검역 = soup.find(
        "div", class_="data_table midd mgt24").find_all("td", headers="status_level l_type1")

    기준 = soup2.find("div", class_="liveNumOuter").find(
        "span", class_="livedate")

    print("지역별 확진자 수")
    print(기준.text, "\n")
    print("서울: %s명" % 서울.text)
    print("부산: %s명" % 부산.text)
    print("대구: %s명" % 대구.text)
    print("인천: %s명" % 인천.text)
    print("광주: %s명" % 광주.text)
    print("대전: %s명" % 대전.text)
    print("울산: %s명" % 울산.text)
    print("세종: %s명" % 세종.text)
    print("경기: %s명" % 경기.text)
    print("강원: %s명" % 강원.text)
    print("충북: %s명" % 충북.text)
    print("충남: %s명" % 충남.text)
    print("전북: %s명" % 전북.text)
    print("전남: %s명" % 전남.text)
    print("경북: %s명" % 경북.text)
    print("경남: %s명" % 경남.text)
    print("제주: %s명" % 제주.text)
    print("검역: %s명" % 검역.text)
    print("합계: %s명" % 합계.text)
