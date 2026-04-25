"""
[가위바위보 게임]
- 사용자와 컴퓨터가 가위/바위/보 선택
- 승패를 판별하여 승리 횟수 누적
- 먼저 3승을 달성하면 게임 종료
"""


import random

list_a = {0: '가위', 1: '바위', 2: '보' }

def rsp_choice(who):                                                             # w : 매개변수
    rsp = None                                                        # 가위바위보
    if who == '회원님':                                                 # 사용자
        while True:
            rsp = input("가위, 바위, 보 중에 하나를 입력해 주세요: ")
            if rsp in ['가위', '바위', '보']:
                break
            print("사용자가 잘못 선택했어요")
    else:
        rsp = list_rsp[random.randint(0,2)]
    return rsp

def  referee(user_rsp,pc_rsp,win_number):        #승부결정(유저,컴퓨터,승리횟수)
    win = judge_rsp[user_rsp][pc_rsp]                 #사전 가위바위보 심판

    if win == 'user':
        win_number[win] = win_number[win] +  1
        print("{}가 승리했어요.({} 승리횟수: {})".format('회원님',('회원님'),win_number['user']))
    elif win == 'pc':
        win_number[win] = win_number[win] +  1
        print("{}가 승리했어요.({} 승리횟수: {})".format('컴퓨터',('컴퓨터'),win_number['pc']))
    else:                                                                #비길때
        print("이번판은 무승부예요")

    return win_number

win_count = {'user': 0, "pc": 0}                            # 승리횟수

list_rsp = {0: '가위', 1: '바위', 2: '보' }
judge_rsp = {
    '가위':{'가위': None, '바위': 'pc', '보': 'user'},
    '바위':{'가위': 'user', '바위': None, '보': 'pc'},
    '보':{'가위': 'pc', '바위': 'user', '보': None}
}

while True:
    #사용자의 가위바위보 선택
    user_rsp = rsp_choice('회원님')
    pc_rsp = rsp_choice('컴퓨터')

    #승부결정, 승 횟수 누적
    win_count = referee(user_rsp, pc_rsp, win_count) #승리횟수

    if win_count['user'] >= 3 or win_count['pc'] >= 3:
        break
