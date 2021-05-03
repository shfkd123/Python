print("======== 문제 01 ========")
first_num = int(input("첫번째 숫자를 입력하세요"))
second_num = int(input("두번째 숫자를 입력하세요"))
sum = first_num + second_num
print("숫자의 합은 ", sum ,"입니다.")

print("======== 문제 02 ========")
fn = int(input("첫번째 숫자를 입력하세요"))
sn = int(input("두번째 숫자를 입력하세요"))

sum = 0
for fn in range(fn, sn+1):
    sum += fn
print("모든 수의 합 : ", sum)
#print("모든 수의 합은 {} 입니다.", format(sum))

print("======== 문제 03 ========")
gugudan = int(input("몇단을 출력할까요? : "))
for i in range(1, 10):
    print(gugudan ,"* " + str(i) , "= " + str(gugudan*(i)))

print("======== 문제 04 ========")
s = 0
n1 = int(input("첫번째 숫자를 입력하세요"))
n2 = int(input("두번째 숫자를 입력하세요"))
for n1 in range(n1, n2+1):
    if(n1 % 2 == 0):
        s += n1
print("짝수의 합은 " , s)
        
print("======== 문제 05 ========")
s = 0
n1 = int(input("첫번째 숫자를 입력하세요"))
n2 = int(input("두번째 숫자를 입력하세요"))
for n1 in range(n1, n2+1):
    if(n1 % 2 == 1):
        s += n1
print("홀수의 합은 " , s)