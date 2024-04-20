

def dictionary(word):
    dict_words = {
        "sheen" : "Beautiful, good-looking, attractive, radiant, shiny.",
        "innate" : "Inborn: existing or having existed since birth.",
        "claik" : "To honk or cry like a goose.",
        "exercise" : "Any activity designed to develop or hone a skill or ability.",
        "reflexible" : "Capable of being reflected, or thrown back.",
        "slow-motional" : "Resembling or relating to slow motion.",
        "prowl" : "To role ober, through, or about in a stealthy manner, especially, to search in, as for prey or booty.",
        "booty": "A form of prize which, when a ship was captured at sea, could be distributed at once",
        "loo" : "A lavatory: a room used for urication and defecation.",
        "lavatory" : "A vessel or fixture for washing."
    }
    try:
        print(f"{word} : {dict_words[word]}")
    except KeyError as e:
        print("Error: ", e, "does not exist in the dictionary!")
    


user_input = input("Enter word: ")
dictionary(user_input)