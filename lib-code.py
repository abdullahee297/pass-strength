from zxcvbn import zxcvbn
import getpass

def check_password_strength():
    password = getpass.getpass("Enter password: ")

    result = zxcvbn(password)

    print("\n🔒 Password Strength Analysis")
    print("-" * 40)
    print(f"Score (0-4): {result['score']}")
    print(f"Guesses needed: {result['guesses_log10']} (log10 scale)")
    print(f"Crack time (offline fast attack): {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    print(f"Crack time (online attack): {result['crack_times_display']['online_throttling_100_per_hour']}")
    
    print("\nFeedback:")
    for suggestion in result['feedback']['suggestions']:
        print(f" - {suggestion}")

if __name__ == "__main__":
    check_password_strength()
