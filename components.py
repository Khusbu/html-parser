import utility

# parse_case_details parses Case Details section and returns a hash
def parse_case_details(soup):
    case_details_table = soup.find_all("span", class_="case_details_table")
    if case_details_table:
        case_details_hash = {}
        for row in case_details_table:
            all_text = row.find_all(text=True)
            for i in range(0, len(all_text), 2):
                case_details_hash[utility.prettify(all_text[i])] = utility.prettify(all_text[i+1]) 
        return case_details_hash
    else:
        return None

# parse_case_status parses Case Status section and returns a hash
def parse_case_status(soup):
    case_status = soup.find(text="Case Status").parent.find_next_sibling("div").find_all("strong")
    if case_status:
        case_status_hash = {}
        for i in range(0, len(case_status), 2):
            case_status_hash[utility.prettify(case_status[i].text)] = utility.prettify(case_status[i+1].text)
        return case_status_hash
    else:
        return None

# parse_petitoner_and_advocate parses Petitoner and Advocate section and returns a hash
def parse_petitoner_and_advocate(soup):
    petitoner_and_advocate = soup.find("span", class_="Petitioner_Advocate_table")
    return utility.parse_html_textarea(petitoner_and_advocate)

# parse_respondent_and_advocate parses Respondent and Advocate section and returns a hash
def parse_respondent_and_advocate(soup):
    respondent_and_advocate = soup.find("span", class_="Respondent_Advocate_table")
    return utility.parse_html_textarea(respondent_and_advocate)

# parse_acts_table parses Acts section and returns a hash
def parse_acts_table(soup):
    acts_table = soup.find("table", id="act_table")
    return utility.parse_html_table(acts_table)

# parse_history_table parses History section and returns a hash
def parse_history_table(soup):
    history_table = soup.find("table", class_="history_table")
    return utility.parse_html_table(history_table)

# parse_orders_table parses Orders section and returns a hash
def parse_orders_table(soup):
    table_list = []
    order_table = soup.find_all("table", class_="order_table")
    if order_table:
        heading = order_table[0].find_all("td")
        for table in order_table[1:]:
            cols = table.find_all("td")
            row_hash = {}
            for key, value in zip(heading, cols):
                row_hash[utility.prettify(key.text)] = utility.prettify(value.text)
            if row_hash:
                table_list.append(row_hash)
        return table_list
    else:
        return None
