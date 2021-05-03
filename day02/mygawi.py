import random

mine = input("가위/바위/보를 선택하세요")
com = ""
result = ""

rand = random.random()

if rand < 0.3:
    com = "가위"
elif 0.3 < rand < 0.6:
    com  = "바위"
else: 
    com = "보"
    
if mine == com:
    result = "비김"
elif mine == "가위" and com == "보" :
    result = "승리"
elif mine == "가위" and com == "바위" :
    result = "패배"  
elif mine == "보" and com == "가위" :
    result = "패배"
elif mine == "보" and com == "바위" :
    result = "승리"
elif mine == "바위" and com == "가위" :
    result = "승리"
elif mine == "바위" and com == "보" :
    result = "패배"
else :
    result = "뭔가 이상"
    
print("com:",com)
print("mine:",mine)
print("result:",result)

        
