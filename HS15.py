import requests
def getJSON():
    from_currency=input("Wypisz znak waluty z której chcesz konwerowac (np. USD, PLN): ")
    to_currency=input("Wpisz znak waluty na którą chcesz konwertować: ")
    response = requests.get("https://v6.exchangerate-api.com/v6/454cd169b3beedfde93a573b/latest/"+from_currency) #Wczytuję API
    if response.status_code == 200:
        data = response.json() #Wczytuję plik JSON
        conversion_rates = data.get('conversion_rates') #Wczytuję listę 'conversion_rates' w pliku JSON
        if to_currency in conversion_rates:
            conversion_rate = conversion_rates[to_currency] #Wczytuję konkretną walutę z wszystkich możliwych
            print("1",from_currency,"=",conversion_rate,to_currency,sep=" ")
        else: print("Wymienionej waluty docelowej nie ma w odpowiedzi od serwera")
    else: print("Wpisana waluta początkowa nie istnieje")
getJSON()