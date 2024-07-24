with open("./Input/Letters/starting_letter.txt") as letter:
    template = letter.read()
    with open("./Input/Names/invited_names.txt") as people:
        for name in people.readlines():
            body = template.replace("[name]", name.strip("\n"))
            with open(f"./Output/ReadyToSend/Letter_for_{name}.txt", "w") as readyLetter:
                readyLetter.write(body)
