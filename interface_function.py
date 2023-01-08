from subwayGame import stationDict
from random import randint
# ----------------함수 설명-----------------
# interface_function.py 구성 요소
# 1. drinkingGame 클래스 
#  - 변수
#      1. lastLoser      (각 게임에서 진 사람을 해당 변수에 담음. 그 다음 게임을 선택할 사람을 정하기 위함)
#      2. playerList     (게임에 참가하는 플레이어들의 이름 리스트)
#      3. playerLimit    (각 게임에 참가하는 플레이어들의 치사량 리스트 순서는 위의 이름 리스트 순서대로)
#      4. loseCount      (게임 끝날 때마다 진 횟수 출력해야해서 추가. 플레이어들의 진 횟수. 순서는 위와 동일)
#  - 함수
#      1. selectGame     (마지막에 진 사람이 게임을 선택하게 함 input으로 받는 숫자에 따라 게임 결정)
#      2. printLimit     (각 플레이어마다 진 횟수와 남은 치사량 출력)
#      3. changeStatus   (게임이 끝날 때마다 진 횟수와 남은 치사량 업데이트)
#      4. printGameOver  (게임이 끝났음을 아스키아트로 출력하고 진 사람 출력)

# 그 외의 함수
# printGameList()        (게임 리스트 출력)
# printIntro()           (게임 인트로 출력)
# printSelectLimit()     (주량 선택 인터페이스 출력)

