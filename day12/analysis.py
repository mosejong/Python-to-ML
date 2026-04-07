import pandas as pd

# 데이터 불러오기
sales_df = pd.read_csv("data/파일명.csv", encoding="cp949")

# 커피-음료 업종 필터링
filtered_df = sales_df[
    sales_df['서비스_업종_코드_명'] == '커피-음료'
]

# 상권별 토요일 매출 합계
sum_df = filtered_df.groupby('상권_코드_명')['토요일_매출_금액'].sum().reset_index()
sum_df = sum_df.sort_values(by='토요일_매출_금액', ascending=False)

# 상권별 토요일 매출 평균
mean_df = filtered_df.groupby('상권_코드_명')['토요일_매출_금액'].mean().reset_index()
mean_df = mean_df.sort_values(by='토요일_매출_금액', ascending=False)

# 결과 출력
print("=== 토요일 매출 TOP 10 (총합) ===")
print(sum_df.head(10))

print("\n=== 토요일 매출 TOP 10 (평균) ===")
print(mean_df.head(10))