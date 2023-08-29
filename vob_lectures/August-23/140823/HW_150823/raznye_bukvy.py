line = '''кенгууцлшгкмпар
блфцылнпауклгушынкалшфгыцнукалшнфгцул
кшнафцушгкаумралфроцсопуысбалфрыидлсвпмдуцилшфыцру'''

letter_list = []
for buk in line:
    # if not (buk in letter_list):
    if buk not in letter_list:
        letter_list.append(buk)
print(letter_list)
