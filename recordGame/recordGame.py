def recordGame() :
    import pandas as pd
    import random

    #---------------------------------------------csv파일 읽어오기----------------------------------------------
    data = pd.read_csv('./recordGameData.csv') #경로 나중 변경
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

    while True :
        #유저
        userAnswer = input('👤 유저네임님 차례입니다! {}의 노래 제목을 입력해주세요! :'.format(roundSinger))
        #유저 입력값 전처리
        userAnswer = userAnswer.replace(" ", "")
        userAnswer = userAnswer.lower()

        if userAnswer not in answerList[round]:
            print("❌ {}의 노래제목이 아닙니다! \n누가 술을 마셔~🍺 유저네임(이)가 술을 마셔!🍻 \n".format(roundSinger))
            break
        elif userAnswer in overlapList:
            print("🤪 다른 플레이어가 이미 말한 제목입니다! \n동구 밭~🎵 과수원 샷~샷~샷샷샷!🧪 \n")
            break
        else:
            print("🎊 정답입니다 🎊 \n")
            overlapList.append(userAnswer)

        #컴퓨터
        computerPick = random.randint(0,11)    
        coumputerAnswer = computerData[computerPick] 
        print('🖥  컴퓨터가 | {} | 를 말했습니다!\n'.format(coumputerAnswer))
        if coumputerAnswer not in answerList[round]:
            print("❌ {}의 노래제목이 아닙니다! \n누가 술을 마셔~🍺 컴퓨터가 술을 마셔!🍻 \n".format(roundSinger))
            break
        elif coumputerAnswer in overlapList:
            print("🤪 다른 플레이어가 이미 말한 제목입니다! \n동구 밖~🎵 과수원 샷~샷~샷샷샷!🧪 \n")
            break
        else:
            # print("🎊🎊🎊🎊 정답입니다 🎊🎊🎊🎊\n")
            overlapList.append(coumputerAnswer)

recordGame()