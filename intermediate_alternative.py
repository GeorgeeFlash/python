"""
    A quize program that tests users on thier knowledge on
    African countries and their capitals.

    
"""
import random

quize = {
    "South Africa": "Pretoria",
    "Nigeria": "Abuja",
    "Egypt": "Cairo",
    "Algeria": "Algiers",
    "Ethiopia": "Addis Ababa",
    "Morocco": "Rabat",
    "Kenya": "Nairobi",
    "Angola": "Luanda",
    "Cote d'Ivoire": "Yamoussoukro",
    "Tanzania": "Dar es Salaam",
    "Ghana": "Accra",
    "DRC": "Kinshasa",
    "Uganda": "Kampala",
    "Tunisia": "Tunis",
    "Cameroon": "Yaounde",
    "Zimbabwe": "Harare",
    "Libya": "Tripoli",
    "Senegal": "Dakar",
    "Zambia": "Lusaka",
    "Sudan": "Khartoum",
}

country, capital = random.choice(list(quize.items()))
quize_list = list(quize.items())
quize_length = len(quize_list)
repeat_quize = 'yes'

while repeat_quize == 'yes':
    for question_num in range(quize_length):
        print(f"What is the capital of {country}")
        rand = random.choice(list(quize.items()))
        print(f"A. {capital} B. {rand[1]}")
        user_response = input("Type Response: ")
        if user_response.lower() == capital.lower():
            print("Correct!")
        else:
            print("Wrong!")
            print(f"Ans: ", capital)
            print(f"user_response: ", user_response)
    repeat_quize = input("Do you wish to repeat the quize? (type 'yes' or 'no'): ")
    
