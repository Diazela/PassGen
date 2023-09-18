import string
import random

password = "".join(random.sample(string.ascii_letters + string.digits + string.punctuation,16))

print(password)
