quiz = {"What is my name:":"B",
        "What is my current county ":"A",
        "How old am I ":"A" ,
        "Which food do I like most ":"C",
        "Which place that I got born ":"D",
        "Which one of the following is not a programmming language":"B"}

answ = [["A. John","B. Joseph","C. Mark","D. Both"],
        ["A. Taita Taveta","B. Mombasa","C. Nairobi","D. Kisii"],
        ["A. 20","B. 18","C. 21","D. 19"],
        ["A. Ugali","B. Pilau","C. Chicken","D. Fish"],
        ["A. Emuhaya","B. Maseno","C. Hamisi","D. Luanda"],
        ["A. C++","B. HTML","C. Python","D. None of the of the above"]]
qiuz_num = 1
correct = 0
got = []
for i in quiz:
    print("------------------------------------")
    print(i)
    for j in answ[qiuz_num-1]:
        print(j)
    qiuz_num += 1
    guess = input("Choose A, B, C, D,").upper()
    got.append(guess)
    if guess == quiz.get(i):
        print("Correct!!!")
        correct = correct + 1
    else:
        print("Wrong!!!")
print("\n\nCorrect answers are: ",end=' ')
for n in quiz:
    print(quiz.get(n),end=' ')
print("\nYour choices are:   ",end=' ')
for m in got:
    print(m,end=' ')
print()
score = (correct/len(quiz))*100
if score >50:
    print("You have passed passmark Congragulations!!!!")
elif score >0 and score < 50:
    print("You tried")
elif score == 50:
    print("Average")
else:
    print("You failed...")
print("You got", correct, "question(s) correct which is {:.1f}%".format(score))
print("\n------------------CREATED BY JOSEPH-------------------\n")
