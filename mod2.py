# Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan",
# "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# и вытащите 4 рандомных имени оттуда и сохраните в другой список.
import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
n = []
for i in range(4):
    n.append(random.choice(names))
    print(n)
