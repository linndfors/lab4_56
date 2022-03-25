#----------Person class----------
class Person():
    '''
    class for create character
    '''
    name_list = {}
    def __init__(self, person_name, person_replic, description) -> None:
        '''
        init func
        >>> character = Person('mike', 'bye', 'lady')
        >>> print(character.person_name)
        mike
        '''
        self.person_replic = person_replic
        self.person_name = person_name
        self.description = description
    def write_name(self):
        '''
        Write down characters in list
        >>> character = Person('mike', 'bye', 'lady')
        >>> print(character.write_name())
        None
        '''
        Person.name_list[self.person_name] = self
    def describe(self):
        '''
        Describe character
        >>> character = Person('mike', 'bye', 'lady')
        >>> character.describe()
        mike("lady")
        '''
        print(f'{self.person_name}("{self.description}")')
    def talk(self) -> bool : 
        '''
        Talk with character
        >>> character = Person('mike', 'bye', 'lady')
        >>> character.talk()
        bye
        '''
        print(self.person_replic)
        if '?' in self.person_replic:
            return True

class Enemy(Person):
    def __init__(self, person_name, person_replic, description, fear) -> None:
        '''
        init func
        >>> enemy = Enemy('joe', 'boo', 'ghost', 'light')
        >>> print(enemy.fear)
        light
        '''
        super().__init__(person_name, person_replic, description)
        self.fear = fear
    def fight(self, weapon):
        '''
        Fight with weapon, check if you get win
        >>> light = Item('light', 'Light as a sun')
        >>> enemy = Enemy('joe', 'boo', 'ghost', light)
        >>> print(enemy.fight('light'))
        True
        '''
        self.weapon = weapon
        if self.weapon == self.fear.item_name:
            return True

class Friend(Person):
    def __init__(self, person_name, person_replic, description, present = None) -> None:
        '''
        init func
        >>> friend = Friend('mark', 'salut', 'boy', 'flowers')
        >>> print(friend.present)
        flowers
        '''
        super().__init__(person_name, person_replic, description)
        self.present = present
    def talk(self) -> bool:
        '''
        Talk with characters, who can give you something
        >>> flowers = Item('flowers', 20)
        >>> friend = Friend('mark', 'salut', 'boy', flowers)
        >>> friend.talk()
        salut
        mark give you "flowers"
        Your backpack: ['flowers']
        '''
        result = super().talk()
        if self.present:
            if self != seller_man:
                backpack[0].append(self.present)
                backpack[1].append(self.present.item_name)
                print(f'{self.person_name} give you "{self.present.item_name}"')
                print(f'Your backpack: {backpack[1]}')
        return result
        

class Boss(Enemy):
    def __init__(self, person_name, person_replic, description, fear, super_skill) -> None:
        '''
        the main enemy
        >>> boss = Boss('jek', 'Hello', 'Guy', 'no fear)', 'punch')
        >>> print(boss.person_name)
        jek
        '''
        super().__init__(person_name, person_replic, description, fear)
        self.super_skill = super_skill
    def spec_fight(self, energy):
        '''
        Special fight with Boss
        '''
        self.talk()
        print("Every year, one and the same....\nYou are going here,\
 and you don't know anything about Ukraine. \n\
You even won't be able to answer a couple of the questions about Ukraine.")
        print('-----THE GAME STARTED-----')
        independence = input('When Ukraine became independent?(year)\n>>>')
        if independence != '1991':
            energy -= 25
            print('HAHA NOOOOOO')
            print(f'Now your energy = {energy}')
        emblem = input('What is ilustrated on Ukrainian emblem?\n>>>')
        if emblem.lower() != 'trident':
            energy -= 25
            print('HAHA NOOOOOO')
            print(f'Now your energy = {energy}')
        father = input('Our father is?\n>>>')
        if father.lower() != 'bandera':
            energy -= 25
            print('HAHA NOOOOOO')
            print(f'Now your energy = {energy}')
        times = input('How many times Ukraine won Evrovision?\n>>>')
        if times != '2':
            energy -= 25
            print('HAHA NOOOOOO')
            print(f'Now your energy = {energy}')
        if energy > 0:
            print('Hmmm, weird, allright, do you have a national tatoo?')
            if 'tatoo' in backpack[1]:
                return 'Okay, you won'
        else:
            print('HA HA HA, AS I MENTIONED \nYOU STUPID JERK')
            print(f'Baba Luda make a "{self.super_skill}" and kill you :(')
            return




