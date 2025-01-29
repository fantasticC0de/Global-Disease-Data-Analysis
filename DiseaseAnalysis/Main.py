import pandas as pd
import matplotlib as plt
import time
import random

# Variables

Data_Title = '''

-------------------------------------------------

Global Health - Jordan James-Vinales

-------------------------------------------------
'''

Selected_Year = 0
Selected_Disease = ""
Selected_Country = ""
Selected_Information = ""

GlobalHealthDataTable = "/Users/Student/Engineering Practicum/DiseaseAnalysis/Data/GlobalHealth.csv"
df = pd.read_csv(GlobalHealthDataTable)

# Functions

def Random_Response():
    responses = ["Great!", "Interesting!", "Amazing!", "Wonderful!", "Great!"]
    return random.choice(responses)

def Welcome_Message():
    print("Welcome to the Global Health Statistic's data table!\n")
    time.sleep(2)
    print("Here you will be able see the effects diseases have/had on countries of your choice.\n")

def Prompt_Options():
    global Selected_Country
    global Selected_Disease
    global Selected_Year
    global Selected_Information
    
    
    while True:
        CountryInput = input("Select a country:\n 1. Russia(R)\n 2. USA(U)\n 3. Canada(C)\n 4. Mexico(M)\n 5. Japan(J) ").upper()
        if CountryInput == "R":
            Selected_Country = "Russia"
            break
        elif CountryInput == "U":
            Selected_Country = "USA"
            break
        elif CountryInput == "C":
            Selected_Country = "Canada"
            break
        elif CountryInput == "M":
            Selected_Country = "Mexico"
            break
        elif CountryInput == "J":
            Selected_Country = "Japan"
            break
        else:
            if CountryInput.isdigit():
                print("\nSelect a country using a letter only\n")
            else:
                if len(CountryInput) != 1:
                    print("\nInput should be 1 character long\n")
                else:
                    print("\nPlease select a listed country (R, U, C, M or J)\n")
            time.sleep(2)

    print("")
    print(Random_Response())
    print("")
    
    time.sleep(1)

    while True:
        YearInput = input("Select a year between 2014-2024 by typing the last 2 digits: ")
        
        try:
            if 14 <= int(YearInput) <= 24:
                year = 2000 + int(YearInput)
                Selected_Year = year
                break
            else:
                print("")
                print("Invalid input. Please enter a number between 14 and 24.")
                print("")

        except:
            print("")
            print("Please use numbers.")
            print("")

    time.sleep(1)

    while True:
        print("")
        DiseaseInput = input("Select a disease:\n 1. Ebola(E)\n 2. Cancer(C)\n 3. COVID-19(CV)\n 4. Parkinson's Disease(P)\n 5. Rabies(R)\n 6. Tuberculosis(T) ").upper()

        if DiseaseInput == "E":
            Selected_Disease = "Ebola"
            break
        elif DiseaseInput == "C":
            Selected_Disease = "Cancer"
            break
        elif DiseaseInput == "CV":
            Selected_Disease = "COVID-19"
            break
        elif DiseaseInput == "P":
            Selected_Disease = "Parkinson's Disease"
            break
        elif DiseaseInput == "R":
            Selected_Disease = "Rabies"
            break
        elif DiseaseInput == "T":
            Selected_Disease = "Tuberculosis"
            break
        else:
            if DiseaseInput.isdigit():
                print("\nSelect a disease using a letter only\n")
            else:
                if len(DiseaseInput) != 2:
                    print("\nInput should be 1 or 2 characters long\n")
                else:
                    print("\nPlease select a listed disease (E, C, CV, P, R, T)\n")
            time.sleep(2)
    
    time.sleep(1)

    while True:
        print("")
        SelectedInformationInput = input("Select a research topic:\n 1. Mortality rate(M)\n 2. Prevalence Rate(P)\n 3. Incidence Rate(I)\n 4. Recovery Rate(R)\n 5. Population Affected(PA) ").upper()

        if SelectedInformationInput == "M":
            Selected_Information = "Mortality Rate (%)"
            break
        elif SelectedInformationInput == "P":
            Selected_Information = "Prevalence Rate (%)"
            break
        elif SelectedInformationInput == "I":
            Selected_Information = "Incidence Rate (%)"
            break
        elif SelectedInformationInput == "R":
            Selected_Information = "Recovery Rate (%)"
            break
        elif SelectedInformationInput == "PA":
            Selected_Information = "Population Affected"
            break
        else:
            if SelectedInformationInput.isdigit():
                print("\nSelect a topic using a letter only\n")
            else:
                if len(SelectedInformationInput) != 2:
                    print("\nInput should be 1 or 2 characters long\n")
                else:
                    print("\nPlease select a listed disease (M, P, I, R, PA)\n")
            time.sleep(2)


# Template:

#Selcted_Country = df[(df['Year'] == 2020) & (df['Disease Name'] == "COVID-19") & (df['Country'] == "Russia")]
#print(Selcted_Country["Prevalence Rate (%)"].head(1).values)

# Game Functionality:

print(Data_Title)

time.sleep(1)

Welcome_Message()

time.sleep(3)

Prompt_Options()
print("")
print("Fetching data...")
time.sleep(2)
print("")

Selcted_data = df[(df['Year'] == Selected_Year) & (df['Disease Name'] == Selected_Disease) & (df['Country'] == Selected_Country)]
result_data = Selcted_data[Selected_Information].head(1).values

print(Selected_Country,"in",Selected_Year,"had a",Selected_Information,"of",result_data,"from",Selected_Disease)

