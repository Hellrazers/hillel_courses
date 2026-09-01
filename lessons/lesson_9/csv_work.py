import csv

with open('users.csv') as csvfile:
    reader = list(csv.reader(csvfile))
    # for row in reader:
    #     print(row)


# print(reader)
column_name = reader[0]
values_list = reader[1:]

dict_values = [dict(zip(column_name, value)) for value in values_list]
print(dict_values)

for row in dict_values:
    if int(row['Age']) > 25:
        print(f'name: {row['Name']} age: {row['Age']}')



# for row in reader[1:]:
#     # print(row)
#     if int(row[1]) > 25:
#         print(f'name: {row[0]} age: {row[1]}')