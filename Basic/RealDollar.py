#This program convert real in dollar
import requests
real = float(input("Enter how much reals do you want: "))

response = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
data = response.json()
dollar = float(data['USDBRL']['bid'])

print("The current dollar cost R$ {:.2f}. The value converted is US$ {:.2f}".format(dollar, real / dollar))