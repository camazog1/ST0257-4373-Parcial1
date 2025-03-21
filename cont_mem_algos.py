def first_fit(memory: list[tuple], req: int, index: int):

    # print(f'Request: {req:#0{8}x}')

    if not memory:
        return None

    temp = index
    
    while True:
        if memory[index][1] >= req:

            new_base = memory[index][0]
            new_limit = req

            memory[index] = (memory[index][0] + req, memory[index][1] - req)

            if memory[index][1] == 0:
                memory.pop(index)
                
                if index > len(memory) - 1:
                    index = 0

            return memory, new_base, new_limit, index
        
        index = (index + 1) % len(memory)
        
        if index == temp:
            return None

if __name__ == "__main__":

    memory = [
        (114812928, 5242880),   
        (101814272, 12582912),  
        (85983232, 15728640),   
        (75497472, 10485760),   
        (31457280, 4194304),    
        (38928384, 20971520),   
        (119627776, 18874368),  
        (138330368, 7340032),   
    ]

    reqs = [
        12582912,  
        10485760,  
        11534336,  
    ]

    index = 0 

    print('Initial memory:')

    for index_memory, (base_memory, limit_memory) in enumerate(memory):
        print(f'Segmento[{index_memory}] = {base_memory} : {limit_memory}')
    print('-----------------------------------')

    for req in reqs:
        print(f'Request: {req}')
        memory, base, limit, index = first_fit(memory, req, index)

        print("New memory:\n")
        for index_memory, (base_memory, limit_memory) in enumerate(memory):
            print(f'Segmento[{index_memory}] = {base_memory} : {limit_memory}')

        if base is not None:
            print(f'new Index: {index}')
            print(f'New base address: {base}')
            print(f'New limit: {limit}')
            print('-----------------------------------')
        else:
            print('Not enough space available.')
            print('-----------------------------------')