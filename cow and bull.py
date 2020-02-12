rightNumber = '3341'
print('Welcome to the Cows and Bulls game!')
guessNumber = input('Enter a number:\n>>')
attempts = 1
cow = 0
bull = 0
rightNumberList = []
guessNumberList = []
while rightNumber != guessNumber:
    attempts += 1
#count cow
    for i in [0, 1, 2, 3]:
        if rightNumber[i] == guessNumber[i] :
            cow += 1
        else:
            rightNumberList.append(rightNumber[i])
            guessNumberList.append(guessNumber[i])
#count bull
    for n in guessNumberList:
        if n in rightNumberList:
            rightNumberList.remove(n)
            bull += 1
    print(cow, 'Cow(s)', bull, 'Bull(s)')
#restart
    cow = 0
    bull = 0
    rightNumberList = []
    guessNumberList = []
    guessNumber = input('Enter a number:\n>>')
#finish
print('4 Cow(s) 0 Bull(s)')
print('Well done! The correct number is:', rightNumber, '\nIt only took', attempts, 'attempts')   