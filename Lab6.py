import re  # Import the regular expression module
#akito motomura
class Backend:
    def __init__(self):
        """Initialize the Backend class and read data from a text file."""
        self.lines = []  # Initialize an empty list to store cleaned lines
        with open('/Users/motomuraakiranin/Desktop/python_second_quarter/lab6/countries-languages.txt', 'r') as file:
            for line in file:
                line = line.strip()
                cleaned_line = re.sub(r'\"|\(.*?\)|\d+(\.\d+)?%', '', line)
                # Clean the line by removing unwanted characters using regular expressions
                self.lines.append(cleaned_line)  # Add the cleaned line to the list

    def all_country(self):
        """Yield each country's information one by one."""
        for index, line in enumerate(self.lines, start=1):
            yield [str(index) + ". " + line]  # Yield the formatted line with index

    def country_line(self, start, end):
        """Yield country information within the specified range of line numbers."""
        for index, line in enumerate(self.lines, start=1):
            if start <= index <= end:
                yield [str(index) + ". " + line]  # Yield the formatted line with index
        if index < start:
            print("No countries at these lines")  # Print message if no countries found at the start line
        elif index < end:
            print("Reached last country")  # Print message if the last country is reached

    def popular_lang(self, letter):
        """Yield information about popular languages starting with the specified letter."""
        for line in self.lines:
            if line.startswith(letter):
                yield line.split(",")  # Yield languages for countries starting with the specified letter


class Frontend(Backend):
    def print_all_country(self):
        """Print all countries one by one until the user presses Enter."""
        g = self.all_country()
        while True:
            user_ = input("Press Enter to get next country: ")
            if user_ == "":
                try:
                    print(next(g)[0])  # Print the next country's information
                except StopIteration:
                    print("No more lines")  # Print message when all countries are printed
            else:
                break  # Exit the loop if user enters anything other than Enter

    def print_country_line(self):
        """Print country information based on user-defined line numbers range."""
        input_list = []
        while len(input_list) < 2:
            try:
                start = int(input("Enter starting line number:"))
                if start <= 0:
                    raise ValueError("Enter a positive number")  # Raise an error for negative or zero input
                end = int(input("Enter ending line number:  "))
                if end < start:
                    raise ValueError("Enter a bigger number")  # Raise an error if end is less than start
                input_list.append(start)
                input_list.append(end)
            except ValueError as e:
                print(e)  # Print the error message
        g = self.country_line(input_list[0], input_list[1])
        for line in g:
            formatted_line = line[0]
            country, languages = formatted_line.split(',', 1)
            languages = languages.split(',')
            print(format(country.strip(), "<30") + ":" + ",".join(languages[0:4]))
            for i in range(4, len(languages), 4):
                group = ",".join(languages[i:i + 4])
                print(" " * 30 + group)

    def print_popular_lang(self):
        """Print information about countries and popular languages based on user input."""
        while True:
            try:
                user_ = input("Enter the first letter of country names: ").capitalize()
                break  # Exit the loop if valid input is entered
            except ValueError:
                print("Enter a valid input")  # Print message for invalid input

        g = self.popular_lang(user_)
        language_countries = {}
        country_list = []
        for country_data in g:
            country_name = country_data[0].strip()
            languages = country_data[1:]
            country_list.append(country_name)
            for language in languages:
                language = language.strip()
                if language not in language_countries:
                    language_countries[language] = []
                language_countries[language].append(country_name)
        print("Countries starting with", user_, ":")
        print(", ".join(country_list))  # Print countries starting with the specified letter
        popular_languages = sorted(language_countries.items(), key=lambda x: len(x[1]), reverse=True)

        if popular_languages:
            print("Popular languages:")
            for language, countries in popular_languages:
                if len(countries) >= 2:
                    print(f"{language}: {', '.join(countries)}")  # Print popular languages and their countries
                else:
                    print("There is no popular language")
                    break  # Exit the loop if there are no popular languages

    def run(self):
        """Run the program with a menu-driven interface for user interaction."""
        while True:
            print()
            print("1. All countries\n2. Countries in range of lines \n3. Countries starting with letter\n4. Quit")
            try:
                user_ = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input")  # Print message for invalid input
            if user_ == 1:
                print("Data for one country at a time")
                self.print_all_country()
            elif user_ == 2:
                self.print_country_line()
            elif user_ == 3:
                self.print_popular_lang()
            elif user_ == 4:
                break  # Exit the program if the user chooses to quit


# Create an instance of the Frontend class and run the program
frontend_instance = Frontend()
frontend_instance.run()





    
