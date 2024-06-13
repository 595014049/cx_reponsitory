#!/usr/bin/env python
import warnings
import logging
from pandas.errors import SettingWithCopyWarning
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
import pandas as pd
import numpy as np
import datetime
import mplfinance as mpf
import time





def format_time(lst):
    lst = [int(lst[0] / 1000)] + lst[1:5]
    return lst
##start代表最新的一根k线
##length代表要检查的长度
def get_low_position(df, start, end):
    end=end if end <= len(df)+1 else len(df)+1
    new_df = df.iloc[len(df) - end+1:len(df) - start + 1]

    flag_support = False
    flag_pressure = False
    alines = []
    #注意这里是先左边的往中间走，右边的不动，然后确定好了两端，下次就不用遍历这块，节省时间（1）
    for j in range(len(new_df)):
        ##如果找到了，就不要在在这个区间里面找了
        if flag_support and flag_pressure:
            break
        # 先确认是否在走过的区间内
        # 只计算最近X根为起点的支撑线和压力线
        if j >= 100:
            break
        for i in range(len(new_df)):
            ##如果找到了，就不要在在这个区间里面找了
            if flag_support and flag_pressure:
                print('全部查完')
                break
            #两端相内走，不能相撞
            if i + j >= len(new_df) - 2:
                continue
            i_index = new_df.index[i]
            i_row = new_df.iloc[i]['row']
            j_index = new_df.index[len(new_df) - j - 1]
            j_row = new_df.iloc[len(new_df) - j - 1]['row']
            if not flag_support:
                print('flag_support')
                i_low = new_df.iloc[i]['low']
                j_low = new_df.iloc[len(new_df) - j - 1]['low']
                # 判断是否是支撑线,右上角的,如果不是,走人
                if j_low > i_low:
                    slope_low = (j_low - i_low) / (j_row - i_row)
                    # 比较斜率，计算比较顽皮的K线
                    new_df_part_support = new_df.iloc[i + 1:len(new_df) - j - 1, :]
                    overflow_count_support = len(new_df_part_support[(new_df_part_support['low'] - i_low) / (new_df_part_support['row'] - i_row) < slope_low])
                    print(overflow_count_support)
                    if overflow_count_support / len(new_df_part_support) == 0 and len(new_df_part_support) >= 30:
                        line = [(i_index, i_low), (j_index, j_low)]
                        alines.append(line)
                        flag_support = True
            if not flag_pressure:
                i_high = new_df.iloc[i]['high']
                j_high = new_df.iloc[len(new_df) - j - 1]['high']
                # 判断是否是压力线,右下角的,如果不是,走人
                if j_high < i_high:
                    slope_high = (j_high - i_high) / (j_row - i_row)
                    # 比较斜率，计算比较顽皮的K线
                    new_df_part_pressure = new_df.iloc[i + 1:len(new_df) - j - 1, :]
                    overflow_count_pressure = len(new_df_part_pressure[(new_df_part_pressure['high'] - i_high) / (new_df_part_pressure['row'] - i_row) > slope_high])
                    if overflow_count_pressure / len(new_df_part_pressure) == 0 and len(new_df_part_pressure) >= 30:
                        line = [(i_index, i_high), (j_index, j_high)]
                        alines.append(line)
                        flag_pressure = True
    return alines



# #print(result)


warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
##显示全部小数位10位
pd.set_option('display.precision', 10)
df = pd.read_csv('./data.csv')#.iloc[0:500]



#保留
# spot_client = Client(base_url="https://api.binance.com")
# data=spot_client.klines("FLOKIUSDT", "1h" , limit=300)
# result = [format_time(item) for item in data]
# df = pd.DataFrame(result, columns=['date', 'open','high','low','close'])
# df.to_csv('./data.csv', index=False)
#
df['row'] = range(1, len(df) + 1)
df['open'] = df['open'].astype(float)
df['high'] = df['high'].astype(float)
df['low'] = df['low'].astype(float)
df['close'] = df['close'].astype(float)

df.index = pd.DatetimeIndex(pd.to_datetime(df['date'], unit='s'))

#计算低位和低位相连，包括K线最多的
alines = get_low_position(df, 1, 500)
#print(df)
#print(df['low'])
print('这里')

# 添加移动平均线参数
addplot = [
    #保留
    #mpf.make_addplot(df[['low']].values, color="r", width=1.5),
]
# 蜡烛颜色
market_colors = mpf.make_marketcolors(up='green', down='red')
style = mpf.make_mpf_style(marketcolors=market_colors)
##绘制K线图
mpf.plot(df, type='candle',
         figratio=(20, 10),
         ##额外添加的线
         alines=alines,
         #也是均线
         #mav=(2,5,10),
         # 显示非交易日期
         # show_nontrading=True,
         addplot=addplot,
         style=style)
mpf.show()
