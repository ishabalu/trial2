""" Tells the status of the tank in the chemical plant
"""

def do_action(present, redmark, bluemark):
    if(level>high):
        print("Close to the valve")
    elif(level<low):
        print("buy more liquid")
    else:
        print("everything under control")
    # Compare present with redmark and bluemark
    # to decide the appropriate action


def get_current_level():
    lev=input("what is the current level")
    lev=int(lev)
    return lev# Get value from user
    # Return integer

# Main starts from here
capacity = 900
high = 0.8*capacity# calculate using "capacity" variable
low =0.2*capacity # calculate using "capacity" variable
level = get_current_level()
do_action(level, high, low)
