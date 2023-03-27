import pandas as pd
import matplotlib.pyplot as plt
import os
from time import sleep

#ADD A REQUIREMENTS.TXT FILE (IVAN)
#LOOK AT RESOLVING THE WARNINGS WITH FIXEDFORMATTER AND FIXEDLOCATOR (JAMES)
#CREATE A WAY FOR USERS TO CONTINUE INPUT AFTER INITIAL INPUT -OR- EXPLAIN IN THE README THAT THE USER NEEDS TO EXIT THE GRAPH WINDOW (JAMES)
#UPDATE README WITH CHANGES MADE LIKE THE FILE HAS A .PY NOW AND REQUIREMENTS.TXT FILE HAS ALL OF THE REQUIRED PACKAGES

#Loads data into a DataFrame from a file located in this project's 'assets' folder as part of the data reading feature (Feature #1) in this project's README file
columns = ["Bird Type", "March 1 - May 31 (Spring)", "June 1 - August 31 (Summer)", "September 1 - November 30 (Autumn)", "December 1 - February 28 (Winter)"]
df = pd.read_csv("assets/Bird_Sightings_Annville_KY.csv", usecols=columns)

#Acquires information about least and most sighted birds using functions as part of the custom functions feature (Feature #3) in this project's README file
def get_most_sighted_bird(df, season):
    return df.loc[df[season].idxmax(), "Bird Type"]
def get_least_sighted_bird(df, season):
    return df.loc[df[season].idxmin(), "Bird Type"]

#This function shows graphs for the most and least sighted birds across all seasons in a side-by-side format
def menu_option_1():
    #Acquires information about seasonal bird sightings using functions as part of the custom functions feature (Feature #3) in this project's README file
    most_sighted_spring = get_most_sighted_bird(df, "March 1 - May 31 (Spring)")
    least_sighted_spring = get_least_sighted_bird(df, "March 1 - May 31 (Spring)")
    most_sighted_summer = get_most_sighted_bird(df, "June 1 - August 31 (Summer)")
    least_sighted_summer = get_least_sighted_bird(df, "June 1 - August 31 (Summer)")
    most_sighted_autumn = get_most_sighted_bird(df, "September 1 - November 30 (Autumn)")
    least_sighted_autumn = get_least_sighted_bird(df, "September 1 - November 30 (Autumn)")
    most_sighted_winter = get_most_sighted_bird(df, "December 1 - February 28 (Winter)")
    least_sighted_winter = get_least_sighted_bird(df, "December 1 - February 28 (Winter)")

    x1 = [most_sighted_spring, least_sighted_spring]
    y1 = [df.loc[df["Bird Type"] == most_sighted_spring, "March 1 - May 31 (Spring)"].values[0], 
      df.loc[df["Bird Type"] == least_sighted_spring, "March 1 - May 31 (Spring)"].values[0]]
    x2 = [most_sighted_summer, least_sighted_summer]
    y2 = [df.loc[df["Bird Type"] == most_sighted_summer, "June 1 - August 31 (Summer)"].values[0], 
      df.loc[df["Bird Type"] == least_sighted_summer, "June 1 - August 31 (Summer)"].values[0]]
    x3 = [most_sighted_autumn, least_sighted_autumn]
    y3 = [df.loc[df["Bird Type"] == most_sighted_autumn, "September 1 - November 30 (Autumn)"].values[0], 
      df.loc[df["Bird Type"] == least_sighted_autumn, "September 1 - November 30 (Autumn)"].values[0]]
    x4 = [most_sighted_winter, least_sighted_winter]
    y4 = [df.loc[df["Bird Type"] == most_sighted_winter, "December 1 - February 28 (Winter)"].values[0], 
      df.loc[df["Bird Type"] == least_sighted_winter, "December 1 - February 28 (Winter)"].values[0]]

    #Formats information for data visualization as part of the basic plots feature (Feature #4) in this project's README file
    plt.rcParams["figure.autolayout"] = True
    fig, [ax1, ax2, ax3, ax4] = plt.subplots(1, 4)
    ax1.bar(x1, y1, color="green")
    ax1.set_title("March 1 - May 31")
    ax1.set_ylabel("Amount of Birds Sighted")
    ax1.set_xlabel("Bird Type")
    ax1.set_xticklabels(x1, rotation=90)
    ax2.bar(x2, y2, color="red")
    ax2.set_title("June 1 - August 31")
    ax2.set_ylabel("Amount of Birds Sighted")
    ax2.set_xlabel("Bird Type")
    ax2.set_xticklabels(x2, rotation=90)
    ax3.bar(x3, y3, color="orange")
    ax3.set_title("September 1 - November 30")
    ax3.set_ylabel("Amount of Birds Sighted")
    ax3.set_xlabel("Bird Type")
    ax3.set_xticklabels(x3, rotation=90)
    ax4.bar(x4, y4, color="purple") #GRAPH IS COMPARING ALL PREVIOUS GRAPHS IN THE SET, NEED TO FIX
    ax4.set_title("December 1 - February 28")
    ax4.set_ylabel("Amount of Birds Sighted")
    ax4.set_xlabel("Bird Type")
    ax4.set_xticklabels(x4, rotation=90)

    #Visualizes data as part of the basic plots feature (Feature #4) in this project's README file
    plt.show()

