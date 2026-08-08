import os
import subprocess

def main():
    print("DevSecOps Python App is running!")
    env_name = os.getenv("APP_ENV", "development")
    print(f"Environment: {env_name}")

    # Безопасный вызов через список аргументов
    subprocess.run(["echo", "Hello from secure process!"], check=True)

if __name__ == "__main__":
    main()