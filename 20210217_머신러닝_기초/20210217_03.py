# 데이터로 그래프 그리기

import seaborn as sns
# 연습용 데이터와 가시화 툴을 제공하는 라이브러리
import matplotlib.pyplot as plt

# 그림 그려주는 라이브러리

# 샘플 데이터 가지고 오기
anscombe = sns.load_dataset("anscombe")
print(anscombe)

# I 인 데이터 가지고 오기
print(anscombe[anscombe['dataset'] == 'I'])

# dataset 별로 구분하기
data1 = anscombe[anscombe['dataset'] == "I"]
data2 = anscombe[anscombe['dataset'] == "II"]
data3 = anscombe[anscombe['dataset'] == "III"]
data4 = anscombe[anscombe['dataset'] == "IV"]

print(data1)
print(data2)
print(data3)
print(data4)

print(data1.std())  # 표준 편차
print(data2.std())
print(data3.std())
print(data4.std())

# 그래프 그리기
plt.plot(data1['x'], data1['y'])
# plt.show()

# 흰 도화지
fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.plot(data1['x'], data1['y'], 'o')
ax2.plot(data1['x'], data1['y'], 'o')
ax3.plot(data1['x'], data1['y'], 'o')
ax4.plot(data1['x'], data1['y'], 'o')

# 서브 플롯 이름정하기
ax1.set_title('Data1')
ax2.set_title('Data2')
ax3.set_title('Data3')
ax4.set_title('Data4')

# 도화지 이름정하기
fig.suptitle('Anscombe Data')

# 레이아웃 맞추기
fig.tight_layout()

fig.show()
