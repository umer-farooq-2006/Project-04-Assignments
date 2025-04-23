def mad_libs():
    print("Let's create a funny story! Fill in the blanks:")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")

    story = f"""
    Once upon a time in {place}, there was a very {adjective} {noun}.
    Every day, it {verb} around the town making everyone feel {emotion}.
    The end!
    """

    print("\nHere's your Mad Libs story:")
    print(story)

# Run the game
mad_libs()
