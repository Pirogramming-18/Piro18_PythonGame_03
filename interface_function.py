from subwayDictionary import stationDict, subwayList
import random
from time import sleep
import pandas as pd
# ----------------함수 설명-----------------
# interface_function.py 구성 요소
# 1. drinkingGame 클래스 
#  - 변수
#      1. lastLoser      (각 게임에서 진 사람을 해당 변수에 담음. 그 다음 게임을 선택할 사람을 정하기 위함)
#      2. playerList     (게임에 참가하는 플레이어들의 이름 리스트)
#      3. playerLimit    (각 게임에 참가하는 플레이어들의 치사량 리스트 순서는 위의 이름 리스트 순서대로)
#      4. loseCount      (게임 끝날 때마다 진 횟수 출력해야해서 추가. 플레이어들의 진 횟수. 순서는 위와 동일)
#      5. userName       (사용자 이름 따로 저장)
#      6. stationDict    (지하철게임 때 쓰기 위한 노선 딕셔너리)
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
  
  lastLoser = ""  #각 게임 구현에서 마지막으로 진 사람을 선택해줘야함
  playerList = []
  playerLimit = []
  loseCount = []
  userName =""
  stationDict = stationDict #지하철 노선 저장한 딕셔너리
  isUpDownGame = False #up down 게임은 이긴 사람 빼고 벌주 마셔야하므로 다르게 처리
  
  def __init__(self, playerList, playerLimit, loseCount):
    self.playerList = playerList
    self.playerLimit = playerLimit
    self.loseCount = loseCount
    self.userName = playerList[0]
    self.lastLoser = playerList[0]
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
          self.subwayGame()
        elif gameNumber == "5":
          self.recordGame()
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
    if not self.isUpDownGame:
      idx = self.playerList.index(self.lastLoser)
      self.playerLimit[idx] -= 1
      self.loseCount[idx] += 1
    else:
      for i in range(len(self.lastLoser)):
            idx = self.playerList.index(self.lastLoser[i])
            self.playerLimit[idx] -= 1
            self.loseCount[idx] += 1
      self.lastLoser = self.lastLoser[0]
    
    
  #369 게임(1번게임)
  def game1(self):
    self.isUpDownGame = False
    print("  ____ ___  ___   ___   ___  __ __  ___    ___  ___  ___  ___  ___  _ ")
    print(" <__ /| __>| . | /  _> | . ||  \  \| __>  / __>|_ _|| . || . \|_ _|| | ")
    print(" <_ \ | . \`_  / | <_/\|   ||     || _>   \__ \ | | |   ||   / | | |_/ ")
    print(" <___/`___/ /_/  `____/|_|_||_|_|_||___>  <___/ |_| |_|_||_\_\ |_| <_> ")
    print("")
    print("369 게임입니다. 3, 6, 9가 들어간 개수만큼 박수 '짝'을 입력해 주세요. ex) 3일 때 '짝', 36일 때 '짝짝'")
    print("")
    count = 0
    a = ['3', '6', '9']
    num = len(self.playerList)
    #while과 for구문의 이중break를 도와주는 breaker를 사용
    breaker = False
    #확률을 설정하도록 여러 bool이 담긴 리스트를 이용
    B = [True, True, True, False, False, False]
    while True:
      for i in range(num):
        if i == 0:
          count += 1
          say = input(f'{self.playerList[0]}: ')
          #현재 숫자의 3, 6, 9 숫자의 합을 구하여 입력받은 say 속의 수와 같은지를 비교하는 람다함수
          #해석하면, "str(count)를 x로 받아서 sum([x.count(n) for n in a])값을 반환하라"
          lam = (lambda x: sum([x.count(n) for n in a]))(str(count))
          if lam:
            # 3, 6, 9가 중복되는 두 자리 숫자를 '짝짝'으로 처리 가능하도록 함
            answer = '짝' * lam
            if say != answer:
              print("")
              print(f'아 누가누가 술을 마셔 {self.playerList[0]}이(가) 술을 마셔 원~~~샷!')
              self.lastLoser = self.playerList[0]
              breaker = True
              break
          else:
            #ValueError를 막기위해 int(say)대신 str(count)로 설정
            if str(count) != say:
              print("")
              print(f'아 누가누가 술을 마셔 {self.playerList[0]}이(가) 술을 마셔 원~~~샷!') 
              self.lastLoser = self.playerList[0]
              breaker = True
              break
        else :
          count += 1
          reply = count
          print(f'{self.playerList[i]}: ', end='')
          lam = (lambda x: sum([x.count(n) for n in a]))(str(count))
          if lam:
            answer = '짝' * lam
            #'reply = answer'될 확률을 75%로 지정
            b = random.randint(0, 3)
            if B[b]:
              reply = answer
            print(reply)
            if reply != answer:
              print("")
              print(f'아 누가누가 술을 마셔 {self.playerList[i]}이(가) 술을 마셔 원~~~샷!')
              self.lastLoser = self.playerList[i]
              breaker = True
              break
          else:
            #'reply = count+1'될 확률을 25%로 지정
            b = random.randint(2, 5)
            if B[b]:
              reply = count+1
            print(reply)
            if count != int(reply):
              print("")
              print(f'아 누가누가 술을 마셔 {self.playerList[i]}이(가) 술을 마셔 원~~~샷!') 
              self.lastLoser = self.playerList[i]
              breaker = True
              break
      if breaker == True :
        break

  #딸기 게임(2번 게임)
  def game2(self):
    print("딸기 게임입니다")
    self.isUpDownGame = False


    print("🍓🍓🍓🍓🍓 딸기가 좋아 🍓 딸기가 좋아 🍓 좋아 좋아 좋아 좋아 좋아 좋아 🍓🍓🍓🍓",end="\n\n") 
    num = 1
    while(1):
                try:
                    for i in range(0,len(self.player_list)):
                            print(f"🍓이번 차례는 {self.player_list[i]} !",end="\n")          
                            cnt = random.randint(num,num+1)
                                                
                        
                            
                            player = ("딸기"+" ") * cnt
                            print(player,end="\n\n")
                                
                            # if(cnt // 4 == 1):
                            #     player 
                                
                            if(player.count('딸기') != num):
                                print("마셔 마셔!")
                                print(f"{self.player_list[i]}아 원샷해라.")
                                loser = self.player_list[i]
                                #패배자 
                                self.lastLoser = loser
                                print("패배자 : ",self.lastLoser)
                                raise Exception
                            num += 1
                    
                except:             
                        break
        
  #UP&DOWN 게임(3번 게임)
  def game3(self):
    print("UP&DOWN 게임입니다")
    self.isUpDownGame = True
    print (""" _ _         _                  
          | | | ___  _| | ___  _ _ _ ._ _ 
          | ' || . \/ . |/ . \| | | || ' |
          `___'|  _/\___|\___/|__/_/ |_|_|
               |_|                        
    """)

    print (""" ___                     ___    _                _    _  _  _ 
              /  _>  ___ ._ _ _  ___  / __> _| |_  ___  _ _  _| |_ | || || |
              | <_/\<_> || ' ' |/ ._> \__ \  | |  <_> || '_>  | |  |_/|_/|_/
              `____/<___||_|_|_|\___. <___/  |_|  <___||_|    |_|  <_><_><_>
    """)
    print ("게임을 시작합니다! 숫자를 맞춰주세요!")
    up = 100
    down = 1
    index = self.playerList.index(self.lastLoser)
    if index == 0:
        while True:
            number = int(input("당신이 낸 숫자를 친구들이 맞춥니다! 숫자를 입력해주세요🤪 : "))
            if number < 1 or number > 100:
                print("1부터 100까지의 수를 입력해주세요.")
            else:
                break
    else:
        number = random.randint(down, up) #난수 생성
        
    tries=0 #시도횟수
    n = 8 #기회 8번
    
    while tries < n: #시도횟수가 8번이 될때까지 반복
        try:
            player = self.playerList[index] # index번째
            if player == self.lastLoser:
                index += 1                
                if index == len(self.playerList):
                    index = 0
                continue
            else:
                if index == 0:
                    guess = int(input("숫자를 짐작해보세요!! : "))
                else:
                    guess = random.randint(down, up)
                    print('{} : {}'.format(player, guess))
                tries += 1
            
                if guess != number:
                    if number < guess:
                        print ("땡 ~ DOWN!!!")
                        up = guess -1
                    if number > guess:
                        print ("땡 ~ UP!!!")
                        down = guess + 1
                else:
                    print ("""
                             ___                                        _  _  _ 
                            /  _>  ___ ._ _ _  ___  ___  _ _  ___  _ _ | || || |
                            | <_/\<_> || ' ' |/ ._>/ . \| | |/ ._>| '_>|_/|_/|_/
                            `____/<___||_|_|_|\___.\___/|__/ \___.|_|  <_><_><_>
                           """)
                    print ("🍻 정답!! 문제를 낸 사람이 벌주를 마십니다! 🍻")
                    self.lastLoser = [self.lastLoser]
                    break
                    
                if tries == n:
                    print ("""
                             ___                                        _  _  _ 
                            /  _>  ___ ._ _ _  ___  ___  _ _  ___  _ _ | || || |
                            | <_/\<_> || ' ' |/ ._>/ . \| | |/ ._>| '_>|_/|_/|_/
                            `____/<___||_|_|_|\___.\___/|__/ \___.|_|  <_><_><_>
                           """)
                    print ("정답은 {0}이었습니다!".format(number))
                    print ("🍻 기회를 다 썼습니다!! 못맞추신 분들 벌주 마시세요~~~ 🍻")
                    self.lastLoser = self.playerList[1:]
                    break
                  
                index += 1                
                if index == len(self.playerList):
                    index = 0
                
        except Exception as e:
            print ("❌숫자를 입력하셔야합니다!!❌", e)
            
            
  #지하철 게임(4번 게임)
  def subwayGame(self):
    self.isUpDownGame = False
    #INPUT으로 받을 지하철 노선
    subwayLine = ""
    
    #컴퓨터 차례
    if self.lastLoser != self.playerList[0]:
      idx = random.randint(0, len(subwayList)-1)
      subwayLine = subwayList[idx]
      print(f"지하철~🚇 지하철~🚇 지하철~🚇 지하철~🚇 몇호선~? {subwayLine}")
    
    #유저 차례
    else:
      subwayLine = input("지하철~🚇 지하철~🚇 지하철~🚇 지하철~🚇 몇호선~? : ")
      while subwayLine not in self.stationDict:
        print("살리고~~~ 살리고~~~ 살리고~ 살리고~ 살리고~")
        print("지하철 호선 목록: ", " ".join(subwayList))
        subwayLine = input("지하철~🚇 지하철~🚇 지하철~🚇 지하철~🚇 몇호선~? : ")

    wrongAnswer = False # 답이 맞는지 체크하기 위한 플래그
    answerList = [] #중복 체크하기 위함
    idx = self.playerList.index(self.lastLoser) #처음 시작하는 사람 인덱스
    correctSubway = self.stationDict[subwayLine]
    
    #컴퓨터의 대답에 오답도 추가하여 확률적으로 대답하게 함
    if subwayLine != "2호선":
      wrongSubway = self.stationDict["2호선"][:10]
    else:
      wrongSubway = self.stationDict["1호선"][:10]
    computerSubway = correctSubway + wrongSubway
    num = len(computerSubway)
    
    #게임 시작
    while not wrongAnswer:
      
      #유저 차례
      if self.playerList[idx] == self.playerList[0]:
        answer = input(f"{self.playerList[0]}의 차례입니다. {subwayLine}의 역을 하나 말해주세요: ")
        answer =answer[:-1]
        
      #컴퓨터 차례
      else:
        answer = computerSubway[random.randint(0, num-1)]
        print(f"{self.playerList[idx]}의 차례입니다. {subwayLine}의 역을 하나 말해주세요: {answer}역")
      
      #잘못된 노선 말한 경우
      if answer not in correctSubway:
        print(f"{self.playerList[idx]} 땡! {answer}는 {subwayLine}이 아닙니다. 마셔~ 마셔~ 먹고 뒤져~🍾")
        wrongAnswer = True
        self.lastLoser = self.playerList[idx]
        break
      
      #중복된 노선 말한 경우
      elif answer in answerList: #호선이 틀리거나 중복된 경우
        print(f"{self.playerList[idx]} 땡! 이미 말한 역입니다. 마셔~ 마셔~ 먹고 뒤져~🍾")
        wrongAnswer = True
        self.lastLoser = self.playerList[idx]
        break
      
      #중복 체크하기 위해 리스트에 말한 대답 추가
      answerList.append(answer)

      #유저 번갈아가면서 하기 위해 인덱스 바꾸기
      idx += 1
      if idx ==len(self.playerList):
        idx = 0
        
  #레코드 게임(5번 게임)
  def recordGame(self) :

    self.isUpDownGame = False
    #---------------------------------------------csv파일 읽어오기----------------------------------------------
    data = pd.read_csv('./recordGame/recordGameData.csv') #경로 나중 변경
    data = data[['singer', 'song']]

    singerData = ['블랙핑크', '르세라핌', '뉴진스', '아이브', '데이식스']   #가수 리스트
    computerDataList = []              #컴퓨터가 말할 수 있는 데이터 리스트    
    answerList = []                    #정답인지 아닌지 확인하기 위한 전체(가수/노래제목) 데이터 리스트


    #-------------------------------pandas모듈 사용해서 정답 데이터 / 컴퓨터 사용 데이터 만들기-------------------------------------
    for singer in singerData:
        #이번 라운드 가수의 노래 랜덤 추출 (정답)
        data_answer = data.loc[data['singer'] == singer, :]
        tmpAnswerList = data_answer['song'].values.tolist()
        #정답지에 전처리 데이터 추가
        answerList.append(tmpAnswerList)

        data_answer = data_answer.sample(frac=1).reset_index(drop=True)
        #이번 라운드 가수 노래 제외 랜덤 추출 (오답)
        data_wrong = data.loc[data['singer'] != singer, :]
        data_wrong = data_wrong.sample(frac=1).reset_index(drop=True)

        #정답 비율 설정 (12개 중 9개 정답)
        data_answer = data_answer[:10]
        #오답 비율 설정 (12개 중 3개 오답)
        data_wrong = data_wrong[:2]

        #정답과 오답 합쳐서 computer가 말할 수 있는 데이터 리스트 만들기
        computerEachData = pd.concat([data_answer,data_wrong])
        #computer가 말할 수 있는 데이터 인덱스 초기화 및 랜덤으로 배열
        computerEachData = computerEachData.sample(frac=1).reset_index(drop=True)
        computerDataList.append(computerEachData['song'].values.tolist())

    
    #---------------------------데이터 전처리(공백 제거 / 소문자로 변환 / ''제거) 및 이번 round 가수 랜덤으로 정하기----------------------
    #컴퓨터 전체 데이터 전처리
    for i in range(len(computerDataList)):
        for j in range(len(computerDataList[i])):
            computerDataList[i][j] = computerDataList[i][j].replace(" ", "")
            computerDataList[i][j] = computerDataList[i][j].lower()
            computerDataList[i][j] = computerDataList[i][j][1:-1]

    #['블랙핑크', '르세라핌', '뉴진스', '아이브', '데이식스'] 랜덤으로 접근
    round = random.randint(0,4)

    #컴퓨터가 이번 판에서 사용하는 데이터
    computerData = computerDataList[round]
    #이번 판에서 사용하는 가수 이름
    roundSinger = singerData[round] 

    #정답지 전처리
    for i in range(len(answerList[round])):
        answerList[round][i] = answerList[round][i].replace(" ", "")
        answerList[round][i] = answerList[round][i].lower()
        answerList[round][i] = answerList[round][i][1:-1]

    #---------------------------------------------------게임 시작---------------------------------------------------
    print("💿 레코드 레코드 잉잉잉! 레코드 레코드 잉잉잉! 💿\n")
    print('💗 {}💗의 노래 제목을 말해주세요!👯 다른 가수의 노래를 말하거나 중복되면 그대 눈동자에 cheers..⭐️\n\n'.format(roundSinger))

    #중복방지
    overlapList = []
    recordGameEnd = False
    while not recordGameEnd :
        #유저
        userAnswer = input('👤 {}님 차례입니다! {}의 노래 제목을 입력해주세요! :'.format(self.userName, roundSinger))
        #유저 입력값 전처리
        userAnswer = userAnswer.replace(" ", "")
        userAnswer = userAnswer.lower()

        if userAnswer not in answerList[round]:
            print("❌ {}의 노래제목이 아닙니다! \n누가 술을 마셔~🍺 {}가 술을 마셔!🍻 \n".format(roundSinger, self.userName))
            self.lastLoser = self.userName
            break
        elif userAnswer in overlapList:
            print("🤪 다른 플레이어가 이미 말한 제목입니다! \n동구 밭~🎵 과수원 샷~샷~샷샷샷! 🧚🏻‍♀️{}🧚🏻‍♀️ 원샷!\n".format(self.userName))
            self.lastLoser = self.userName
            break
        else:
            print("🎊 정답입니다 🎊 \n")
            overlapList.append(userAnswer)

        #컴퓨터 self.playerList[1:]
        for turnPlayer in self.playerList[1:]:
          #인덱스 에러 예외처리
          try:
              computerPick = random.randint(1,12)    
              coumputerAnswer = computerData[computerPick-1] 
          except IndexError as e:
              computerPick = random.randint(1,12)    
              coumputerAnswer = computerData[computerPick-1] 

          print('🖥  {}님이 | {} | 를 말했습니다!\n'.format(turnPlayer, coumputerAnswer))
          sleep(1)
          if coumputerAnswer not in answerList[round]:
              print("❌ {}의 노래제목이 아닙니다! \n누가 술을 마셔~🍺 {}(이)가 술을 마셔!🍻 \n".format(roundSinger, turnPlayer))
              self.lastLoser = turnPlayer
              recordGameEnd = True
              break
          elif coumputerAnswer in overlapList:
              print("🤪 다른 플레이어가 이미 말한 제목입니다! \n동구 밖~🎵 과수원 샷~샷~샷샷샷! 🧟{}🧟 원샷!\n".format(turnPlayer))
              self.lastLoser = turnPlayer
              recordGameEnd = True
              break
          else:
              # print("🎊 정답입니다 🎊\n")
              overlapList.append(coumputerAnswer)
    
    
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
  print("                                                     🍺 5. 레코드 게임                                              ") # 이름 추후 수정
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