class drinkingGame():
  
  lastLoser = "태훈"  #각 게임 구현에서 마지막으로 진 사람을 선택해줘야함
  playerList = []
  playerLimit = []
  loseCount = []
  userName ="태훈"
  stationDict = stationDict
  def __init__(self, playerList, playerLimit, loseCount):
    self.playerList = playerList
    self.playerLimit = playerLimit
    self.loseCount = loseCount
    self.userName = playerList[0]
    
  #임시 게임
  def selectGame(self, name):
    correctNumber = False
    while not correctNumber:
      gameNumber = input(f"{name} (이 )가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? : ")
      if not str.isdigit(gameNumber):
        print("잘못된 입력입니다")
      elif 1<= int(gameNumber) <=5:
        if gameNumber == "1":
          self.game1()
        elif gameNumber == "2":
          self.game2()
        elif gameNumber == "3":
          self.game3()
        elif gameNumber == "4":
          self.game4()
        elif gameNumber == "5":
          self.game5()
        correctNumber =True
      else:
        print("1과 5사이의 정수를 입력해주세요")

  # 게임이 끝날 때마다 치사량을 출력하기 위한 함수
  def printLimit(self):
    num = len(self.playerList)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(num):
      print(f"{self.playerList[i]} 은(는 ) 지금까지 {self.loseCount[i]}🍺! 치사량까지 {self.playerLimit[i]}")
  
  
  # 각 게임에서 진 사람을 클래스의 변수인 lastLoser에 넣으면 그 다음에 자동으로 남은 치사량과 진 횟수를 업데이트
  def changeStatus(self):
    idx = self.playerList.index(self.lastLoser)
    self.playerLimit[idx] -= 1
    self.loseCount[idx] += 1
    
  def game1(self):
    print("369 게임입니다")
  def game2(self):
    print("딸기 게임입니다")
  def game3(self):
    print("UP&DOWN 게임입니다")
  def game4(self):
    print("지하철 게임입니다")
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
      
      idx = self.playerList.index(self.lastLoser)
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

        if self.playerList[idx] == self.playerList[0]:
          answer = input(f"{self.playerList[0]}의 차례입니다. {subwayLine}의 역을 하나 말해주세요: ")
          answer =answer[:-1]
        else:
          answer = computerSubway[randint(0, num-1)]
          print(f"{self.playerList[idx]}의 차례입니다. {subwayLine}의 역을 하나 말해주세요: {answer}역")
        
        if answer not in correctSubway:
          print(f"{self.playerList[idx]} 땡! {answer}는 {subwayLine}이 아닙니다. 마셔~ 마셔~ 먹고 뒤져~🍾")
          wrongAnswer = True
          self.lastLoser = self.playerList[idx]
          break
        elif answer in answerList: #호선이 틀리거나 중복된 경우
          print(f"{self.playerList[idx]} 땡! 이미 말한 역입니다. 마셔~ 마셔~ 먹고 뒤져~🍾")
          wrongAnswer = True
          self.lastLoser = self.playerList[idx]
          break
        answerList.append(answer)

        idx += 1
        if idx ==len(self.playerList):
          idx = 0
  def game5(self):
    print("레코드 게임입니다")
    
    
  def printGameOver(self):
    print("---------------------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------------------")
    print(" ____       ______                  ____                  _____       __  __     ____       ____        ")
    print("/\  _`\    /\  _  \     /'\_/`\    /\  _`\               /\  __`\    /\ \/\ \   /\  _`\    /\  _`\      ")
    print("\ \ \L\_\  \ \ \L\ \   /\      \   \ \ \L\_\             \ \ \/\ \   \ \ \ \ \  \ \ \L\_\  \ \ \L\ \    ")
    print(" \ \ \L_L   \ \  __ \  \ \ \__\ \   \ \  _\L              \ \ \ \ \   \ \ \ \ \  \ \  _\L   \ \ ,  /    ")
    print("  \ \ \/, \  \ \ \/\ \  \ \ \_/\ \   \ \ \L\ \             \ \ \_\ \   \ \ \_/ \  \ \ \L\ \  \ \ \\\ \   ")
    print("   \ \____/   \ \_\ \_\  \ \_\\\ \_\   \ \____/              \ \_____\   \ `\___/   \ \____/   \ \_\ \_\ ")
    print("    \/___/     \/_/\/_/   \/_/ \/_/    \/___/                \/_____/    `\/__/     \/___/     \/_/\/ / ")
    print()
    print("---------------------------------------------------------------------------------------------------------")
    print(f"{self.lastLoser}이 (가 ) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                 🍺 다음에 술 마시면 또 불러주세요~ 안녕! 🍺                               ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



# 게임 리스트를 출력하기 위한 함수

def printGameList():
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍺 오늘의 Alchohol GAME 🍺~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("                                                     🍺 1. 369 게임                                                                 ")
  print("                                                     🍺 2. 딸기 게임                                                                ")
  print("                                                     🍺 3. UP & DOWN 게임                                                           ")
  print("                                                     🍺 4. 지하철 게임                                                              ")
  print("                                                     🍺 5. 단어 들어간 노래 말하기 게임                                              ") # 이름 추후 수정
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def printIntro():
  print("------------------------------------------------------------------------------------------------------------------------------------")
  print("     ___       __        ______  __    __    ______    __    __    ______    __           _______      ___      .___  ___.  _______ ")
  print("    /   \     |  |      /      ||  |  |  |  /  __  \  |  |  |  |  /  __  \  |  |         /  _____|    /   \     |   \/   | |   ____|")
  print("   /  ^  \    |  |     |  ,----'|  |__|  | |  |  |  | |  |__|  | |  |  |  | |  |        |  |  __     /  ^  \    |  \  /  | |  |__   ")
  print("  /  /_\  \   |  |     |  |     |   __   | |  |  |  | |   __   | |  |  |  | |  |        |  | |_ |   /  /_\  \   |  |\/|  | |   __|  ")
  print(" /  _____  \  |  `----.|  `----.|  |  |  | |  `--'  | |  |  |  | |  `--'  | |  `----.   |  |__| |  /  _____  \  |  |  |  | |  |____ ")
  print("/__/     \__\ |_______| \______||__|  |__|  \______/  |__|  |__|  \______/  |_______|    \______| /__/     \__\ |__|  |__| |_______|")
  print("")
  print("------------------------------------------------------------------------------------------------------------------------------------")
  print("🍻                      ⸜(｡˃ ᵕ ˂ )⸝      안주 먹을 시간이 없어요😵 마시면서 배우는 술 게임🍾     ⸜(｡˃ ᵕ ˂ )⸝                       🍻")
  
def printSelectLimit():
  print()
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍾 소주 기준 당신의 주량은? 🍾~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("                                                   🍾 1. 소주 반병 (2잔)                                                            ")
  print("                                                   🍾 2. 소주 반병에서 한병 (4잔)                                                    ")
  print("                                                   🍾 3. 소주 한병에서 한병 반 (6잔)                                                 ")
  print("                                                   🍾 4. 소주 한병 반에서 두 병 (8잔)                                                ")
  print("                                                   🍾 5. 소주 두병 이상 (10잔)                                                       ")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

