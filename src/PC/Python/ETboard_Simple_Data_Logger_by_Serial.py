# ******************************************************************************************
# FileName     : ETboard_Simple_Data_Logger.py
# Description  : 이티보드로 수신한 데이터를 CSV 파일로 저장하기
# Author       : 손철수
# Created Date : 2023.06.12
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time                             # 시간 모듈 가져오기
import serial                           # 시리얼 통신 모듈 가져오기

# global variable
com_port = 'COM6'                       # 시리얼 포트 번호
ser = serial.Serial()                   # 시리얼 포트
string_line = ''                        # 수신 메시지 버퍼


# setup
def setup():
    global ser, com_port
    ser.baudrate = 115200               # 이티보드 시리얼 통신 속도 115,200
    ser.port = com_port                 # 시리얼 통신 포트 번호 지정
    ser.open()                          # 시리얼 통신 포트 열기
    

# main
def loop():
    read_etboard()                      # 이티보드로 부터 데이터 읽기
    write_csv()                         # 읽은 데이터를 CSV로 저장
    time.sleep(0.1)                     # 0.1초 기다리기


# read_etboard
def read_etboard():
    global string_line
    byte_line = ser.readline()          # 시리얼 통신 포트에서 메시지 읽기 / 바이트 스트링 형태
    string_line = byte_line.decode('utf-8')     # utf-8 형식의 문자 형식으로 변환
    string_line = string_line.rstrip()          # 문자열 끝에 개행 문자('\n')같은 것 제거
    print(string_line)                  # 메시지를 화면에 출력하기


# wrtie_csv
def write_csv():
    global string_line
    file = open('data.csv', 'a', newline='')    #
    file.write(string_line)
    file.write('\n')
    file.close()


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
