# creating a txt file
write_file = open('sample.txt', 'w')
write_file.write("this is just a sample text\n")
write_file.close()


# reading file
read_file = open('sample.txt' , 'r')
text = read_file.read()

print(text)
