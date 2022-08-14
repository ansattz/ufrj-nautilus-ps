# @ansattz
import readline

def menu():
    print('========= GUIDE =========')
    print('')
    print('1 - Why Linux')
    print('2 - Docker')
    print('3 - Docker Compose')
    print('')
    print('==========================')
    print('')
    print('4 - Activities')
    print('0 - Close Guide')
    print('')
    print('==================================')

while True:
    menu()
    
    option = input('Choose one option: ')
    if option == '1':
        print('')
        print("""The advantages of embedded Linux over proprietary embedded 
systems include multiple suppliers for software, development
and support; no royalties or licensing fees; a stable kernel; 
the ability to read, modify and redistribute the source code. 
The more important thing is: ROS --Robot Operating System,
used in Nautilus -- is supported only by linux systems.""")
        print('')
    elif option == '2':
        print('') 
        print("""Docker is a software that runs on the command line and 
allows you to automate the deployment of applications within 
software containers.""")
        print('')
        print("""Docker containers wrap a piece of software in a complete
file systems that contains everything needed to run:
code, runtime, system tools, system libraries - anything 
that can be installed on a server. This ensures that the 
software will always work the same, regardless of its environment.""")
        print('')
    elif option == '3':
        print('')
        print("""Compose is a tool for defining and running
multi-container Docker applications. With Compose, 
you use a YAML file to configure your application’s services. 
Then, with a single command, you create and start all 
the services from your configuration.""")
        print('')
    elif option == '4':
        print('')
        print("""- create_container.sh is a bash script to create the first container
without any pre-settings. 
\u001b[33m chmod +x create_container.sh \u001b[0m
\u001b[33m ./create_container.sh \u001b[0m """)
        print('')
        print("""- Dockerfile simplify the construction of a container. 
With Dockerfile we are able to build images however we want (check repos), 
like in a GNU Parabola.
\u001b[33m docker build .\u001b[0m """)
        print('')
        print("""- docker-compose.yml is the YAML file to apply a pre-setting to
initialize our container.
\u001b[33m docker-compose up -d; docker attach <service> \u001b[0m """)
        print('')
    elif option == '0':
        print('')
        print("""\u001b[34m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⢀⣤⣤⡄⠀⠀⠀⠀⠀⣴⣶⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡄⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠋⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢤⣤⠄⠀⠀⢤⡤⠄⢤⡤⠤⢤⡄⠠⢤⡤⠤⣄⠀⠀⢤⣤⠄⢀⣀⣀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⡀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⠀⠀⠀⠀⡇⠀⢸⡇⠀⢀⠁⠀⢸⡇⠀⣹⡇⠀⠀⣿⠀⢸⣿⣿⣦⠀⢸⣿⠀⣀⣀⣀⡀⠀⣀⡀⠀⣀⣀⣀⣾⣇⡀⣈⣉⡀⣿⡇⢀⣀⠀⢀⣀⠀⠀⣀⣀⣀⠀⠀
⠀⠀⠀⣿⠀⠀⠀⠀⡇⠀⢸⡟⠒⠻⠀⠀⢸⡗⢶⣏⠀⠀⠀⣿⠀⢸⣿⡇⢻⣧⣸⣿⠀⣻⣭⣿⣷⠀⣿⡇⠀⣿⣿⠉⣿⡏⠁⣿⣿⡇⣿⡇⢸⣿⠀⢸⣿⠀⣿⣿⣭⣉⠀⠀
⠀⠀⠀⢿⣄⠀⠀⣸⠃⠀⢸⡇⠀⠀⠀⠀⢸⡇⠀⢿⣄⠀⠀⣿⠀⢸⣿⡇⠀⢻⣿⣿⢸⣿⣃⣼⣿⠀⢿⣧⣀⣿⣿⠀⣿⣇⡀⣿⣿⡇⣿⡇⢸⣿⣄⣸⣿⠀⣀⣘⣻⣿⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠋⠙⠃⠀⠀⠙⠋⠙⠀⠀⠉⠃⣸⠏⠀⠈⠉⠁⠀⠀⠉⠉⠀⠉⠉⠉⠉⠀⠈⠉⠉⠉⠉⠀⠈⠉⠁⠉⠉⠁⠉⠁⠀⠉⠉⠉⠉⠀⠉⠉⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        \u001b[0m""")
        print('')
        break
    else:
        print('')
        print('=======> Invalid option')
        print('')





