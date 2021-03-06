from bs4 import BeautifulSoup
import requests
from time import sleep


def clima():
    # Carrega página com informações sobre o clima #
    html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content

    # Faz parser no html da página #
    soup = BeautifulSoup(html, 'html.parser')

    # Captura dados navegando nos elementos do html #
    resume = soup.find(class_='-gray -line-height-24 _center')
    tempMin = soup.find(id='min-temp-1')
    tempMax = soup.find(id='max-temp-1')

    # Mostra resultados #
    print('\n Resumo: ' + resume.text)
    print(' Temp. Mínima: ' + tempMin.string)
    print(' Temp. Máxima: ' + tempMax.string)

clima()

print('\n')

while True:
    q1 = str(input('Deseja realizar outra previsão? \n [S] para sim\n [N] para não\n')).upper()
    if q1 == 'S':
        clima()

    if q1 == 'N':
        print('Fechando ..')
        sleep(2)
        exit()
