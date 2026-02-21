#creating a class

class Computer:
    def __init__(self, storage):
        self.storage = storage
    
    def add_external_drive(self, external_storage):
        self.storage += external_storage
        print(f"Your computer now has {self.storage} GB of storage.")
    
    @classmethod
    def power_on(cls):
        print("Your computer is starting up!")

my_computer = Computer(512)
my_computer.power_on()
my_computer.add_external_drive(256)

#Inheritance
class Computer:
    def __init__(self, software_version):
        self.software_version = software_version

    def install_app(self, app_name, app_store):
        if app_store:
            print(f"Installing {app_name} from App store.")
        else:
            print(f"Installing {app_name} from other provider.")
    
    def update_software(self, new_software_version):
        self.software_version = new_software_version

class Tablet(Computer):
    #Override the install_app() method
    def install_app(self, app_name):
        print(f"{app_name} is being installed from the Tablet App Store.")

my_tablet = Tablet("1.1.1")

#Call the new install_app() method
my_tablet.install_app("Facebook")


# Overloading comparison __eq__
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
    
john = Person("John")
james = Person("James")
print(john == james)

#Adding two objects
class Team:
    def __init__(self, team_members):
        self.team_members = team_members

    def __add__(self, other):
        return Team(self.team_members + other.team_members)
    
rookies = Team(["Casey", "Emmitt"])
veterans = Team(["Mike", "Chuck"])
dream_team = rookies + veterans
print(dream_team.team_members)