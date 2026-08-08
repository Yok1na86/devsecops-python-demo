import os
import subprocess

def main():
    print("DevSecOps Test App")
    
    # Искусственная уязвимость для Bandit (Command Injection)
    user_input = "echo test"
    subprocess.Popen(user_input, shell=True)

if __name__ == "__main__":
    main()