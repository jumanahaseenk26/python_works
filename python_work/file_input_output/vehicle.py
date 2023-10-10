f=open("C:\\Users\\hp\\Desktop\\python_works\\file_input_output\\number.txt")
numbers=[line.rstrip("\n") for line in f]
kerala_reg=[n for n in numbers  if n.startswith("kl")]
print(kerala_reg)