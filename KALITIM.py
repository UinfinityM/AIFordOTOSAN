from math import acosh
from operator import index



import streamlit as st
import os
import pandas as pd
import google.generativeai as genai
import fitz
from click import prompt


from dotenv import load_dotenv
from PIL import Image
from PyPDF2 import PdfFileReader
from numpy.ma.core import minimum_fill_value
from pyparsing import oneOf


st.set_page_config(layout="wide")
st.sidebar.header("KAHVE DÜNYASINA HOŞ GELDİNİZ")




GOOGLE_API_KEY="AIzaSyAkaefwdG_Ekhb3qVMBSc_HrtiS20o0Pp0"
genai.configure(api_key=GOOGLE_API_KEY)


safety_settings = [
 {
   "category": "HARM_CATEGORY_HARASSMENT",
   "threshold": "BLOCK_ONLY_HIGH",
 },
 {
   "category": "HARM_CATEGORY_HATE_SPEECH",
   "threshold": "BLOCK_ONLY_HIGH",
 },
 {
   "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
   "threshold": "BLOCK_ONLY_HIGH",
 },
 {
   "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
   "threshold": "BLOCK_ONLY_HIGH",
 }
]


modelMUJDEHAN = genai.GenerativeModel(
 model_name='gemini-1.5-flash-latest',
 safety_settings=safety_settings,


)
import streamlit as st
import streamlit as st
import streamlit as st

class Coffee:
    def __init__(self, name, water, coffee, milk=0):
        self.name = name
        self.water = water
        self.coffee = coffee
        self.milk = milk

class CoffeeMachine:
    def __init__(self):
        self.ingredients = {"water": 1000, "coffee": 1000, "milk": 1000}
        self.prices = {"espresso": 10.0, "cappuccino": 20.0, "latte": 5.0}
        self.profit = 0
        self.cash = 0
        self.menu = {
            "espresso": Coffee("espresso", 100, 30),  # Updated coffee amount
            "cappuccino": Coffee("cappuccino", 0, 50, 20),  # Updated milk amount
            "latte": Coffee("latte", 40, 30, 50)  # Updated water amount
        }

    def check_ingredients(self, coffee):
        if (self.ingredients["water"] >= coffee.water and
            self.ingredients["coffee"] >= coffee.coffee and
            self.ingredients["milk"] >= coffee.milk):
            return True
        return False

    def make_coffee(self, coffee_type):
        coffee = self.menu[coffee_type]
        if self.check_ingredients(coffee):
            self.ingredients["water"] -= coffee.water
            self.ingredients["coffee"] -= coffee.coffee
            self.ingredients["milk"] -= coffee.milk
            self.profit += self.prices[coffee_type]
            self.cash += self.prices[coffee_type]
            st.write(f"{coffee.name.capitalize()} hazır! Afiyet olsun!")
            self.report()
        else:
            st.write(f"ÜZGÜNÜZ, {coffee.name.capitalize()} için yeterli malzeme yok!")

    def report(self):
        st.write("\n--- Güncel Rapor ---")
        st.write(f"Su: {self.ingredients['water']} ml")
        st.write(f"Kahve: {self.ingredients['coffee']} ml")
        st.write(f"Süt: {self.ingredients['milk']} ml")
        st.write(f"Biriken Para: {self.cash} TL")
        st.write(f"Para: {self.profit} TL\n")

    def process_coins(self, tl5, tl10):
        total = tl5 * 5 + tl10 * 10
        return round(total, 2)

    def get_payment(self, coffee_type):
        amount = self.prices[coffee_type]
        st.write(f"Ücret: {amount} TL. Lütfen para ekleyin.")
        tl5 = st.number_input("Kaç 5 TL?", min_value=0, step=1)
        tl10 = st.number_input("Kaç 10 TL?", min_value=0, step=1)
        payment = self.process_coins(tl5, tl10)
        if payment < amount:
            st.write("Üzgünüm, yeterli para yok. Para iade edildi.")
            return False
        elif payment > amount:
            st.write(f"Para üstü: {round(payment - amount, 2)} TL")
        self.cash += payment
        st.write(f"Biriken Para: {self.cash} TL")
        return True

machine = CoffeeMachine()

st.title("Kahve Makinesi")
choice = st.selectbox("Ne istersiniz? (espresso/latte/cappuccino/rapor/kapat): ",
                      ['espresso', 'latte', 'cappuccino', 'rapor', 'kapat'])

if choice == 'kapat':
    st.write("Kahve makinesi kapatılıyor. Hoşçakalın!")
elif choice == 'rapor':
    machine.report()
else:
    if machine.get_payment(choice):
        machine.make_coffee(choice)
