name_order = ['Emily', 'Haley', 'Abigail']
final_color_list = []

color_dict = {'Abigail': 'rgb(124, 68, 191)', 'Emily': 'rgb(0, 62,240)', 'Haley': 'rgb(255, 201, 56)'}

for name in name_order:
    for color in list(color_dict.keys()):
        if name == color:
            final_color_list.append(color_dict[color])
            
print(final_color_list)


name_list = ['Demetrius', 'Jodi', 'Kent', 'Leah', 'Linus', 'Pam', 'Robin', 'Sandy', 'Shane', 'Abigail', 'Alex', 'Clint', 'Dwarf', 'Emily', 'George', 'Gus', 'Haley', 'Jas', 'Krobus', 'Lewis', 'Marnie', 'Maru', 'Penny', 'Pierre', 'Sam', 'Sebastian', 'Vincent', 'Willy', 'Wizard', 'Caroline', 'Elliott', 'Evelyn', 'Harvey']

total = 0
for i in name_list:
    total += 1
print(total)