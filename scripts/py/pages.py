from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class intro(Page):
    pass


# class Rondas(Page):
#     def vars_for_template(self):
#         image = self.participant.vars['images'][self.round_number - 1]
#         return {'img_to_show': image}


# class ResultsWaitPage(WaitPage):
#     pass

class question(Page):
    form_model = "player"
    form_fields = ["selection"]

class Results(Page):
    form_model = "player"

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [question,Results]