#
# World McCrea
# 6/14/24
# Code to show my knowledge of list functions
# Also practice using as many things as I can before midterm
#



def main(): #I dont really think I need a main here but it works so Im using it.
    # Get IP address from user
    ip = input("Please enter an IP address or 'Q' to quit: ").strip() # remove whitespace in input
    while ip.upper() != 'Q': # setting up my while loop and setting so case won't matter
        # Validate the IP address format
        ip_tokens = ip.split('.') # create list of input tokens
        if len(ip_tokens) != 4: # input validation
            print("Error: An IP address should consist of 4 parts separated by periods.")
            ip = input("Please enter a valid IP address or 'Q' to quit: ").strip()  # Prompt the user again
            continue # this makes the program continue forward for more validation

        # Check if each part is a number and within the range 0-255
        for token in ip_tokens:
            if not token.isdigit(): # if the octets from the ip arent digits. Weird way to say it, lol
                print(f"Error with {token}: Each part of the IP address should be a number.") # Womp womp error
                ip = input("Please enter a valid IP address or 'Q' to quit: ").strip()  # Prompt the user again
                break
            elif int(token) < 0 or int(token) > 255: # if elif check to see if between 0 and 255
                print(f"Error with {token}: Each part of the IP address should be a number between 0 and 255.")
                ip = input("Please enter a valid IP address or 'Q' to quit: ").strip()  # Prompt the user again
                break
        else:
            # all input valid, reformat the IP address with colons
            colon_ip = ":".join(ip_tokens) #create a new list with the reformatted ips
            print(f"Reformatted IP address: {colon_ip}")
            ip = input("Please enter a valid IP address or 'Q' to quit: ").strip()  # Prompt the user again
            print(colon_ip)


            break  # Exit the loop


if __name__ == "__main__": # dunder main lol, that's a funny name
    main()
