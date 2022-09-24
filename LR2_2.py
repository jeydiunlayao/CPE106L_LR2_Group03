text = input('Enter file name: ')

with open(text,'r') as file:

   

   data = []

   for line in file:

         data.append(line.strip())

print('The number of lines in the file is:', len(data))

while True:

   lnum = int(input('Enter line number: '))

   if lnum == 0:

       break

   else:

       num = lnum - 1

       print(data[num])