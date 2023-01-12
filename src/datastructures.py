
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
            "first_name":"John",
            "last_name": "Jackson",
            "age": 33,
            "lucky_numbers": [7,13,22],
            "id": self. _generateId(),
            },

            {"first_name":"Jane",
            "last_name": "Jackson",
            "age": 35,
            "lucky_numbers": [10,14,23],
             "id": self. _generateId(),
            },

            {
            "first_name":"Jimmy",
            "last_name": "Jackson",
            "age" :[5],
            "lucky_numbers": [1],
             "id": self._generateId(),
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        pass

    def delete_member(self, id):
        #pop
        for member in self.members:
            if member ["id"] == id:
            index = self._members.index(member)
            self._members.pop(index)
            return 200

    def get_member(self, id):
        for member in self.members:
            if member ["id"] == id:
               return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
