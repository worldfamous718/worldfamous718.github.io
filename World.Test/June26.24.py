#
# World McCrea
# 6/26/2024
# Practicing my skills for development

# first I need practice opening and manipulating files

def main():
    access_key = 357
    attempts = 0
    trys = int(input('Enter your 3 digit access key '))
    while True:
        if trys == access_key:

            with open('example.txt', 'r') as file1:
                for line in file1:
                    components = line.strip().split(',')
                    for i in components:
                        # fix errors and typos
                        if i == 'Boseball':
                            print("Baseball, is America's favorite past-time")
                        elif i == 'Brondy':
                            print('Brandy, is a very good friend of mine')
                        elif i == 'Pathon':
                            print('Python, is a valuable tool')
                            components.append('Python is my favorite language')
                            print(f'{i}')
                        else:
                            trys != access_key
                            attempts += 1
                            if attempts == 1:
                                print(f'Access denied, {attempts} 1st attempt ')
                                trys = int(input('Enter your 3 digit access key '))
                            elif attempts == 2:
                                print(f'Access denied, {attempts} One more attempt ')
                                trys = int(input('Enter your 3 digit access key '))
                            elif attempts == 3:
                                print('Access permanently DENIED!')


if __name__ == '__main__':
    main()
















