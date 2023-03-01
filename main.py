import os
import time
import requests

try:
    from colorama import Fore
except ImportError:
    raise RuntimeError(
        "The colorama module must be installed\nYou can install it with 'pip install colorama'"
    )
try:
    from discord_webhook import DiscordWebhook
except ImportError:
    raise RuntimeError(
        "The discord-webhook module must be installed\nYou can install it with 'pip install discord-webhook'"
    )
try:
    import requests
except ImportError:
    raise RuntimeError(
        "The requests module must be installed\nYou can install it with 'pip install requests'"
    )
DEFAULT_MESSAGE = "@everyone it seems someone leaked your webhook url!!!"


def is_valid_webhook(url: str) -> bool:
    try:
        res = requests.post(
            url,
            json={"content": DEFAULT_MESSAGE + " https://arabic.cat/webhooks"},
        )
        return bool(res.status_code == 204)
    except requests.exceptions.RequestException:
        return False


def ask(msg, convertor):
    try:
        return convertor(input(msg))
    except ValueError:
        print(f"{Fore.RED}Invalid Input")
        return ask(msg, convertor)


def main():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print(
            f"{Fore.CYAN}\r\n\n                       ▄▀▄     ▄▀▄" + "\n"
            "                      ▄█░░▀▀▀▀▀░░█▄" + "\n"
            "                  ▄▄  █░░░░░░░░░░░█" + "\n"
            "                 █▄▄█ █░░▀░░┬░░▀░░█ █▄▄█" + "\n"
            "\n"
            "                 Author: Kars#2762\n"
            "                 GitHub: https://github.com/ArabicCat\n\n"
        )
        url = input(
            f"{Fore.GREEN}Enter the webhook URL you wanna spam. \n> "
        )

        if not is_valid_webhook(url):
            print(f"{Fore.RED}Error: Invalid webhook URL")
            continue

        msg = input("\nEnter the message you wanna spam. (leave empty for default)\n> ")
        amount = ask(
            "\nEnter the amount you wanna spam the message. (30+ = RATELIMMITED)\n> ",
            int,
        )

        if not msg:
            msg = DEFAULT_MESSAGE

        webhook = DiscordWebhook(url=(url), rate_limit_retry=True, content=((msg + " https://discord.gg/DM8GtTT4rX")))
        count = 1
        while count <= (amount):
            webhook.execute()
            print(f"{Fore.YELLOW}Send message #{count}")
            count += 1
            time.sleep(0.1)

        again = input(f"{Fore.GREEN}\nPress ENTER to exetute the script again.")
        if again.lower() != "":
            break
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()
