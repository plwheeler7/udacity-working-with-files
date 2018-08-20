# Bad word detector program
import string
import random

rude_words = ["shit", "ass", "darn", "blast","fudge", "moiste", "kerfluffle", "smelly", "splat", "sophestry",]
print (string.punctuation)

with open("output_file.txt",'w',encoding = 'utf-8') as f: # opens new file, overwrties old, keeps file open while with function open
   f.write("Clean Program\n\n")

            # f = open("output_file.txt","w") - alternate to above
            # f.write("Clean Program\n\n")
            # f.close()

def check_line(line):
    words = line.split(" ")
    
    rude_count = 0
    new_line = []
    for i in words:
        i=i.strip(string.punctuation)
        i2 = i
        i=i.lower()
        # print(f"word = {i} ")
        if i in rude_words:
            rude_count +=1
            print(f"Shame on you!, your file has the word {i} in it!")
            new_word = ""
            for n in i:
                new_word= new_word+random.choice(string.punctuation)
                # new_word="*"*len(i)
            # print(i,new_word)
            line = line.replace(i2,new_word)
            # print(line)
            # print(new_line)
    f = open("output_file.txt","a") #appending to newly created file above
    f.write(line)
    f.close()
    return rude_count

# using the with function closes file when complete

def check_file(file_name):
    with open(file_name) as myfile:
        rude_count = 0
        for line in myfile:
            rude_count += check_line(line)
      
    if rude_count == 0:
        print("You are a saint!")
    else: 
        print(f"You have a whopping {rude_count} rude words in your file!")
        # print(rude_count)


# use __name_=='__main__' to tell python not to run all modules just when program is opened??
if __name__ == '__main__':
    check_file("README.me")


        
    



