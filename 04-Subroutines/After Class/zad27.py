from collections import Counter
import re
tekst = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
samogloski = re.findall("[aeyioąęuó]",tekst)
print(Counter(samogloski))