# loading some libs
import numpy as np
import matplotlib.pyplot as plt

PI2 = 2 * 3.1415926
samplerates = 16000	# 音频采样率
freq		= 800	# 音频物理频率
offset		= 0		# 音频初始相位
amp			= 1.0	# 音频幅度
duration	= 1.0   # 音频持续时间 s


n = round(duration * samplerates)
peroid = duration / freq     # 1 peroid time
ts = np.arange(0,peroid,peroid/200)
phases = PI2 * freq * ts + offset  # 2*PI*ft + x
phases1 = PI2 * freq * ts + offset + 0.5  # 2*PI*ft + x
y = amp * np.sin(phases)
y1 = amp * np.sin(phases1)


# draw your audio waves
# setting size for your picture
fig = plt.figure(figsize=(10, 10))

# total 2*1 = 2 sub picture
# pic1 is the first one
# pic2 is the second one
pic1 = fig.add_subplot(2,1,1)
pic2 = fig.add_subplot(2,1,2)

# pic1
pic1.scatter(ts*500, y, color='red')
pic1.set_xlabel('time*500')
pic1.set_ylabel('vol')

# pic2
pic2.scatter(ts*500,y1, color='g', linestyle='--')

plt.show()

plt.close()



