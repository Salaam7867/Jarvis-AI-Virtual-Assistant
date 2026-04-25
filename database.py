memory = []

def store_command(cmd):
    memory.append(cmd)

def get_memory():
    return memory[-5:]