# Imports
from pyfiglet import Figlet
import sys
import random
from basic_functions import get_valid_input


# Main
def main():
    #* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------
    if len(sys.argv) != 1 and len(sys.argv) != 3:
    
        print("\nError 1: Too many or none arguments  \n Usage: python fancy_font.py [-f or --font] [Name_of_font]\n")
        sys.exit(1)

    if len(sys.argv) == 3:
        
        if not sys.argv[1] in ["-f", "--font"]:
            print("\nError 2: Use -f or --font to specify the font  \n Usage: python fancy_font.py [-f or --font] [Name_of_font]\n")
            sys.exit(2)
    #* Ensure proper usage ------------------------------------------------------------------------------------------------------------------------------------
    
    # Create a new Figlet instance
    figlet = Figlet()
    
    # Determine the font to use
    font_name = sys.argv[2] if len(sys.argv) == 3 else random.choice(figlet.getFonts())
    
    #  Set the font, wherein f is the name of the font as a str 
    figlet.setFont(font = font_name)

    # Output the rendered text
    print(figlet.renderText(get_valid_input(str, "Enter text: ")))


# Start
if __name__ == "__main__":
    main()    
