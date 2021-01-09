import os
from datetime import date

class View:

    def __init__(self):
        self.clear = lambda: os.system('cls')
        self.separator = lambda: print("_________________________")

    def print_menu(self):
        print("1 - get GROUPS by name\n"
              "2 - get MUSICIANS by name\n"
              "3 - get GENRES by year\n"
              "4 - get PLACES by city\n"
              "5 - get FESTIVALS by date\n"
              ###
              "6 - get PLACES->city by GROUPS->id\n"
              "7 - get FESTIVALS by MUSICIANS->name\n"
              "8 - get MUSICIANS by GENRES->example\n"
              ###
              "9 - update MUSICIANS\n"
              "10 - update FESTIVALS\n"
              "11 - update GENRES\n"
              "12 - update GROUPS\n"
              "13 - update PLACES\n"
              ###
              "14 - delete GENRES\n"
              "15 - delete MUSICIANS\n"
              "16 - delete GROUPS\n"
              "17 - delete FESTIVALS\n"
              "18 - delete PLACES\n"
              ###
              "19 - set random GENRES\n"
              "20 - set random MUSICIANS\n"
              "21 - set random GROUPS\n"
              "22 - set random FESTIVALS\n"
              "23 - set random PLACES\n"
              "24 - set random GROUP_LIST\n"
              ###
              "25 - get all GENRES\n"
              "26 - get all MUSICIANS\n"
              "27 - get all GROUPS\n"
              "28 - get all FESTIVALS\n"
              "29 - get all PLACES\n"
              ###
              "30 - add GENRES\n"
              "31 - add MUSICIANS\n"
              "32 - add GROUPS\n"
              "33 - add FESTIVALS\n"
              "34 - add PLACES\n"
              "35 - exit\n")

    def menu(self):
        choice = 0
        self.print_menu()
        choice = input(">>>>>>Choose your fighter: ")
        return choice

    def print_festivals(self, festivals):
        for festival in festivals:
            print("id", festival[0])
            print("place_id", festival[1])
            print("name", festival[2])
            print("date", festival[3])

    def print_genres(self, genres):
        for genre in genres:
            print("id", genre[0])
            print("name", genre[1])
            print("example", genre[2])
            print("year", genre[3])

    def print_group_list(self, group_list):
        for list in group_list:
            print("group_id", list[0])
            print("fest_id", list[1])
            print("id", list[2])

    def print_groups(self, groups):
        for group in groups:
            print("id", group[0])
            print("name", group[1])
            print("genre_id", group[2])
            print("country", group[3])

    def print_musicians(self, musicians):
        for musician in musicians:
            print("id", musician[0])
            print("name", musician[1])
            print("birthday", musician[2])
            print("role", musician[3])
            print("group_id", musician[4])

    def print_places(self, places):
        for place in places:
            print("id", place[0])
            print("country", place[1])
            print("city", place[2])

    def add_festival(self):
        festival = {}
        festival["name"] = self.get_string('name')
        festival["date"] = self.get_date('date')
        festival["place_id"] = self.get_number('place_id')
        return festival

    def add_genre(self):
        genre = {}
        genre["name"] = self.get_string('name')
        genre["example"] = self.get_string('example')
        genre["year"] = self.get_number('year')
        return genre

    def add_group_list(self):
        group_list = {}
        group_list["group_id"] = self.get_number('group_id')
        group_list["fest_id"] = self.get_number('fest_id')
        return group_list

    def add_group(self):
        group = {}
        group["name"] = self.get_string('name')
        group["genre_id"] = self.get_number('genre_id')
        group["country"] = self.get_string('country')
        return group

    def add_musician(self):
        musician = {}
        musician["name"] = self.get_string('name')
        musician["birthday"] = self.get_date('birthday')
        musician["role"] = self.get_string('role')
        musician["group_id"] = self.get_number('group_id')
        return musician

    def add_place(self):
        place = {}
        place["country"] = self.get_string('country')
        place["city"] = self.get_string('city')
        return place

    def update_festivals(self):
        festival = {}
        festival["id"] = self.get_number('id')
        festival["place_id"] = self.get_number('place_id')
        festival["name"] = self.get_string('name')
        festival["date"] = self.get_date('date')
        return festival

    def update_genres(self):
        genre = {}
        genre["id"] = self.get_number('id')
        genre["name"] = self.get_string('name')
        genre["example"] = self.get_string('example')
        genre["year"] = self.get_number('year')
        return genre

    def update_group_list(self):
        list = {}
        list["group_id"] = self.get_number('group_id')
        list["fest_id"] = self.get_number('fest_id')
        list["id"] = self.get_number('id')
        return list

    def update_groups(self):
        group = {}
        group["id"] = self.get_number('id')
        group["name"] = self.get_string('name')
        group["genre_id"] = self.get_number('genre_id')
        group["country"] = self.get_string('country')
        return group

    def update_musicians(self):
        musician = {}
        musician["id"] = self.get_number('id')
        musician["name"] = self.get_string('name')
        musician["birthday"] = self.get_date('birthday')
        musician["role"] = self.get_string('role')
        musician["group_id"] = self.get_number('group_id')
        return musician

    def update_places(self):
        place = {}
        place["id"] = self.get_number('id')
        place["country"] = self.get_string('country')
        place["city"] = self.get_string('city')
        return place

    def get_number(self, str):
        while True:
            try:
                num = int(input('Enter '+ str +': '))
                if num < 0:
                    print("enter positive value ")
                    continue
            except ValueError:

                print("you should enter integer value ")
                continue
            break
        return num

    def get_date(self, str):
        while True:
            try:
                print('Enter ' + str)
                year1 = int(input("Enter year: "))
                month1 = int(input("Enter month: "))
                day1 = int(input("Enter day: "))
                if year1 < 0 or month1 < 0 or day1 < 0:
                    print("enter positive values ")
                    continue
            except ValueError:
                print("you should enter integer value ")
                continue
            break
        return date(year1, month1, day1)

    def get_string(self, str):
        return input('Enter '+ str +': ')
