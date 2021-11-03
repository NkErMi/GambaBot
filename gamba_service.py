import random

from gamba_user import GambaUser


class GambaService:
    def __init__(self):
        self.gamba_users = []

    def get_user(self, id):
        user = None
        for x in self.gamba_users:
            if x.id == id:
                user = x
        return user

    def new_user(self, id, name):
        user = GambaUser(id, name, 500)
        self.gamba_users.append(user)

    def get_status(self, id):
        user = self.get_user(id)
        if user is None:
            return 'User has not joined the gamba'
        else:
            return user.name + ' has $' + str(user.money) + ' available to gamble '

    def gamble(self, id, content):
        elements_list = content.split(' ')
        size = len(elements_list)
        # Make sure user only writes one thing after $gamble eg. $gamble 500
        if size != 2:
            return 'That is not how you gamble! (size not two)'

        # Parse number in the second element from a string to an int
        gamble_amount_not_parsed = elements_list[1]
        gamble_amount = int(gamble_amount_not_parsed) if gamble_amount_not_parsed.isdigit() else None

        # Make sure that the second element is a number that the user wants to gamble
        if gamble_amount is None:
            return 'That is not how you gamble!'

        user = self.get_user(id)
        if user is None:
            return 'user has not joined the gamba'

        if gamble_amount > user.money:
            return 'You cannot gamble more than you have'

        if gamble_amount <= 0:
            return 'You have to gamble more than 0'

        # First we subtract the gamble amount from the user's own money
        user.money = user.money - gamble_amount

        number = random.randint(1, 2)

        if number == 1:
            # User won - double the money
            user.money = user.money + (gamble_amount * 2)
            return user.name + ' won ' + '$' + str(gamble_amount * 2) + ' , and now has ' + '$' + str(user.money)
        else:
            # User lost - We have already subtracted the money above
            return user.name + ' lost ' + '$' + str(gamble_amount) + ', and now has ' + '$' + str(user.money)

    def add(self, id, content):
        user = self.get_user(id)
        if user is None:
            return 'You have not joined the gamba'

        elements_list = content.split(' ')
        size = len(elements_list)
        if size != 2:
            return 'This is not how you add money (size not two)'

        add_amount_not_parsed = elements_list[1]
        add_amount = int(add_amount_not_parsed) if add_amount_not_parsed.isdigit() else None

        add_command = elements_list[0]
        if add_command != '$add':
            return 'Invalid command'

        if add_amount is None:
            return 'You cannot add money (invalid amount)'

        if add_amount <= 0:
            return 'You have to add more than 0'

        if add_amount > 500:
            return 'You have crossed the limit'

        new_balance = add_amount + user.money
        user.money = new_balance
        return 'Your new balance is ' + str(user.money)
































