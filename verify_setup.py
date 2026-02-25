import sys
import os

def check_python_version():
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro} (OK)")
        return True
    else:
        print(f"❌ Python version: {version.major}.{version.minor}.{version.micro} (Need 3.8+)")
        return False

def check_packages():
    required_packages = {
        'streamlit': 'streamlit',
        'google.generativeai': 'google-generativeai',
        'dotenv': 'python-dotenv',
        'PIL': 'Pillow'
    }

    all_installed = True
    for module, package in required_packages.items():
        try:
            __import__(module)
            print(f"✅ {package} is installed")
        except ImportError:
            print(f"❌ {package} is NOT installed")
            all_installed = False

    return all_installed

def check_env_file():
    if os.path.exists('.env'):
        print("✅ .env file exists")
        with open('.env', 'r') as f:
            content = f.read()
            if 'GOOGLE_API_KEY' in content and 'your_api_key_here' not in content:
                print("✅ Google API key is configured")
                return True
            else:
                print("❌ Google API key not configured in .env file")
                print("   Please add your API key to the .env file")
                return False
    else:
        print("❌ .env file not found")
        return False

def check_app_file():
    if os.path.exists('app.py'):
        print("✅ app.py file exists")
        return True
    else:
        print("❌ app.py file not found")
        return False

def main():
    print("=" * 50)
    print("Civil Engineering Insight Studio - Setup Verification")
    print("=" * 50)
    print()

    checks = []

    print("1. Checking Python version...")
    checks.append(check_python_version())
    print()

    print("2. Checking required packages...")
    checks.append(check_packages())
    print()

    print("3. Checking .env configuration...")
    checks.append(check_env_file())
    print()

    print("4. Checking app.py file...")
    checks.append(check_app_file())
    print()

    print("=" * 50)
    if all(checks):
        print("✅ ALL CHECKS PASSED!")
        print("=" * 50)
        print()
        print("You're ready to run the application!")
        print("Run this command: streamlit run app.py")
    else:
        print("❌ SOME CHECKS FAILED")
        print("=" * 50)
        print()
        print("Please fix the issues above before running the app.")
        print("See SETUP_GUIDE.md for detailed instructions.")
    print()

if __name__ == "__main__":
    main()
