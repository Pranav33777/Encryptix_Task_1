import random
import re

class SupportBot:
    negative_res = ("no", "nope", "sorry", "nay", "not a chance")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell")

    def _init_(self):
        self.support_responses = {
            'ask_about_product': r'.\s*product.',
            'technical_support': r'.technical.*support.',
            'about_returns': r'.\s*return.*policy.',
            'general_query': r'.how.*help.'
        }

    def greet(self):
        self.name = input("Hello! Welcome to our customer support. What's your name?\n")
        will_help = input(f"Hi {self.name}, how can I assist you today?\n").lower()
        if will_help in self.negative_res:
            print("Alright, have a great day!")
            return
        self.chat()
        
    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Thank you for reaching out. Have a great day!")
                return True
        return False

    def chat(self):
        reply = input("Please tell me your query: ").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)).lower()

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match:
                if intent == 'ask_about_product':
                    return self.ask_about_product()
                elif intent == 'technical_support':
                    return self.technical_support()
                elif intent == 'about_returns':
                    return self.about_returns()
                elif intent == 'general_query':
                    return self.general_query()
        return self.no_match_intent()

    def ask_about_product(self):
        responses = (
            "Our product is top-notch!\n",
            "We offer a variety of products for your needs.\n"
        )
        return random.choice(responses)

    def technical_support(self):
        responses = (
            "Please visit our technical support page!\n",
            "You can also contact our tech support team for assistance.\n"
        )
        return random.choice(responses)

    def about_returns(self):
        responses = (
            "We have a 30-day return policy!\n",
            "Please make sure that the product is in its original condition.\n"
        )
        return random.choice(responses)

    def general_query(self):
        responses = (
            "How can I assist you further?\n",
            "Is there anything else you need help with?\n"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Sorry, I didn't quite get that!\n",
            "Can you please provide more details?\n"
        )
        return random.choice(responses)

# Instantiate the bot and start the conversation
bot = SupportBot()
bot.greet()
