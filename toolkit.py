import threading
import os
from pathlib import Path
import argparse


base_dir = Path(__file__).parent
lepus_dir = Path(base_dir / 'Lepus')

if os.name == "nt":
    py_command = "python"
else:
    py_command = "python3"


def nmap_task(domain_):
    os.system("nmap -sT -sV --version-intensity 0 -O -v --reason {} -oA {}.nmap -p 21,22,23,80,443,81,8443,8080,8081,8888,25,1403,3306,3389,135,139,445".format(domain_, domain_))


def lepus_task(domain_):
    os.chdir(lepus_dir)
    subdomains_txt_path = os.path.join("lists", "subdomains.txt")
    os.system("{} lepus.py {} -w {} --permutate --reverse".format(py_command, domain_, subdomains_txt_path))


if __name__ == "__main__":
    # print("ID of process running the main program: {}".format(os.getpid()))
    # print("Main Thread Name: {}".format(threading.main_thread().name))

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domains", action="store", dest="domains", help="set a domain or list of domains",
                        type=str, default=None)
    parser.add_argument("-i", "--ips", action="store", dest="ips", help="set an ip or ip range",
                        type=str, default=None)
    args = parser.parse_args()

    if args.domains:
        print("running domain tools")
        print(args.domains)
        lepus = threading.Thread(target=lepus_task, name='Lepus', args=[args.domains])
        lepus.start()
    if args.ips:
        print("running ip tools")
        nmap = threading.Thread(target=nmap_task, name='Lepus', args=[args.ips])
        nmap.start()

    try:
        lepus.join()
    except NameError:
        pass
    try:
        nmap.join()
    except NameError:
        pass
