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
    "Cote d'Ivoire": "Cote d'Ivoire",
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

rand = random.choice(list(quize.items()))
print(rand[1])

l = len(list(quize.items()))
print(l)