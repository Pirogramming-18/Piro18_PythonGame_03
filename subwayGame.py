import requests
from bs4 import BeautifulSoup as bs
from random import randint

#지하철 API 활용
url ="http://openapi.seoul.go.kr:8088/645a615953616263353156426b7544/xml/SearchSTNBySubwayLineInfo/1/768/"
response = requests.get(url)
soup = bs(response.text, "html.parser")
stations = soup.select("row")

#지하철 노선 이름
subwayList = ["1호선","2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선", "인천1호선", "인천2호선", "수인분당선"\
    ,"신분당선", "경의중앙선", "공항철도선", "경춘선", "의정부경전철", "용인경전철", "경강선", "우이신설경전철", "서해선", "김포도시철도선", "신림선"]

stationDict = dict()

#1호선부터 9호선 딕셔너리에 추가
for i in range(1, 10):
  numberStationList = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == f"0{i}호선"]
  stationDict[f"{i}호선"] = numberStationList

#이외의 다른 노선도 딕셔너리에 추가
temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "인천선"]
stationDict["인천1호선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "인천2호선"]
stationDict["인천2호선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "수인분당선"]
stationDict["수인분당선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "신분당선"]
stationDict["신분당선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "경의선"]
stationDict["경의중앙선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "공항철도"]
stationDict["공항철도선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "경춘선"]
stationDict["경춘선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "의정부경전철"]
stationDict["의정부경전철"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "용인경전철"]
stationDict["용인경전철"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "경강선"]
stationDict["경강선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "우이신설경전철"]
stationDict["우이신설경전철"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "서해선"]
stationDict["서해선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "김포도시철도"]
stationDict["김포도시철도선"] = temp

temp = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == "신림선"]
stationDict["신림선"] = temp