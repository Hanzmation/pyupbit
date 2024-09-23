# 주봉
import myupbit

# 기본 요청시 200개
df = myupbit.get_ohlcv("KRW-BTC", "week")
print(df)
