import requests
# from interface_function import drinkingGame
from bs4 import BeautifulSoup as bs
from random import randint

playerList = [ "태훈", "건이","유민"]
playerLimit = [2, 4, 8]
loseCount = [0, 0, 0]

url ="http://openapi.seoul.go.kr:8088/645a615953616263353156426b7544/xml/SearchSTNBySubwayLineInfo/1/768/"
response = requests.get(url)
soup = bs(response.text, "html.parser")
stations = soup.select("row")

stationDict = dict()

#1호선부터 9호선 추가
for i in range(1, 10):
  numberStationList = [ele.select_one("station_nm").text for ele in stations if ele.select_one("line_num").text == f"0{i}호선"]
  stationDict[f"{i}호선"] = numberStationList

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

subwayList = ["1호선","2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선", "인천1호선", "인천2호선", "수인분당선"\
    ,"신분당선", "경의중앙선", "공항철도선", "경춘선", "의정부경전철", "용인경전철", "경강선", "우이신설경전철", "서해선", "김포도시철도선", "신림선"]

'''class subwayGame(drinkingGame):
# class subwayGame():
  subwayList = ["1호선","2호선", "3호선", "4호선", "5호선", "6호선", "7호선", "8호선", "9호선", "인천1호선", "인천2호선", "수인분당선"\
    ,"신분당선", "경의중앙선", "공항철도선", "경춘선", "의정부경전철", "용인경전철", "경강선", "우이신설경전철", "서해선", "김포도시철도선", "신림선"]
  
  def __init__(self, playerList, playerLimit, loseCount, stationDict):
    self.stationDict = stationDict
    super().__init__(playerList, playerLimit, loseCount)
  
  def subwayGameStart(self):
    subwayLine = ""
    if self.lastLoser != self.playerList[0]:
      idx = randint(0, len(self.subwayList)-1)
      subwayLine = self.subwayList[idx]
      print(f"지하철~🚇 지하철~🚇 지하철~🚇 지하철~🚇 몇호선~? {subwayLine}")
    else:
      subwayLine = input("지하철~🚇 지하철~🚇 지하철~🚇 지하철~🚇 몇호선~? : ")
      while subwayLine not in self.stationDict:
        print("살리고~~~ 살리고~~~ 살리고~ 살리고~ 살리고~")
        print("지하철 호선 목록: ", " ".join(self.subwayList))
        subwayLine = input("지하철~🚇 지하철~🚇 지하철~🚇 지하철~🚇 몇호선~? : ")
      
      idx = playerList.index(self.lastLoser)
      wrongAnswer = False
      answerList = []
      correctSubway = self.stationDict[subwayLine]
      if subwayLine != "2호선":
        wrongSubway = self.stationDict["2호선"][:10]
      else:
        wrongSubway = self.stationDict["1호선"][:10]
      computerSubway = correctSubway + wrongSubway
      num = len(computerSubway)
      

      while not wrongAnswer:

        if playerList[idx] == playerList[0]:
          answer = input(f"{playerList[0]}의 차례입니다. {subwayLine}의 역을 하나 말해주세요: ")
          answer =answer[:-1]
        else:
          answer = computerSubway[randint(0, num-1)]
          print(f"{playerList[idx]}의 차례입니다. {subwayLine}의 역을 하나 말해주세요: {answer}역")
        
        if answer not in correctSubway:
          print(f"{playerList[idx]} 땡! {answer}는 {subwayLine}이 아닙니다. 마셔~ 마셔~ 먹고 뒤져~🍾")
          wrongAnswer = True
          self.lastLoser = playerList[idx]
          break
        elif answer in answerList: #호선이 틀리거나 중복된 경우
          print(f"{playerList[idx]} 땡! 이미 말한 역입니다. 마셔~ 마셔~ 먹고 뒤져~🍾")
          wrongAnswer = True
          self.lastLoser = playerList[idx]
          break
        answerList.append(answer)

        idx += 1
        if idx ==len(playerList):
          idx = 0
        
sub = subwayGame(playerList, playerLimit, loseCount, stationDict)
sub.subwayGameStart()'''