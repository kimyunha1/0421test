import matplotlib.pyplot as plt

# 1. 데이터 설정
x_days = [1, 2, 3, 4, 5]
y_temp = [20, 22, 25, 23, 26] # 오류 포인트 1

# 2. 그래프 그리기
plt.plot(x_days, y_temp, marker='o', color='b')

# 3. 그래프 설정
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (C)")

# 4. 출력
print("그래프를 생성합니다...")
# 오류 포인트 2

plt.show()

# 5. 잘못된 함수 호출
plt.savefig("my_graph.png") # 오류 포인트 3