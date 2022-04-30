# program to generate html code to make forms
# types of form inputs are entered by user

# example output:
#                First name: <br>
#                <input type="text" name="fname" size="30" maxlength="30" required><br><br>
#                
#                Surname: <br>
#                <input type="text" name="sname" size="30" maxlength="30" required><br><br>
#                
#                Number of guests (between 1 and 6): <br>
#                <input type="number" name="people" min="1" max="6" required><br><br>
#                
#                Indoors/Outdoors: <br>
#                <input type="radio" name="whereEat" value="indoors" required>Indoors
#                <input type="radio" name="whereEat" value="outdoors" required>Outdoors<br><br>
#                
#                Select resteraunt: 
#                <select name="restaurant" multiple>
#                    <option value="dmains">Davidson's Mains</option>
#                    <option value="stockbridge">Stockbridge</option>
#                    <option value="blackhall">Blackhall</option>
#                    <option value="pentlands">Pentlands</option>
#                    <option value="balerno">Balerno</option>
#                </select><br><br>
#                
#                Please enter any dietary requirements: <br>
#                <textarea cols="30" rows="5">N/A</textarea><br><br>
#                
#                <button type="submit" value="submit" onclick="alert('Form entered')">Submit</button>

mainStr = "\n\n"

def getNumOfInputs(): # gets how many input types
    numOfInputs = input("Enter how many form inputs to add: ")
    while type(numOfInputs) != int:
        try:
            numOfInputs = int(numOfInputs)
        except ValueError: # checks if input is a number
            print("Error, input must be a number.")
            numOfInputs = input("Please enter how many form inputs to add again: ")

    return numOfInputs


def getTypeOfInputs(numOfInputs): # gets which type of input each input is
    inputs = []
    valids = ['1', '2', '3', '4', '5']
    for i in range(numOfInputs):
        print("Pick an input type: ")
        print("""
        [1] text
        [2] number
        [3] radiobutton
        [4] dropdown
        [5] textarea
        """)
        currentInput = input()
        while currentInput not in valids:
            print("Error, please enter one of the values in square")
            currentInput = input()

        inputs.append(int(currentInput))

    return inputs


