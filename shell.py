import subprocess
import os
import signal

def handle_sigint(sig, frame):
    # Print a newline to move to a new line after the interrupted command
    print("\n")

# Register the SIGINT signal handler
signal.signal(signal.SIGINT, handle_sigint)

# Customizable prompt
prompt = "$ "

while True:
    # Prompt for user input
    command = input(prompt)

    # Exit the shell if the user enters 'exit' or 'quit'
    if command.lower() in ['exit', 'quit']:
        break

    # Split the command into tokens
    tokens = command.split()

    # Check if the command is 'cd'
    if tokens[0] == 'cd':
        # Handle 'cd' without arguments - change to the home directory
        if len(tokens) == 1:
            os.chdir(os.path.expanduser("~"))
        else:
            try:
                # Change to the specified directory
                os.chdir(tokens[1])
            except FileNotFoundError:
                print("Directory not found:", tokens[1])
            except NotADirectoryError:
                print("Not a directory:", tokens[1])
        continue

    # Execute the command using subprocess
    try:
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print("Command failed with exit code:", result.returncode)
    except Exception as e:
        print("Error:", e)
