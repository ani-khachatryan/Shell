import os
import shutil
import subprocess
import pathlib
from termcolor import colored


def ls():
    for x in os.listdir(os.curdir):
        if os.path.isfile(x):
            print(colored(x, "green"))
        else:
            print(colored(x, "yellow"))

def pwd():
    print(os.getcwd())

def cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print("cd: {}: No such file or directory".format(path))

def cp(source, dest):
    shutil.copyfile(source, dest)

def mv(source, dest):
    source = os.path.abspath(source)
    shutil.move(source, dest)

def rm(path):
    try:
        os.remove(os.path.abspath(path))
    except Exception:
        print("rm: {}: No such file or directory".format(path))

def rmdir(name):
    try:
        path = os.path.abspath(name)
    except Exception:
        print("rmdir: {}: No such file or directory".format(path))
        return
    
    if len(os.listdir(path)) == 0:
        os.rmdir(path)
    else:
        print("rmdir: {}: Directory not empty".format(path))

def mkdir(name):
    try:
        path = os.path.abspath(name)
    except Exception:
        print("mkdir: {}: Directory already exists".format(name))
        return
    os.mkdir(path)

def run(command):
    process = subprocess.Popen(command.split(), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    print(stderr.decode())

def main():
    while True:
        input_ = input("$ ")
        command = input_.split()[0]
        if command == "ls":
            ls()
        elif command == "pwd":
            pwd()
        elif command == "cd":
            cd(' '.join(input_.split()[1:]))
        elif command == "cp":
            cp(input_.split()[1], input_.split()[2])
        elif command == "mv":
            mv(input_.split()[1], input_.split()[2])
        elif command == "rm":
            rm(' '.join(input_.split()[1:]))
        elif command == "rmdir":
            rmdir(' '.join(input_.split()[1:]))
        elif command == "mkdir":
            mkdir(' '.join(input_.split()[1:]))
        elif command == "run":
            run(' '.join(input_.split()[1:]))
        elif command == "exit":
            break
        else:
            print("{}: command not found".format(command))

main()

