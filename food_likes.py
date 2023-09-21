# STARDEW VALLEY

# Output how each character will react to a gifted item
# [Food]: Love: [characters], Like: [characters], Neutral: [characters], 
#         Dislike: [characters], Hate: [characters]

# 34 villagers

import js
import json
import plotly
import plotly.graph_objects as go
from PIL import Image
# from pyodide.http import open_url
# import ospython -m http.server
# import pandas as pd

def main():
    """Search through the csv files to find the character names"""
    
    food_dict = {}
    value = 0
    graph_name = []
    value_list = []
    name_order = []
    final_color_list = []
    name_value_list = []
    wanted_status = ""
    csvfolder = "csv/"
    imagefolder = "images/"

    while wanted_status.lower() != 'quit':
        
        wanted_status = input("Food: ")
        
        # Load item file 
        filename = wanted_status
        extension = '.csv'
        
        fileexten = csvfolder + filename.lower() + extension.lower()
        
        # List of all items currently searchable in this program
        foods = ['amaranth', 'ancient fruit', 'artichoke', 'beet', 'blackberry', 'blue jazz', 'blueberry', 'bok choy', 'cactus fruit', 'cauliflower', 'chanterelle', 'coffee bean', 'common mushroom', 'corn', 'cranberries', 'daffodil', 'dandelion', 'eggplant' 'fairy rose', 'fiddlehead fern', 'garlic', 'grape', 'green bean', 'hazelnut', 'hot pepper', 'kale', 'leek', 'melon', 'morel', 'parsnip', 'pineapple', 'poppy', 'potato', 'pumpkin', 'radish', 'red cabbage', 'red mushroom', 'rhubarb', 'salmonberry', 'sap', 'spice berry', 'spring onion', 'starfruit', 'strawberry', 'summer spangle', 'sunflower', 'sweet gem berry', 'sweet pea', 'tea leaves', 'tomato', 'tulip', 'unmilled rice', 'wheat', 'wild horseradish', 'wild plum', 'yam']
        
        
        # If the item can not be found, throw error 
        if wanted_status.lower() not in foods: 
            raise FileNotFoundError("Sorry, that food does not exist!")
        data = open(fileexten)
        
        # Read the file
        lines = data.readlines()
        # Leave lines that are empty
        lines = [line for line in lines if line.strip() != ""]
    
        # Read the file line by line 
        for line in lines:
            # Strip trailing characters and split words on a line into ...
            # ... separate strings 
            line = line.rstrip()
            line = line.split()
            
            # Separate the list into each desired section 
            if 'Food:' == line[0]:
                food = line[1]
                
            elif 'Love' == line[0]:
                status = line[0]
                # Assign a value for graphing purposes
                value = 5
                name_list = []
    
            elif 'Like' == line[0]:
                status = line[0]
                # Reset the name list
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
                # When reading a character's name, add a pairing of the name and 
                # corresponding value to identify how it should be graphed                 
                name_value_list.append((name, value))
                # This list is to ensure the graph prints in descending order 
                # based on the values
                name_order.append(name)
                name_list.append(name)
                graph_name.append(name)
                value_list.append(value)
                # Map the list of names to their value
                food_dict[status] = name_list
                
        # Set up the design of the graph         
        layout = go.Layout(
            title = "How do the Stardew Valley Villagers Feel About {0}?".format(filename.capitalize()),
            xaxis_title="Villagers",
            #yaxis_title="Preference",
            yaxis_range = [0,6],
            #xaxis= 'y',
            #yaxis= 'x3',
            template='plotly', # Or plotly_dark?
            font= dict(
                family='Stardew Valley',
                size= 18,),
            yaxis = dict(color = 'white')
            )

        fig = go.Figure(
            # bar graph
            data=go.Bar(x=graph_name, y=value_list), 
            layout = layout
        )

        ### NOTE: ELLIOT IS SPELLED AS 'ELLIOTT'
        # Colours assigned to each character
        color_dict = {
            'Abigail': 'rgb(124, 68, 191)', 'Emily': 'rgb(0, 62,240)', 'Haley': 'rgb(255, 201, 56)', 'Leah':'rgb(57, 137, 33)', 'Maru': 'rgb(112, 19, 74)', 'Penny': 'rgb(223, 67, 60)', 'Alex':'rgb(153, 62, 0)', 'Elliott':'rgb(187, 34, 44)', 'Harvey':'rgb(179, 78, 32)', 'Sam':'rgb(255, 255, 150)', 'Sebastian': 'rgb(57, 30, 71)', 'Shane':'rgb(41, 134, 189)', 'Caroline': 'rgb(70, 153, 81)', 'Clint': 'rgb(119, 116, 113)', 'Demetrius': 'rgb(55, 73, 212)', 'Dwarf': 'rgb(145, 86, 42)', 'Evelyn': 'rgb(182, 0, 91)', 'George': 'rgb(98, 141, 188)', 'Gus': 'rgb(219, 130, 0)', 'Jas': 'rgb(228, 160, 255)', 'Jodi': 'rgb(249, 119, 79)', 'Kent': 'rgb(67, 85, 28)', 'Krobus': 'rgb(17, 0, 38)', 'Leo' : 'rgb(183, 33, 25)', 'Lewis': 'rgb(169, 158, 151)', 'Linus': 'rgb(254, 230, 42)', 'Marnie': 'rgb(227, 74, 22)', 'Pam': 'rgb(248, 136, 196)', 'Pierre': 'rgb(178, 72, 54)', 'Robin': 'rgb(255, 159, 2)', 'Sandy': 'rgb(211, 10, 77)', 'Vincent': 'rgb(229, 89, 78)', 'Willy': 'rgb(91, 72, 60)', 'Wizard': 'rgb(112, 52, 237)'
        }

        # Set the bar for each character to their assigned colour 
        for name in name_order:
            for color in list(color_dict.keys()):
                if name == color:
                    final_color_list.append(color_dict[color])

        # Coloured used (for personal reference)
        #Abigail = 'rgb(124, 68, 191)'
        #Emily = 'rgb(0, 62,240)'
        #Haley = 'rgb(255, 201, 56)'
        #Leah = 'rgb(57, 137, 33)'
        #Maru = 'rgb(112, 19, 74)'
        #Penny = 'rgb(223, 67, 60)'
        #Alex= 'rgb(153, 62, 0)'
        #Elliot= 'rgb(187, 34, 44)'
        #Harvey = 'rgb(179, 78, 32)'
        #Sam= 'rgb(255, 255, 150)'
        #Sebastian= 'rgb(57, 30, 71)'
        #Shane = 'rgb(41, 134, 189)'
        #Caroline= 'rgb(70, 153, 81)'
        #Clint = 'rgb(119, 116, 113)'
        #Demetrius = 'rgb(55, 73, 212)'
        #Dwarf= 'rgb(145, 86, 42)'
        #Evelyn = 'rgb(182, 0, 91)'
        #George = 'rgb(98, 141, 188)'
        #Gus = 'rgb(219, 130, 0)'
        #Jas = 'rgb(228, 160, 255)'
        #Jodi= 'rgb(249, 119, 79)'
        #Kent = 'rgb(67, 85, 28)'
        #Krobus = 'rgb(17, 0, 38)'
        #Leo = 'rgb(183, 33, 25)'
        #Lewis = 'rgb(169, 158, 151)'
        #Linus = 'rgb(254, 230, 42)'
        #Marnie = 'rgb(227, 74, 22)'
        #Pam = 'rgb(248, 136, 196)'
        #Pierre = 'rgb(178, 72, 54)'
        #Robin = 'rgb(255, 159, 2)'
        #Sandy= 'rgb(211, 10, 77)'
        #Vincent= 'rgb(229, 89, 78)'
        #Willy = 'rgb(91, 72, 60)'
        #Wizard = 'rgb(112, 52, 237)'        

        # design the traces which appear when hovering over a bar 
        fig.update_traces(marker_color=final_color_list, marker_line_color='rgb(255, 255, 255)',
                          marker_line_width=1.5, opacity=1.0)
        
        nameextenarray = []
        # Images of each character icon placed above their corresponding bar
        x = -0.0304
        for name_tuple in name_value_list:
            x += 0.0304
            # get villager's portrait image
            nameexten = imagefolder + name_tuple[0] + '_Icon' + '.png'
            nameextenarray.append(nameexten)
            
            fig.add_layout_image(
                dict(
                    x = x,
                    sizex= 0.38,
                    sizey=0.38,
                    y=name_tuple[1] + 0.4,
                    xref="paper",
                    yref="y",
                    opacity=1.0,
                    source = Image.open(nameexten)
                    
                )
            )
            
        nameextenarray.sort()
        for i in range(len(nameextenarray)):
            i = 0
            for j in range(len(name_order)):
                print("('{0}', '{1}'),".format(name_order[i],nameextenarray[j]))
                i += 1
                
        print(name_order)            
    
    
    # Image of ITEM (top right)
        foodexten = imagefolder + filename.capitalize() + '.png'
        fig.add_layout_image(
            dict(
                source=Image.open(foodexten),
                xref="paper", yref="paper",
                x=1, y=1.01,
                sizex=0.1, sizey=0.1,
                xanchor="right", yanchor="bottom"
            )        
            )
        
    # Images of PREFERENCES (on y axis)
        fig.add_layout_image(
            dict(
                source=Image.open('images/Love.png'),
                xref="paper", yref="paper",
                x=-0.025, y=0.78,
                sizex=0.06, sizey=0.065,
                xanchor="left", yanchor="bottom"
            )        
            )      
        fig.add_layout_image(
            dict(
                source=Image.open('images/Like.png'),
                xref="paper", yref="paper",
                x=-0.025, y=0.62,
                sizex=0.06, sizey=0.06,
                xanchor="left", yanchor="bottom"
            )        
            )    
        fig.add_layout_image(
            dict(
                source=Image.open('images/Neutral.png'),
                xref="paper", yref="paper",
                x=-0.025, y=0.45,
                sizex=0.06, sizey=0.065,
                xanchor="left", yanchor="bottom"
            )        
            )    
        fig.add_layout_image(
            dict(
                source=Image.open('images/Dislike.png'),
                xref="paper", yref="paper",
                x=-0.025, y=0.30,
                sizex=0.06, sizey=0.065,
                xanchor="left", yanchor="bottom"
            )        
            )    
        fig.add_layout_image(
            dict(
                source=Image.open('images/Hate.png'),
                xref="paper", yref="paper",
                x=-0.025, y=0.15,
                sizex=0.06, sizey=0.065,
                xanchor="left", yanchor="bottom"
            )        
            )
        
        # Image of SDV LOGO
        fig.add_layout_image(
            dict(
                source=Image.open('images/logo.png'),
                xref="paper", yref="paper",
                x=0.425, y=1.01,
                sizex=0.12, sizey=0.12,
                xanchor="left", yanchor="bottom"
            ))
            


        # Use white square to cover up irrelevant numbers on y axis

        #fig.add_layout_image(
            #dict(
                #source=Image.open('white.png'),
                #xref="paper", yref="paper",
                #x=-0.025, y=0.98,
                #xanchor="left", yanchor="bottom",
                #sizex=0.03, sizey=0.3,
            #))           

        
        if wanted_status.lower() != 'quit':
            fig.show()        
            
        # print the preference (e.g. Love) and the corresponding characters
        for key, value in food_dict.items():            
            print('{0}: {1}'.format(key, value))
    
        data.close()    


    return food_dict


main()
