from random import*
playerList = ['홍길동','유재석','박지성']
userName = ['홍길동']

# 세명이 돌아야됨 -> 인덱스 0,1,2 -> 0,1,2
def udgame(lastLoser):
    up = 100
    down = 1
    index = playerList.index(lastLoser)
    if index == 0:
        while True:
            number = int(input("친구들이 맞출 숫자를 입력해주세요 : "))
            if number < 1 or number > 100:
                print("1부터 100까지의 수를 입력해주세요.")
            else:
                break
    else:
        number = randint(down, up) #난수 생성
        
    tries=0 #시도횟수
    n = 8 #기회 8번

    while tries < n: #시도횟수가 5번이 될때까지 반복
        try:
            player = playerList[index] # index번째
            if player == lastLoser:
                index += 1                
                if index == len(playerList):
                    index = 0
                continue
            else:
                if index == 0:
                    guess = int(input("숫자를 짐작하세요 : "))
                else:
                    guess = randint(down, up)
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
                    print ("정답!! 문제를 낸 사람이 벌주를 마십니다!")
                    return lastLoser
            
                if tries == n:
                    print ("정답은 {0}이었습니다!".format(number))
                    print ("기회를 다 썼습니다!! 못맞추신 분들 벌주 마시세요~~~")
                    lastLoser = playerList[1:]
                    return lastLoser
            
                index += 1                
                if index == len(playerList):
                    index = 0
                
        except Exception as e:
            print ("숫자를 입력하셔야합니다!!", e)
        

            
print(udgame('유재석'))
