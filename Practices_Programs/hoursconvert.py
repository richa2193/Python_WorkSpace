seconds = int(input("Enter the number of second : "))

hours = seconds//3600
minutes = (seconds % 3600) // 60
remining_second = seconds % 60

print(hours, ":", minutes, ":", remining_second)

