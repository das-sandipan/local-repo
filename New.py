from datetime import date

def year_turns_100 (Age : int, current_year: int ) -> int:
    return current_year + (100 - Age)
def main():
    current_year = date.today().year

    name = input ("Enter your Name: ").strip()
    Age_input = input ("Enter your Age: ").strip()
    Age = int(Age_input)

    year_100 = year_turns_100 (Age, current_year)

    
    if Age<100:
        print(f"Hi, {name} You will turn to 100 in the year {year_100}")
    elif Age==100:
        print(f"Hi, {name} you are now 100 year old {current_year}")
    else:
        print(f"Hi, {name} You already became 100 years old on {year_100}")

if __name__ == "__main__":
    main()