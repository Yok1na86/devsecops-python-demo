import os
import subprocess

def main():
    print("DevSecOps Python App is running!")
    env_name = os.getenv("APP_ENV", "development")
    print(f"Environment: {env_name}")

    # Небезопасный вызов (Bandit обнаружит B602: subprocess_popen_with_shell_equals_true)
    user_input = "echo Hello"
    subprocess.Popen(user_input, shell=True)

if __name__ == "__main__":
    main()