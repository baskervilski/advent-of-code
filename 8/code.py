
#%%


#%%

with open('input.txt') as f:
    commands = [l.strip().split() for l in f.readlines()]
# %%
commands
# %%

def run_program(commands_):

    acc = 0

    curr_comm_idx = 0
    past_commands = []

    while True:

        past_commands.append(curr_comm_idx)

        curr_comm, curr_arg = commands_[curr_comm_idx]
        if curr_comm == 'nop':
            curr_comm_idx += 1
        elif curr_comm == 'jmp':
            curr_comm_idx += int(curr_arg)
        elif curr_comm == 'acc':
            acc += int(curr_arg)
            curr_comm_idx += 1
        else:
            raise ValueError(f"Unknown command {curr_comm}!")

        if curr_comm_idx in past_commands:
            print("Command", curr_comm_idx, "planned to be executed for the 2nd time! Aborting.")
            print("Current accumulator value:", acc)
            print("Iteration:", i)
            
            return -1
        elif curr_comm_idx == len(commands_):
            print('Program reached the end!')
            print('Acc:', acc)
            return acc



run_program(commands)
# %%
nop_jmp_indices = [i for i, cmd in enumerate(commands) if cmd[0] in ['jmp', 'nop']]
nop_jmp_indices
# %%
for i in nop_jmp_indices:
    mutated_commands = [c[:] for c in commands]
    mutated_commands[i][0] = 'nop' if (mutated_commands[i][0] == 'jmp') else 'nop'
    
    if run_program(mutated_commands) != -1:
        break
# %%
