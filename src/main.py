from utils import greet_user, calculate_sum


def hello_world():
    print("Hello, world!")  # Proper indentation for code quality checks


def main():
    hello_world()
    
    # Use our utility functions
    print(greet_user("Developer"))
    
    # Calculate and display sum
    result = calculate_sum(5, 10)
    print(f"The sum of 5 and 10 is: {result}")
    
    # Added comment to test code quality checks
    print("Code quality check test")


if __name__ == "__main__":
    main()