#--------Item class----------
class Item():
    def __init__(self, item_name, description) -> None:
        '''
        items you can keep in backpack
        >>> flowers = Item('flowers', 'roses')
        >>> print(flowers.item_name)
        flowers
        '''
        self.item_name = item_name
        self.description = description
    def describe(self):
        '''
        Describe items in details
        >>> flowers = Item('flowers', 'roses')
        >>> flowers.describe()
        flowers("roses")
        '''
        # for elem in Location.items_seeker[self.room.name]:
        print(f'{self.item_name}("{self.description}")')
class Weapon(Item):
    '''
    items that can be weapon
    '''
    def __init__(self, item_name, description, damage) -> None:
        '''
        init func
        >>> knife = Weapon('knife', 'silver', 20)
        >>> print(knife.damage)
        20
        '''
        super().__init__(item_name, description)
        self.damage = damage

class Help(Item):
    '''
    items that can be help
    '''
    def __init__(self, item_name, description, amount, profit) -> None:
        '''
        init func
        >>> gum = Help('gum', 'strawberry', 3, 13)
        >>> print(gum.profit)
        13
        '''
        super().__init__(item_name, description)
        self.profit = profit
        self.amount = amount



#-----------Location class------------
class Location():
    '''
    location class
    '''
    items_seeker = {}
    characters_seeker = {}
    def __init__(self, name, street) -> None:
        '''
        init func
        >>> shop = Location('Antique store', 'Krakivska St')
        >>> print(shop.name)
        Antique store
        '''
        self.name = name
        self.street = street
    def get_details(self):
        '''
        Describe location in details
        >>> shop = Location('Antique store', 'Krakivska St')
        >>> shop.get_details()
        Antique store, located on Krakivska St
        '''
        print(f'{self.name}, located on {self.street}')
    def get_ways(self):
        '''
        Return possible ways, where you can go
        >>> shop = Location('Antique store', 'Krakivska St')
        >>> shop.get_ways()
        <BLANKLINE>
        Possible ways to go:
        Lviv center
        '''
        print('\nPossible ways to go:')
        if type(choice_room[self.name]) != tuple:
            print(choice_room[self.name].name)
        else:
            for elem in choice_room[self.name]:
                print(elem.name) 
    def set_character(self, character):
        '''
        Set character in current location
        >>> shop = Location('Antique store', 'Krakivska St')
        >>> character = Person('mike', 'bye', 'lady')
        >>> shop.set_character(character)
        >>> print(shop.character.person_name)
        mike
        '''
        self.character = character
        if self.name not in Location.characters_seeker:
            Location.characters_seeker[self.name] = self.character
        else:
            Location.characters_seeker[self.name] = [Location.characters_seeker[self.name], self.character]
    def set_item(self, item):
        '''
        set item in the location
        >>> shop = Location('Antique store', 'Krakivska St')
        >>> apple = Item('apple', 'red')
        >>> shop.set_item(apple)
        >>> print(shop.item.item_name)
        apple
        '''
        self.item = item
        if self.name not in Location.items_seeker:
            Location.items_seeker[self.name] = self.item
        else:
            Location.items_seeker[self.name] = Location.items_seeker[self.name], self.item
        # print(Location.items_seeker)
    def characters(self) -> bool:
        '''
        check if anybody in the room
        >>> shop = Location('Antique store', 'Krakivska St')
        >>> shop.characters().person_name
        'Big Mykola'
        '''
        try:
            # return self.character
            return Location.characters_seeker[self.name]
        except:
            return
    def items(self):
        '''
        check if there is any item
        >>> frankivskyi_district = Location('Frankivskyi District', 'Frankivskya St')
        >>> frankivskyi_district.items().item_name
        'gun'
        '''
        try:
            return Location.items_seeker[self.name]
        except:
            return
    def move(self, room_to_move_in):
        '''
        move to another location
        >>> shop = Location('Antique store', 'Krakivska St')
        >>> print(shop.move('Lviv center').name)
        Lviv center
        '''
        self.room_to_move_in = room_to_move_in
        for room in room_list:
            if room.name == self.room_to_move_in:
                return room



