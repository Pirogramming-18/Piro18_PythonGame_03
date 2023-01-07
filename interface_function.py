
# 게임이 끝날 때마다 치사량을 출력하기 위한 함수
def printLimit(playerList, playerLimit, loseCount):
  num = len(playerList)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  for i in range(num):
    print(f"{playerList[i]} 은(는 ) 지금까지 {loseCount[i]}🍺! 치사량까지 {playerLimit[i]}")
    
# 게임 리스트를 출력하기 위한 함수

def printGameList():
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🍺 오늘의 Alchohol GAME 🍺~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("                                                     🍺 1. 369 게임                                                                 ")
  print("                                                     🍺 2. 딸기 게임                                                                ")
  print("                                                     🍺 3. UP & DOWN 게임                                                           ")
  print("                                                     🍺 4. 지하철 게임                                                              ")
  print("                                                     🍺 5. 단어 들어간 노래 말하기 게임                                              ") # 이름 추후 수정
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  
class drinkGame:
  
  def __init__(self, playerList, playerLimit, loseCount):
    self.playerList = playerList
    self.playerLimit = playerLimit
    self.loseCount = loseCount
    
  
  #임시 게임
  def game1():
    print("369 게임입니다")
  def game2():
    print("딸기 게임입니다")
  def game3():
    print("UP&DOWN 게임입니다")
  def game4():
    print("지하철 게임입니다")
  def game5():
    print("레코드 게임입니다")
    