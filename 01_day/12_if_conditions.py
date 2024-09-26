temperature = 50
humidity = 70
rain = True

if (temperature > 30 or humidity < 70) and not rain:
    print("Dry weather")
# without braces
# not rain          False
# humidity < 70     False
#                   False and False = False
# temperature > 30  True
#                   True or False = True

# with braces
# temperature > 30      True
# humidity < 70         False
#                       True or False = True
# not rain              False
#                       True and False = False
