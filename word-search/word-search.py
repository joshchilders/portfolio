import sys
import random


# Words to find
THEME_WORD_LIST  = {"office": ["MICHAEL", "DWIGHT", "JIM", "PAM", "ANDY", "STANLEY", "PHYLLIS", "ANGELA", "OSCAR", "KEVIN", "MEREDITH", "CREED", "RYAN", "KELLY", "TOBY", "DARRYL",
                    "HOLLY", "JAN", "ROY", "DAVID", "CHARLES", "GABE", "ERIN", "MOSE", "PETE", "CLARK", "BOBVANCE", "VIKRAM", "SCARN", "PAPER", "DUNDER", "MIFFLIN"],
                    "potter": ["HARRY", "RON", "HERMIONE", "HAGRID", "DRACO", "NEVILLE", "DUMBLEDORE", "MCGONAGALL", "SEVERUS", "VOLDEMORT", "SIRIUS", "HOGWARTS", "GRYFFINDOR", "HUFFLEPUFF", "RAVENCLAW", "SLYTHERIN",
                    "PADFOOT", "GINNY", "DOBBY", "TRELAWNEY", "FLITWICK", "UMBRIDGE", "SPROUT", "POMFREY", "DOBBY", "LUNA", "MYRTLE", "FILCH", "SNITCH", "WIZARD", "WITCH", "MAGIC"],
                    "lotr": ["FRODO", "SAMWISE", "BILBO", "MERRY", "PIPPIN", "GANDALF", "ARAGORN", "LEGOLAS", "GIMLI", "BOROMIR", "FARAMIR", "GOLLUM", "SMEAGOL", "SAURON", "SARUMAN", "STRIDER",
                    "MIDDLEEARTH", "SHIRE", "MORDOR", "RIVENDELL", "GONDOR", "ROHAN", "MORIA", "FANGORN", "HUMAN", "HOBBIT", "ELF", "DWARF", "ORC", "GOBLIN", "WIZARD", "RING"]}

# Grid size settings
DIFFICULTY_GRID_SIZE = {"easy": 20, "medium": 30, "hard": 40}
DIFFICULTY_WORD_AMOUNT = {"easy": 16, "medium": 24, "hard": 32}

def main():

    # Check command-line arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        sys.exit("Usage: 1. python word-search.py theme [filename]\n          -> available themes: office, potter, lotr")
    else:
        theme = sys.argv[1].lower()
        validTheme = False
        for key in THEME_WORD_LIST:
            if theme == key:
                validTheme = True
                words = get_word_list(theme)
                break
        if validTheme == False:
            sys.exit("Available themes: office, potter, lotr")
        # Open text file
        if len(sys.argv) == 3:
            fileName = sys.argv[2]
        else:
            fileName = "word-search"
        txtFile = open(f"{fileName}.txt", "w")
    
    # Get difficulty from user
    difficulty = get_difficulty()
    size = DIFFICULTY_GRID_SIZE[difficulty]
    amount = DIFFICULTY_WORD_AMOUNT[difficulty]

    # Create a grid of specific size based on difficulty
    grid = create_grid(size)

    # Hide words inside grid
    grid = hide_words(grid, size, words, amount)

    # Write answer key (before randomizing grid)
    write_answer_key(grid, size)

    # Randomize all other letters in grid
    grid = randomize_grid(grid, size)

    # Print puzzle to terminal
    print_puzzle(grid, size, words, amount)

    # Write puzzle to text file
    write_puzzle(grid, size, words, amount, txtFile)


def get_word_list(theme):

    words = []

    for i in range(len(THEME_WORD_LIST[theme])):
        words.append(THEME_WORD_LIST[theme][i])

    return words


def get_difficulty():

    while True:
        userInput = input("Difficulty: ").lower()
        if userInput == "easy" or userInput == "e":
            difficulty = "easy"
            break
        elif userInput == "medium" or userInput == "m":
            difficulty = "medium"
            break
        elif userInput == "hard" or userInput == "h":
            difficulty = "hard"
            break
    
    return difficulty