#---------objects-------
amulet = Item('amulet', 'A gold amulet with small emarald')
slingshot = Weapon('slingshot', 'A wood slingshot, like in your childhood', 25)
tatoo = Item('tatoo', 'An ukrainian symbolic')
police_call = Weapon('phone', 'You can make a call to police', 15)
gun_palanytsya = Weapon('gun', 'Named: "Palanytsya"', 20)
map = Item('map', 'a large map of Lviv, with mark on it')
syrnyky = Help('syrnyky', 'delicates from Trapezna', 4, 5)

items_list = [amulet, slingshot, tatoo, police_call, gun_palanytsya, map, syrnyky]

valera = Enemy('Valera', 'Hey, you jerk, what are you doing here?\n\
Do you want to get a push? \nHa-ha-ha. Come here\n',
    '18 year old guy, called "Valera" sitted near a fontain and\
 eat sunflower seeds. He was wore in total-black Adidas costume and on his head was red cap.\
    \nSudenly he noticed you and stand to warm up.', police_call)

moskal = Enemy('Moskal', 'Hey, banderovets, chto ty hochesh, idi otsuda poka ne pozdno',
'A man, probably 30-35 years old, he has a Russian flag on his jacket. \nHe stay near coffee-house\
and had an angry conversation with seller. \nYa vam russkim yazykom povtoryau...', gun_palanytsya)

kaposnyk = Enemy('Little kaposnyk', "Hi, hi, hi you'll never catch me",
'A little boy, playing hide and seek with his friends', slingshot)

angry_grany = Boss('Babya Luda', "Oh, how I hate all this tourist, I'm so tired of you.",
'An old woman with 3 white cats, sitt with angry face and swear on everybody, whom she noticed',
tatoo, 'spit')

bohdan = Friend('Bohdan', 'Guys, please wait for me I should talk for a few minutes.\n\
Hey are you allright, do you find an amulate?', 'A tall, handsome guy. He was a history student\n\
and your good friend.')

yaroslav_hrytsak = Friend('Yaroslav Hrytsak', 'Colleague, I want help you, please take this\
 map, it will be really usefull', 'A popular historic, who teaches History in UCU', map)

pani_svitlana = Friend('Pani Svitlana', "Go with me, I'll show you an exit",
'A beautiful girl, in yellow dress with kinda funny dog in her hands.',
slingshot)

seller_man = Friend('Big Mykola', 'Hello, lovely, if you want the amulet, you should pay kash.\nDo you has it?',
'A big, fat man, who work in this antiquar shop for whole life.\n\
His shirt was in something yellow yeww', amulet)

characters = [valera, moskal, kaposnyk, angry_grany, bohdan, yaroslav_hrytsak, pani_svitlana, seller_man]
for human in characters:
    human.write_name()

ucu_campus = Location('UCU', 'Kozelnytska St')
your_room = Location('My room', 'Kozelnytska St')
trapezna = Location('Trapezna', 'Kozelnytska St')
stryiskyi_park = Location('Stryiskyi park', 'Stryiska St')
center = Location('Lviv center', 'Krakivska St')
shop = Location('Antique store', 'Krakivska St')
frankivskyi_district = Location('Frankivskyi District', 'Frankivskya St')

