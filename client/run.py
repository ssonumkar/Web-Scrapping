from service.manage_source_code import Manage_Source_Code
from constants import PASSWORD,URL,USERNAME

source_code = Manage_Source_Code.get_source_code(URL,USERNAME,PASSWORD)
table = Manage_Source_Code.get_table(source_code,"div","table-wrap",1)
rows = Manage_Source_Code.get_rows(table)

events = {}
events["Events"] = []
id = 0
for row in rows[1:]:
    cols = row.find_all("td")  # get data of each row in list
    cols = [ele.text.strip() for ele in cols]
    print(cols)
