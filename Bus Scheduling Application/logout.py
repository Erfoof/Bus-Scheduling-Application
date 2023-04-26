def logout():
	answer = str(input("Do you want to log out? (Yes/No):"))
	while answer != "Yes" or "No" :
		print("Please input the right answer.")
		answer = input("Do you want to log out? (Yes/No):")
	if answer == Yes :
		loginmenu()
	elif answer == No :
		mainmenu()