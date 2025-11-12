miles = float(
    input("William, please tell me how many miles you want converted to kilometers: ")
)
if miles < 0:
    print("Miles can not be negative")
else:
    kilometers = miles * 1.6
    print(
        f"William, {miles} miles is equal to {kilometers} kilometers! Isn't that amazing?"
    )
    fahrenheit = float(
        input(
            "William, please tell me the temperature in Fahrenheit you want converted to celcius: "
        )
    )
    if fahrenheit > 1000:
        print("You can not enter a temperature over 1000 fahrenheit")
    else:
        celcius = (fahrenheit - 32) * 5.0 / 9.0
        print(
            f"William, {fahrenheit} degrees Fahrenheit is equal to {celcius} degrees Celcius! Isn't that amazing?"
        )
        gallons = float(
            input(
                "William, please tell me how many gallons you want converted to liters: "
            )
        )
        if gallons < 0:
            print("Gallons can not be negative")
        else:
            liters = gallons * 3.9
            print(
                f"William, {gallons} gallons is equal to {liters} liters! Isn't that amazing?"
            )
            pounds = float(
                input(
                    "William, please tell me how many pounds you want converted to kilograms: "
                )
            )
            if pounds < 0:
                print("Pounds can not be negative")
            else:
                kilograms = pounds * 0.45
                print(
                    f"William, {pounds} pounds is equal to {kilograms} kilograms! Isn't that amazing?"
                )
                inches = float(
                    input(
                        "William, please tell me how many inches you want converted to centimeters: "
                    )
                )
                if inches < 0:
                    print("Inches can not be negative")
                else:
                    centimeters = inches * 2.54
                    print(
                        f"William, {inches} inches is equal to {centimeters} centimeters! Isn't that amazing?"
                    )
