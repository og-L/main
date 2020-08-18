import urllib.request
from bs4 import BeautifulSoup

my_bilnumer = input("Hvað er bílnúmerið þitt?")

my_request = urllib.request.urlopen("https://www.samgongustofa.is/umferd/okutaeki/okutaekjaskra/uppfletting?vq=" + my_bilnumer)

my_HTML = my_request.read().decode("utf8")

soup = BeautifulSoup(my_HTML, 'html.parser')

my_string = soup.get_text().split()

CO2_stuff_index = my_string.index("CO2-gildi")

print(my_string[CO2_stuff_index+2])



