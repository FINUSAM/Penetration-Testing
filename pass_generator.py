import string
alpha = list(string.ascii_uppercase)
num = [0,1,2,3,4,5,6,7,8,9]
alphanum = alpha + num

PASSWORD = "AAAAA 0000 A"

for i in range(len(alpha)):
    for m in range(len(alpha)):
        for l in range(len(alpha)):
            for k in range(len(alpha)):    
                for j in range(len(alpha)):
                    PASSWORD = alpha[i] + alpha[m] + alpha[l] + alpha[k] + alpha[j]
                    print(PASSWORD)