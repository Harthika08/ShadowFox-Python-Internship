completed = 0
for i in range(10):
    completed += 10
    print("completed" , completed ,"jumping jacks")
    
    if completed == 100:
        print("Congratulations!,you completed the workout.")
        break
    tired = input("Are you tired?(yes/no): ").lower()
    
    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no):").lower()
        if skip == "yes" or skip =="y":
            print(f"you have completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"you have {100 - completed} jumping jacks remaining.")
    else:
        print(f"you have {100 - completed} jumping jacks remaining.")