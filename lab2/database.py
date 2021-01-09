import psycopg2
from datetime import date

class Database:

    def __init__(self):
        self.connection = None
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(user = "postgres",
                                               password = "sweden",
                                               host = "127.0.0.1",
                                               port = "5432",
                                               database = "festival")
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgresSQL connection is closed")

    def print_pg_version(self):
        self.cursor.execute("select version();")
        record = self.cursor.fetchone()
        print("You are connected to - ", record, "\n")

##############################################################
    def get_group_by_name(self, the_name):
        '''1 - get GROUPS by name'''
        try:
            self.cursor.execute(f"select * from groups where name like '%{the_name}%'")
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error", error)

    def get_musician_by_name(self, the_name):
        '''2 - get MUSICIANS by name'''
        try:
            self.cursor.execute(f"select * from musicians where name like '%{the_name}%'")
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error", error)

    def get_genre_by_year(self, id_f, id_t):
        '''3 - get GENRES by year'''
        try:
            self.cursor.execute("select * from genres where year between '%s' and '%s'" % (id_f, id_t))
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error", error)

    def get_place_by_city(self, the_city):
        '''4 - get PLACES by city'''
        try:
            self.cursor.execute(f"select * from places where city like '%{the_city}%'")
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error", error)

    def get_festival_by_date(self, id_f, id_t):
        '''5 - get FESTIVALS by date'''
        try:
            self.cursor.execute("select * from festivals where date between '%s' and '%s'" % (id_f, id_t))
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error", error)

    ###################################################################

    def get_place_city_by_group_id(self, num1:int, num2:int):
        """6 - get PLACES->city by GROUPS->id"""
        try:
            self.cursor.execute("with tab1 as ( " 
	                            "select fest_id from group_list"
	                            f" where group_id between {num1} and {num2} ), "
                                "tab2 as (select place_id from festivals"
	                            " where id in (select fest_id from tab1))"
                                " select places.* from places, tab2 where id=tab2.place_id")
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error", error)

    def get_festival_by_musician_name(self, name):
        '''7 - get FESTIVALS by MUSICIANS->name'''
        try:
            self.cursor.execute("with tab1 as( "
                                "select distinct group_id from musicians "
                                f"where name like '%{name}%'), "
                                "tab3 as( "
                                "select distinct fest_id  from group_list "
                                f"where group_id in (select group_id from tab1)) "
                                "select festivals.* from festivals, tab3 "
                                "where id = tab3.fest_id ")
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error", error)

    def get_musician_by_genre_example(self, genre_id, group_id, example):
        '''8 - get MUSICIANS by GENRES->example'''
        try:
            self.cursor.execute("with tab1 as( "
                                "select distinct id from genres "
                                f"where example like '%{example}%'), "
                                "tab2 as( "
                                "select id from groups "
                                "where genre_id in (select id from tab1)) "
                                "select * from musicians, tab2 "
                                "where group_id = tab2.id "
                                "")
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error", error)

    #########################################################################

    def update_musician_by_id(self, id, name, birthday, role):
        '''9 - update MUSICIANS'''
        try:
            self.cursor.execute(
                f"update musicians set name='{name}', birthday='{birthday}', role='{role}' where id={id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "update"
            else:
                return "Can't find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in update", error)

    def update_festival_by_id(self, id, name, date):
        '''10 - update FESTIVALS'''
        try:
            self.cursor.execute(
                f"update festivals set name='{name}', date='{date}', where id={id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "update"
            else:
                return "Can't find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in update", error)

    def update_genres_by_id(self, id, name, example, year):
        '''11 - update GENRES'''
        try:
            self.cursor.execute(
                f"update genres set name='{name}', example='{example}' year='{year}', where id={id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "update"
            else:
                return "Can't find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in update", error)

    def update_groups_by_id(self, id, name, country):
        '''12 - update GROUPS'''
        try:
            self.cursor.execute(
                f"update groups set name='{name}', country='{country}', where id={id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "update"
            else:
                return "Can't find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in update", error)

    def update_places_by_id(self, id, city, country):
        '''13 - update PLACES'''
        try:
            self.cursor.execute(
                f"update places set city='{city}', country='{country}', where id={id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "update"
            else:
                return "Can't find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in update", error)

    #################################################

    def  delete_genre(self, id:int):
        """14 - delete GENRES"""
        try:
            self.cursor.execute(
                f"delete from genres where id = {id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "delete"
            else:
                return "Cant find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in delete 1", error)

    def delete_musician(self, id:int):
        """15 - delete MUSICIANS"""
        try:
            self.cursor.execute(
                f"delete from musicians where id = {id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "delete"
            else:
                return "Cant find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in delete 1", error)

    def delete_group(self, id:int):
        """16 - delete GROUPS"""
        try:
            self.cursor.execute(
                f"delete from musicians where group_id in (select id from groups where id = {id})")
            self.connection.commit()
            if self.cursor.rowcount:
                try:
                    self.cursor.execute(
                        f"delete from groups where id = {id})")
                    self.connection.commit()
                    if self.cursor.rowcount:
                        return "delete"
                    else:
                        return "Cant find entity by id"
                except(Exception, psycopg2.Error) as error:
                    self.connect.rollback()
                    print("error in delete 2", error)
            else:
                return "Cant find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in delete 1", error)
        return "error"

    def delete_festivals(self, id:int):
        """17 - delete FESTIVALS"""
        try:
            self.cursor.execute(
                f"delete from festivals where id = {id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "delete"
            else:
                return "Cant find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in delete 1", error)
            return "error"

    def delete_places(self, id:int):
        """18 - delete PLACES"""
        try:
            self.cursor.execute(
                f"delete from places where id = {id}")
            self.connection.commit()
            if self.cursor.rowcount:
                return "delete"
            else:
                return "Cant find entity by id"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in delete 1", error)
            return "error"
    #####################################

    def set_random_genres(self, num:int):
        """19 - set random GENRES"""
        try:
            self.cursor.execute("insert into genres (name, example, year) "
                                "select rand.name, rand.example, rand.year "
                                "from (SELECT "
                                "(md5(random()::text)) as name, "
                                "(md5(random()::text)) as example, "
                                "2020 - trunc(Random()*1000)::integer as year "
                                f"from generate_series(1,{num})) as rand")
            self.connection.commit()
            if self.cursor.rowcount:
                return "generated genres"
            else:
                return "NULL"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in generate", error)

    def set_random_musicians(self, num:int):
        """20 - set random MUSICIANS"""
        try:
            self.cursor.execute("insert into musicians (name, birthday, role, group_id) "
                                "select rand.name, rand.birthday, rand.role, rand.group_id "
                                "from (SELECT groups.id as  group_id, "
                                "(md5(random()::text)) as name, "
                                "(md5(random()::text)) as role, "
                                "((current_date - '100 years'::interval) + trunc(random() * 365) * '1 day'::interval + trunc(random() * 3) * '1 year'::interval ) as birthday "
                                f"from  generate_series(1, 10), groups ORDER BY random() limit {num}) as rand")
            self.connection.commit()
            if self.cursor.rowcount:
                return "generated musicians"
            else:
                return "NULL"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in generate", error)

    def set_random_groups(self, num:int):
        """21 - set random GROUPS"""
        try:
            self.cursor.execute("insert into groups (genre_id, name, country) "
                                "select rand.genre_id, rand.name, rand.country "
                                "from (select genres.id as genre_id, "
                                "md5(random()::text) as country, "
                                "md5(random()::text) as name "
                                f"from  generate_series(1, 1000), genres ORDER BY random() limit {num}) as rand ")
            self.connection.commit()
            if self.cursor.rowcount:
                return "generated groups"
            else:
                return "NULL"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in generate", error)

    def set_random_festivals(self, num):
        """22 - set random FESTIVALS"""
        try:
            self.cursor.execute("insert into festivals (place_id, name, date) "
                                "select rand.place_id, rand.name, rand.date "
                                "from (select places.id as place_id, "
                                "md5(random()::text) as name, "
                                "((current_date - '70 years'::interval) + trunc(random() * 365) * '1 day'::interval + trunc(random() * 3) * '1 year'::interval ) as date "
                                f"from  generate_series(1, 1), places ORDER BY random() limit {num}) as rand")
            self.connection.commit()
            if self.cursor.rowcount:
                return "generated festivals"
            else:
                return "NULL"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in generate", error)

    def set_random_places(self, num):
        """23 - set random PLACES"""
        try:
            self.cursor.execute("insert into places (country, city) "
                                "select rand.country, rand.city "
                                "from (SELECT "
                                "(md5(random()::text)) as country, "
                                "(md5(random()::text)) as city "
                                f"from generate_series(1,{num})) as rand")
            self.connection.commit()
            if self.cursor.rowcount:
                return "generated places"
            else:
                return "NULL"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in generate", error)

    def set_random_group_list(self, num):
        """24 - set random GROUP_LIST"""
        try:
            self.cursor.execute("insert into group_list (group_id, fest_id) "
                                "select rand.group_id, rand.fest_id "
                                "from (select groups.id as group_id, festivals.id as fest_id    "
                                "from festivals, groups) as rand "
                                "left join group_list on (rand.group_id=group_list.group_id "
                                                        "and rand.fest_id=group_list.fest_id) "
                                f"where group_list.id is NULL order by random() limit {num} ")
            self.connection.commit()
            if self.cursor.rowcount:
                return "generated group_list"
            else:
                return "NULL"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in generate", error)

    def get_all_genres(self):
        """25 - get all GENRES"""
        self.cursor.execute("select * from genres")
        self.connection.commit()
        return self.cursor.fetchall()

    def get_all_musicians(self):
        """26 - get all MUSICIANS"""
        self.cursor.execute("select * from musicians")
        self.connection.commit()
        return self.cursor.fetchall()

    def get_all_groups(self):
        """27 - get all GROUPS"""
        self.cursor.execute("select * from groups")
        self.connection.commit()
        return self.cursor.fetchall()

    def get_all_festivals(self):
        """28 - get all FESTIVALS"""
        self.cursor.execute("select * from festivals")
        self.connection.commit()
        return self.cursor.fetchall()

    def get_all_places(self):
        """29 - get all PLACES"""
        self.cursor.execute("select * from places")
        self.connection.commit()
        return self.cursor.fetchall()

    def add_genre(self, name:str, example:str, year:int):
        """30 - add GENRES"""""
        try:
            self.cursor.execute(
                f"insert into genres (name, example, year) values ('{name}', '{example}', '{year}')")
            self.connection.commit()
            return "inserted"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in add", error)

    def add_musician(self, name:str, birthday:date, role:str, group_id:int):
        """31 - add MUSICIANS"""""
        try:
            self.cursor.execute(
                f"insert into musicians (name, birthday, role, group_id) values ('{name}', '{birthday}', '{role}', {group_id})")
            self.connection.commit()
            return "inserted"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in add", error)

    def add_group(self, name:str, genre_id:int, country:str):
        """32 - add GROUPS"""""
        try:
            self.cursor.execute(
                f"insert into groups (name, genre_id, country) values ('{name}', {genre_id}, '{country}')")
            self.connection.commit()
            return "inserted"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in add", error)

    def add_festival(self, name:str, date:date, place_id:int):
        """33 - add FESTIVALS"""""
        try:
            self.cursor.execute(
                f"insert into festivals (name, date, place_id) values ('{name}', '{date}', {place_id})")
            self.connection.commit()
            return "inserted"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in add", error)

    def add_place(self, country:str, city:str):
        """34 - add PLACES"""""
        try:
            self.cursor.execute(
                f"insert into places (country, city) values ('{country}', '{city}')")
            self.connection.commit()
            return "inserted"
        except(Exception, psycopg2.Error) as error:
            self.connect.rollback()
            print("error in add", error)