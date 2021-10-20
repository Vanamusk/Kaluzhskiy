alphabet = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'.split(', ')
shifred = input().split()
deshifred =  []
if 'End' in shifred:
	while a!= 'End':
		if int(a) < 0:
			letter = ' '
		else:
			letter = alphabet[int(a)]
			deshifred.append(letter)
	print(''.join(deshifred))
else:
	print('No end')
