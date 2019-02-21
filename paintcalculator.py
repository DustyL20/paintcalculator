def paintcalculator():

    int_or_ext = input("Interior or Exterior? ")

    if int_or_ext in ["interior", "Interior"]:
        height = int(input("Enter wall height in feet: "))
        width = int(input("Enter wall width in feet: "))
        total_doors = int(input("how many doors? "))
        total_windows = int(input("how many windows? "))
        #assumes standard 3'x7' doors & 3'5' windows
        door_sq_ft = total_doors * 21
        window_sq_ft = total_windows * 15

        total_sq_ft = (height * width) - door_sq_ft - window_sq_ft

        print("Total square feet:", total_sq_ft)
        #assumes 400 sq ft per gallon of latex paint
        gallons_per_coat = total_sq_ft / 400

        print("You will need", gallons_per_coat, "gallons for one coat")

    elif int_or_ext in ["exterior","Exterior"]:
        height = int(input("Enter wall height in feet: "))
        width = int(input("Enter wall width in feet: "))
        total_doors = int(input("how many doors? "))
        total_windows = int(input("how many windows? "))
        # assumes standard 3'x7' doors & 3'5' windows
        door_sq_ft = total_doors * 21
        window_sq_ft = total_windows * 15

        total_sq_ft = (height * width) - door_sq_ft - window_sq_ft

        print("Total square feet:", total_sq_ft)
        #assumes 350 sq ft per gallon of latex paint
        gallons_per_coat = total_sq_ft / 350

        print("You will need", gallons_per_coat, "gallons for one coat")

    else:
        print("Not recognized.")

while True:
    paintcalculator()






