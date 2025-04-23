import time

def countdown_timer(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f'{mins:02d}:{secs:02d}'
        print("⏳", timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("\nTime's up! ⏰")

# User input
try:
    total_seconds = int(input("Enter countdown time in seconds: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Please enter a valid number.")
