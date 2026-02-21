from colorama import Fore, Back, Style, init

init(autoreset=True)

ASCII_ART = r"""
  _   _      _ _         __        __         _     _ _
 | | | | ___| | | ___    \ \      / /__  _ __| | __| | |
 | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
 |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
 |_| |_|\___|_|_|\___/      \_/\_/ \___/|_|  |_|\__,_(_)
"""

def main():
    print(Fore.CYAN + Style.BRIGHT + ASCII_ART)
    print(Fore.GREEN + Style.BRIGHT + "  Hello, World!")
    print(Fore.YELLOW + "  Welcome to fancy_hello.py!")
    print(Style.RESET_ALL)

if __name__ == "__main__":
    main()
