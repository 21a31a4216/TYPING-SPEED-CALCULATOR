import time
def calculate_typing_speed():
    prompt = "CODECLAUSE INTERNSHIP PROGRAM"
    print("Type the following sentence:")
    print(prompt)
    input("Press Enter when you're ready to start...")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    typing_speed = words_typed / (time_taken / 60)
    print("Time taken:", round(time_taken, 2), "seconds")
    print("Words typed:", words_typed)
    print("Typing speed:", round(typing_speed, 2), "WPM")
calculate_typing_speed()