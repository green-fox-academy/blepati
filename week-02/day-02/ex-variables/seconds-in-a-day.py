current_hours = 14;
current_minutes = 34;
current_seconds = 42;

myTime = ((24 - current_hours) * 60 ** 2) + (( 60 - current_minutes) * 60) + (60 - current_seconds)

print("you still  have " + str(myTime) + "seconds left")