#This function shows graphs for bird sightings during Spring and Summer in a side-by-side format
def menu_option_2():
    df.fillna(0, inplace=False) #Eliminates null values by replacing them with 0s as part of the data cleaning feature (Feature #2) in the README file
    
    #Acquires information about seasonal bird sightings using functions as part of the custom functions feature (Feature #3) in this project's README file
    x1=df["Bird Type"]
    y1=df["March 1 - May 31 (Spring)"]
    x2=df["Bird Type"]
    y2=df["June 1 - August 31 (Summer)"]

    #Formats information for data visualization as part of the basic plots feature (Feature #4) in this project's README file
    plt.rcParams["figure.autolayout"] = True
    fig, [ax1, ax2] = plt.subplots(1, 2)
    ax1.bar(x1, y1, color="green")
    ax1.set_title("March 1 - May 31")
    ax1.set_ylabel("Amount of Birds Sighted")
    ax1.set_xlabel("Bird Type")
    ax1.set_xticklabels(x1, rotation=90)
    ax2.bar(x2, y2, color="red") #GRAPH IS COMPARING ALL PREVIOUS GRAPHS IN THE SET, NEED TO FIX
    ax2.set_title("June 1 - August 31")
    ax2.set_ylabel("Amount of Birds Sighted")
    ax2.set_xlabel("Bird Type")
    ax2.set_xticklabels(x2, rotation=90)

    #Visualizes data as part of the basic plots feature (Feature #4) in this project's README file
    plt.show()

#This function shows graphs for bird sightings during Autumn and Winter in a side-by-side format
def menu_option_3():
    df.fillna(0, inplace=False) #Eliminates null values by replacing them with 0s as part of the data cleaning feature (Feature #2) in the README file
    
    #Acquires information about seasonal bird sightings using functions as part of the custom functions feature (Feature #3) in this project's README file
    x1=df["Bird Type"]
    y1=df["September 1 - November 30 (Autumn)"]
    x2=df["Bird Type"]
    y2=df["December 1 - February 28 (Winter)"]

    #Formats information for data visualization as part of the basic plots feature (Feature #4) in this project's README file
    plt.rcParams["figure.autolayout"] = True
    fig, [ax1, ax2] = plt.subplots(1, 2)
    ax1.bar(x1, y1, color="orange")
    ax1.set_title("September 1 - November 30")
    ax1.set_ylabel("Amount of Birds Sighted")
    ax1.set_xlabel("Bird Type")
    ax1.set_xticklabels(x1, rotation=90)
    ax2.bar(x2, y2, color="purple") #GRAPH IS COMPARING ALL PREVIOUS GRAPHS IN THE SET, NEED TO FIX
    ax2.set_title("December 1 - February 28")
    ax2.set_ylabel("Amount of Birds Sighted")
    ax2.set_xlabel("Bird Type")
    ax2.set_xticklabels(x2, rotation=90)

    #Visualizes data as part of the basic plots feature (Feature #4) in this project's README file
    plt.show()

