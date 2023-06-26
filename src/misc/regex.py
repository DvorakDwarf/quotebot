import re

quote = "asdadasd''asdad'd'asd"
quote = re.sub("'", "", quote)

print(quote)