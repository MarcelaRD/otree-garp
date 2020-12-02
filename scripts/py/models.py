from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Marcela'

doc = """
This app is for testing preferences
"""

import random
class Constants(BaseConstants):
    name_in_url = 'garp_test'
    players_per_group = None
    num_rounds = 4
   # imgs  = ['img1.jpg', 'img2.jpg',]

class Subsession(BaseSubsession):

    def creating_session(self):
        print('in creating_session', self.round_number)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    selection = models.IntegerField(label="Elije el punto que mas prefieres",
    choices=[1, 2, 3, 4, 5, 6, 7, 8,9,10],
                                 widget=widgets.RadioSelectHorizontal
                                    )


