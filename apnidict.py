"""this is a program in which you will enter the 
word from the given choice and you will know the meaning of that word """
print("choose any  word from the   word given below \n 1.set \n 2. list \n 3. tuple \n 4.variables \n 5. dictionaries")
word=input()
dict={"set":"A set is a collection which is unordered, unchangeable*, and unindexed.","list":"Lists are used to store multiple items in a single variable.","tuple":"Tuples are used to store multiple items in a single variable","variable":"Variables are containers for storing data values.","dictionaries":"Dictionaries are used to store data values in key:value pairs."}
print(dict[word])
