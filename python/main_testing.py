def main():
    #filename = input("Food: ")
    #extension = '.csv'
    food_dict = {}
    value = 0
    graph_name = []
    value_list = []
    name_order = []
    final_color_list = []
    name_value_list = []    
    wanted_status = ""
    while wanted_status.lower() != 'quit':
        wanted_status = input("Food: ")
        
        if wanted_status.lower() != 'quit':
            extension = '.csv'
            fileexten = wanted_status.lower() + extension.lower()
            
            data = open(fileexten)
            lines = data.readlines()
            lines = [line for line in lines if line.strip() != ""]    
            
            for line in lines:
                line = line.rstrip()
                line = line.split()
                
                if 'Food:' == line[0]:
                    food = line[1]
                    
                elif 'Love' == line[0]:
                    status = line[0]
                    value = 5
                    name_list = []
        
                elif 'Like' == line[0]:
                    status = line[0]
                    name_list = []
                    value = 4
                  
                elif 'Neutral' == line[0]:
                    status = line[0]
                    name_list = []
                    value = 3
                elif 'Dislike' == line[0]:
                    status = line[0]
                    name_list = []
                    value = 2
                elif 'Hate' == line[0]:
                    status = line[0]
                    name_list = []            
                    value = 1
                else:
                    name = line[0]
                    name_value_list.append((name, value))
                    name_order.append(name)
                    name_list.append(name)
                    graph_name.append(name)
                    value_list.append(value)
                    food_dict[status] = name_list            
                    
            print(food_dict)

    return food_dict

main()