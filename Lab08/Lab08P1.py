#
# World McCrea
# 6/25/2024
# Lab08 Files and exception handling
# Using as much as I can to keep clean coding practices

#

def main():
    # create 5 counters set to zero
    CRITICAL = 0
    ERROR = 0
    WARNING = 0
    INFO = 0
    UNKNOWN = 0

    # Attempt to open the file with exception error handling
    try:
        with open('program.log', 'r') as file1:  # this way I don't have to remember to close the file
            for line in file1:
                #  split into components by spaces and strip off default bits
                components = line.strip().split(' ')

                error_category = components[3]  # This would be the index for error category

                # Update the counters based on the error category
                if error_category == 'CRITICAL':
                    CRITICAL += 1
                elif error_category == 'ERROR':
                    ERROR += 1
                elif error_category == 'WARNING':
                    WARNING += 1
                elif error_category == 'INFO':
                    INFO += 1
                else:
                    UNKNOWN += 1  # Increment the unknown counter for unknown or unexpected categories

    except FileNotFoundError:  # if the file isn't found, none of that will run. I will get File not found error.
        print('File was not found')
        exit()

    # Display the results of errors
    print(f"CRITICAL: {CRITICAL}")
    print(f"ERROR: {ERROR}")
    print(f"WARNING: {WARNING}")
    print(f"INFO: {INFO}")
    print(f"UNKNOWN: {UNKNOWN}")

main()
