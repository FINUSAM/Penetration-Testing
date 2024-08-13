from PyPDF2 import PdfReader
reader = PdfReader("faheem.pdf")

import string
alpha = list(string.ascii_uppercase)
num = [0,1,2,3,4,5,6,7,8,9]
alphanum = alpha + num

count = 0

for i in range(len(alpha)):
    for m in range(len(alpha)):
        for l in range(len(alpha)):
            for k in range(len(alpha)):    
                for j in range(len(alpha)):
                    for n in range(len(alpha)):
                        PASSWORD = alpha[i] + alpha[m] + alpha[l] + alpha[k] + alpha[j] + "9814" + alpha[n]
                        try:
                            reader.decrypt(PASSWORD)
                            (len(reader.pages))
                            print(count, PASSWORD, "correct")
                            exit
                        except:
                            count = count + 1
                            if count%10000 == 0:
                                print(PASSWORD, "Incorrect")
