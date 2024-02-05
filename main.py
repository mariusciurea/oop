from read_write import TextFileWriter, FileNameError, FileExtensionError

# print(help(TextFileWriter))
file = TextFileWriter('dummy_2.txt')
print(dir(file))
print(help(file.write_to_file))

l = [1, 2]
print(help(l.append))
