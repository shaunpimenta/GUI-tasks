import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
kivy.require('2.0.0')

# Set the app size
Window.size = (500, 700)

# Designate Our .kv design file
Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    # Create a button pressing function
    def button_press(self, button):
        # create a variable that contains whatever was there in the textbox
        prior = self.ids.calc_input.text

        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # Create Function to remove last character in textbox
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove the last item in the textbox
        prior = prior[:-1]
        # Output ack to the textbox
        self.ids.calc_input.text = prior
       
    # Create function to make textbox positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there's a - sign already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
           self.ids.calc_input.text = f'-{prior}' 



    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        # Split out text box by +
        num_list = prior.split("+")
        
        if  "+" in prior and "." not in num_list[-1]:
             # Add a decimal to the end of the text
             prior = f'{prior}.'
             # Output back to the text box
             self.ids.calc_input.text = prior

        elif "." in prior:
            pass
        else:
             # Add a decimal to the end of the text
             prior = f'{prior}.'
             # Output back to the text box
             self.ids.calc_input.text = prior

    # Create Addition Function
    def math_sign(self, sign):
        # create a variable that contains whatever was there in the textbox
        prior = self.ids.calc_input.text
        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'


     # Create equals to Function
    def equals(self):
        prior = self.ids.calc_input.text

        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            # loop through our list
            for number in num_list:
                answer = answer + float(number)

            # print the answer in the text box
            self.ids.calc_input.text = str(answer)

  # class CalculatorApp(App):
  #   def _init_(self, **kwargs):
  #       super()._init_(**kwargs)
  #       self.build()
  #
  #   def build(self):
  #       return MyLayout()

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()