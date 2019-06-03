#!/usr/bin/env python
# -*- coding: utf-8 -*-
#**********************************************************************
#                     -Yüklenecek Kütüphaneler-
#**********************************************************************
import serial
from time import sleep, time
import numpy as np

#**********************************************************************
#               -Port Ayarları Ve Sabit Tamınlamalar-
#**********************************************************************
port = '/dev/ttyUSB0'
baud = 115200
lastime = 0
timeout = 10
SagToplamAlınan     = np.uint16(0)
SolToplamAlınan     = np.uint16(0)
ToplamDataAlınan    = np.uint32(0)
SagOnMesafeOkunan   = np.uint8(0)
SagArkaMesafeOkunan = np.uint8(0)
SolOnMesafeOkunan   = np.uint8(0)
SolArkaMesafeOkunan = np.uint8(0)
#********************************************************************
#       -Serial Port Açıldı Ve Zaman Asımı AYarlandı -
#********************************************************************
SerialOkunan = np.uint32(0)
ser = serial.Serial(port=port, baudrate=baud)
ser.timeout(1)
sleep(0.2)
#********************************************************************
#-Bu Fonksiyon Serialden Gelen 32bit Veriyi 8Bit Parcalara Ayırır   -
#********************************************************************
def Parcala(Okunan):
    ToplamDataAlınan =Okunan
    SolToplamAlınan     =  (ToplamDataAlınan) & 0xFFFF
    SagToplamAlınan     =  (ToplamDataAlınan >> 16) & 0xFFFF
    SagArkaMesafeOkunan =  (SagToplamAlınan)& 0xFF
    SagOnMesafeOkunan   =  (SagToplamAlınan >> 8) & 0xFF
    SolArkaMesafeOkunan =  (SolToplamAlınan)& 0xFF
    SolOnMesafeOkunan   =  (SolToplamAlınan >> 8) & 0xFF
    print("---------------------------------------")
    print("<#####################################>")
    print("---------------------------------------")

    print("Alıcı ToplamData",      ToplamDataAlınan)
    print("Alıcı SagToplamAlınan", SagToplamAlınan)
    print("Alıcı SolToplamAlınan", SolToplamAlınan)

    print("---------------------------------------")

    print("SagOnMesafeOkunan",   SagOnMesafeOkunan )
    print("SagArkaMesafeOkunan", SagArkaMesafeOkunan)
    print("SolOnMesafeOkunan",   SolOnMesafeOkunan)
    print("SolArkaMesafeOkunan", SolArkaMesafeOkunan)

    print("---------------------------------------")
    print("<#####################################>")
    print("---------------------------------------")


while true:
    OkunanSensor = ser.readline()
    print("Gelen Ham Veri ",OkunanSensor)
    print("---------------------------------------")
    print("-Parcalara Ayrılmıs Veriler -")
    print("---------------------------------------")
    Parcala(OkunanSensor)
    sleep(0.02)
