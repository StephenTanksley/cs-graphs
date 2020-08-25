import random
import math

first_names = ["Sleve", "Onson", "Darryl", "Anatoli", "Rey", "Glenallen", "Mario", "Raul", "Kevin",
               "Tony", "Bobson", "Willie", "Jeromy", "Scott", "Shown", "Dean", "Mike", "Dwigt", "Tim", "Karl", "Todd", "Nert", "Kenn", "Fergit", "Coll", "Lood", "Taenis", "Marnel", "Dony", "Gin", "Wob", "Tanny", "Hudgyn", "Fraven", "Rarr", "Dorse", "Roy", "Tenpe", "Varlin", "Pott", "Am", "Snarry", "Bobs", "Renly", "Ceynei", "Hom", "Odood", "Gary", "Jaris", "Erl", "Lenn", "Dan", "Yans", "Mob", "Bannoe", "Jinneil", "Morkon"]

last_names = ["McDichael", "Sweemey", "Archideld", "Smorin", "McSriff", "Mixon", "McRlwain",
              "Chamgerlain", "Nogilny", "Smehrik", "Dugnutt", "Dustice", "Gride", "Dourque", "Furcotte", "Wesrey", "Truk", "Rortugal", "Sandaele", "Dandleton", "Sernandez", "Bonzalez", "Bisels", "Nitvarn", "Hote", "Bitzron", "Janglosti", "Tellron", "Hary", "Olerberz", "Ginlons", "Wonkoz", "Mlitnirt", "Sasdarl", "Pooth", "Dick", "Hintline", "Gamo", "Laob", "Genmist", "O'Erson", "Shitwon", "Peare", "Mlynren", "Doober", "Wapko", "Jorgeudey", "Banps", "Forta", "Jivliiz", "Wobses", "Boyo", "Loovensan", "Welronz", "Rodylar", "Swermirstz", "Robenko"]


len_first_list = len(first_names)
len_second_list = len(last_names)


print(len_first_list)
print(len_second_list)


def random_name(arr):
    index = math.floor(random.random() * len(arr))
    return arr[index]


# I want to make sure all the names are unique, so I'm going to store them as a set.
full_names = []


def full_name(name1, name2):

    first_name = random_name(name1)
    last_name = random_name(name2)
    full_names.append(f"{first_name} {last_name}")
    return


for _ in range(2001):
    full_name(first_names, last_names)


print(full_names)
