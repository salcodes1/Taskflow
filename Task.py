from subprocess import *


class ArgumentNotProvidedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Task:

    __slots__ = ('commands', 'default_values')

    def __init__(self, commands, default_values):
        self.commands = commands
        self.default_values = default_values

    # parseandreplace
    # parses command and replaces arguments with values
    # string = the string which will be parsed
    # dt = dictionary providing arguments and their value

    def parseandreplace(self, string: str, dt: dict) -> str:
        i = 0
        while i < len(string):
            if string[i] == '$' and string[i + 1] == '$':
                aux = ""
                j = i + 2
                while j < len(string) and string[j] != "$":
                    aux += str(string[j])
                    j += 1
                if aux in dt:
                    string = string.replace("$$" + aux + "$$", dt[aux], 1)
                else:
                    if aux in self.default_values:
                        string = string.replace("$$" + aux + "$$", self.default_values[aux], 1)
                    else:
                        raise ArgumentNotProvidedException(f"Argument not provided: {aux}. -- Aborting executing.")
            i += 1
        return string

    # execute
    # executes command sequence
    # dt = dictionary providing arguments and their value

    def execute(self, dt: dict) -> None:
        sstr = ""

        p = Popen("/bin/sh", stdin=PIPE)
        for i in self.commands:
            sstr += self.parseandreplace(i, dt) + " && "

        sstr = sstr[::-1].replace(" && ", "", 1)[::-1]
        p.communicate(sstr.encode())
        p.terminate()
        if p.stdout:
            return p.stdout
        else:
            return ""

    def append(self, string: str) -> None:
        self.commands.append(string)

    def findanddelete(self, string: str) -> None:
        del self.commands[self.commands.index(string)]

    def delete(self, index: int) -> None:
        if index < len(self.commands):
            del self.commands[index]
        else:
            raise IndexError
