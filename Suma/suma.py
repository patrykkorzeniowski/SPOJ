import sys

def main():
    suma = 0
    for line in sys.stdin:  # Pobieranie danych aż do EOF
        suma += int(line.strip())  # Konwersja na liczbę i dodanie do sumy
        print(suma)  # Wypisanie aktualnej sumy

main()
