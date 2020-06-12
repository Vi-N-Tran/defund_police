# If you would like to add to this list, please let me know at alandgton@gmail.com
# Currently mayors and city council members and police commissioners

# a dictionary that maps states to dictionaries that map counties to contacts
# contacts are tuples (name, county, email, police budget, total budget)
mailing_list = {
    "California" : {
        "Test": [("Mayor Sam Liccardo", "San Jose", "vi.n.tran.23@dartmouth.edu", "440,587,360", "1,318,447,965")],
        "San Jose" : [
            ("Mayor Sam Liccardo", "San Jose", "mayoremail@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Vice Mayor Charles Jones", "San Jose", "District1@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Sergio Jimenez", "San Jose", "District2@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Raul Peralez", "San Jose", "District3@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Lan Diep", "San Jose", "District4@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Magdalena Carrasco", "San Jose", "District5@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Devora Davis", "San Jose", "District6@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Maya Esparza", "San Jose", "District7@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Sylvia Arenas", "San Jose", "District8@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Pam Foley", "San Jose", "District9@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Councilmember Johnny Khamis", "San Jose", "District10@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("Budget Director Jim Shannon", "San Jose", "Jim.Shannon@sanjoseca.gov", "440,587,360", "1,318,447,965"),
            ("City Manager Dave Sykes", "San Jose", "Dave.sykes@sanjoseca.gov", "440,587,360", "1,318,447,965"),
        ],
        "Oakland": [
            ("Mayor Libby Schaaf", "Oakland", "officeofthemayor@oaklandnet.com", "329,868,493", "1,632,148,913"),
            ("Ethics Commission", "Oakland", "ethicscommission@oaklandca.gov", "329,868,493", "1,632,148,913"),
            ("Councilmember Dan Kalb", "Oakland", "dkalb@oaklandca.gov", "329,868,493", "1,632,148,913"),
            ("Councilmember Rebecca Kaplan", "Oakland", "rkaplan@oaklandca.gov", "329,868,493", "1,632,148,913"),
            ("Councilmember Nikki Fortunato Bas", "Oakland", "nfbas@oaklandca.gov", "329,868,493", "1,632,148,913"),
            ("Councilmember Lynette Gibson McElhaney", "Oakland", "LMcElhaney@oaklandca.gov", "329,868,493", "1,632,148,913"),
            ("Councilmember Sheng Thao", "Oakland", "district4@oaklandca.gov", "329,868,493", "1,632,148,913"),
            ("Councilmember Loren Taylor", "Oakland", "District6@oaklandca.gov", "329,868,493", "1,632,148,913"),
            ("Councilmember Noel Gallo", "Oakland", "Ngallo@oaklandca.gov", "329,868,493", "1,632,148,913"),
            ("Councilmember Larry Reid", "Oakland", "lreid@oaklandnet.com", "329,868,493", "1,632,148,913"),
        ]
    },
    "New York": {
        "Buffalo": [
                    ("Mayor Bryon W. Brown", "Buffalo", "mayor@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember Darius G. Pridgen", "Buffalo", "dpridgen@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember David A. Rivera", "Buffalo", "darivera@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember Christopher P. Scanlon ", "Buffalo", "cscanlon@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember Joel P. Feroleto", "Buffalo", "jferoleto@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember Bryan Bollman", "Buffalo", "bbollman@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember Mitch Nowakowski", "Buffalo", "mnowakowski@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember Joseph Golombek, Jr.", "Buffalo", "jgolombek@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember Ulysees O. Wingo, Sr.", "Buffalo", "uwingo@city-buffalo.com", "86,053,364", "418,965,384"),
                    ("Councilmember Rasheed N.C. Wyatt", "Buffalo", "rwyatt@city-buffalo.com", "86,053,364", "418,965,384"),
                ],
        # Missing budget data
        # "NYC": [
        #     ("Mayor Bill de Blasio", "NYC", "bdeblasio@cityhall.nyc.gov"),
        #     ("Councilperson Corey Johnson", "NYC", "SpeakerJohnson@council.nyc.gov"),
        #     ("Councilperson Keith Powers", "NYC", "kpowers@council.nyc.gov"),
        #     ("Senator Brad Hoylman", "NYC", "hoylman@nysenate.gov"),
        #     ("Senator Brian Kavanaugh", "NYC", "kavanagh@nysenate.gov"),
        #     ("Assemblymember Richard Gottfried", "NYC", "GottfriedR@assembly.state.ny.us"),
        #     ("Assemblymember Deborah Glick", "NYC", "glickd@assembly.state.ny.us"),
        # ],
        "Rochester": [
            ("Mayor Lovely A. Warren", "Rochester", "info@cityofrochester.gov", "95,866,000", "529,659,100"),
            ("Councilmember Loretta C. Scott", "Rochester", "Loretta.Scott@cityofrochester.gov","95,866,000", "529,659,100"),
            ("Councilmember Malik D. Evans", "Rochester", "Malik.Evans@cityofrochester.gov", "95,866,000", "529,659,100"),
            ("Councilmember Mitchell D. Gruber", "Rochester", "Mitch.Gruber@cityofrochester.gov", "95,866,000", "529,659,100"),
            ("Councilmember Willie J. Lightfoot", "Rochester", "Willie.Lightfoot@cityofrochester.gov", "95,866,000", "529,659,100"),
            ("Councilmember Jacklyn Ortiz", "Rochester", "Jacklyn.Ortiz@cityofrochester.gov", "95,866,000", "529,659,100"),
            ("Councilmember LaShay D. Harris", "Rochester", "LaShay.Harris@cityofrochester.gov", "95,866,000", "529,659,100"),
            ("Councilmember Mary Lupien", "Rochester", "Mary.Lupien@cityofrochester.gov", "95,866,000", "529,659,100"),
            ("Councilmember Michael A. Patterson", "Rochester", "Michael.Patterson@cityofrochester.gov", "95,866,000", "529,659,100"),
            ("Councilmember Jose Peo", "Rochester", "Jose.Peo@cityofrochester.gov", "95,866,000", "529,659,100"),
        ],
    }
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
