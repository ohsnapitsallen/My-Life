#Create a function where the program asks the user to enter lines then writes the input to the text file
def mylife():
    with open("mylife.txt", "a") as output_file:
        content = str(input("Enter line: "))
        output_file.write(str(content) + "\n")

morelines = ' '
#Create a loop to ask the user if they want to write more lines to the file
while morelines != "n":
    mylife()
    print("Are there more lines? y/n")
    morelines = input()
#Starts the function again if user wants to write more
  if morelines == "y":
      print("Please enter another line")
      #Ends the program if the user is done
  elif morelines == "n":
      break
#Restarts the loop if the input is an invalid response
   else:
       print("Invalid input, please try again.")
