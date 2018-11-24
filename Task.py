from subprocess import *


class ArgumentNotProvidedException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Task:

    def __init__(self, commands, default_values):
        self.__commands__ = commands
        self.default_values = default_values

    # parseandreplace
    # parses command and replaces arguments with values
    # string = the string which will be parsed
    # dt = dictionary providing arguments and their value

    def parseandreplace(self, string, dt={}):
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

    def execute(self, dt):
        sstr = ""

        p = Popen("/bin/sh", stdin=PIPE)
        for i in self.__commands__:
            sstr += self.parseandreplace(i, dt) + " && "

        sstr = sstr[::-1].replace(" && ", "", 1)[::-1]
        p.communicate(sstr.encode())
        p.terminate()
        if p.stdout:
            return p.stdout
        else:
            return ""

    def append(self, string):
        self.__commands__.append(string)

    def delete(self, string):
        del self.__commands__[self.__commands__.index(string)]
