def computeFourWeeks(poidsRmMax):
    poidsRmMax90=0.9*poidsRmMax

    percentSem1=[0.65,0.75,0.85]
    percentSem2=[0.70,0.80,0.90]
    percentSem3=[0.75,0.85,0.95]
    percentSem4=[0.40,0.50,0.60]

    sem1 = []
    sem2 = []
    sem3 = []
    sem4 = []

    for i in percentSem1:
        sem1.append(poidsRmMax90*i)

    for i in percentSem2:
        sem2.append(poidsRmMax90*i)

    for i in percentSem3:
        sem3.append(poidsRmMax90*i)

    for i in percentSem4:
        sem4.append(poidsRmMax90*i)


    print(sem1,sem2,sem3,sem4)