#!/usr/bin/python
import getopt
import sys
import os
import subprocess, signal
from os import listdir
from os.path import isfile, join

WEBDIR = 'web'
DATADIR = 'data'


def kill_process(out, process, user):
    for line in out.splitlines():
        if process in line and user in line:
            print 'Found the process', line
            pid = int(line.split(None, 1)[0])
            print 'Killing Pid:', pid
            os.kill(pid, signal.SIGKILL)


def run_os_command(command):
    print "command:", command
    p = subprocess.Popen(str(command), stdout=subprocess.PIPE)
    print "communicat"
    out, err = p.communicate()
    return out


def delete_user_web_data(user):
    cwd = os.getcwd()
    web = os.path.join(cwd, WEBDIR)
    # data = os.path.join(cwd, DATADIR)
    delete_by_file_name_in_dir(web, user)
    # delete_by_file_name_in_dir(data, user)


def delete_by_file_name_in_dir(dirPath, fileContain):
    onlyfiles = [f for f in listdir(dirPath) if isfile(join(dirPath, f))]
    for f in onlyfiles:
        if fileContain in str(f):
            print 'Gonna Delete', f


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hu:", ["user="])
    except getopt.GetoptError:
        print 'test.py -u <email>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -u <email>'
            sys.exit()
        elif opt in ("-u", "--user"):
            user = arg
    out = run_os_command('ps -ax')
    kill_process(out, "run.sh", user)
    kill_process(out, "pokecli", user)
    delete_user_web_data(user)

    print "You Player Has been Stopped!"


if __name__ == '__main__':
    main(sys.argv[1:])
