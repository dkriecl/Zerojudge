correct=int(input())
score=0
if correct<=10:
    score=correct*6
elif correct>10 and correct<=20 :
    score=60+((correct-10)*2)
elif correct>20 and correct<=40:
    score=80+((correct-20)*1)
elif correct >= 40:
    score=100
elif correct==0:
    score=0
    
print(score)