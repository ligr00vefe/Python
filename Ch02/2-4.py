"""
    날짜 : 2020/06/22
    이름 : 권기민
    내용 : 튜플 자료형 실습하기 교재 p85
"""

# 튜플 생성하기
tp1 = (1, 2, 3, 4, 5)
tp2 = 1, 2, 3, 4, 5
tp3 = '김유신', '김춘추', '장보고', '강감찬', '이순신'

# 튜플 원소 출력
print('tp1 : ', tp1)
print('tp2 : ', tp2)
print('tp2[1] : ', tp2[1])
print('tp2[4] : ', tp2[4])
print('tp3[0] : ', tp3[0])
print('tp3[4] : ', tp3[4])

# 튜플 원소 삭제 - 튜플은 정적 리스트이므로 원소 삭제를 할 수 없음
# del tp1[0]

# 튜플 원소 수정 - 튜플은 정적 리스트이므로 원소 수정을 할 수 없음
# tp2[0] = 7

# 교재 p86 ~ p87 실습하기