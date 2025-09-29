import time

# Countdown function with progress bar
def countdown(minutes, session_name):
    total_seconds = minutes * 60
    for elapsed in range(total_seconds):
        remaining = total_seconds - elapsed
        mins, secs = divmod(remaining, 60)
        bar_length = 20
        filled_length = int(bar_length * elapsed // total_seconds)
        bar = '#' * filled_length + '-' * (bar_length - filled_length)
        print(f"{session_name} [{bar}] {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
    print(f"{session_name} [{'#'*20}] 00:00 - Session Complete!      ")

# Log completed cycles
def log_cycle(cycle_num):
    with open("pomodoro_log.txt", "a") as file:
        file.write(f"Cycle {cycle_num} completed!\n")

# Main Pomodoro Timer
def pomodoro_timer():
    print("="*30)
    print("       POMODORO TIMER")
    print("="*30)
    
    # User input with validation
    while True:
        work_min = input("Enter work session time in minutes: ")
        if work_min.isdigit() and int(work_min) > 0:
            work_min = int(work_min)
            break
        print("Please enter a valid number greater than 0.")
    
    while True:
        break_min = input("Enter break time in minutes: ")
        if break_min.isdigit() and int(break_min) > 0:
            break_min = int(break_min)
            break
        print("Please enter a valid number greater than 0.")
    
    while True:
        cycles = input("Enter number of Pomodoro cycles: ")
        if cycles.isdigit() and int(cycles) > 0:
            cycles = int(cycles)
            break
        print("Please enter a valid number greater than 0.")
    
    # Run Pomodoro cycles
    for i in range(1, cycles + 1):
        print(f"\nCycle {i} - Work Session Started! Focus 💪")
        countdown(work_min, "WORK")
        
        print("Break time! Relax 😌")
        countdown(break_min, "BREAK")
        
        print(f"Cycle {i} completed!\n")
        log_cycle(i)
    
    print("="*30)
    print("All Pomodoro cycles completed! Great job! 🎉")
    print("Check 'pomodoro_log.txt' to see your completed cycles.")

if __name__ == "__main__":
    pomodoro_timer()
