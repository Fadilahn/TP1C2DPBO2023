# Import Student class from Student module
from Student import Student

# Define the EnglishClubMember class which inherits from Student
class EnglishClubMember(Student):
    _english_level = 0

    def __init__(self, name, gender, nim):
        super().__init__(name, gender, nim)

    def learn_english(self):
        # Increase the english level of the member by 1 and print the current level
        self._english_level += 1
        print(f"{self._name} learns English. Current level: {self._english_level}")

    def design_proker(self, proker, english_club):
        # Add the proker to the EnglishClub's proker list and print the action
        english_club.add_proker(proker)
        print(f"{self._name} designs proker {proker}.")
        print(f"Proker {proker} is added to the proker list of EnglishClub.")

# Define the EnglishClub class
class EnglishClub:
    _members = []
    _prokers = []

    def __init__(self):
        pass

    def add_member(self, member):
        # Add a member to the EnglishClub's member list if the member is an instance of EnglishClubMember
        if isinstance(member, EnglishClubMember):
            self._members.append(member)

    def add_proker(self, proker):
        # Add a proker or multiple prokers to the EnglishClub's proker list
        if isinstance(proker, list):
            self._prokers.extend(proker)
        else:
            self._prokers.append(proker)

    def displayProkers(self):
        # Display the EnglishClub's proker list
        print("Proker English Club:")
        for i, proker in enumerate(self._prokers):
            print(f"{i+1}. {proker}")

    def displayMembers(self):
        # Display the EnglishClub's member list
        print(f"Member English Club:")
        for i, member in enumerate(self._members):
            print(i+1, member.getName())

    def selectLeader(self):
        # Find the member with the highest english level and select them as the leader of EnglishClub
        max_english_level = -1
        selected_member = None
        for member in self._members:
            if member._english_level > max_english_level:
                max_english_level = member._english_level
                selected_member = member
        print(f"{selected_member.getName()} is selected as the Leader of EnglishClub.")