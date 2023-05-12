"""Simlified Markdown editor """


class Markdown_editor:
    """Markdown editor class"""

    def __init__(self):
        """List for save"""

        self.save = []

    def user_input(self):
        """user input"""

        text = input(f"Text:>>")
        return text

    def text(self):
        """full text"""

        self.save.append(self.user_input())
        print(*self.save)

    def help_command(self):
        """Special command '!help'"""

        print("""[plain]
[bold]
[italic]
[inlaine-code]
[link]
[header]
[unordered-list]
[ordered-list]
[new-line]""")

    def file_save(self, filename):
        """Saving text in the file"""

        with open(filename, "w", encoding="utf-8") as file:
            file.write('\n'.join(self.save))

    def plain(self):
        """plain format"""

        self.save.append(self.user_input())
        print(*self.save)

    def bold(self):
        """bold format"""

        formated = f"**{self.user_input()}**"
        self.save.append(formated)
        print(*self.save)

    def italic(self):
        """italic format"""

        formated = f"*{self.user_input()}*"
        self.save.append(formated)
        print(*self.save)

    def inlaine_code(self):
        """inlaine-code format"""

        formated = f"`{self.user_input()}`"
        self.save.append(formated)
        print(*self.save)

    def link(self):
        """link format"""

        input_label_link = f"[{input('Label:>>')}]({input('URL:>>')})"
        self.save.append(input_label_link)
        print(*self.save)

    def header(self):
        """header formar"""

        def lvl():
            """Header's level"""

            while True:
                try:
                    input_lvl = int(input("Level:>>"))
                    if 6 < input_lvl or 1 > input_lvl:
                        raise Exception("Invalid value")
                    return input_lvl
                except Exception:
                    print("Invalid value. Make sure the value you choose is a number between 1 and 6")

        input_header = f"{'#' * lvl()} {input('input header:>> ')}\n"
        self.save.append(input_header)
        print(*self.save)

    def unordered_list(self):
        """unordered-list format"""

        number_of_rows = int(input(f"Number of rows:>>"))
        counter = 1
        while counter <= number_of_rows:
            rows = f"* {input(f'Row#{counter}>>')}\n"
            self.save.append(rows)
            counter += 1
        print(*self.save)

    def ordered_list(self):
        """ordered-list format"""

        number_of_rows = int(input(f"Number of rows:>>"))
        counter = 1
        while counter <= number_of_rows:
            rows = f"{counter}. {input(f'Row#{counter}>>')}\n"
            self.save.append(rows)
            counter += 1
        print(*self.save)

    def new_line(self):
        """new-line format"""
        formated = "\n"
        self.save.append(formated)
        print(*self.save)

    def main_menu(self):
        """Main_menu"""

        global user_input
        while True:
            try:
                user_input = input("Choose a formatter: > ")
                values_list = ["!help", "!done", "plain", "bold", "italic",
                               "inlaine-code", "link", "header", "unordered-list",
                               "ordered-list", "new-line"]
                if user_input not in values_list:
                    raise Exception("Unknown formatting type or command")
            except Exception:
                print("Unknown formatting type or command")
            match user_input:
                case "!help":
                    self.help_command()
                case "!done":
                    filename = "output.md"
                    self.file_save(filename)
                    continue
                case "plain":
                    self.plain()
                case "bold":
                    self.bold()
                case "italic":
                    self.italic()
                case "inlaine-code":
                    self.italic()
                case "link":
                    self.link()
                case "header":
                    self.header()
                case "unordered-list":
                    self.unordered_list()
                case "ordered-list":
                    self.ordered_list()
                case "new-line":
                    self.new_line()


def start_menu():
    """Start menu SME"""
    answer = input(f"Welcome to the simplified markdown editor!\n Are you want start job?\n"
                   f"|1. yes|\n|2. no |\nUser:>> ")
    while True:
        match answer:
            case "yes":
                markdown = Markdown_editor()
                markdown.main_menu()
            case "no":
                exit()
        print(f"You must select (yes or no)")
        answer = input("User:>> ")


start_menu()
