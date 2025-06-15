import random
import itertools

namen = [["Elvis", "Roti", "Kai", "HJ"], ["Diede","Mirthe", "Taco", "Sophie", "Myrthe"]]
alleNamen =  ["Elvis", "Roti", "Kai", "HJ", "Diede", "Mirthe", "Taco", "Sophie", "Myrthe"]

laatsteTaken = ["Roti", "Mirthe", "Sophie", "Elvis", "Taco", "HJ", "Kai", "Diede", "Myrthe"]
maanden = ["Januari", "Februari", "Maart", "April", "Mei", "Juni"]
# maanden = ["Juli", "Augustus", "September", "Oktober", "November", "December"]

taken = [
    "WC Heren",
    "WC Dames",
    "Keuken - 1",
    "Keuken - 2",
    "Glas en Papier",
    "Vloer - 1",
    "Vloer - 2",
    "Douches",
    "Woonkamer",
]


schema = {}
success = False
# seed = 1449
while not success:
    # seed += 1
    # random.seed(seed)
    success = True

    namenLeftTaakjes = {}

    for taak in taken:
        namenLeftTaakjes[taak] = set(alleNamen.copy())
    for i in range(0, len(taken)):
        namenLeftTaakjes[taken[i]].remove(laatsteTaken[i])

        # print(namenLeftTaakjes)
        # break
    for i in namen[0]:
        namenLeftTaakjes["WC Dames"].remove(i)
    for i in namen[1]:
        namenLeftTaakjes["WC Heren"].remove(i)
    # break   

    # break
    for i in range(0, len(maanden)):
        if(i == 1):
            for j in range(0, len(taken)):
                namenLeftTaakjes[taken[j]].add(laatsteTaken[j])
        maand = maanden[i]
        schema[maand] = {}
        namenLeft = set(alleNamen.copy())
        if not success:
            break

        for taak in taken:


            if taak == "WC Heren":
                randomPersoon = random.randint(0, 3)
                schema[maand][taak] = namen[0][randomPersoon]
                namenLeft.remove(namen[0][randomPersoon])
            elif taak == "WC Dames":
                randomPersoon = random.randint(0, 4)
                schema[maand][taak] = namen[1][randomPersoon]
                namenLeft.remove(namen[1][randomPersoon])
            else:
                mogelijkeNamen = list(namenLeft.intersection(namenLeftTaakjes[taak]))
                if taak == "Vloer - 1" and i > 1:
                    for naam in alleNamen:
                        if schema[maanden[i - 1]]["Vloer - 2"] == naam and mogelijkeNamen.__contains__(naam):
                            mogelijkeNamen.remove(naam)
                if taak == "Vloer - 2" and i > 1:
                    for naam in alleNamen:
                        if schema[maanden[i - 1]]["Vloer - 1"] == naam and mogelijkeNamen.__contains__(naam):
                            mogelijkeNamen.remove(naam)
                if taak == "Douches" and i > 1:
                    for naam in alleNamen:
                        if schema[maanden[i - 1]]["Glas en Papier"] == naam and mogelijkeNamen.__contains__(naam):
                            mogelijkeNamen.remove(naam)
                if taak == "Glas en Papier" and i > 1:
                    for naam in alleNamen:
                        if schema[maanden[i - 1]]["Douches"] == naam and mogelijkeNamen.__contains__(naam):
                            mogelijkeNamen.remove(naam)
                if taak == "WC Heren" and i > 1:
                    for naam in alleNamen:
                        if schema[maanden[i - 1]]["WC Heren"] == naam and mogelijkeNamen.__contains__(naam):
                            mogelijkeNamen.remove(naam)
                if taak == "WC Dames" and i > 1:
                    for naam in alleNamen:
                        if schema[maanden[i - 1]]["WC Dames"] == naam and mogelijkeNamen.__contains__(naam):
                            mogelijkeNamen.remove(naam)
                        

                if len(mogelijkeNamen) == 0:
                    success = False
                    break
                randomPersoon = random.randint(0, len(mogelijkeNamen) - 1)
                schema[maand][taak] = mogelijkeNamen[randomPersoon]
                namenLeft.remove(mogelijkeNamen[randomPersoon])
                namenLeftTaakjes[taak].remove(mogelijkeNamen[randomPersoon])
    if not success:
        continue

    taakFrequency = {}
    maandFrequency = {}

    for taak in taken:
        taakFrequency[taak] = {}
        for naam in list(itertools.chain.from_iterable(namen)):
            taakFrequency[taak][naam] = 0
        for i in range(len(maanden)):
            maand = maanden[i]
            persoon = schema[maand][taak]
            taakFrequency[taak][persoon] += 1

            if i > 0 and persoon == schema[maanden[i - 1]][taak]:
                success = False

            if taak != "WC Heren" or taak != "WC Dames":
                isValid = taakFrequency[taak][persoon] < 3
            else:
                isValid = taakFrequency[taak][persoon] < 2
            if not isValid:
                success = False

    for maand in maanden:
        maandFrequency[maand] = {}
        for naam in list(itertools.chain.from_iterable(namen)):
            maandFrequency[maand][naam] = 0
        for taak in taken:
            persoon = schema[maand][taak]
            maandFrequency[maand][persoon] += 1
            if maandFrequency[maand][persoon] == 2:
                success = False

f = open("demofile2.txt", "w")

f.write("taak\t")

for maand in maanden:
    f.write(maand + "\t\t\t")

f.write("\n")


for taak in taken:
    f.write(taak + "\t")
    for maand in maanden:
        f.write(schema[maand][taak] + "\t\t\t")
    f.write("\n")

