# ******************************************************************************************
# FileName     : 03._uart_multi_sensors.py
# Description  : 빨간색 LED가 깜박이면서 VR(A0), CDS(A1), Temp(A2) 값을 시리얼포트로 보낸다
# Author       : 손철수
# Created Date : 2023.07.26
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
sensor1 = ADC(Pin(A0))                # 가변저항 핀 지정
sensor2 = ADC(Pin(A1))                # 가변저항 핀 지정
sensor3 = ADC(Pin(A2))                # 가변저항 핀 지정

# setup
def setup():    
    led_red.init(Pin.OUT)             # D2를 LED 출력모드 설정
    uart.init(baudrate=115200,        # 시리얼 통신 속도 지정
              tx=1, rx=3)             # 이티보드 통신 핀 번호 지정
    sensor1.atten(ADC.ATTN_11DB)      # 가변저항 입력 모드 설정
    sensor2.atten(ADC.ATTN_11DB)      # 조도센서 입력 모드 설정
    sensor3.atten(ADC.ATTN_11DB)      # 온도센서 입력 모드 설정


# main loop
def loop():
    led_red.value(HIGH)               # 빨강 LED 켜기
    time.sleep(0.5)                   # 0.5초 기다리기

    led_red.value(LOW)                # 빨강 LED 끄기
    time.sleep(0.5)                   # 0.5초 기다리기
    
    sensor_result1 = sensor1.read()   # 가변저항 값 읽기
    sensor_result2 = sensor2.read()   # 조도센서 값 읽기
    sensor_result3 = sensor3.read()   # 온도센서 값 읽기    
    uart.write(str(sensor_result1)+','+
               str(sensor_result2)+','+
               str(sensor_result3))   # 시리얼 포트로 메시지 보내기
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