room_list = [ucu_campus, your_room, trapezna, stryiskyi_park, center, shop, frankivskyi_district]
choice_room = {your_room.name: (ucu_campus, trapezna), ucu_campus.name:(your_room, trapezna),
trapezna.name:(your_room, ucu_campus), ucu_campus.name: (stryiskyi_park, trapezna, your_room),
stryiskyi_park.name: (center, ucu_campus), center.name: (shop, frankivskyi_district, stryiskyi_park),
shop.name: center, frankivskyi_district.name: (ucu_campus, center)}


trapezna.set_character(bohdan)
ucu_campus.set_character(yaroslav_hrytsak)
stryiskyi_park.set_character(pani_svitlana)
stryiskyi_park.set_character(valera)
shop.set_character(seller_man)
center.set_character(moskal)
frankivskyi_district.set_character(angry_grany)
frankivskyi_district.set_character(kaposnyk)

trapezna.set_item(syrnyky)
your_room.set_item(police_call)
your_room.set_item(tatoo)
frankivskyi_district.set_item(gun_palanytsya)

current_room = your_room
backpack = [[], []]

find_amulet = False
dead = False
energy = 50


while energy > 0 and find_amulet == False:

    print("\n")
    current_room.get_details()
    current_room.get_ways()

    inhabitant = current_room.characters()
    if inhabitant is not None:
        print('\nCharacters you can talk with:')
        if type(inhabitant) == list:
            for in_elem in inhabitant:
                in_elem.describe()
        else:
            inhabitant.describe()

    item = current_room.items()
    if item is not None:
        print('\nCurrent items you can take:')
        if type(item) == tuple:
            for elem in item:
                elem.describe()
        else:
            item.describe()

    command = input('\nPlease chose yout action("take", "eat", "talk", "exit"\
 or write place to go from the list below "Possible ways to go")\n\ntalk - talk with cracter in the room\n\
eat - eat stuff and raise your hp\ntake - take an item to your backpack\nexit - end Game\n>>> ')

    if command in choice_room.keys():
        for place in room_list:
            if place.name == command:
                if current_room == shop:
                    current_room = center
                elif place in choice_room[current_room.name]:
        # Move in the given direction
                    current_room = current_room.move(command)
                else:
                    print('There is no way\nSorry ;(')
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            if type(inhabitant) == list:
                if len(inhabitant) == 1:
                    inhabitant = inhabitant[0]
            if type(inhabitant) != list:
                if isinstance(inhabitant, Friend):
                    if inhabitant.talk():
                        answer = input('>>> ')
                        if inhabitant == bohdan:
                            if answer.lower() == 'yes':
                                if 'amulet' in backpack[1]:
                                    print('Good job, my friend!\nThank you so much <3')
                                    find_amulet = True
                                else:
                                    print('*There is no amulet :(')
                            else:
                                print('So time is running out')
                        elif inhabitant == seller_man:
                            if 'amulet' not in backpack[1]:
                                if answer.lower() == 'yes':
                                    if 'money' in backpack[1]:
                                        print('Oh, good here your amulet <3')
                                        print(f'{seller_man.person_name} give you "{amulet.item_name}"')
                                        backpack[1].append(amulet.item_name)
                                        backpack[1].remove('money')
                                        print(f'Your backpack: {backpack[1]}')
                                    else:
                                        print("You don't have money)\nSo, return only with cash")
                                else:
                                    print("So, return only with cash")
                            else:
                                print('Shop closed')
                    inhabitant.present = None
                if isinstance(inhabitant, Enemy):
                    if inhabitant == angry_grany:
                                print('-------You meet a BOSS---------')
                                print(f'Your enemy: {inhabitant.person_name}')
                                super_fight = angry_grany.spec_fight(energy)
                                if super_fight is not None:
                                    print(super_fight)
                                    Location.characters_seeker[current_room.name].remove(inhabitant)
                                    backpack[1].remove('tatoo')
                                else:
                                    print('Sorry, you loose a boss, so bye-bye\nYour mission failed')
                                    energy = 0
                                    break
                    else:
                        inhabitant.talk()
                        print(f'Your enemy: {inhabitant.person_name}')
                        print(f'How will you kick {inhabitant.person_name}?')
                        print(backpack[1])
                        while True:
                            weapon = input('>>>')
                            if weapon not in backpack[1]:
                                if len(backpack[1]) == 0:
                                    print('Oh, your backpack is empty\nYou loose:(')
                                    weapon = 1
                                    break
                                else:
                                    print('There is no such stuff')
                            else:
                                break
                        if inhabitant.fight(weapon):
                            for this_item in items_list:
                                if this_item.item_name == weapon:
                                    print(f'You make {this_item.damage} damage')
                            print(f'My congratulation! You defeated {inhabitant.person_name}')
                            if inhabitant == moskal:
                                backpack[1].append('money')
                                print('Moskal run out and give you all his money')
                                del Location.characters_seeker[current_room.name]
                                backpack[1].remove(weapon)
                        else:
                            print('Ohh, bad deal, youl loose 25 hit points')
                            energy -= 25
            else:
                name_of_person = input('Here is more then one person, with whom you want to\
have a conversation?\nWrite name:')
                for human_name in Person.name_list.keys():
                    if human_name == name_of_person:
                        if Person.name_list[human_name] == angry_grany:
                                print('-------You meet a BOSS---------')
                                print(f'Your enemy: {human_name}')
                                super_fight = angry_grany.spec_fight(energy)
                                if super_fight is not None:
                                    print(super_fight)
                                    Location.characters_seeker[current_room.name].remove(Person.name_list[human_name])
                                    backpack[1].remove('tatoo')
                                else:
                                    print('Sorry, you loose a boss, so bye-bye\nYour mission failed')
                                    energy = 0
                                    break
                        else:
                            Person.name_list[human_name].talk()
                            if isinstance(Person.name_list[human_name], Enemy):
                                print(f'Your enemy: {human_name}')
                                print(f'How will you kick {human_name}?')
                                print(backpack[1])
                                while True:
                                    weapon = input('>>>')
                                    if weapon not in backpack[1]:
                                        if len(backpack[1]) == 0:
                                            print('Oh, your backpack is empty\nYou loose:(')
                                            weapon = 1
                                            break
                                        else:
                                            print('There is no such stuff')
                                    else:
                                        break
                                if Person.name_list[human_name].fight(weapon):
                                    for this_item in items_list:
                                        if this_item.item_name == weapon:
                                            print(f'You make {this_item.damage} damage')
                                    print(f'My congratulation! You defeated {human_name}')
                                    Location.characters_seeker[current_room.name].remove(Person.name_list[human_name])
                                    backpack[1].remove(weapon)
                                else:
                                    print('Ohh, bad deal, youl loose 25 hit points')
                                    energy -= 25
                            else:
                                Person.name_list[human_name].present = None               
    elif command == "eat":
        if "syrnyky" in backpack[1]:
            while True:
                print(f'You have {syrnyky.amount}')
                syr_count = int(input(f'How many "syrnykiv" you want to eat(1 "syrnyk" = {syrnyky.profit} hit points)?\n>>>'))
                if syr_count <= syrnyky.amount:
                    for _ in range(syr_count):
                        energy += syrnyky.profit
                        syrnyky.amount -= 1
                        if syrnyky.amount == 0:
                            backpack[1].remove('syrnyky')
                    print(f'Your energy: {energy}')
                    break
                else:
                    print("You don't have so")
        else:
            print('There is nothing to eat')
    elif command == "exit":
        print('Thanks for the game <3')
        exit()
    elif command == "take":
        if item is not None:
            if type(item) != tuple:
                print("You put the " + item.item_name + " in your backpack")
                backpack[0].append(item)
                backpack[1].append(item.item_name)
            else:
                for elem in item:
                    print("You put the " + elem.item_name + " in your backpack")
                    backpack[0].append(elem)
                    backpack[1].append(elem.item_name)
            print(f'Your backpack: {backpack[1]}')
            Location.items_seeker[current_room.name] = None
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
