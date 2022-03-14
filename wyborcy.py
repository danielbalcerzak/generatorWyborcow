#   STUDENT DANIEL BALCERZAK

import random

SEX = ["female", 'male']
YEAR = 2020
MIN_YEAR = 20
MAX_YEAR = 114
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 30
MIN_PESEL_COMPONENT = 10000
MAX_PESEL_COMPONENT = 99999
ITERATIONS = 20000
MALE_NAMES_INFILE = "imionameskie.txt"
FEMALE_NAMES_INFILE = "imionazenskie.txt"
CITIES_INFILE = 'miasta.txt'
FEMALE_SURNAMES_INFILE = 'nazwiskazenskie.txt'
MALE_SURNAMES_INFILE = 'nazwiskameskie.txt'
STREETS_INFILE = 'ulice.txt'

#   Funkcja strip_white_signs przyjmuje argumenty w postaci zmiennej zawartości pliku i wykonuje wycięcie białych znaków
#   Funkcja zwraca zawartość w postaci listy


def strip_white_signs(file_content):
    list_of_data = []
    for i in file_content:
        list_of_data.append(i.strip())
    return list_of_data


#   Funkcja operation_on_file() przyjmuje argumenty w postaci nazwy plików i wykonuje operacje otwarcia i zamknięcia
#   pliku. W funkcji wykonywoływane są funkcje operujące na danych. Funkcja zraca zawartość pliku w postaci listy.


def operation_on_file(file_name):
    infile = open(file_name, "r", encoding="utf-8")
    read_file = infile.readlines()
    content_list = strip_white_signs(read_file)
    infile.close()
    return content_list


#   Funkcja years_and_pesel nie przyjmuje argumentów. Generuje rok urodzenia w postaci dd.mm.rrrr oraz numer pesel.
#   Funkcja zwraca datę urodzenia oraz numer pesel.


def years_and_pesel():
    year_short = random.randint(MIN_YEAR, MAX_YEAR)
    year_long = str(YEAR - year_short)
    month = str(random.randint(MIN_MONTH, MAX_MONTH))
    if int(month) < 10:
        month = ("0" + month)
    day = str(random.randint(MIN_DAY, MAX_DAY))
    if int(day) < 10:
        day = ("0" + day)
    pesel_component_number = str(random.randint(MIN_PESEL_COMPONENT, MAX_PESEL_COMPONENT))
    day_of_birth = (day + '.' + month + '.' + year_long)
    pesel_number = (year_long[-2:] + month + day + pesel_component_number)
    return day_of_birth, pesel_number


#   Funkcja make_list_dict przyjmuje argumenty w postaci list. Funkcja losuje płeć oraz na jej podstawie, dobiera
#   dane z odpowiednich list. Zapisuje te dane w postaci słownika i dodaje do listy w ilość wskazanej w zmiennej
#   globalnej. Funkcja zwraca stworzoną listę.


def make_list_dict(female_names, female_surnames, cities, streets, male_names, male_surnames):
    electorate_list = []
    for i in range(ITERATIONS):
        if random.choice(SEX) == "female":
            female_name = random.choice(female_names)
            female_surname = random.choice(female_surnames)
            street = random.choice(streets)
            city = random.choice(cities)
            home_number = random.randint(1, 100)
            local_number = random.randint(1, 100)
            date_of_birth, pesel_number = years_and_pesel()
            female_voter = {'imie': female_name, 'nazwisko': female_surname, "miasto": city, "ulica": street,
                            "nr": home_number, "mieszkanie": local_number, "data_ur": date_of_birth,
                            "pesel": pesel_number}
            electorate_list.append(female_voter)
        else:
            male_name = random.choice(male_names)
            male_surname = random.choice(male_surnames)
            street = random.choice(streets)
            city = random.choice(cities)
            home_number = random.randint(1, 100)
            local_number = random.randint(1, 100)
            date_of_birth, pesel_number = years_and_pesel()
            male_voter = {'imie': male_name, 'nazwisko': male_surname, "miasto": city,  "ulica": street,
                          "nr": home_number, "mieszkanie": local_number, "data_ur": date_of_birth,
                          "pesel": pesel_number}
            electorate_list.append(male_voter)
    return electorate_list


#   Funkcja write_csv przyjmuje argument w postaci listy i tworzy plik wyborcy.csv.
#   Zapisuje dane ze słownika i zamyka plik.


def write_csv(electorate_list):
    csv_outfile = open('wyborcy.csv', 'w', newline='\n', encoding="utf-8")
    csv_outfile.write('imie;' + 'nazwisko;' + 'miasto;' + 'ulica;' + 'nr;' + 'mieszkanie;' + 'data_ur;' + 'pesel')
    for dictionary in electorate_list:
        csv_outfile.write('\n')
        for key, value in dictionary.items():
            if key == "pesel":
                csv_outfile.write(str(value))
            else:
                csv_outfile.write(str(value) + ';')
    csv_outfile.close()


#   Funkcja main() służy jako punkt wyjścia do wykonania programu


def main():
    cities_list = operation_on_file(CITIES_INFILE)
    female_names_list = operation_on_file(FEMALE_NAMES_INFILE)
    male_names_list = operation_on_file(MALE_NAMES_INFILE)
    female_surnames_list = operation_on_file(FEMALE_SURNAMES_INFILE)
    male_surnames_list = operation_on_file(MALE_SURNAMES_INFILE)
    street_list = operation_on_file(STREETS_INFILE)
    electorate = make_list_dict(female_names_list, female_surnames_list, cities_list, street_list, male_names_list,
                                male_surnames_list)
    write_csv(electorate)


main()
