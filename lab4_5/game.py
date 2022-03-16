'''
OOP part for game
'''
class Room:
    '''
    Contains methods for rooms
    '''
    list_of_rooms = {}
    def __init__(self, name_of_room) -> None:
        '''
        room name
        >>> kitchen = Room("Kitchen")
        >>> print(kitchen.name_of_room)
        Kitchen
        '''
        self.name_of_room = name_of_room
        self.list_of_rooms = Room.list_of_rooms
    def set_description(self, description_message):
        '''
        description of the room
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        >>> print(kitchen.description_message)
        A dank and dirty room buzzing with flies.
        '''
        self.description_message = description_message
    def link_room(self, place, direction):
        '''
        Find direction where you can go from current room
        >>> kitchen = Room("Kitchen")
        >>> dining_hall = Room("Dining Hall")
        >>> kitchen.link_room(dining_hall, "south")
        >>> print(kitchen.direction)
        south
        '''
        self.place = place
        self.direction = direction
        if self.name_of_room not in self.list_of_rooms:
            self.list_of_rooms[self.name_of_room] = [(self.place, self.direction)]
        else:
            self.list_of_rooms[self.name_of_room].append((self.place, self.direction))
    def set_character(self, character):
        '''
        set character in the room
        >>> dining_hall = Room("Dining Hall")
        >>> dining_hall.set_character('dave')
        >>> print(dining_hall.character)
        dave
        '''
        self.character = character
    def set_item(self, item_name):
        '''
        set item in the room
        >>> ballroom = Room("Ballroom")
        >>> ballroom.set_item('cheese')
        >>> print(ballroom.item_name)
        cheese
        '''
        self.item_name = item_name
    def get_details(self):
        '''
        return name and description of the room
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_description("A dank and dirty room buzzing with flies.")
        >>> print(kitchen.get_details())
        Kitchen
        --------------------
        A dank and dirty room buzzing with flies.
        None
        '''
        print(self.name_of_room)
        print('--------------------')
        print(self.description_message)
        for room in self.list_of_rooms:
            if room == self.name_of_room:
                for vars in self.list_of_rooms[room]:
                    print(f'{vars[0].name_of_room} is {vars[1]}')
    def get_character(self) -> bool:
        '''
        check if anybody in the room
        >>> kitchen = Room("Kitchen")
        >>> inhabitant = kitchen.get_character()
        >>> print(inhabitant)
        None
        '''
        try:
            return self.character
        except:
            return
    def get_item(self):
        '''
        check if there ia any item
        >>> dining_hall = Room("Dining Hall")
        >>> item = dining_hall.get_item()
        >>> print(item)
        None
        '''
        try:
            return self.item_name
        except:
            return
    def move(self, side_direction):
        '''
        func to move to another room
        >>> kitchen = Room("Kitchen")
        >>> current_room = kitchen.move('south')
        >>> print(current_room.name_of_room)
        Dining Hall
        '''
        self.side_direction = side_direction
        for elem in self.list_of_rooms:
            for vars in self.list_of_rooms[elem]:
                if vars[1] == self.side_direction:
                    return vars[0]

class Enemy:
    '''
    work with enemies
    '''
    counter = 0
    def __init__(self, character, description) -> None:
        '''
        character name and description
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> print(dave.character)
        Dave
        '''
        self.character = character
        self.description = description
    def set_conversation(self, conversation_message):
        '''
        character's replic
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        >>> print(dave.conversation_message)
        What's up, dude! I'm hungry.
        '''
        self.conversation_message = conversation_message
    def set_weakness(self, weakness_item):
        '''
        set weakness of the enemy
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_weakness("cheese")
        >>> print(dave.weakness_item)
        cheese
        '''
        self.weakness_item = weakness_item
    def describe(self):
        '''
        return info about enemy
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> print(dave.describe())
        Dave
        A smelly zombie
        None
        '''
        if self.character:
            print(self.character)
            print(self.description)
    def talk(self):
        '''
        return enemy speach
        >>> kitchen = Room("Kitchen")
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        >>> kitchen.set_character(dave)
        >>> inhabitant = kitchen.get_character()
        >>> print(inhabitant.talk())
        [Dave says]: What's up, dude! I'm hungry.
        None
        '''
        print(f'[{self.character} says]: {self.conversation_message}')
    def fight(self, fight_with_item):
        '''
        func to fight with enemy
        >>> kitchen = Room("Kitchen")
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_weakness("cheese")
        >>> kitchen.set_character(dave)
        >>> inhabitant = kitchen.get_character()
        >>> print(inhabitant.fight('cheese'))
        True
        '''
        self.fight_with_item = fight_with_item
        if self.fight_with_item == self.weakness_item:
            Enemy.counter += 1
            print(f'You fend {self.character} off with the {self.fight_with_item}')
            return True
        else:
            return
    def get_defeated(self):
        '''
        if enemy defeated
        >>> kitchen = Room("Kitchen")
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_weakness("cheese")
        >>> kitchen.set_character(dave)
        >>> inhabitant = kitchen.get_character()
        >>> print(inhabitant.get_defeated())
        1
        '''
        return Enemy.counter
    

class Item:
    '''
    work with item
    '''
    def __init__(self, name_of_item) -> None:
        '''
        name of item
        >>> book = Item("book")
        >>> print(book.name_of_item)
        book
        '''
        self.name_of_item = name_of_item
    def set_description(self, description_message):
        '''
        description of item
        >>> book = Item("book")
        >>> book.set_description("A really good book entitled 'Knitting for dummies'")
        >>> print(book.description_message)
        A really good book entitled 'Knitting for dummies'
        '''
        self.description_message = description_message
    def describe(self):
        '''
        return item description
        >>> book = Item("book")
        >>> book.set_description("A really good book entitled 'Knitting for dummies'")
        >>> book.describe()
        The [book] is here - A really good book entitled 'Knitting for dummies'
        '''
        print(f'The [{self.name_of_item}] is here - {self.description_message}')
    def get_name(self):
        '''
        return item name
        >>> book = Item("book")
        >>> print(book.get_name())
        book
        '''
        return self.name_of_item
