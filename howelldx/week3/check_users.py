def check_users(current_users, new_users):

    pass

    new_list = []
    for current_u in current_us:
        new_list.append(current_u.lower())

    for new_u in new_us:
        if new_u.lower() in current_us:
            print("The username {} is taken. Please enter a new username.". format(new_u))
        else:
            print("Username available! You may proceed with {} as your username.". format(new_u))

if __name__ == "__main__":

    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']

new_us = ['george', 'ringo', 'superman', 'hannibal']

check_users(current_us, new_us)
