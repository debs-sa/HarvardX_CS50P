results = ["Mario", "Luigi"]

results.append("Princess") #add elements to the end of the list
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."])
results.remove(["Bowser", "Donkey Kong Jr."])
results.extend(["Bowser", "Donkey Kong Jr."])

print(results)

########################################################################

results = ['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donkey Kong Jr.']

results.remove("Bowser")
results.insert(0, "Bowser")
results.reverse() #reverse list


print(results)