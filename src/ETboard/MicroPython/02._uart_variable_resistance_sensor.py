# ******************************************************************************************
# FileName     : 02._uart_variable_resistance_sensor.py
# Description  : 빨간색 LED가 깜박이면서 VR(A0) 값을 시리얼포트로 보낸다
# Author       : 손철수
# Created Date : 2023.06.12
# Reference    :
# Modified     : 
# ******************************************************************************************

# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *
from machine import UART

# global variable
led_red = Pin(D2)                     # 빨강 LED 핀 지정
uart = UART(1)                        # 시리얼 통신 포트 지정
sensor = ADC(Pin(A0))                 # 가변저항 핀 지정

# setup
def setup():    
    led_red.init(Pin.OUT)             # D2를 LED 출력모드 설정
    uart.init(baudrate=115200,        # 시리얼 통신 속도 지정
              tx=1, rx=3)             # 이티보드 통신 핀 번호 지정
    sensor.atten(ADC.ATTN_11DB)       # 가변저항 입력 모드 설정


# main loop
def loop():
    led_red.value(HIGH)               # 빨강 LED 켜기
    time.sleep(0.5)                   # 0.5초 기다리기

    led_red.value(LOW)                # 빨강 LED 끄기
    time.sleep(0.5)                   # 0.5초 기다리기
    
    sensor_result = sensor.read()     # 가변저항 센서 값 읽기    
    uart.write(str(sensor_result))    # 시리얼 포트로 메시지 보내기
    uart.write('\n')                  # 시리얼 포트로 구분자 문자 보내기


if __name__ == "__main__":
    setup()
    while True:
        loop()
        
        
# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================  