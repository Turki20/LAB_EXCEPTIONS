
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    done = True
    while done:
        try: 
            user_input = input("Enter a temperature and its unit (e.g., 25 C or 77 F): ")
            user_input = user_input.strip() # remove spaces between the string
            temp_and_unit = user_input.split(" ")
        
            if len(temp_and_unit) != 2: raise ValueError("invalid input, please try again.")
            if temp_and_unit[1] == "C" or temp_and_unit[1] == "F": 
                if temp_and_unit[1] == "C":
                    c = celsius_to_fahrenheit(int(temp_and_unit[0]))
                    print(f"Temperature in Fahrenheit: {c} F")
                else:
                    f = fahrenheit_to_celsius(int(temp_and_unit[0]))
                    print(f"Temperature in Celsius: {f} C")
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except Exception as e:
            print(e)
        else:
            done = False
    
main()
