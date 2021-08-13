import matplotlib.pyplot as plt # 그림 그리기 스킬

'''figure = plt.figure() # 그림 한 개 넣기
axes = figure.add_subplot(1,1,1)
plt.show()


figure = plt.figure() # 그림 두 개 넣기
axes1 = figure.add_subplot(1,2,1)
axes2 = figure.add_subplot(1,2,2)
plt.show()


figure = plt.figure() # 꺾은선 그래프 그리기
axes = figure.add_subplot(1,1,1)
x = [0,1,2,3,4]
y = [4,1,3,5,2]
axes.plot(x,y)
plt.show()


figure = plt.figure() # 두 개의 꺾은선 그래프
axes3 = figure.add_subplot(1,1,1)
x1 = [0,1,2,3,4]
y1 = [4,1,3,5,2]
x2 = [0,1,2,3,4]
y2 = [0,8,5,3,1]
axes3.plot(x1,y1)
axes3.plot(x2,y2)
plt.show()


figure = plt.figure() # 꺾은선 그래프와 화살표그래프
axes = figure.add_subplot(1,1,1)
axes.plot([0,1,2,3,4],[0,3,0,3,0],linestyle = 'dotted',linewidth = 5.0)
axes.plot([0,1,2,3,4],[1,2,3,6,5],color='r',marker ='v')
plt.show()'''

from matplotlib import font_manager,rc # 그래프에 한국어 폰트 넣기
figure = plt.figure()
import matplotlib
font_path='C://Windows/Fonts/malgun.ttf'
font_name=font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)
plt.plot(['봄','여름','가을','겨울'],[20.5,30.5,15.5,1.5])
plt.show()