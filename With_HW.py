step_counter = int(input('How many steps do u want to add '))
file_variable = open('example_file.txt','w')
for num in range(1, num_lines + 1):
entry = input('#{num} What would you like to add to the file? ')
file_variable.write(f'{entry}\n')
file_variable.close
