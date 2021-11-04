class InputStream:

    def __init__(self, length):
        self.stream = [] 
        self.pointer = 0 # cursor pointer, default value len(stream)
        self.num_chars = 0
        self.length = length


    def append(self, value):

        if not self.num_chars >= self.length:
            self.stream.insert(self.pointer, value)
            self.pointer += 1
            self.num_chars += 1

            return True

        return False


    def delete(self):

        if self.num_chars > 0 and self.pointer > 0:

            self.pointer -= 1    
        # by default self.pointer's value is len(stream),                      
        # so we first have to decrease it before deleting the element

            self.num_chars -= 1
            del self.stream[self.pointer]

            return True

        return False


    def __str__(self):

        return ''.join(self.stream)


def cinput(term, length : int, prompt=''):

    user_input = InputStream(length)

    print(prompt, end='', flush=True)

    with term.raw(), term.cbreak():

        while (char := term.inkey()).code != term.KEY_ENTER:

            if not char.is_sequence:

                if user_input.append(char):
                    print(char, end='', flush=True)
                    

            else:

                if char.code == term.KEY_DELETE or char.code == term.KEY_BACKSPACE:

                    if user_input.delete():
                        print(f'{term.move_left()} {term.move_left()}', end='', flush=True)


    return str(user_input)


if __name__ == '__main__':

    from blessed import Terminal

    term = Terminal()

    a = cinput(term, 10, "[Kiril]: ")
    print()
    print(a)

