from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Poketmon Name",
                 ["Pikachu", "Squirle", "Charander"])
table.add_column("Type",
                 ["Electric", "Water", "Fire"])

# table.align["Poketmon Name"] = "l"
# table.align["Type"] = "l"
table.align = "l"


print(table.align)
print(table)


