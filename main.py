import pandas as pd
import random

file_path = 'students.csv'

data = pd.read_csv(file_path)

genders = data['gender'].unique()

students = []
print(data)
seat = data['name']
random.shuffle(seat)
print(list(seat))