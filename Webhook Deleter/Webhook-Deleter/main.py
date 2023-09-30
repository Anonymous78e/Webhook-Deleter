import os
import requests
import colorama
from dhooks import Webhook
import time

def main():
    print(f"""{colorama.Fore.RED}
          
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗                    ██████╗ ███████╗██╗     ███████╗████████╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝                    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝                     ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗                     ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗                    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                                     

                                                                                                                                           """)

def webh_intro():
    main()
    input(f"{colorama.Fore.RED} Press Enter to start the program... ")
    os.system("cls")

def webh():
    print(f"""{colorama.Fore.RED}
     



██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗                    ██████╗ ███████╗██╗     ███████╗████████╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝                    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝                     ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗                     ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗                    ██████╔╝███████╗███████╗███████╗   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                    ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                                     

                                                                                                                                           """)

    webhookdeleter = input(f"{colorama.Fore.RED} \nWebhook link: {colorama.Fore.WHITE}")

    webhookchecker = requests.get(webhookdeleter)
    if webhookchecker.status_code == 404:
        print("The webhook is non-existent or already deleted")
        time.sleep(2)
        os.system("cls")
        webh()
    if webhookchecker.status_code == 10015:
        print("The webhook is non-existent or already deleted")
        time.sleep(2)
        os.system("cls")
        webh()
    if webhookchecker.status_code == 401:
        print("The webhook is non-existent or already deleted")
        time.sleep(2)
        webh()
    else:
        hook = Webhook(webhookdeleter)
        print(" ")
        x = requests.delete(webhookdeleter)
        print(f"{colorama.Fore.RED} \nThe Webhook has been deleted successfully ! ")
        time.sleep(5)
        os.system("cls")
        webh()

if __name__ == "__main__":
    webh_intro()
    webh()
