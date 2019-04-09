from tqdm import tqdm
import re

# https://www.mofa.go.jp/mofaj/files/000023536.pdfを参照
countries = {
    "Antigua and Barbuda": "Antigua_and_Barbuda",
    "Bosnia and Herzegovina": "Bosnia_and_Herzegovina",
    "Brunei Darussalam": "Brunei_Darussalam",
    "Burkina Faso": "Burkina_Faso",
    "Cape Verde": "Cape_Verde",
    "Central African Republic": "Central_African_Republic",
    "Costa Rica": "Costa_Rica",
    "Democratic People's Republic of Korea": "Democratic_People's_Republic_of_Korea",
    "Democratic Republic of the Congo": "Democratic_Republic_of_the_Congo",
    "Dominican Republic": "Dominican_Republic",
    "El Salvador": "El_Salvador",
    "Equatorial Guinea": "Equatorial_Guinea",
    "Guinea-Bissau": "Guinea_Bissau",
    "Guinea Bissau": "Guinea_Bissau",
    "Lao People's Democratic Republic": "Lao_People's_Democratic_Republic",
    "New Zealand": "New_Zealand",
    "Papua New Guinea": "Papua_New_Guinea",
    "Republic of Korea": "Republic_of_Korea",
    "Republic of Moldova": "Republic_of_Moldova",
    "Russian Federation": "Russian_Federation",
    "Saint Kitts and Nevis": "Saint_Kitts_and_Nevis",
    "Saint Lucia": "Saint_Lucia",
    "Saint Vincent and the Grenadines": "Saint_Vincent_and_the_Grenadines",
    "San Marino": "San_Marino",
    "Sao Tome and Principe": "Sao_Tome_and_Principe",
    "Saudi Arabia": "Saudi_Arabia",
    "Solomon Islands": "Solomon_Islands",
    "South Africa": "South_Africa",
    "South Sudan": "South_Sudan",
    "The formar Yugoslav Republic of Macedonia": "The_formar_Yugoslav_Republic_of_Macedonia",
    "Timor Leste": "Timor_Leste",
    "Trinidad and Tobago": "Trinidad_and_Tobago",
    "United Arab Emirates": "United_Arab_Emirates",
    "United Kingdom": "United_Kingdom",
    "United of Republic of Tanzania": "United_of_Republic_of_Tanzania",
    "Viet Nam": "Viet_Nam",
    "United States": "United_States"
}

if __name__ == "__main__":
    with open("corpus_tmp.txt", "r") as fp_read:

        with open("corpus.txt", "w") as fp_write:
            for line in tqdm(fp_read):
                for country in countries:
                    line = re.sub(country, countries[country], line)
                fp_write.write(line)
                fp_write.write("\n")
