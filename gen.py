import os, ctypes, json, requests, datetime, getpass
from colorama import Fore
from requests import get

def banner():
    print(f"""
                        {Fore.RED}Dev By Tahg{Fore.RESET}
██╗░░██╗███████╗██╗░░░██╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░░░░░░░██████╗░███████╗███╗░░██╗
██║░██╔╝██╔════╝╚██╗░██╔╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔════╝░██╔════╝████╗░██║
█████═╝░█████╗░░░╚████╔╝░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║█████╗██║░░██╗░█████╗░░██╔██╗██║
██╔═██╗░██╔══╝░░░░╚██╔╝░░░░████╔═████║░██║░░██║██╔══██╗██║░░██║╚════╝██║░░╚██╗██╔══╝░░██║╚████║
██║░╚██╗███████╗░░░██║░░░░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░░░░░░╚██████╔╝███████╗██║░╚███║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝
    {Fore.RED}GitHub: {Fore.BLUE}https://github.com/T4hg/ {Fore.RESET}
    """)

def gen():
    prefix = f"{Fore.RED}Keyword {Fore.BLUE}GEN {Fore.GREEN}· {Fore.WHITE}"
    system_prefix = f"{Fore.RED}$ {Fore.GREEN}"
    keyword = input(prefix + "Keyword (EXAMPLE: netflix): ")

    cfg = open("config.json", "r")
    config = json.load(cfg)

    headers = {
	    "Content-type": "application/json",
	    "X-RapidAPI-Host": "keywords4.p.rapidapi.com",
	    "X-RapidAPI-Key": config.get('api_key')
    }
    parametros = {
        "search": keyword,
        "country":"us"
    }
    url = "https://keywords4.p.rapidapi.com/google-topLevel-10-keywords"
    pc_usuario = getpass.getuser()
    directorio = rf"C:\Users\{pc_usuario}\Documents\KeywordsGEN-APP"
    try:
        keywords = requests.get(url, headers=headers, params=parametros).text
        try:
            try:
                os.mkdir(directorio)
            except:
                pass
            file = open(directorio + rf"\{keyword}-app.json", "w+")
            file.write(keywords)
            file.close()
        except:
            pass
    except:
        print(system_prefix + "Error URL\n")
        gen()
    
    keywordx = open(directorio + rf"\{keyword}-app.json", "r")
    key_json = json.load(keywordx)
    keyget = key_json.get('googleGuggestedKeywords')

    date = datetime.datetime.now()
    file_txt = open(f"keyword-{keyword}.txt", "a+", encoding="utf-8")
    file_txt.write(f"{keyword} - {date}\n\n")
    for x in keyget:
        file_txt.write(f"{x}\n")
    file_txt.close()

    print(f"""
    {Fore.GREEN}If you like the app, don't forget to give it a {Fore.YELLOW}star {Fore.GREEN}on GitHub

    {Fore.WHITE}ENTER TO BACK""")
    input()
    gen()
if __name__ == '__main__':
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Keyword Generator | Developed by Tahg - GitHub: https://github.com/T4hg/')
    banner()
    gen()