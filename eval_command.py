from instructions import instructions
from helpers.voice_conversion import voice_conversion


# evaluates the voice command
def eval_command(command):
    # checks for the instruction
    command = voice_conversion(command, "command")
    instruction = command.split()[0]
    # exits if instruction is "exit"
    if instruction.lower() == "exit":
        print("Exiting...")
        quit()

    # if there is nothing after the instruction, invalid command
    if len(command.split()) == 1:
        return False

    # gets and runs voice command that will be used with the instruction
    to_parse = " ".join(command.split()[1:])
    if instruction in instructions:
        return instructions[instruction](to_parse)
    else:
        return False
