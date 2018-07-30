abrest = 4
rows = 5
seatnames = 'ABCDEFGHIJKLMNOPQRSTUVW'
for i in range(abrest*rows):
    seatname = str(1 + i//abrest) + seatnames[i % abrest]
    print('	MODULE\n\
		{\n\
		name = InternalSeat\n\
		seatTransformName = SeatTransform (' +
		str(i+1)  + ')\n\
		kerbalEyeOffset = 0, 0.02, 0\n\
		displayseatName =' + seatname + '\n\
		allowCrewHelmet = false\n\
		}')