#This function shows graphs for bird sightings across all 4 seasons in a side-by-side format
def menu_option_4():
    df.fillna(0, inplace=False) #Eliminates null values by replacing them with 0s for as part of the data cleaning feature (Feature #2) in the README file
    
    #Acquires information about seasonal bird sightings using functions as part of the custom functions feature (Feature #3) in this project's README file
    x1=df["Bird Type"]
    y1=df["March 1 - May 31 (Spring)"]
    x2=df["Bird Type"]
    y2=df["June 1 - August 31 (Summer)"]
    x3=df["Bird Type"]
    y3=df["September 1 - November 30 (Autumn)"]
    x4=df["Bird Type"]
    y4=df["December 1 - February 28 (Winter)"]

    #Formats information for data visualization as part of the basic plots feature (Feature #4) in this project's README file
    plt.rcParams["figure.autolayout"] = True
    fig, [ax1, ax2, ax3, ax4] = plt.subplots(1, 4)
    ax1.bar(x1, y1, color="green")
    ax1.set_title("March 1 - May 31")
    ax1.set_ylabel("Amount of Birds Sighted")
    ax1.set_xlabel("Bird Type")
    ax1.set_xticklabels(x1, rotation=90)
    ax2.bar(x2, y2, color="red")
    ax2.set_title("June 1 - August 31")
    ax2.set_ylabel("Amount of Birds Sighted")
    ax2.set_xlabel("Bird Type")
    ax2.set_xticklabels(x2, rotation=90)
    ax3.bar(x3, y3, color="orange")
    ax3.set_title("September 1 - November 30")
    ax3.set_ylabel("Amount of Birds Sighted")
    ax3.set_xlabel("Bird Type")
    ax3.set_xticklabels(x3, rotation=90)
    ax4.bar(x4, y4, color="purple") #GRAPH IS MULTICOLORED, NEED TO FIX
    ax4.set_title("December 1 - February 28")
    ax4.set_ylabel("Amount of Birds Sighted")
    ax4.set_xlabel("Bird Type")
    ax4.set_xticklabels(x4, rotation=90)

    #Visualizes data as part of the basic plots feature (Feature #4) in this project's README file 
    plt.show()

def menu_option_5():
    os.system("clear")

def menu_option_6():
    print("See you next time! Happy Trails!")
    sleep(1)
    quit()

def main_menu_descriptions():
    print("Please type the corresponding number and press enter to select a menu option:")
    sleep(0.5)
    print("1: See graphs of the most and least sighted bird(s) for each season")
    sleep(0.5)
    print("2: See graphs of the birds sighted during Spring and Summer")
    sleep(0.5)
    print("3: See graphs of the birds sighted during Autumn and Winter")
    sleep(0.5)
    print("4: See graphs of all bird sightings across all seasons")
    sleep(0.5)
    print("5: Clear Screen")
    sleep(0.5)
    print("6: Quit")

#Menu allows users multiple data views in a simple to use format using functions as part of the custom functions feature (Feature #3) in this project's README file
def main():
    main_menu_descriptions()
    userinput = input()
    if (userinput == "1" or userinput == "1 " or userinput == "1." or userinput == "1. " or userinput == " 1" or userinput == "1)" or userinput == "1) " or userinput == "1:" or userinput == "1: " or userinput == "1;" or userinput == "1; " or userinput == "1," or userinput == "1, "):
        menu_option_1()
        main()
    elif (userinput == "2" or userinput == "2 " or userinput == "2." or userinput == "2. " or userinput == " 2" or userinput == "2)" or userinput == "2) " or userinput == "2:" or userinput == "2: " or userinput == "2;" or userinput == "2; " or userinput == "2," or userinput == "2, "):
        menu_option_2()
        main()
    elif (userinput == "3" or userinput == "3 " or userinput == "3." or userinput == "3. " or userinput == " 3" or userinput == "3)" or userinput == "3) " or userinput == "3:" or userinput == "3: " or userinput == "3;" or userinput == "3; " or userinput == "3," or userinput == "3, "):
        menu_option_3()
        main()
    elif (userinput == "4" or userinput == "4 " or userinput == "4." or userinput == "4. " or userinput == " 4" or userinput == "4)" or userinput == "4) " or userinput == "4:" or userinput == "4: " or userinput == "4;" or userinput == "4; " or userinput == "4," or userinput == "4, "):
        menu_option_4()
        main()
    elif (userinput == "5" or userinput == "5 " or userinput == "5." or userinput == "5. " or userinput == " 5" or userinput == "5)" or userinput == "5) " or userinput == "5:" or userinput == "5: " or userinput == "5;" or userinput == "5; " or userinput == "5," or userinput == "5, "):
        menu_option_5()
        main()
    elif (userinput == "6" or userinput == "6 " or userinput == "6." or userinput == "6. " or userinput == " 6" or userinput == "6)" or userinput == "6) " or userinput == "6:" or userinput == "6: " or userinput == "6;" or userinput == "6; " or userinput == "6," or userinput == "6, "):
        menu_option_6()
    else:
        print("Sorry, your input was not recognized...")
        sleep(0.5)
        main()

main()