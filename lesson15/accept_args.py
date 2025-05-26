
def hello(name,lang):
   greetings = {
      "English": "Hello",
        "Spanish": "Hola",
        "French": "Bonjour",
        "Igbo": "Ndewo",
   }
   msg = f"{greetings[lang]}, {name}! Welcome to the program."
   print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="A simple program to demonstrate argument parsing."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", type=str, required=True,
        help="Your name to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="lang", type=str, choices=["English", "Spanish", "French", "Igbo"],
        default="English",
        help="Language for the greeting (default: English)."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)