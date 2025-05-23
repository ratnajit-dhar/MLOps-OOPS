class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""
                        Welcome to Chatbook !! How would you like to proceed?
                        1. Press 1 to Signup
                        2. Press 2 to Signin
                        3. Press 3 to write a post
                        4. Press 4 to message a friend
                        5. Press any other key to exit\n
                        """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter your email: ")
        password = input("Setup your password: ")
        self.username = email
        self.password = password
        print("You have signed up successfully!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("You need to signup first by pressing 1!")
        else:
            username = input("Enter your email: ")
            password = input("Enter your password: ")
            if username == self.username and password == self.password:
                print("You have signed in successfully!")
                self.loggedin = True
            else:
                print("Invalid credentials, please try again.")
            
obj = chatbook()
