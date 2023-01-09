from random import randint

class StrawBerry():
    
    def __init__(self):
        self.player_list=['유민','건','서진','다은']
            
    def strawberry(self):

            print("🍓🍓🍓🍓🍓 딸기가 좋아 🍓 딸기가 좋아 🍓 좋아 좋아 좋아 좋아 좋아 좋아 🍓🍓🍓🍓",end="\n\n") 
            num = 1
            while(1):
                try:
                    for i in range(0,len(self.player_list)):
                            print(f"🍓이번 차례는 {self.player_list[i]} !",end="\n")          
                            cnt = randint(num,num+1)
                                                
                        
                            
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
                    

if __name__ == "__main__":
    game = StrawBerry()
    game.strawberry()