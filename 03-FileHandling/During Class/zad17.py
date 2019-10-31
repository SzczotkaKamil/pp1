import re
quote = "To be, or not to be, that is the question"
samogloski = re.findall('[aeiuoy]',quote)
print(len(samogloski))