# file = open("Ouch.txt")
# text = file.read()
# print(text)
# file.close()

with open("Ouch.txt",'a') as f:

    f.write('\nThis is something new, isn\'t it?')
    print(help(open))