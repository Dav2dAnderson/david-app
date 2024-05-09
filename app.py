import yt_dlp
import requests
import json

david = """
·▄▄▄▄       ▄▄▄·      ▌ ▐·    ▪      ·▄▄▄▄  
██▪ ██     ▐█ ▀█     ▪█·█▌    ██     ██▪ ██ 
▐█· ▐█▌    ▄█▀▀█     ▐█▐█•    ▐█·    ▐█· ▐█▌
██. ██     ▐█ ▪▐▌     ███     ▐█▌    ██. ██ 
▀▀▀▀▀•      ▀  ▀     . ▀      ▀▀▀    ▀▀▀▀▀• \n\n\t\t\t\t\t\tby David\n
"""

print(david)


class DownloaderY:
    def __init__(self) -> None:
        print("=====================================\n[INFO] Welcome to the YouTube Video Downloader!")
    
    def download_video(self, url):
        ydl_opts = {
            'format': 'best',  
            'outtmpl': '%(title)s.%(ext)s',  
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    
    def menu(self):
        print("Menu:\n -- YouTube\n -- Exit")


class Calculator:
    def __init__(self):
        print("================================\nWelcome to the Calculator!")
    
    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Can not be divided by zero"
        return a / b

    def menu(self):

        print("================================================\nChoose one of the operations below: ")
        print("-- plus")
        print("-- minus")
        print("-- multiply")
        print("-- divide")
        print("-- exit")


class Currency:
    def __init__(self):
        print("===============================================\n[INFO] Welcome to the Currency Rate")

    def rate(self):
        url = 'http://cbu.uz/ru/arkhiv-kursov-valyut/json/'
        try:
            r = requests.get(url)
            data = r.json()
            return data
        except Exception as e:
            print("[ERROR]", e)
    
    def menu(self):
        print("""========================Menu=========================""")
        currencies = "[1] - USD(US Dollar)\n[2] - EUR(Euro)\n[3] - RUB(Russian Rubl)\n[4] - GBP(Pound Sterling)\n[5] - AZN(Azerbaijan Manat)\n[6] - BRL(Brazilian Real)\n[7] - JPY(Japan Yen)\n[8] - CNY(Yuan Renminbi)\n[9] - KRW(The Korean Republic Won)\n[10] - KZT(Kazakhstan Tenge)\n[11] - SAR(Saudi Riyal)\n[12] - TRY(Turkish Lira)\n"
        currencies_list = currencies.split("\n")

        split_point = len(currencies_list) // 2

        first_half = currencies_list[:split_point]
        second_half = currencies_list[split_point:]

        for line1, line2 in zip(first_half, second_half):
            print(f"{line1:<40} {line2}")
        print("\n[13] - Exit")


def programm():
    print("##################Hello, Dear!#####################\n")
    print("Category:\n [1] - Calculator\n [2] - Video downloader from YouTube\n [3] - Currency rate\n\n ")
    category = int(input("Choose one category: "))

    if category == 1:
        calculator = Calculator()
        while True:
            calculator.menu()
            print("================================================")
            choice = input("Your choice(plus, minus, multiply, divide, exit): ")
            if choice == "exit":
                print("[INFO] Exit")
                break
            try:
                a = float(input("Enter a: "))
                b = float(input("Enter b: "))
                print("===============================================")
            
                if choice == "plus":
                    result = calculator.add(a, b)

                elif choice == "minus":
                    result = calculator.substract(a, b)

                elif choice == "multiply":
                    result = calculator.multiply(a, b)
                
                elif choice == "divide":
                    result = calculator.divide(a, b)
                else:
                    print("[ERROR] Wrong choice")
                    
                print("Result:", result, "\n\n")
            
            except ValueError as e:
                print("[ERROR] Please, enter only numbers!" )   
    
    elif category == 2:
        downloader = DownloaderY()
        while True:
            downloader.menu()
            choice = input("Choose one option:")
            if choice == "YouTube":
                url = input("Enter URL of video:")
                downloader.download_video(url)
            elif choice == "Exit":
                print("[INFO] Exit")
                break
            else:
                print("[ERROR] Unknown option!")
    
    elif category == 3:
        currency = Currency()
        currency.menu()
        while True:
            print("\n")
            choice = int(input("Choose one currency: "))
            courses = currency.rate()
            if choice == 1:
                print("==================================")
                print(f"#{courses[0]['Ccy']}#")
                print(f"Rate: {courses[0]['Rate']} - UZS\nDate: {courses[0]['Date']}")
                print("==================================")
            elif choice == 2:
                print("==================================")
                print(f"#{courses[1]['Ccy']}#")
                print(f"Rate: {courses[1]['Rate']} - UZS\nDate: {courses[1]['Date']}")
                print("==================================")
            elif choice == 3:
                print("==================================")
                print(f"#{courses[2]['Ccy']}#")
                print(f"Rate: {courses[2]['Rate']} - UZS\nDate: {courses[2]['Date']}")
                print("==================================")
            elif choice == 4:
                print("==================================")
                print(f"#{courses[3]['Ccy']}#")
                print(f"Rate: {courses[3]['Rate']} - UZS\nDate: {courses[3]['Date']}")
                print("==================================")
            elif choice == 5:
                print("==================================")
                print(f"#{courses[5]['Ccy']}#")
                print(f"Rate: {courses[5]['Rate']} - UZS\nDate: {courses[5]['Date']}")
                print("==================================")
            elif choice == 6:
                print("==================================")
                print(f"#{courses[10]['Ccy']}#")
                print(f"Rate: {courses[10]['Rate']} - UZS\nDate: {courses[10]['Date']}")
                print("==================================")
            elif choice == 7:
                print("==================================")
                print(f"#{courses[4]['Ccy']}#")
                print(f"Rate: {courses[4]['Rate']} - UZS\nDate: {courses[4]['Date']}")
                print("==================================")
            elif choice == 8:
                print("==================================")
                print(f"#{courses[14]['Ccy']}#")
                print(f"Rate: {courses[14]['Rate']} - UZS\nDate: {courses[14]['Date']}")
                print("==================================")
            elif choice == 9:
                print("==================================")
                print(f"#{courses[35]['Ccy']}#")
                print(f"Rate: {courses[35]['Rate']} - UZS\nDate: {courses[35]['Date']}")
                print("==================================")
            elif choice == 10:
                print("==================================")
                print(f"#{courses[37]['Ccy']}#")
                print(f"Rate: {courses[37]['Rate']} - USZ\nDate: {courses[37]['Date']}")
                print("==================================")
            elif choice == 11:
                print("==================================")
                print(f"#{courses[57]['Ccy']}#")
                print(f"Rate: {courses[57]['Rate']} - UZS\nDate: {courses[57]['Date']}")
                print("==================================")
            elif choice == 12:
                print("==================================")
                print(f"#{courses[66]['Ccy']}#")
                print(f"Rate: {courses[66]['Rate']} - UZS\nDate: {courses[66]['Date']}")
                print("==================================")
            elif choice == 13:
                break
            else:
                print("[ERROR] Wrong choice")
programm()




