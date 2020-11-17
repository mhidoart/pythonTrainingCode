nums = [1,5,9,7]
while True:
    n = input("write a number : \n")
    if str(n).lower() == "q":
        break
    try:
        n=int(n)
    except:
        print("please write an integer ! \n")
        
    if n in nums:
        print("congrats you successfully guessed a number in the list try to guess another number or press q to quit. \n")
    else:
        print("try again !")
print("good bye, restart the program if u want to play agian")
