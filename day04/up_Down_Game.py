import random

min_num = 1         # 게임의 최솟값
max_num = 100       # 게임의 최댓값
chance = 10     # 게임 기회
regame = True


while regame :
    count = 1       # 게임 진행 횟수
    print('Up&Down_Game')
    print(f'{min_num}~{max_num}의 숫자중 랜덤한 숫자를 {chance}번 안에 맞춰야 합니다')
    answer = random.randint(min_num,max_num)    # 정답 설정
    while count <= chance :
        try :
            num = int(input('정답입력 : '))
        except ValueError :
            print('정수를 입력하세요.')
            continue
        if num > max_num or num < min_num :
            print(f'올바른 숫자를 입력하세요. {min_num} ~ {max_num}까지의 숫자')
            continue
        if num > answer :
            print(f'{count}회차 결과 : Down')
        elif num < answer :
            print(f'{count}회차 결과 : Up')
        else :
            print(f'{count}회차 결과 : 정답입니다.')
            break

        if count == chance :
            print(f'{chance} 기회를 모두 소진하였습니다.')
            print(f'정답은 {answer}였습니다.')
            break
        else :
            print(f'{chance-count}번 남았습니다.')
        count += 1
    while True:
        ans = input('재시작 하시겠습니까? (Y/N) ').lower()

        if ans == 'y':
            regame = True
            break
        elif ans == 'n':
            regame = False
            break
        else : print('다시 입력하세요')