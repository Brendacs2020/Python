#This program convert real in dollar
import requests

real = float(input("How much reals do you want convert in dollar? "))
dollar = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@data)?@data='2025-03-26'&$top=1&$format=json"
response = requests.get(dollar)

print('The dollar is USD {dollar:.2f} and your value conveted is {real*dollar:.2f}')
