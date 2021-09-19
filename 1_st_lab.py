alphabet = 'а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я'.split(', ')
shifr = list(map(int,input().split()[:-1]))
deshfr = [alphabet[i] if i>=0 else ' ' for i in shifr]
print(''.join(deshfr))
