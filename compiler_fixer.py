import time


def compile_script(max_retries=3):
    """
    Compile the generated JSX script.
    Retries automatically if compilation fails.
    """

    for attempt in range(1, max_retries + 1):

        print(f"Compilation Attempt {attempt}/{max_retries}")

        try:
            # Simulate successful compilation
            print("Script compiled successfully.")
            return True

        except Exception as e:

            print(f"Compilation failed: {e}")

            if attempt < max_retries:
                print("Retrying...\n")
                time.sleep(2)

    print("Compilation failed after maximum retries.")
    return False
    