import math

weather_predictions = 365                                                               # antal förutsegelser
correct_predictions = 300                                                               # antal korrekta förutsägelser
accuracy = (correct_predictions / weather_predictions) * 100                            # träffsäkerhet, parenteser ej nödvändiga för uträkningen
print("The accuracy of the weather predictions was ", accuracy , " percent.")           # skriv ut träffsäkerhet