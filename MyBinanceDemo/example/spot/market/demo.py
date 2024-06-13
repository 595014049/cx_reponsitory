from pbinance import Binance
from pprint import pprint
import datetime
##https://www.zhihu.com/people/pyted


def format_time(lst):
    lst = [datetime.datetime.fromtimestamp(int(lst[0] / 1000)).strftime("%Y-%m-%d %H:%M:%S")] + lst[1:]
    return lst


if __name__ == '__main__':
    # 实例化Binance
    # 如果仅获取行情信息不需要key和secret，与账户交易相关的功能需要填写key和secret
    binance = Binance(
        key='zWgyAe75Bic1wHhjARAn2gZfgWa8ss5dnSk24bcTqJt1RPuyLf9xcyaN3ZpMsJy4',
        secret='zM8yYsZQj6woXAVkWKISDNvu6k3nARMKSFu3QSb6v8mHPZOryYeN9EcrrX1TFLRW',
    )
    # spot表示现货 get_ticker_bookTicker获取最优挂单价格
    result = binance.spot.market.get_klines(
        symbol='FLOKIUSDT',
        interval='1h'
    )
    print(result.get('data'))
    result = [format_time(item) for item in result.get('data')]
    pprint(result)