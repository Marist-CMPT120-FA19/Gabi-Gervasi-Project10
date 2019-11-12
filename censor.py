
def censor(word):
    for i in range(len(word)):
        if word[i].isalpha():
            word=word[:i] + '*' + word [i+1:]
    return word



def main():
    file= input ("Enter the name of the file to censor: ")
    text= open(file, 'r')
    words_file= input ("Enter the name of the file containing the censord words: ")
    censored= open(words_file, 'r')
    censored_words= censored.read().split()

    censored_text= ""
    for line in text:
        words=line.split()
        for i in range(len(words)):
            word= ""
            for letter in words [i]:
                if letter.isalpha():
                    word+= letter
            if word in censored_words:
                words[i]= censor(words[i])
        censored_text += " ".join(words) + '\n'

        text.close()
        censored.close()

        newfile=open("censored:" + file, 'w')
        newfile.write(censored_text)
        newfile.close()
        
        

        

main()

            
