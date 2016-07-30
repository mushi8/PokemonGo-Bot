import getopt

import sys

import StopMyUser
import json
import os


def change_user_location(user, location):
    with open('./conf/' + user + '.json', 'r') as data_file:
        data = json.load(data_file)
        data_file.close()
        print data
        data['location'] = str(location)
        data['location_cache'] = False
        print data
        with open('./conf/' + user + '.json', 'w') as data_file:
            json.dump(data, data_file, indent=4)
            data_file.close()


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hu:l:", ["user=", "location="])
    except getopt.GetoptError:
        print 'test.py -u <email> -l <location>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -u <email> -l <location>'
            sys.exit()
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-l", "--location"):
            location = arg
    change_user_location(user, location)
    out = StopMyUser.run_os_command('ps -ax')
    StopMyUser.kill_process(out, "python", user)
    StopMyUser.delete_user_web_data(user)

    print "You Player Will restart soon"


if __name__ == '__main__':
    main(sys.argv[1:])
