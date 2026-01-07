step_counter = int(input('How many steps do u want to add '))
file_variable = open('step_counter.txt','w')
for num in range(1, user_days + 1):
steps = input ("The amount of days u have walked")
step_counter.write(f'{entry}\n')
step_counter.close
file_object = open('example.txt','r')
for line in file_object:
print(line)
file_object.close
