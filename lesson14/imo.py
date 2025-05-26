from random import choice

capital = 'Owerri'

bird = 'Eagle'

flower = 'Rose'

song = "Anyi Choro Udo"

def randonFunFacts():
    funFacts = [
        "Owerri is known as the 'Heartland' of Nigeria.",
        "The Eagle is a symbol of strength and freedom.",
        "The Rose is often associated with love and beauty.",
        "Anyi Choro Udo means 'We want peace' in Igbo language.",
        "The state is also known for palm oil production, cassava, and local crafts."
    ]

    index = choice("01234")
    print(funFacts[int(index)])

if __name__ == '__main__':
    print("This module is being run directly.")
    randonFunFacts()