# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Text, List, Optional, Union
from rasa_sdk.forms import FormAction
from rasa_sdk.forms import FormValidationAction


from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class SetAntecedentesSi(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_antecedentes_si"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [[SlotSet("antecedentes", "si")]]

class SetAntecedentesNo(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_antecedentes_no"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = 'no'

        return [SlotSet("antecedentes", "no")]

class SetResultadoDefs(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_defs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.get("res_def")
        res += 1

        return [SlotSet("res_def", res)]

class ProbabilidadInicial(Action):
    # return the name of the action
    def name(self) -> Text:
        return "probabilidad_inicial"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get all the entities extracted by rasa
        name= tracker.slots.get("name")
        ages= tracker.slots.get("age")
        antecedentes= tracker.slots.get("antecedentes")
        prob = 2

        # sanity check to ensure that it was filled by rasa
        if name:
            dispatcher.utter_message("Hemos llegado hasta NOMBRE", name)
        if ages:
            dispatcher.utter_message("Hemos llegado hasta EDAD", ages)
        if antecedentes:
            dispatcher.utter_message("Hemos llegado hasta ANTEC", antecedentes)

        age = int(ages)
        if(age < 65 and antecedentes):
            prob = 0
        elif(age > 65 and age < 75 ):
            if(antecedentes == "no"):
                prob = 1
            elif(antecedentes == "si"):
                prob = 2
        elif (age > 75 ):
            if antecedentes == "no":
                prob = 2
            elif antecedentes == "si":
                prob = 3


        print(prob)
        return [SlotSet("prob", prob)]










