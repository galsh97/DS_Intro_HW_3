#1
def read_line(n=input('Enter a line number: '), file= input('Enter file name: ')):
    try:
        n = int(n)
        file = open(file, 'r')
        line = file.readlines()
        return print(line[n-1])
    
    except FileNotFoundError:
         print('File not found')
         
    except ValueError:
         print('Invalid input detected')

    except IndexError:
         print('line' + " " + str(n) + " "  + "dosen't exist.")

#2
import re
def logest_words(file=input('Enter file name: ')):
    try:
        file = open(file, 'r')
        word = []
        for line in file:
            word.append(re.split('\W', line))
        longest = []
        listi = []
        for ww in word:
            for w in ww:  
                listi.append(w)
        for i in range(5):
            longest.append(max(listi, key=len))
            listi.remove(max(listi, key=len))
        return print(longest)   
    except:
        print("File not found")
        return []
    


