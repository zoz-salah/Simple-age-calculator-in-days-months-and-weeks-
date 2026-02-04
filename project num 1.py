def ageCalc(age):
    dage = (int(age)*365) #Day counter
    mage = (int(age) * 12)#Month counter
    wage = (int(age) * 52)#Week counter
    sage = (int(age) * 31536000) #Age in secounds
    print("\nYour age in DAYS : " , dage)
    print("\nYour age in WEEKS : " , wage)
    print("\nYour age in MONTHS : " , mage)
    print("\nYour age in SECONDS : " , sage)

def main():
    pass  
    print("---------------------------------------")
    print("𝖠𝖦𝖤 𝖨𝖭 𝖣𝖠𝖸,𝖬𝖮𝖭𝖳𝖧,𝖶𝖤𝖤𝖪 , SEC 𝖢𝖠𝖫𝖢𝖴𝖫𝖠𝖳𝖮𝖱")
    print("----------------------------------------")

    age = input("\n Please enter your AGE : ")
    ageCalc(age)
   

      
    

main()
