from matplotlib import pyplot

infile = open("Specimen_RawData_2.csv",'r')

infile.readline()
infile.readline()

cnt = 0
time, extension, displacement, strain, load  = [0], [], [], [], [0]
loadslope = []
movingavr = []
#Time,Extension,Displacement (Strain 1),Strain 1,Load
#(sec),(mm),(mm),(mm/mm),(N)
#this parses the file
for line in infile:
    cnt += 1
    line = line.split(',')
    time.append(float(line[0]))
    extension.append(float(line[1]))
    displacement.append(float(line[2]))
    strain.append(float(line[3]))
    load.append(float(line[4]))
    slope = load[-2] - load[-1]
    if abs(slope) > 100:
        slope = 0
    loadslope.append(slope)

rollsize = 100
#for idx in range(len(loadslope)-rollsize):
#    total = 0
#    for offset in range(rollsize):
#        total += loadslope[idx+offset]
#    average = total / rollsize
#    movingavr.append(average)


print "datapoints:", cnt
pyplot.plot(time[:5000],extension[:5000])
pyplot.plot(time[:5000],displacement[:5000])
pyplot.plot(time[:5000],strain[:5000])
#pyplot.plot(time[:5000],load[:5000])
#pyplot.plot(time[:5000],movingavr[:5000])
#pyplot.plot(time[:5000],loadslope[:5000])

pyplot.show()
