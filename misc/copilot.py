import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_consonants(string) -> list:
    """
    Function that takes string as input and
    1) uses lower() to input string
    2) returns list of consonants in the string
    3) if there is no consonant, returns empty list
    4) if there is "x" in string, prints "x is found!"
    """

    string = string.lower()
    consonants = []
    for letter in string:
        if letter in "bcdfghjklmnpqrstvwxyz":
            consonants.append(letter)
        if letter == "x":
            print("x is found!")
    return consonants


print(get_consonants("I am a string, X"))


var: dict = {1: "a", 2: "b"}
type(var)
