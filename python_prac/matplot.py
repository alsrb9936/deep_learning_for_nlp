import matplotlib.pyplot as plt

# matplot 그래프 그리기
plt.title('test')
plt.plot([1,2,3,4,5],[20,40,60,80,100])
plt.show()


# x,y 축 레이블 넣기
plt.title('test2')
plt.plot([1,2,3,4],[2,4,8,6])
plt.xlabel('hours')
plt.ylabel('score')
plt.show() 

# 그래프 라인 추가
plt.title('students')
plt.plot([1,2,3,4],[2,4,8,6])
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10]) # 라인 새로 추가
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student']) # 범례 삽입
plt.show()