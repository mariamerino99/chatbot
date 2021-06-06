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

import datetime
from typing import Text, List, Optional, Union
from rasa_sdk.forms import FormAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import ReminderScheduled, ReminderCancelled


from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class SetAntecedentesSi(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_antecedentes_si"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("antecedentes", "si")]

class SetAntecedentesNo(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_antecedentes_no"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = 'no'

        return [SlotSet("antecedentes", "no")]

class SetChatbotBien(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_chatbot_bien"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = 1

        return [SlotSet("res_chatbot", res)]

class SetChatbotMal(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_chatbot_mal"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = -1

        return [SlotSet("res_chatbot", res)]

class ActionSessionStart(Action):
    # return the name of the action
    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        events = [SessionStarted()]

        # any slots that should be carried over should come after the
        # `session_started` event
        events.extend(self.fetch_slots(tracker))

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("utter_bienvenida"))

        return events

class SetResultadoDefs(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_defs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("res_def")

        resultado = (int(res)+1)
        print(resultado)
        return [SlotSet("res_def", resultado)]

class SetResultadoListaDespues(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_lista_despues"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("lista_compra")
        print(res)
        resultado = len(res)
        return [SlotSet("res_lista_despues", resultado)]

class SetResultadoListaInmediata(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_lista_despues"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("lista_compra")
        print(res)
        resultado = len(res)
        return [SlotSet("res_lista_inmediata", resultado)]

class SetResultadoPropios(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_propios"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("res_propios")
        resultado = (int(res)+1)
        print(resultado)
        return [SlotSet("res_propios", resultado)]

class SetResultadoObjetos(Action):
    # return the name of the action
    def name(self) -> Text:
        return "set_resultado_obj"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        res = tracker.slots.get("res_objetos")
        resultado = (int(res)+1)
        print(resultado)
        return [SlotSet("res_objetos", resultado)]


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
        if name and ages and antecedentes:
            age = int(ages)
            if age < 65 and antecedentes:
                prob = 0
            elif (age > 65 and age < 75):
                if antecedentes == "no":
                    prob = 1
                elif antecedentes == "si":
                    prob = 2
            elif age > 75:
                if antecedentes == "no":
                    prob = 2
                elif antecedentes == "si":
                    prob = 3
            # dispatcher.utter_message("Hemos llegado hasta NOMBRE", name)
        else:
            prob=2

        print("PROB",prob)
        return [SlotSet("prob", prob)]

class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Tiempo puesto")
        print("Tiempo puesto")

        date = datetime.datetime.now() + datetime.timedelta(seconds=30)

        reminder = ReminderScheduled(
            "hacer_preg2",
            trigger_date_time=date,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]

class ActionReactToReminder(Action):
    """Reminds the user to call someone."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:


        dispatcher.utter_message(f"Tiempo!")

        return []








