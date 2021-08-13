'''import pybithumb
import time
while True :

    price = pybithumb.get_current_price("BTC")
    print(price)
    time.sleep(10) # 10초에 한 번씩 비트코인 값 출력'''