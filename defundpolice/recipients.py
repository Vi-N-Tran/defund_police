# If you would like to add to this list, please let me know at alandgton@gmail.com
# Currently mayors and city council members and police commissioners

# a dictionary that maps states to dictionaries that map counties to contacts
# contacts are tuples (name, county, email)
mailing_list = {
    "Arizona" : {
        "Phoenix" : [
            ( "Mayor Kate Gallego", "Phoenix", "vi.n.tran.23@dartmouth.edu", "89", "29102", "SJPD"),
        ],
        "Tuscon" : [
            ( "Mayor Regina Romero", "Tuscon", "vi.n.tran.23@dartmouth.edu", "89", "29102", "SJPD"),
        ],
    },
    "California" : {
        "San Jose" : [
            ( "Mayor Sam Liccardo", "San Jose", "vi.n.tran.23@dartmouth.edu", "89", "29102", "SJPD"),
        ],
        "Santa Clara" : [
            ("Mayor Lisa Gillmore", "Santa Clara", "vi.n.tran.23@dartmouth.edu", "89", "29102", "SJPD"),
        ],
    },
    "Colorado" : {
        "Denver" : [
            ( "Mayor Michael Hancock", "Denver", "vi.n.tran.23@dartmouth.edu", "89", "29102", "SJPD"),
        ],
    },
    "District of Columbia" : {
        "DC" : [
            ( "Mayor Muriel Bowser", "DC", "vi.n.tran.23@dartmouth.edu", "89", "29102", "SJPD"),
        ],
    },
    "Florida" : {
        "Jacksonville" : [
            ( "Name", "Jacksonville", "vi.n.tran.23@dartmouth.edu", "89", "29102", "SJPD"),
        ],
    },
}

def get_all():
    recv = []
    for state in mailing_list:
        for county in mailing_list[state]:
            recv.extend(mailing_list[state][county])
    return recv

def get_state(state):
    recv = []
    for county in mailing_list[state]:
        recv.extend(mailing_list[state][county])
    return recv

def get_city(state, county):
    return mailing_list[state][county]

def get_states():
    lst = ["Select All"]
    lst.extend(mailing_list.keys())
    return lst

def get_cities(state):
    lst = ["Select All"]
    lst.extend(mailing_list[state].keys())
    return lst
