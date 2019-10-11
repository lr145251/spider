import random

from matplotlib import pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# plt.figure(figsize=(10, 10))
fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(20,8))



# 上海
x = range(60)
x_ch = ["11点{}分".format(i) for i in x]
y = [random.uniform(15, 18) for i in range(60)]
y_ticks = range(40)

# 北京
y_beijing = [random.uniform(1, 3) for i in range(60)]

# 绘图
# plt.plot(x, y,label = "上海")
# plt.plot(x,y_beijing,color = "r",linestyle= "--",label = "北京")
ax[0].plot(x, y,label = "上海")
ax[1].plot(x,y_beijing,color = "r",linestyle= "--",label = "北京")


# 处理fig
# plt.legend(loc="best")
ax[0].legend(loc="best")
ax[1].legend(loc="best")
# 更改坐标
ax[0].set_xticks(x[::5], x_ch[::5])
ax[0].set_yticks(y_ticks[::5])

ax[1].set_xticks(x[::5], x_ch[::5])
ax[1].set_yticks(y_ticks[::5])
# plt.xticks(x[::5], x_ch[::5])
# plt.yticks(y_ticks[::5])
# plt.title("中午11点0分到12点之间的温度变化图示")
ax[0].set_title("中午11点0分到12点之间的温度变化图示")
ax[1].set_title("中午11点0分到12点之间的温度变化图示")
# plt.xlabel("时间")
ax[0].set_xlabel("时间")
ax[1].set_xlabel("时间")
# plt.ylabel("温度")
ax[0].set_ylabel("温度")
ax[1].set_ylabel("温度")

plt.show()
