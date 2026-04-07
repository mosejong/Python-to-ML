from chatbot_logic import EmotionChatbot

"""
==========================================================================
[ 프로젝트명: 갈문왕(Gal-Mun-Wang) 감성 케어 챗봇 ]
--------------------------------------------------------------------------
■ 제작자: 모세종 (Mosejong)
■ 탄생 배경 (The Genesis):
  - NLP 학습 중 Word2Vec은 제작자의 이름을 외면하였으나,
  - fastText 모델이 '모세종'이라는 단어를 낱낱이 쪼개어 분석한 결과,
  - 신라 시대의 왕호인 '갈문왕(葛文王)'과 가장 유사하다는 신탁(?)을 내림.
  - 이에 감명받은 제작자는 본인의 페르소나를 '갈문왕'으로 확정하고,
  - 145,954개의 백성(데이터)의 마음을 어루만지는 챗봇 제국을 건설함.
==========================================================================
"""

# 1. 엔진 가동
bot = EmotionChatbot('chat_data_premium.pkl')

print("\n" + "="*50)
print("       ✨ 갈문왕의 감성 케어 챗봇 엔진 가동 ✨")
print("="*50)

# 2. 페르소나 설정 (데이터셋의 '남성', '여성' 규격에 맞게!)
print("\n비서: 대화 시작 전, 갈문왕님의 정보를 낱낱이 알려주소서.")
user_gender = input("성별 (남성/여성): ").strip()
user_age = input("연령대 (청소년/청년/중년/노년): ").strip()

print(f"\n비서: 확인되었습니다. {user_age} {user_gender} 모드로 최적화합니다.")
print("비서: 대화를 마치시려면 '종료'라고 말씀해 주십시오.\n")

# 3. 대화 루프
while True:
    user_text = input("나: ").strip()
    
    # [종료 로직] 강제 종료 대신 우아한 퇴장!
    if user_text == '종료':
        print("\n" + "-"*50)
        print("비서: 오늘 대화도 즐거웠습니다. 평안한 밤 되소서, 갈문왕님! 👑")
        print("-"*50)
        break
    
    # 챗봇 답변 생성
    response, score = bot.get_answer(user_text, user_gender, user_age)
    
    if score == 0:
        print(f"갈문왕 챗봇: {response}")
    else:
        print(f"갈문왕 챗봇: {response['답변']}")
        # 분석 정보는 살짝 들여쓰기해서 가독성 높이기!
        print(f"   └ [감정: {response['감정_대분류']} / 키워드: {response['상황키워드']} / 유사도: {score:.2f}]")