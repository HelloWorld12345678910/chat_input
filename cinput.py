class InputStream:

    def __init__(self):
        self.stream = [] 
        self.pointer = 0 # cursor pointer, default value len(stream)


    def append(self, value):
        self.stream.insert(self.pointer, value)
        self.pointer += 1


    def __str__(self):

        return ''.join(self.stream)


def cinput(term, prompt):

    user_input = InputStream()

    print(prompt, end='', flush=True)

    with term.raw(), term.cbreak():

        while (char := term.inkey()).code != term.KEY_ENTER and not char.is_sequence:

            print(char, end='', flush=True)
            user_input.append(char)


    return str(user_input)


if __name__ == '__main__':

    from blessed import Terminal

    term = Terminal()

    a = cinput(term, "[Kiril]: ")
    print()
    print(a)

