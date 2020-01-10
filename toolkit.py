import threading
import os
from pathlib import Path

base_dir = Path(__file__).parent
lepus_dir = Path(base_dir / 'Lepus')

if os.name == "nt":
    py_command = "python"
else:
    py_command = "python3"


def task1():
    print("Task 1 assigned thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2(domain_):
    os.system("nmap -sT -sV --version-intensity 0 -O -v --reason {} -oA {}.nmap -p 21,22,23,80,443,81,8443,8080,8081,8888,25,1403,3306,3389,135,139,445".format(domain_, domain_))


def task3(domain_):
    os.chdir(lepus_dir)
    subdomains_txt_path = Path(lepus_dir / 'lists' / 'subdomains.txt')
    os.system("{} lepus.py {} -w {} --permutate --reverse".format(py_command, domain_, subdomains_txt_path))


if __name__ == "__main__":
    print("ID of process running the main program: {}".format(os.getpid()))
    print("Main Thread Name: {}".format(threading.main_thread().name))

    domain = "4cmedicalgroup.com"

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2', args=[domain])
    t3 = threading.Thread(target=task3, name='Lepus', args=[domain])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
