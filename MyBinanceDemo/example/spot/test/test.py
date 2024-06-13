#https://blog.csdn.net/daizikui/article/details/136160868
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

# plt.rcParams['font.family'] = ['SimHei']  # 设置中文字体
# plt.rcParams['axes.unicode_minus'] = False  # 设置负号显示

# 读取股票数据
df = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)
# 清洗数据
df['Close'] = df['Close'].astype(float)
df['Open'] = df['Open'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)

ma5 = df['MA5'] = df['Close'].rolling(5, min_periods=1).mean()
ma20 = df['MA20'] = df['Close'].rolling(20, min_periods=1).mean()
# 添加移动平均线参数
ap0 = [
    mpf.make_addplot(ma5, color="b", width=1.5),
    mpf.make_addplot(ma20, color="y", width=1.5),
]

market_colors = mpf.make_marketcolors(up='red', down='green', )

my_style = mpf.make_mpf_style(marketcolors=market_colors)
# 绘制K线图
mpf.plot(df, type='candle',
         figratio=(10, 4),
         mav=(10, 20),
         volume=True,
         # 显示非交易日期
         # show_nontrading=True,
         addplot=ap0,
         style=my_style)

mpf.show()