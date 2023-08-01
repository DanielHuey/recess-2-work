from bs4 import BeautifulSoup
from requests import get
import openpyxl


book = openpyxl.Workbook()
sheet = book.active
sheet.title = 'Bird Songs'
sheet.append(['name','number_of_birds','number_of_background_recordings'])

response = get("https://xeno-canto.org/collection/species/all")
bs = BeautifulSoup(response.text, 'html.parser')
species = bs.find('table',class_="results").find_all('tr')
for s in species:
    name = s.find('td').span.text.strip()
    number = s.find('td', width='20').text.strip()
    rec = s.find('td', width='30').text.strip()
    sheet.append([name,number,rec])

book.save('Bird_Songs.xlsx')



