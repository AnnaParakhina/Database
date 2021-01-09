from database import Database
from view import View

database = Database()
database.connect()
database.print_pg_version()

view = View()
choice = '0'

while choice != '35':
    choice = view.menu()
    view.separator()
    if choice == '1':
        view.print_groups(database.get_group_by_name(view.get_string('name')))
    elif choice == '2':
        view.print_musicians(database.get_musician_by_name(view.get_string('name')))
    elif choice == '3':
        view.print_genres(database.get_genre_by_year(view.get_number('year 1'),
                                                     view.get_number('year 2')))
    elif choice == '4':
        view.print_places(database.get_place_by_city(view.get_string('city')))
    elif choice == '5':
        view.print_festivals(database.get_festival_by_date(view.get_date('date 1'),
                                                           view.get_date('date 2')))
    elif choice == '6':
        view.print_places(database.get_place_city_by_group_id(view.get_number('group_id 1'),
                                                              view.get_number('group_id 2')))
    elif choice == '7':
        view.print_festivals(database.get_festival_by_musician_name(view.get_string('name')))
    elif choice == '8':
        view.print_musicians(database.get_musician_by_genre_example(view.get_string('example')))
    elif choice == '9':
        musician = view.update_musicians()
        print(database.update_musician_by_id(musician["id"],
                                             musician["name"],
                                             musician["birthday"],
                                             musician["role"]))
    elif choice == '10':
        festival = view.update_festivals()
        print(database.update_festival_by_id(festival["id"],
                                             festival["name"],
                                             festival["date"]))
    elif choice == '11':
        genre = view.update_genres()
        print(database.update_genres_by_id(genre["id"],
                                           genre["name"],
                                           genre["example"],
                                           genre["year"]))
    elif choice == '12':
        group = view.update_groups()
        print(database.update_groups_by_id(group["id"],
                                           group["name"],
                                           group["country"]))
    elif choice == '13':
        place = view.update_places()
        print(database.update_places_by_id(place["id"],
                                           place["country"],
                                           place["city"]))
    elif choice == '14':
        print(database.delete_genre(view.get_string('id')))
    elif choice == '15':
        print(database.delete_musician(view.get_string('id')))
    elif choice == '16':
        print(database.delete_group(view.get_string('id')))
    elif choice == '17':
        print(database.delete_festivals(view.get_string('id')))
    elif choice == '18':
        print(database.delete_places(view.get_string('id')))
    elif choice == '19':
        print(database.set_random_genres(view.get_number('count')))
    elif choice == '20':
        print(database.set_random_musicians(view.get_number('count')))
    elif choice == '21':
        print(database.set_random_groups(view.get_number('count')))
    elif choice == '22':
        print(database.set_random_festivals(view.get_number('count')))
    elif choice == '23':
        print(database.set_random_places(view.get_number('count')))
    elif choice == '24':
        print(database.set_random_group_list(view.get_number('count')))
    elif choice == '25':
        view.print_genres(database.get_all_genres())
    elif choice == '26':
        view.print_musicians(database.get_all_musicians())
    elif choice == '27':
        view.print_groups(database.get_all_groups())
    elif choice == '28':
        view.print_festivals(database.get_all_festivals())
    elif choice == '29':
        view.print_places(database.get_all_places())
    elif choice == '30':
        genre = view.add_genre()
        print(database.add_genre(genre["name"],
                                 genre["example"],
                                 genre["year"]))
    elif choice == '31':
        musician = view.add_musician()
        print(database.add_musician(musician["name"],
                                    musician["birthday"],
                                    musician["role"],
                                    musician["group_id"]))
    elif choice == '32':
        group = view.add_group()
        print(database.add_group(group["name"],
                                 group["genre_id"],
                                 group["country"]))
    elif choice == '33':
        fest = view.add_festival()
        print(database.add_festival(fest["name"],
                                    fest["date"],
                                    fest["place_id"]))
    elif choice == '34':
        place = view.add_place()
        print(database.add_place(place["country"],
                                 place["city"]))
    elif choice == '35':
        break
    else:
        print("incorrect input")
    view.separator()
database.close()