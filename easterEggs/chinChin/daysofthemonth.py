month = input("Enter month: ")
year = int(input("Enter year: "))

match(month.lower()):
    case "january" | "march" | "may" | "july" | "august" | "october" | "december":
        print(f"{month} has 31 days")
    case "april" | "june" | "september" | "november" :
        print(f"{month} has 31 days")
    case "february":
        if year % 4 == 0:
            print(f"{month} has 29 days")
        else:
            print(f"{month} has 28 days")
  
