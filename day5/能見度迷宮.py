import random
class person():
    def __init__(self,man):
        self.man=man

    def ability(self):
        ability=0
        if ord(man)>=65 and ord(man)<=90:
            ability=91-ord(man)
        elif ord(man)>=97 and ord(man)<=122:
            ability=123-ord(man)
        return ability

class MeeGon():
    def __init__(self,lon):
        self.lon=lon

    def SanMeeGon(self):
        map=list("?"*lon)
        locate=random.randint(1,lon-2)
        print("loca=",locate)
        ran=0

        for i in range(person.ability(man)):
            if int(locate+person.ability(man)/2-i)>lon:
                ran=lon-1
            elif int(locate+person.ability(man)/2-i)<=0:
                ran=0
            else:
                ran=int(locate+person.ability(man)/2-i)-1
            print(ran)
            map[ran]="_"
        map[locate]="人"
        return map

class move():
    def __init__(self,walk,map,ability,r):
        self.walk=walk
        self.map=map
        self.ability=ability
        self.r=r

    def go(self):
        p=0
        for z in range(len(map)-1):
            if self.map[z] =="人":
                p=z

        if self.walk==1:
            for i in range(len(self.map)-1):
                self.map[i]=self.map[i+1]
            if len(self.map)-1-p>=self.ability/2-1:
                self.map[len(self.map)-1]="?"
            else:
                self.map[len(self.map)-1]="_"
            if p<=self.ability/2+1 and self.r==0:
                self.map[0]="*"
            if p==1 and r==0:
                self.map[0]="人"

        elif self.walk==2:
            for i in range(len(self.map)-1):
                j=len(self.map)-i-2
                self.map[j+1]=self.map[j]
            if p>=self.ability/2:
                self.map[0]="?"
            else:
                self.map[0]="_"
            if len(self.map)-1-p<=self.ability/2 and self.r==1:
                self.map[len(self.map)-1]="*"
            if p==len(self.map)-2 and self.r==1:
                self.map[len(self.map)-1]="人"

        return self.map
    

if __name__ == '__main__':
    man = str(input("人物:"))
    print("你的能見度是:",person.ability(man))
    lon = int(input("迷宮長度:"))
    print("遊戲開始!!!")
    map=MeeGon.SanMeeGon(lon)
    r=random.randint(0,1)
    if map[0]=="_" and r==0:
        map[0]="*"
    elif map[len(map)-1]=="_" and r==1:
        map[len(map)-1]="*"
    print(map)

    while True:
        map=move(int(input("往哪走?(1左2右):")),map,person.ability(man),r).go()
        print(map)
        if r==0:
            if map[len(map)-1]=="人":
                break
        elif r==1:
            if map[0]=="人":
                break
    print("you win!!")
