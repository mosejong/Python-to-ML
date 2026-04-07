import pandas as pd
from sentence_transformers import SentenceTransformer

# 1. 모델과 데이터 로드
model = SentenceTransformer('jhgan/ko-sroberta-multitask')
df = pd.read_excel('감성대화말뭉치(최종데이터)_Training.xlsx')

# 2. 공통적으로 가져갈 '꿀정보' 컬럼들 정의
# 신체질환이랑 감정 소분류까지 싹 챙겨야지!
meta_cols = ['연령', '성별', '상황키워드', '신체질환', '감정_대분류', '감정_소분류']

# 3. 1, 2, 3턴 데이터를 각각 정성스럽게 추출 (공통 정보 포함)
df1 = df[meta_cols + ['사람문장1', '시스템문장1']].rename(columns={'사람문장1': '질문', '시스템문장1': '답변'})
df2 = df[meta_cols + ['사람문장2', '시스템문장2']].rename(columns={'사람문장2': '질문', '시스템문장2': '답변'})
df3 = df[meta_cols + ['사람문장3', '시스템문장3']].rename(columns={'사람문장3': '질문', '시스템문장3': '답변'})

# 4. 수직으로 합체! (이제 모든 정보가 '질문/답변' 옆에 살아있다!)
total_df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)

# 5. 빈칸(NaN) 날리기 (대화가 3단까지 안 간 경우 등)
total_df = total_df.dropna(subset=['질문', '답변']).reset_index(drop=True)

print(total_df.shape)

# 6. 임베딩 작업 (시간이 좀 걸리니 인내심을 갖고!)
print(f"총 {len(total_df)}개의 고퀄리티 데이터를 임베딩합니다... 짐의 챗봇이 똑똑해지는 중!")
total_df['embedding'] = model.encode(total_df['질문'].tolist()).tolist()

# 7. 내일 아침의 쾌적함을 위해 피클 저장
total_df.to_pickle('chat_data_premium.pkl')
print("전처리 끝! 이제 퇴근 가즈아!")
