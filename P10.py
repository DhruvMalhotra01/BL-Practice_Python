import time

seconds = int(input("Enter the timer in seconds : "))

while seconds >= 0:
    mins = seconds // 60
    secs = seconds % 60

    print(f"Time Remaining: {mins:02d}:{secs:02d}")

    if seconds == 0:
        break

    time.sleep(1)
    seconds -= 1

print("Time's up!")