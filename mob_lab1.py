import pandas as pd
from pd import read_csv

df1 = read_csv("data.csv")

NumberTel = 933156729
KIn = 0 #коэф. входящих
KOut = 2 #коэф. исходящих
KSms = 1 #коэф. смс
F = 10 # количество бесплатных сообщений


def CallBill(T, K):
	return (T*K)

def SmsBill(N, KSms, F):
	return ((N-F)*KSms)

Incoming = CallBill(df1[df1.msisdn_dest == NumberTel].call_duration.values, KIn)
SumIncoming = 0
for i in Incoming:
	SumIncoming += Incoming

Outcoming = CallBill(df1[df1.msisdn_origin == NumberTel].call_duration.values, KOut)
SumOutcoming = 0
for i in Outcoming:
	SumOutcoming += Outcoming	
	
Sms = SmsBill(df1[df1.msisdn_origin == NumberTel].sms_number.values, KSms, F)

print(SumIncoming)
print(SumOutcoming)
print(Sms)



		

		
		