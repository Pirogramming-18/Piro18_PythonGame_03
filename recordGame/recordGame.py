#컴퓨터 정답 데이터 길이 15
#정답 비율 70% / 오답 비율 30%

import pandas as pd
import random
data = pd.read_csv('./recordGameData.csv') #경로 나중 변경
data = data[['singer', 'song']]
blackpink = []
lesserafim = []
newjeans = []
ive = []
day6 = []

singerData = ['블랙핑크', '르세라핌', '뉴진스', '아이브', '데이식스']
computerDataList = []
answerList = []

#데이터 설정 pandas 모듈 사용
for singer in singerData:
    data_answer = data.loc[data['singer'] == singer, :]
    tmpAnswerList = data_answer['song'].values.tolist()
    answerList.append(tmpAnswerList)
    data_answer = data_answer.sample(frac=1).reset_index(drop=True)

    data_wrong = data.loc[data['singer'] != singer, :]
    data_wrong = data_wrong.sample(frac=1).reset_index(drop=True)

    data_answer = data_answer[:9]
    data_wrong = data_wrong[:3]

    computerEachData = pd.concat([data_answer,data_wrong])
    computerEachData = computerEachData.sample(frac=1).reset_index(drop=True)

    computerDataList.append(computerEachData['song'].values.tolist())


gameCount = 0

print("💿 레코드 레코드 잉잉잉! 레코드 레코드 잉잉잉! 💿\n")

#컴퓨터가 사용하는 전체 데이터 전처리
for i in range(len(computerDataList)):
    for j in range(len(computerDataList[i])):
        computerDataList[i][j] = computerDataList[i][j].replace(" ", "")
        computerDataList[i][j] = computerDataList[i][j].lower()
        computerDataList[i][j] = computerDataList[i][j][1:-1]

######
round = random.randint(0,4)

computerData = computerDataList[round] #컴퓨터가 이번 판에서 사용하는 데이터
roundSinger = singerData[round] #이번 판에서 사용하는 가수 이름

#정답지 전처리
for i in range(len(answerList[round])):
    answerList[round][i] = answerList[round][i].replace(" ", "")
    answerList[round][i] = answerList[round][i].lower()
    answerList[round][i] = answerList[round][i][1:-1]

#중복방지
overlapList = []

# 유저네임에 클래스 변수 넣기
while True :
    #유저
    userAnswer = input('👤 유저네임 차례입니다! {}의 노래 제목을 입력해주세요! :'.format(roundSinger))
    userAnswer = userAnswer.replace(" ", "")
    userAnswer = userAnswer.lower()
    if userAnswer not in answerList[round]:
        print("❌ {}의 노래제목이 아닙니다! \n탈락입니다! \n".format(roundSinger))
        break
    elif userAnswer in overlapList:
        print("🤪 다른 플레이어가 이미 말한 제목입니다! \n탈락입니다! \n")
        break
    else:
        print("🎊🎊🎊🎊 정답입니다 🎊🎊🎊🎊 \n")
        overlapList.append(userAnswer)

    #컴퓨터
    computerPick = random.randint(0,11)    
    coumputerAnswer = computerData[computerPick] 
    print('🖥  컴퓨터가 {}를 말했습니다!'.format(coumputerAnswer))
    if coumputerAnswer not in answerList[round]:
        print("❌ {}의 노래제목이 아닙니다! \n탈락입니다! \n".format(roundSinger))
        break
    elif coumputerAnswer in overlapList:
        print("🤪 다른 플레이어가 이미 말한 제목입니다! \n탈락입니다! \n")
        break
    else:
        print("🎊🎊🎊🎊 정답입니다 🎊🎊🎊🎊\n")
        overlapList.append(coumputerAnswer)

