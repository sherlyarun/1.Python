class MultipleFunctions:
    def subfields():
        print("Subfields in AI are:")
        lists = ["Machine Learning", "Neural Network", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for temp in lists:
            print(temp)

    def OddEven():
        num = int(input("Enter a number:"))
        if (num % 2) == 0:
            print(num, "is Even number")
            message = "Even number"
        else:
            print(num, "is Odd number")
            message = "Odd number"
        return message

    def Elegible():
        sex = input("Your Gender:")  # This variable 'sex' is collected but not used in the decision logic
        age = int(input("Your Age:"))
        message = "ELEGIBLE"  # It's a good practice to define 'message' before using it in conditions
        if age < 25:
            message = "NOT ELEGIBLE"
        return message

    def percentage():
        sub1 = int(input("Subject1:"))
        sub2 = int(input("Subject2:"))
        sub3 = int(input("Subject3:"))
        sub4 = int(input("Subject4:"))
        sub5 = int(input("Subject5:"))
        total = sub1 + sub2 + sub3 + sub4 + sub5
        print("Total:", total)
        per = total / 500 * 100
        print("Percentage =", per)

    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        area = (height * breadth) / 2
        print("Area of Triangle:", area)
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        # You're asking for 'Breadth' input twice (here and above); assuming this is intentional
        perimeter = height1 + height2 + breadth
        print("Perimeter of Triangle:", perimeter)