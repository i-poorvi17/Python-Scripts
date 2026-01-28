
def search(filename, word):
    found = 0
    with open(filename, 'r') as f:
        for line_no, line in enumerate(f, start=1):
            words = line.strip().split()
            if word in words:
                print(f"Word '{word}' found on line {line_no}")
                found +=1
    if not found :
        print(f"Word '{word}' not found in the file.")

filename =input('enter the file name') 
word = input("Enter the word to search: ")
search(filename, word)


word=input('enter the word')
with open ("try.txt",'r') as f:
    content= f.read()
    if(word in content):
        print("found")
    else:
        print("sorry")
    

