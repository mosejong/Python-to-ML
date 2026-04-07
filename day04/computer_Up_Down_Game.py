
chance = 10
regame = True

while regame :

    min_num = 1
    max_num = 100
    count = 1

    while count <= chance :

        guess = (min_num + max_num) // 2
        print(f'컴퓨터의 {count}회차 추측 : {guess}')

        result = input('Up / Down / 정답 : ').lower()

        if result not in ['up', 'down', '정답']:
            print('다시 입력하세요.')
            continue

        if result == 'up':
            min_num = guess + 1

        elif result == 'down':
            max_num = guess - 1

        else :
            print(f'{count}회차 : 정답')
            break
        
        if min_num > max_num:
            print('입력이 모순됩니다. 다시 생각해보세요.')
            break

        if count != chance:
            print(f'남은 기회는 {chance-count}번 입니다.')

        count += 1

    while True:
        ans = input('재시작 하시겠습니까? (Y/N) ').lower()

        if ans == 'y':
            regame = True
            break
        elif ans == 'n':
            regame = False
            break
        else:
            print('다시 입력하세요')