def parseInputs(inputs, mainStr): # goes through all inputs and appends appropriate info to mainStr
    for inp in inputs:
        if inp == 1: # text
            title = input("\nEnter the title of the text input: ")
            textName = input("Enter the name of the text input: ")
            textSize = input("Enter the size of the text input (enter 0 to not include size): ")
            textMaxLength = input("Enter the max length of the text input (enter 0 to not include max length): ")

            textRequired = input("Enter [Y/N] if the text input is required: ")
            while textRequired.upper() != "Y" and textRequired.upper() != "N":
                print("Error, required value must be either [Y] or [N]")
                textRequired = input("Enter [Y/N] if the text input is required: ")

            mainStr = mainStr + title + ': <br>\n<input type="text" name="' + textName + '"'

            if textSize != "0":
                mainStr = mainStr + ' size="' + textSize + '"'
            if textMaxLength != "0":
                mainStr = mainStr + ' maxlength="' + textMaxLength + '"'
            if textRequired.upper() == "Y":
                mainStr = mainStr + ' required'

            mainStr = mainStr + '><br><br>\n\n'

        elif inp == 2: # number
            numTitle = input("\nEnter the title of the number input: ")
            numName = input("Enter the name of the number input: ")
            numMax = input("Enter the maximum value of the number input (enter 0 to not include maximum): ")
            numMin = input("Enter the minimum value of the number input (enter 0 to not include minimum): ")

            numRequired = input("Enter [Y/N] if the number input is required: ")
            while numRequired.upper() != "Y" and numRequired.upper() != "N":
                print("Error, required value must be either [Y] or [N]")
                numRequired = input("Enter [Y/N] if the number input is required: ")

            mainStr = mainStr + numTitle + ': <br>\n<input type="number" name="' + numName + '"'

            if numMax != "0":
                mainStr = mainStr + ' max="' + numMax + '"'
            if numMin != "0":
                mainStr = mainStr + ' min="' + numMin + '"'
            if numRequired.upper() == "Y":
                mainStr = mainStr + ' required'

            mainStr = mainStr + '><br><br>\n\n'

        elif inp == 3: # radiobutton
            radioTitle = input("\nEnter the title for the radiobutton: ")

            mainStr = mainStr + radioTitle + ': <br>\n'

            buttons = input("Enter the amount of options in the radiobutton: ")
            while type(buttons) != int:
                try:
                    buttons = int(buttons)
                except ValueError: # checks if input is a number
                    print("Error, input must be a number.")
                    buttons = input("Enter the amount of options in the radiobutton: ")
            
            buttonName = input("Enter the name of the options: ")
            for i in range(buttons):
                buttonValue = input("Enter the value of option ["+str(i+1)+"]: ")

                buttonRequired = input("Enter [Y/N] if option ["+str(i+1)+"] is required: ")
                while buttonRequired.upper() != "Y" and buttonRequired.upper() != "N":
                    print("Error, required value must be either [Y] or [N]")
                    buttonRequired = input("Enter [Y/N] if option ["+str(i+1)+"] is required: ")

                buttonTitle = input("Enter the title of option ["+str(i+1)+"]: ")

                mainStr = mainStr + '<input type="radio" name="' + buttonName + '" value="' + buttonValue + '"'

                if buttonRequired.upper() == "Y":
                    mainStr = mainStr + ' required'
                
                mainStr = mainStr + '>' + buttonTitle + '\n'

            mainStr = mainStr + '<br><br>\n\n'

        elif inp == 4: # dropdown
            dropTitle = input("\nEnter the title for the dropdown: ")
            dropName = input("Enter the name of the dropdown: ")

            dropMultiple = input("Enter if multiple options are able to be selected [Y/N]: ")
            while dropMultiple.upper() != "Y" and dropMultiple.upper() != "N":
                print("Error, please enter either [Y] or [N]")
                dropMultiple = input("Enter if multiple options are able to be selected [Y/N]: ")

            mainStr = mainStr + dropTitle + ':\n<select name="' + dropName + '"'

            if dropMultiple.upper() == "Y":
                mainStr = mainStr + ' multiple'
            
            mainStr = mainStr + '>\n'

            options = input("Enter the amount of options in the dropdown: ")
            while type(options) != int:
                try:
                    options = int(options)
                except ValueError: # checks if input is a number
                    print("Error, input must be a number.")
                    options = input("Enter the amount of options in the dropdown: ")

            for i in range(options):
                optionValue = input("Enter the value of option ["+str(i)+"]: ")
                optionTitle = input("Enter the title for option ["+str(i)+"]: ")

                mainStr = mainStr + '\t<option value="' + optionValue + '">' + optionTitle + '</option>\n'

            mainStr = mainStr + '</select><br><br>\n\n'

        else: # textarea
            areaTitle = input("\nEnter the title of the textarea input: ")
            areaCols = input("Enter the number of columns in the textarea (enter 0 to not include the number of columns): ")
            areaRows = input("Enter the number of rows in the textarea (enter 0 to not include the number of rows): ")
            areaDefaultVal = input("Enter the placeholder value inside the textarea (leave blank to leave placeholder value empty): ")

            mainStr = mainStr + areaTitle + ': <br>\n<textarea'

            if areaCols != "0":
                mainStr = mainStr + ' cols="' + areaCols + '"'
            if areaRows != "0":
                mainStr = mainStr + ' rows="' + areaRows + '"'

            mainStr = mainStr + '>'

            if areaDefaultVal != '':
                mainStr = mainStr + areaDefaultVal

            mainStr = mainStr + '</textarea><br><br>\n\n'

    submitTitle = input("\nEnter the title for the submit button: ")
    submitValue = input("Enter the value for the submit button: ")

    submitOnClick = input("Enter [Y/N] if an alert should appear when the submit button is clicked: ")
    while submitOnClick.upper() != "Y" and submitOnClick.upper() != "N":
        print("Error, please enter either [Y] or [N]")
        submitOnClick = input("Enter [Y/N] if an alert should appear when the submit button is clicked: ")

    if submitOnClick.upper() == "Y":
        submitAlert = input("Enter the alert message which appears when the submit button is clicked: ")
        submitAlert = "'" + submitAlert + "'"

        mainStr = mainStr + '<button type="submit" value="' + submitValue + '" onclick="alert(' + submitAlert + ')">' + submitTitle + '</button>'

    else:
        mainStr = mainStr + '<button type="submit" value="' + submitValue + '">' + submitTitle + '</button>'


    return mainStr


numOfInputs = getNumOfInputs()
inputs = getTypeOfInputs(numOfInputs)
mainStr = parseInputs(inputs, mainStr)
print("Copy and paste the following HTML code into the <form> tag:\n\n")
print(mainStr)
print("\n\n")
