from os import access, X_OK
from os.path import isfile
from os import environ


def getaurhelp() -> str:
    """
    func for get installed aur helper in arch system

    returns:
     "yay"
     "paru"
     "pikaur"
     "pakku"
     ""
    """

    # get env variable
    env: str = environ["PATH"]

    # get list of dirs in env variable
    path_dirs: list = env.split(":")

    # supported aur helpers list
    aur_helpers: tuple = ("yay", "paru", "pikaur", "pakku")

    # init for list of aur helpers in user system
    user_aur_helpers_list: list = []

    # for dir in path env dirs
    for bin_dir in path_dirs:
        # for aur helper in list of aur helpers
        for aur_helper in aur_helpers:

            # check binary file of aur helper
            if isfile(f"{bin_dir}/{aur_helper}") is False:
                # print if no file
                print(f"{bin_dir}/{aur_helper} no file")
                continue

            # check file is executable
            if access(f"{bin_dir}/{aur_helper}", X_OK) is False:
                # print is file is not executable
                print(f"{bin_dir}/{aur_helper} file is not executable")
                continue

            # print if file is executable
            print(f"{bin_dir}/{aur_helper} file is executable")

            # add founded aur helper in list
            user_aur_helpers_list.append(f"{aur_helpers}")

    print()

    # if aur helpers not found
    if len(user_aur_helpers_list) == 0:

        print("any aur helpers not found")
        print("install one of this:")

        for i in aur_helpers:
            print("", i)

        return ""

    # if aur helper is only one
    elif len(user_aur_helpers_list) == 1:

        print("installing aur packages")

        # return first aur helper in list
        return user_aur_helpers_list[0]

    # if aur helpers more then one
    else:
        print("What aur helper u wonna use?")

        # print list fo user aur helpers
        for i in user_aur_helpers_list:
            for num in range(0, len(user_aur_helpers_list)):
                # generate print massage
                print(f"{num}) {i}")

        # user input
        uaurh: int = int(input(":"))

        # return aur helper by user input
        return user_aur_helpers_list[uaurh]
