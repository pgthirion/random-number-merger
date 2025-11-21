# Importing of random library in order to add random ints to the files
# Creating a list with the random ints
# Writing the list to a txt file
# Repeating the proccess for the next file
# Joining the files by merging the lists

import random

# First File
list_of_nums = []

for i in range(10):
    list_of_nums.append(str(random.randrange(99,1000)))
list_of_nums.sort()

with open('numbers1.txt', 'w') as output_file:
        output_file.writelines("\n".join(list_of_nums))

# Second File
list_of_nums_2 = []

for i in range(10):
    list_of_nums_2.append(str(random.randrange(99,1000)))

list_of_nums_2.sort()

with open('numbers2.txt', 'w') as output_file:
        output_file.writelines("\n".join(list_of_nums_2))
 
# Joined file

joined_list = list_of_nums + list_of_nums_2
joined_list.sort()
with open('all_numbers.txt', 'w') as output_file:
        output_file.writelines("\n".join(joined_list))
print("Success! All numbers stored into all_numbers.txt")