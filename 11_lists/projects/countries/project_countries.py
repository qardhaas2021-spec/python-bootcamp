countries = [
    "Nigeria", "Brazil", "Japan", "Germany", "Somalia", "Canada",
    "Australia", "India", "France", "Chad", "Peru", "Oman",
    "United States", "United Kingdom", "New Zealand", "Afghanistan",
    "Mexico", "Egypt", "Italy", "China", "UAE", "Fiji", "Cuba",
    "Argentina", "Pakistan", "Indonesia", "Turkey", "Iran", "Iraq",
    "Saudi Arabia", "South Africa", "Kenya", "Ethiopia", "Sudan",
    "Uganda", "Tanzania", "Ghana", "Cameroon", "Senegal", "Mali",
    "Niger", "Libya", "Algeria", "Morocco", "Tunisia", "Angola",
    "Mozambique", "Madagascar", "Zimbabwe", "Zambia", "Rwanda",
    "Burundi", "Malawi", "Botswana", "Namibia", "Lesotho",
    "Eswatini", "Togo", "Benin", "Ivory Coast", "Guinea",
    "Sierra Leone", "Liberia", "Gambia", "Mauritania", "Eritrea",
    "Djibouti", "Comoros", "Seychelles", "Cape Verde", "Gabon",
    "Congo", "South Sudan", "Central African Republic", "Equatorial Guinea",
    "Spain", "Portugal", "Netherlands", "Belgium", "Switzerland",
    "Austria", "Sweden", "Norway", "Denmark", "Finland", "Poland",
    "Ukraine", "Romania", "Hungary", "Czech Republic", "Slovakia",
    "Croatia", "Serbia", "Bulgaria", "Greece", "Albania", "Kosovo",
    "North Macedonia", "Bosnia", "Slovenia", "Montenegro", "Moldova",
    "Belarus", "Lithuania", "Latvia", "Estonia", "Russia", "Georgia",
    "Armenia", "Azerbaijan", "Kazakhstan", "Uzbekistan", "Turkmenistan",
    "Kyrgyzstan", "Tajikistan", "Mongolia", "Nepal", "Bangladesh",
    "Sri Lanka", "Myanmar", "Thailand", "Vietnam", "Cambodia",
    "Laos", "Malaysia", "Singapore", "Philippines", "Taiwan",
    "South Korea", "North Korea", "Yemen", "Jordan", "Lebanon",
    "Syria", "Israel", "Palestine", "Kuwait", "Qatar", "Bahrain",
    "Cyprus", "Iceland", "Ireland", "Luxembourg", "Malta", "Liechtenstein",
    "Andorra", "Monaco", "San Marino", "Vatican",
    "Colombia", "Venezuela", "Chile", "Ecuador", "Bolivia", "Paraguay",
    "Uruguay", "Guyana", "Suriname", "Panama", "Costa Rica", "Nicaragua",
    "Honduras", "El Salvador", "Guatemala", "Belize", "Jamaica",
    "Haiti", "Dominican Republic", "Trinidad and Tobago", "Barbados",
    "Bahamas", "Maldives", "Bhutan", "Timor-Leste", "Papua New Guinea",
    "Samoa", "Tonga", "Vanuatu", "Kiribati", "Palau", "Nauru", "Tuvalu",
    "New Zealand", "Micronesia", "Marshall Islands", "Solomon Islands",
]
countries.sort()
print(countries)

lenght = [len(c) for c in countries]
print(lenght)

max_lenght = max(lenght)
print(max_lenght)

longest_names = [c for c in countries if len(c) == max_lenght]
print(longest_names)

shortest_names = [c for c in countries if len(c) == min(lenght)]
print(f'counries with the shortest names:{shortest_names}')





