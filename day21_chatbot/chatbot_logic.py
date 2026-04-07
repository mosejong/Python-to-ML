import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class EmotionChatbot:
    def __init__(self, data_path, model_name='jhgan/ko-sroberta-multitask'):
        # 1. 전처리된 피클 파일 로드
        print("전처리된 보물 지도를 읽어오는 중...")
        self.df = pd.read_pickle(data_path)
        
        # 2. Sroberta 모델 로드
        self.model = SentenceTransformer(model_name)
        
        # 3. 빠른 계산을 위해 리스트 형태의 임베딩을 넘파이 행렬로 변환
        self.embedding_matrix = np.array(self.df['embedding'].tolist())
        print("챗봇 엔진 가동 준비 완료! 👑")

    def get_answer(self, user_input, user_gender, user_age):
        # [STEP 1] 사용자 질문을 벡터로 변환
        user_embedding = self.model.encode([user_input])
        
        # [STEP 2] 모든 질문 벡터와 코사인 유사도 계산
        # (1, 768)과 (N, 768)을 비교해서 (1, N) 형태의 결과가 나옴
        similarities = cosine_similarity(user_embedding, self.embedding_matrix)[0]

        # [STEP 2.5] ⭐ 갈문왕의 '회심의 튜닝' (가중치 부여) ⭐
        # 반복문을 돌면서 사용자와 성별/연령이 일치하면 점수를 올려줍니다.
        for i in range(len(self.df)):
            if self.df.iloc[i]['성별'] == user_gender:
                similarities[i] += 0.05 # 성별 일치 보너스!
            if self.df.iloc[i]['연령'] == user_age:
                similarities[i] += 0.05 # 연령대 일치 보너스!

        # [STEP 3] 가중치가 반영된 점수 중 가장 높은 인덱스 찾기
        best_idx = np.argmax(similarities)
        max_sim = similarities[best_idx] # 가중치 반영된 최종 점수

        # [STEP 4] 결과물 추출 (질문, 답변, 감정 등)
        result = self.df.iloc[best_idx]
        
        # 유사도(신뢰도)가 너무 낮으면 예외 처리
        if max_sim < 0.4:
            return "짐이 그 말은 이해하기 어렵구나. 조금 더 자세히 말해주겠느냐?", 0
        
        return result, max_sim
    

# 테스트용 코드 (나중에 main.py에서 쓸 부분)
#bot = EmotionChatbot('chat_data_premium.pkl')
#answer, score = bot.get_answer("나 오늘 너무 힘들어")