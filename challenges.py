#region No globals
from tkinter import X
import types ,builtins
def no_globals(f):
    new_globals = {'__builtins__': builtins};new_f = types.FunctionType(f.__code__, globals=new_globals, argdefs=f.__defaults__);new_f.__annotations__ = f.__annotations__;return new_f
#endregion


# ignore this code ^
# ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
# ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
# ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
# ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
# ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
# ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝


# welcome to my python challenge
# the aim is to fill out the folowing functions so that they return the described results based on the input
# all code must be within the given functions
# speed should be your priority
# the @no_globals means that you cannot use variables from outside the function


# |-------------------------------CHALLENGE 1----------------------------------|
# |------------------alphabet list sort  from random letter order -----------|

@no_globals
def alphabetSort(letterList, nameList):
    # you will be provided a list of names and all the letters of the alphabet in the form of a list of letters as single letter strings
    # you must return a sorted list of names in alphabetical order based on the order of the alphabet provided
    # if 2 names have the same first letter move on to the secound and the third ect...
    # speed is prioritised, all code is to be inside this function
    # print statement are discouraged
    ...
    answerList = []
    
    
    
    
    return answerList


# |-------------------------------CHALLENGE 2----------------------------------|
# |------------------Find lowest prime number containg 2 given digets-----------|

@no_globals
def lowestPrimeIncSetPair(num1, num2):
    # you will be provided a pair of numbers and you must find the lowest prime number that contains both of the 2 digets provided
    # for example if you are given the digets [1] and [7]
    # [11] is a prime number but it needs both a [7] and a [1] so the answer is INCORRECT
    # [271] is a prime number that contains both numbers, but lower prime numbers are also valid so it is INCORRECT
    # [17] is a prime number that contains both numbers, there are no lower valid numbers, so the answer is CORRECT



    ans = 0
    return ans


# |-------------------------------CHALLENGE 3----------------------------------|
# |------------------------compare lists of numbers with 50% accuricy --------------------------|

@no_globals
def listCompare(list1, list2):
    # in this chalenge you musy compare 2 lists to see if they contain the same values (the order of the values is irrelevant)
    # the twist is that you only need to be accurate > 60% of the time and so you are encoruged to sacrifice accuricy for speed
    # note that you must be conscistantly over 60% accuricy throughout a test case of 10000 comparasons
    # here are some example of how the comparason works 
    # [a,b] == [b,a]
    # [a,b,c] != [b,c]
    # [a,a,b] != [a,b]
    # [a,a,b] == [a,b,a]
    
    

    
    return # [True | False]


# |--------------------------------CHALLENGE 4----------------------------------|
# |---------------------------- fun with algebra --------------------------------|
@no_globals
def findGraphEquation(pt1, pt2, pt3, pt4, pt5):
    # you will be give a set of 5 points taken from a line on a graph and you must find the equation of the graph
    # the graph can be exponental, linear or parabolic
    # return the equation  in the form of one the folowing lists
    # ["parabolic", a,b,c] where ax^2 + bx + c = 0
    # ["linear", a,b] where ax + b = 0
    # ["exponential", a,b,c] where ab^x +c = 0
    
    # a,b, & c are betwen -99 and 99

    equation = []

    return equation

































# don't change any of the code below this line

#region solution_timer_and_validator
import os, time, random, sys, threading

def spin_cursor():
    while True:
        for cursor in '|/-\\':
            sys.stdout.write(cursor)
            sys.stdout.flush()
            time.sleep(0.1) # adjust this to change the speed
            sys.stdout.write('\b')
            if spinnerDone:
                return
spinnerDone = True
spin_thread = threading.Thread(target=spin_cursor)
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def challengeStart(i):
    global spinnerDone
    print("checking challenge "+i)
    spinnerDone = False
def challangeResault(result):
    global spinnerDone
    if (result == "Invalid"):
        print(colored(250, 0, 0, result))
    else:
        print(colored(0, 250, 0, result/baseline())+"ms BL⁻¹")
    spinnerDone = True
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
os.system("CLS")
print(""*5+"Welcome")

def baseline():
    flip = True
    start = time.perf_counter()
    for i in range(0,10000):
        flip = (flip == False)
    return (time.perf_counter() - start)/10000

alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def q1():
    random.shuffle(alp)
    ans = []
    for i in range(len(alp)):
        for i2 in range(len(alp)):
            for i3 in range(len(alp)):
                ans.append(alp[i]+alp[i2]+alp[i3])
    for i in range(len(ans)//10):
        ans.remove(random.choice(ans))
        item = random.choice(ans)
        if ans.index(item)+1 < len(ans):
            ans[ans.index(item)+1] = item
    ans2 = ans.copy()
    random.shuffle(ans)
    return (ans2, ans, alp)
q1Input = q1()
challengeStart("1")
tic = time.perf_counter()
isCorrect = True
for i in range(100):
    userResault = alphabetSort(q1Input[2], q1Input[1])
    if userResault != q1Input[0]:
        isCorrect = False
        break
toc = time.perf_counter()
if (isCorrect):
    challangeResault((toc-tic)/100)
else:
    challangeResault("Invalid")

challengeStart("2")

primeList = []
for i in range(100):
    if is_prime(i*2-1):
        primeList.append(i*2-1)

def q2():
    while True:
        randomNum1 = random.randint(1,9)
        while True:
            randomNum2 = random.randint(1,9)
            if randomNum2 != randomNum1:
                break
        for i in range(len(primeList)):
            if str(primeList[i]).count(str(randomNum1)) > 0 and str(primeList[i]).count(str(randomNum2)) > 0:
                return (primeList[i], randomNum1, randomNum2)

isCorrect = True
tic = time.perf_counter()
for i in range(1000):
    q2Ans = q2()
    if q2Ans[0] != lowestPrimeIncSetPair(q2Ans[1], q2Ans[2]):
        isCorrect = False
        break
toc = time.perf_counter()
if (isCorrect):
    challangeResault((toc-tic)/1000)
else:
    challangeResault("Invalid")
challengeStart("3")

def q3():
    stringList = []
    for i in range(50):
        stringList.append(random.choice(alp)*random.randint(1,5))
    stringList2 = []
    if random.choice([True, False]):
        for i in range(50):
            stringList2.append(random.choice(alp)*random.randint(1,5))
    else:
        stringList2 = stringList.copy()
        random.shuffle(stringList)
    return (stringList, stringList2)

isCorrect = True
tic = time.perf_counter()

wrong = 0
for i in range(10000):
    q3Ans = q3()
    q3Ans[0].sort()
    q3Ans[1].sort()
    if (q3Ans[0] == q3Ans[1]) != listCompare(q3Ans[0], q3Ans[1]):
        wrong += 1
if wrong > 4000:
    isCorrect = False
toc = time.perf_counter()
if (isCorrect):
    challangeResault((toc-tic)/10000)
else:
    challangeResault("Invalid")

def q4():
    a =  random.randint(-99,99)
    if a == 0: a = 1
    b =  random.randint(-99,99)
    if b == 0: b = 1
    c =  random.randint(-99,99)
    if c == 0: c = 1
    coords = []
    equType = random.choice(["parabolic", "linear", "exponential"])
    if (equType == "linear"):
        for i in range(5):
            x = random.randint(-99,99)
            coords.append([x, a*x+b])
        return(coords, equType, a, b, c)
    if (equType == "parabolic"):
        for i in range(5):
            x = random.randint(1,99)
            coords.append([x, a*x**2+b*x+c])
        return(coords, equType, a, b, c)
    if (equType == "exponential"):
        for i in range(5):
            x = random.randint(1,99)
            coords.append([x, a*(b**(x)) +c])
        return(coords, equType, a, b, c)

isCorrect = True
tic = time.perf_counter()
challengeStart("4")

for i in range(100):
    q4Ans = q4()
    userq4Ans = findGraphEquation(q4Ans[0][0], q4Ans[0][1], q4Ans[0][2], q4Ans[0][3], q4Ans[0][4])
    if len(userq4Ans) != 4:
        isCorrect = False
        break
    if userq4Ans[0] != q4Ans[1]:
        isCorrect = False
    if userq4Ans[0] == "linear":
        x = random.randint(-99,99)
        if userq4Ans[1]*x+userq4Ans[2] != q4Ans[2]*[x]+q4Ans[3]:
            isCorrect = False
            break
    elif userq4Ans[0] == "exponential":
        x = random.randint(-99,99)
        if userq4Ans[1]*x+userq4Ans[2] != q4Ans[2]*[x]+q4Ans[3]:
            isCorrect = False
            break
    elif userq4Ans[0] == "exponential":
        x = random.randint(-99,99)
        if userq4Ans[1]*x+userq4Ans[2]**x+userq4Ans[3] != q4Ans[1]*q4Ans[2]*[x]+q4Ans[3]:
            isCorrect = False
            break

tok = time.perf_counter()
if (isCorrect):
    challangeResault((toc-tic)/100)
else:
    challangeResault("Invalid")


#endregion