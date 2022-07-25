import pandas as pd
sr = pd.Series([17000,18000,1000,5000],
                index=["피자","치킨","콜라","맥주"])
print(sr)
print('\n시리즈 값: {}'.format(sr.values))
print('시리즈 인덱스: {}'.format(sr.index))

values = [[1,2,3],[4,5,6],[7,8,9]]
index = ["A","B","C"]
columns = [1,2,3]

df = pd.DataFrame(values,index,columns)
print(df)

print("\n데이터 프레임 인덱스: {}".format(df.index))
print("데이터 프레임 컬럼: {}".format(df.columns))
print("데이터 프레임 값: '\n{}".format(df.values))

# 리스트로 데이터 프레임 생성
data = [
    ['1000', 'Steve', 90.72], 
    ['1001', 'James', 78.09], 
    ['1002', 'Doyeon', 98.43], 
    ['1003', 'Jane', 64.19], 
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]

df = pd.DataFrame(data)
print(df)

# 컬럼 추가
df = pd.DataFrame(data,columns=['학번','이름','점수'])
print(df)

# 딕셔너리로 생성
data = {
    '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
    }

df = pd.DataFrame(data)
print(df)

# 데이터 프레임 조회

# .head(3) 앞부분 3줄 조회
print(df.head(3))
 
# .tail(3) 뒷부분 3줄 조회
print(df.tail(3))

# pd(['학번']) 학번만 출력
print(df['학번'])