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
y = amp * np.sin(phases)


# draw your audio waves


plt.plot(ts,y)
plt.show()



