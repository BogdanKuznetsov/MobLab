import pandas as pd


df1 = pd.read_csv("data.csv")

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

print(f'{SumIncoming} - плата за входящие звонки клиента')
print(f'{SumOutcoming} - плата за исходящие звонки клиента')
print(f'{Sms} - плата за СМС')
print(f'Итого к олате: {Sms + SumOutcoming + SumIncoming}')



		

		
		