from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#AUX
def inputWrite(x, content):
    x.clear
    x.send_keys(content)
    x.send_keys(Keys.RETURN)

def endDate():
    button = driver.find_element_by_xpath('//button[@id="companytButton"]')
    button.click()

def endClient():
    button = driver.find_element_by_xpath('//button[normalize-space()="Finalizar"]')
    button.click()

#PROGRAM
def inputName(clientName):
    client = driver.find_element_by_xpath('//input[@id="clientName"]')
    inputWrite(client, clientName)

    button = driver.find_element_by_xpath('//button[@id="clientButton"]')
    button.click()

def inputCompany(companyName):
    company = driver.find_element_by_xpath('//input[@id="companyName"]')
    inputWrite(company, companyName)

def inputDates(start, end, done):
    dateStart = driver.find_element_by_xpath('//input[@id="dateStart"]')
    dateEnd = driver.find_element_by_xpath('//input[@id="dateEnd"]')

    inputWrite(dateStart, start)
    inputWrite(dateEnd, end)

    endDate()

    if done:
        endClient()


driver = webdriver.Chrome(executable_path="/Users/matiassosa/Downloads/chromedriver")
driver.get("https://matiasosa.github.io/retirement-system/")

#nombre | char de la empresa | arr de fechas
def execute(clientName, compName, dates):
    inputName(clientName)
    cant = int(len(dates)/2)
    end = False

    for i in range(cant):    
        inputCompany(compName + str(i))
        if i == cant-1:
            end = True
        inputDates(dates[i+i], dates[i+i+1], end)

dates1 = ["07/03/2002", "04/01/2014", "10/1992", "02/1999"]
execute("Matias Sosa", "A", dates1)

dates2 = ["07/03/2002", "04/01/2014", "10/1992", "02/1999"]
execute("Ariel Sosa", "A", dates2)















# Persona 1
# inputName("Matias Sosa")

# inputCompany("A1")
# inputDates("07/03/2002", "04/01/2014", True)

# Persona 2
# inputName("Matias Sosa")

# inputCompany("B1")
# inputDates("10/1992", "02/1999", False)
# inputCompany("B2")
# inputDates("22/05/2000", "31/07/2004", True)

# Persona 3
# inputName("Matias Sosa")

# inputCompany("C1")
# inputDates("06/1974", "02/1981", False)
# inputCompany("C2")
# inputDates("02/1981", "11/1990", False)
# inputCompany("C3")
# inputDates("09/1993", "04/2001", True)

# Persona 4
# inputName("Matias Sosa")

# inputCompany("D1")
# inputDates("12/08/2001", "30/03/2006", False)
# inputCompany("D2")
# inputDates("26/05/2006", "13/11/2009", False)
# inputCompany("D3")
# inputDates("29/01/2010", "10/05/2014", False)
# inputCompany("D4")
# inputDates("22/06/2014", "01/04/2018", False)
# inputCompany("D5")
# inputDates("06/03/2019", "14/03/2022", True)

# Persona 5
# inputName("Matias Sosa")

# inputCompany("E1")
# inputDates("21/02/1998", "16/07/2002", False)
# inputCompany("E2")
# inputDates("09/2002", "11/2010", True)

# Persona 1
# Nombre: Matias Sosa

# Empresa: A1
# Fecha de inicio: 07/03/2002
# Fecha de fin: 04/01/2014

#_____________________

# Persona 2
# Nombre: Gustavo Navarro

# Empresa: B1
# Fecha de inicio: 10/1992
# Fecha de fin: 02/1999

# Empresa: B2
# Fecha de inicio: 22/05/2000
# Fecha de fin: 31/07/2004

#_____________________

# Persona 3
# Nombre: Hugo Garcia

# Empresa: C1
# Fecha de inicio: 06/1974
# Fecha de fin: 02/1981

# Empresa: C2
# Fecha de inicio: 02/1981
# Fecha de fin: 11/1990

# Empresa: C3
# Fecha de inicio: 09/1993
# Fecha de fin: 04/2001

#_____________________

# Persona 4
# Nombre: Omar Ruiz

# Empresa: D1
# Fecha de inicio: 12/08/2001
# Fecha de fin: 30/03/2006

# Empresa: D2
# Fecha de inicio: 26/05/2006
# Fecha de fin: 13/11/2009

# Empresa: D3
# Fecha de inicio: 29/01/2010
# Fecha de fin: 10/05/2014

# Empresa: D4
# Fecha de inicio: 22/06/2014
# Fecha de fin: 01/04/2018

# Empresa: D5
# Fecha de inicio: 06/03/2019
# Fecha de fin: 14/03/2022

#_____________________

# Persona 5
# Nombre: Tomas Gonzalez

# Empresa: E1
# Fecha de inicio: 21/02/1998
# Fecha de fin: 16/07/2002

# Empresa: E2
# Fecha de inicio: 09/2002
# Fecha de fin: 11/2010