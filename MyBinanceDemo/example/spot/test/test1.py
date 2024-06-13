import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# 示例数据
data = pd.DataFrame({
    'Date': pd.date_range(start='2021-01-01', periods=10),
    'High': [100, 102, 105, 103, 107, 105, 108, 110, 112, 115],
    'Low': [95, 97, 98, 96, 99, 101, 103, 105, 107, 109]
})

# 绘制图表
fig, ax = plt.subplots()
ax.plot(data['Date'], data['High'], 'b-', label='High')
ax.plot(data['Date'], data['Low'], 'r-', label='Low')

# 绘制低点连线
for i in range(len(data) - 1):
    ax.plot([data['Date'][i], data['Date'][i + 1]], [data['Low'][i], data['Low'][i + 1]], 'g-')

ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('Stock Low Points Connected')

# 转换为mpld3图表
mpld3.enable_notebook()
mpld3.display()