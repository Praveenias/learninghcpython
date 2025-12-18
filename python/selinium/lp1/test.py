from pathlib import Path
BASE_DIR = Path(__file__).resolve()
print(Path.joinpath(BASE_DIR,"../DS-1/manufacturer.xlsx"))
lis1 = {"a":["b","c"],
        "b":["f","g","c"],
        "c":["mi","h"]}

dict={}
def check_link(url_link,links=[]):
  if url_link in dict:
    return False
  if url_link.isvlid():
    dict[url_link] = True
    links_url = get_all_url():
    for i in links_url:
      check_link(i,links_url)