def create_grid(size):

    grid = []

    # Fill grid with "#" symbols to start
    for i in range(size):
        row = []
        for j in range(size):
            character = "#"
            row.append(character)
        grid.append(row)

    return grid


def hide_words(grid, size, words, amount):

    # Array of factors for each direction
    factor = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [1, 1], [-1, -1], [1, -1]]

    # Seed random number generator
    random.seed()

    # Generate random direction for each word
    i = 0
    while i < amount:
        word = words[i]
        direction = random.randint(0, 7)
        # Horizontal left-to-right
        if direction == 0:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - len(word))
        # Horizontal right-to-left
        elif direction == 1:
            row = random.randint(0, size - 1)
            col = random.randint(len(word) - 1, size - 1)
        # Vertical top-down
        elif direction == 2:
            row = random.randint(0, size - len(word))
            col = random.randint(0, size - 1)
        # Vertical bottom-up
        elif direction == 3:
            row = random.randint(len(word) - 1, size - 1)
            col = random.randint(0, size - 1)
        # Diagonal left-to-right bottom-up
        elif direction == 4:
            row = random.randint(len(word) - 1, size - 1)
            col = random.randint(0, size - len(word))
        # Diagonal left-to-right top-down
        elif direction == 5:
            row = random.randint(0, size - len(word))
            col = random.randint(0, size - len(word))
        # Diagonal right-to-left bottom-up
        elif direction == 6:
            row = random.randint(len(word) - 1, size - 1)
            col = random.randint(len(word) - 1, size - 1)
        # Diagonal right-to-left top-down
        elif direction == 7:
            row = random.randint(0, size - len(word))
            col = random.randint(len(word) - 1, size - 1)

        # Check to see if word will fit in this location
        checkRow = row
        checkCol = col
        for j in range(len(word)):
            if grid[checkRow][checkCol] == "#" or grid[checkRow][checkCol] == word[j]:
                checkRow += factor[direction][0]
                checkCol += factor[direction][1]
                fit = True
            else:
                fit = False
                i -= 1
                break
        
        # If word will fit, place word in grid
        if fit == True:
            for j in range(len(word)):
                grid[row][col] = word[j]
                row += factor[direction][0]
                col += factor[direction][1]
        
        i += 1

    return grid


def write_answer_key(grid, size):

    # Open answer key file
    ansFile = open("answer-key.txt", "w")

    # Write grid to text file
    for i in range(size):
        for j in range(size):
            ansFile.write(f"{grid[i][j]}  ")
        ansFile.write("\n")
    
    ansFile.close()

    return


def randomize_grid(grid, size):

    # Replace all remaining "#" symbols with random letters
    for i in range(size):
        for j in range(size):
            if grid[i][j] == "#":
                grid[i][j] = chr(random.randrange(65, 91))

    return grid


def print_puzzle(grid, size, words, amount):

    # Print board
    for i in range(size):
        for j in range(size):
            print(f"{grid[i][j]}  ", end="")
        print()
    print()
    
    # Print word list
    spacing = 15
    count = 0
    for i in range(amount):
        word = words[i]
        print(f"{word}" + (" " * (spacing - len(word))), end="")
        count += spacing
        if count == size * 3:
            print()
            count = 0
    print()

    return


def write_puzzle(grid, size, words, amount, txtFile):

    # Write grid to text file
    for i in range(size):
        for j in range(size):
            txtFile.write(f"{grid[i][j]}  ")
        txtFile.write("\n")

    # Write word list to text file
    txtFile.write("\n")
    spacing = 15
    count = 0
    for i in range(amount):
        word = words[i]
        txtFile.write(f"{word}" + (" " * (spacing - len(word))))
        count += spacing
        if count == size * 3:
            txtFile.write("\n")
            count = 0
    
    txtFile.close()

    return


main()