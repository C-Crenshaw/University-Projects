# PA 01 : UVAHoops
# Carson Crenshaw (cgc8gdt)

# Get inputs
player = input("What player would you like to calculate statistics for? ")
team = input("What team was the opponent in the game you would like to calculate statistics for? ")
threeattempt = input("How many 3's did " + player + " attempt this game? ")
threemade = input("How many 3's did " + player + " make this game? ")
twoattempt = input("How many 2's did " + player + " attempt this game? ")
twomade = input("How many 2's did " + player + " make this game? ")
freeattempt = input("How many free throws did " + player + " attempt this game? ")
freemade = input("How many free throws did " + player + " make this game? ")

# Process
threemade = int(threemade)
twomade = int(twomade)
threeattempt = int(threeattempt)
twoattempt = int(twoattempt)
freemade = int(freemade)
freeattempt = int(freeattempt)

# Print outputs
print(player + " had a " + str((threemade + twomade) / (threeattempt + twoattempt) * 100) + "% field goal percentage and a " + str((freemade / freeattempt) * 100) + "% free throw percentage")
print(player + " scored " + str((threemade * 3) + (twomade * 2) + freemade) + " points against " + team + ". Wahoowa! ")