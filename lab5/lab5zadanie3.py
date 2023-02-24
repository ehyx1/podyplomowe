#Wyznacz zysk z 3 letniej lokaty bankowej wg założeń:
#• inwestowane środki 46 567,00 zł
#• stałe oprocentowanie roczne 7.5%
#• coroczna kapitalizacja odsetek
#• w obliczeniach zastosuj złożony operator przypisania

onw_founds=46_567.
deposit=onw_founds
factor=1.075

onw_founds *=factor
onw_founds *=factor
onw_founds *=factor

print("Zysk inwestycji wynosi", round(deposit-onw_founds,2),"zł.")

