from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from .forms import *
from .data_functions import *
import csv
import itertools
import functools

player = ["tombrady/2504211"] #if user types in nfl-stats-library.com/profile
ret_player = ["terrybradshaw/2510042"] #if user types in nfl-stats-library.com/retiredprofile

def HallOfFame(request):
    '''Extracts names from the querysets in the HOF SQL table.
    Each section returns a zip() object containing the fullname and queryset of each HOF player.'''

    sixtythree = HOFDisplay.hofdisplay(HOF.objects.filter(year="1963")) #ex. [("Peyton Manning", <QuerySet...>), ()...]--function in data_functions.py
    sixtyfour =  HOFDisplay.hofdisplay(HOF.objects.filter(year="1964"))
    sixtyfive =  HOFDisplay.hofdisplay(HOF.objects.filter(year="1965"))
    sixtysix =  HOFDisplay.hofdisplay(HOF.objects.filter(year="1966"))
    sixtyseven =  HOFDisplay.hofdisplay(HOF.objects.filter(year="1967"))
    sixtyeight =  HOFDisplay.hofdisplay(HOF.objects.filter(year="1968"))
    sixtynine =  HOFDisplay.hofdisplay(HOF.objects.filter(year="1969"))
    seventy =  HOFDisplay.hofdisplay(HOF.objects.filter(year="1970"))
    seventyone =  HOFDisplay.hofdisplay(HOF.objects.filter(year="1971"))
    seventytwo = HOFDisplay.hofdisplay(HOF.objects.filter(year="1972"))
    seventythree = HOFDisplay.hofdisplay(HOF.objects.filter(year="1973"))
    seventyfour = HOFDisplay.hofdisplay(HOF.objects.filter(year="1974"))
    seventyfive = HOFDisplay.hofdisplay(HOF.objects.filter(year="1975"))
    seventysix = HOFDisplay.hofdisplay(HOF.objects.filter(year="1976"))
    seventyseven = HOFDisplay.hofdisplay(HOF.objects.filter(year="1977"))
    seventyeight = HOFDisplay.hofdisplay(HOF.objects.filter(year="1978"))
    seventynine = HOFDisplay.hofdisplay(HOF.objects.filter(year="1979"))
    eighty = HOFDisplay.hofdisplay(HOF.objects.filter(year="1980"))
    eightyone = HOFDisplay.hofdisplay(HOF.objects.filter(year="1981"))
    eightytwo = HOFDisplay.hofdisplay(HOF.objects.filter(year="1982"))
    eightythree = HOFDisplay.hofdisplay(HOF.objects.filter(year="1983"))
    eightyfour = HOFDisplay.hofdisplay(HOF.objects.filter(year="1984"))
    eightyfive = HOFDisplay.hofdisplay(HOF.objects.filter(year="1985"))
    eightysix = HOFDisplay.hofdisplay(HOF.objects.filter(year="1986"))
    eightyseven = HOFDisplay.hofdisplay(HOF.objects.filter(year="1987"))
    eightyeight = HOFDisplay.hofdisplay(HOF.objects.filter(year="1988"))
    eightynine = HOFDisplay.hofdisplay(HOF.objects.filter(year="1989"))
    ninety = HOFDisplay.hofdisplay(HOF.objects.filter(year="1990"))
    ninetyone = HOFDisplay.hofdisplay(HOF.objects.filter(year="1991"))
    ninetytwo = HOFDisplay.hofdisplay(HOF.objects.filter(year="1992"))
    ninetythree = HOFDisplay.hofdisplay(HOF.objects.filter(year="1993"))
    ninetyfour = HOFDisplay.hofdisplay(HOF.objects.filter(year="1994"))
    ninetyfive = HOFDisplay.hofdisplay(HOF.objects.filter(year="1995"))
    ninetysix = HOFDisplay.hofdisplay(HOF.objects.filter(year="1996"))
    ninetyseven = HOFDisplay.hofdisplay(HOF.objects.filter(year="1997"))
    ninetyeight = HOFDisplay.hofdisplay(HOF.objects.filter(year="1998"))
    ninetynine = HOFDisplay.hofdisplay(HOF.objects.filter(year="1999"))
    two = HOFDisplay.hofdisplay(HOF.objects.filter(year="2000"))
    twoone = HOFDisplay.hofdisplay(HOF.objects.filter(year="2001"))
    twotwo = HOFDisplay.hofdisplay(HOF.objects.filter(year="2002"))
    twothree = HOFDisplay.hofdisplay(HOF.objects.filter(year="2003"))
    twofour = HOFDisplay.hofdisplay(HOF.objects.filter(year="2004"))
    twofive = HOFDisplay.hofdisplay(HOF.objects.filter(year="2005"))
    twosix = HOFDisplay.hofdisplay(HOF.objects.filter(year="2006"))
    twoseven = HOFDisplay.hofdisplay(HOF.objects.filter(year="2007"))
    twoeight = HOFDisplay.hofdisplay(HOF.objects.filter(year="2008"))
    twonine = HOFDisplay.hofdisplay(HOF.objects.filter(year="2009"))
    twoten = HOFDisplay.hofdisplay(HOF.objects.filter(year="2010"))
    twoeleven = HOFDisplay.hofdisplay(HOF.objects.filter(year="2011"))
    twotwelve = HOFDisplay.hofdisplay(HOF.objects.filter(year="2012"))
    twothirteen = HOFDisplay.hofdisplay(HOF.objects.filter(year="2013"))
    twofourteen = HOFDisplay.hofdisplay(HOF.objects.filter(year="2014"))
    twofifteen = HOFDisplay.hofdisplay(HOF.objects.filter(year="2015"))
    twosixteen = HOFDisplay.hofdisplay(HOF.objects.filter(year="2016"))
    twoseventeen = HOFDisplay.hofdisplay(HOF.objects.filter(year="2017"))
    twoeighteen = HOFDisplay.hofdisplay(HOF.objects.filter(year="2018"))
    twonineteen = HOFDisplay.hofdisplay(HOF.objects.filter(year="2019"))

    context = {"sixtythree":sixtythree, "sixtyfour":sixtyfour, "sixtyfive":sixtyfive, "sixtysix":sixtysix,
            "sixtyseven":sixtyseven, "sixtyeight":sixtyeight, "sixtynine":sixtynine, "seventy":seventy,
            "seventyone":seventyone, "seventytwo":seventytwo, "seventythree":seventythree, "seventyfour":seventyfour,
            "seventyfive":seventyfive, "seventysix":seventysix, "seventyseven":seventyseven, "seventyeight":seventyeight,
            "seventynine":seventynine, "eighty":eighty, "eightyone":eightyone, "eightytwo":eightytwo,
            "eightythree":eightythree, "eightyfour":eightyfour, "eightyfive":eightyfive, "eightysix":eightysix,
            "eightyseven":eightyseven, "eightyeight":eightyeight, "eightynine":eightynine, "ninety":ninety,
            "ninetyone":ninetyone, "ninetytwo":ninetytwo, "ninetythree":ninetythree, "ninetyfour":ninetyfour,
            "ninetyfive":ninetyfive, "ninetysix":ninetysix, "ninetyseven":ninetyseven, "ninetyeight":ninetyeight,
            "ninetynine":ninetynine, "two":two, "twoone":twoone, "twotwo":twotwo, "twothree":twothree,
            "twofour":twofour, "twofive":twofive, "twosix":twosix, "twoseven":twoseven, "twoeight":twoeight,
            "twonine":twonine, "twoten":twoten, "twoeleven":twoeleven, "twotwelve":twotwelve,
            "twothirteen":twothirteen, "twofourteen":twofourteen, "twofifteen":twofifteen, "twosixteen":twosixteen,
            "twoseventeen":twoseventeen, "twoeighteen":twoeighteen, "twonineteen":twonineteen}

    return render(request, "main/HOF.html", context)

def playersearch(request):
    '''This is for the 'Player Search' page.'''
    queries = [] #to hold querysets

    team_menu = TeamDropdown(request.GET or None) #these are the Django forms for the dropdown menus
    statussearch_menu = StatusSearchDropdown(request.GET or None)
    position_menu = PositionDropdown(request.GET or None)

    lookup = request.GET.get('lookup')
    team_select = request.GET.get('team')
    status_select = request.GET.get('status')
    position_select = request.GET.get('position')
    page = request.GET.get('page')

    if team_select == None and position_select == None and status_select == None and lookup == None: #when the window opens with no GET requests

        passer = Passing.objects.filter(year="2018", position="QB")
        PlayerSearch.paginator_list(passer, queries) #appends the querysets to the query list--function in data_functions.py
        rusher = Rushing.objects.filter(year="2018", position__in=["RB", "FB"])
        PlayerSearch.paginator_list(rusher, queries)
        receiver = Receiving.objects.filter(year="2018", position__in=["WR", "TE"])
        PlayerSearch.paginator_list(receiver, queries)
        defender = Defense.objects.filter(year="2018",position__in=["NT", "DT", "DE", "OLB", "ILB", "MLB", "LB", "CB", "DB", "FS", "SS"])
        PlayerSearch.paginator_list(defender, queries)
        kicker = FieldGoals.objects.filter(year="2018",position="K")
        PlayerSearch.paginator_list(kicker, queries)
        punter = Punting.objects.filter(year="2018",position="P")
        PlayerSearch.paginator_list(punter, queries)
        limited_queries = queries[:200] #creates a new data set with a 200 item limit
        p = Paginator(limited_queries, 50) #creates a paginator object
        players = p.get_page(page) #makes the paginator object iterable
        names = ProfilePage.names_list(players) #processes the name of each player, so that it display 'first last' rather than 'last, first'; ex. "Brady, Tom" --> "Tom Brady"--function in data_functions.py
        q = zip(names, players) #ex. [("Randy Moss", <QuerySet...>), ()...]
        pagecount = StatOrder.pagecount(players) #a list of page numbers with pagination--function in data_functions.py

    elif team_select == "All NFL" and position_select == "All" and status_select == "Active" and lookup == "": #the same process is done for other scenarios with differing GET requests

        passer = Passing.objects.filter(year="2018", position="QB")
        PlayerSearch.paginator_list(passer, queries)
        rusher = Rushing.objects.filter(year="2018", position__in=["RB", "FB"])
        PlayerSearch.paginator_list(rusher, queries)
        receiver = Receiving.objects.filter(year="2018", position__in=["WR", "TE"])
        PlayerSearch.paginator_list(receiver, queries)
        defender = Defense.objects.filter(year="2018",position__in=["NT", "DT", "DE", "OLB", "ILB", "MLB", "LB", "CB", "DB", "FS", "SS"])
        PlayerSearch.paginator_list(defender, queries)
        kicker = FieldGoals.objects.filter(year="2018",position="K")
        PlayerSearch.paginator_list(kicker, queries)
        punter = Punting.objects.filter(year="2018",position="P")
        PlayerSearch.paginator_list(punter, queries)
        limited_queries = queries[:200]
        p = Paginator(limited_queries, 50)
        players = p.get_page(page)
        names = ProfilePage.names_list(players)
        q = zip(names, players)
        pagecount = StatOrder.pagecount(players)

    elif team_select == "All NFL" and status_select == "Retired" and lookup == "":

        retired = RetiredProfiles.objects.all()
        PlayerSearch.paginator_list(retired, queries)
        limited_queries = queries[:200]
        p = Paginator(limited_queries, 50)
        players = p.get_page(page)
        names = ProfilePage.names_list(players)
        q = zip(names, players)
        pagecount = StatOrder.pagecount(players)

    elif team_select != "All NFL" and status_select == "Retired" and lookup == "":

        passer = RetiredPassing.objects.filter(team=team_select)
        PlayerSearch.paginator_list(passer, queries)
        rusher = RetiredRushing.objects.filter(team=team_select)
        PlayerSearch.paginator_list(rusher, queries)
        receiver = RetiredReceiving.objects.filter(team=team_select)
        PlayerSearch.paginator_list(receiver, queries)
        defender = RetiredDefense.objects.filter(team=team_select)
        PlayerSearch.paginator_list(defender, queries)
        kicker = RetiredFieldGoals.objects.filter(team=team_select)
        PlayerSearch.paginator_list(kicker, queries)
        punter = RetiredPunting.objects.filter(team=team_select)
        PlayerSearch.paginator_list(punter, queries)
        ids_raw = [x.player_id for x in queries]
        ids = PlayerSearch.no_duplicate(ids_raw)
        profiles = RetiredProfiles.objects.filter(player_id__in=ids)
        queries.clear()
        PlayerSearch.paginator_list(profiles, queries)
        limited_queries = queries[:200]
        p = Paginator(limited_queries, 50)
        players = p.get_page(page)
        names = ProfilePage.names_list(players)
        q = zip(names, players)
        pagecount = StatOrder.pagecount(players)


    elif team_select != "All NFL" and position_select == "All" and status_select == "Active" and lookup == "":

        passer = Passing.objects.filter(year="2018", team=team_select, position="QB")
        PlayerSearch.paginator_list(passer, queries)
        rusher = Rushing.objects.filter(year="2018", team=team_select, position__in=["RB", "FB"])
        PlayerSearch.paginator_list(rusher, queries)
        receiver = Receiving.objects.filter(year="2018", team=team_select, position__in=["WR", "TE"])
        PlayerSearch.paginator_list(receiver, queries)
        defender = Defense.objects.filter(year="2018", team=team_select, position__in=["NT", "DT", "DE", "OLB", "ILB", "MLB", "LB", "CB", "DB", "FS", "SS"])
        PlayerSearch.paginator_list(defender, queries)
        kicker = FieldGoals.objects.filter(year="2018", team=team_select, position="K")
        PlayerSearch.paginator_list(kicker, queries)
        punter = Punting.objects.filter(year="2018", team=team_select, position="P")
        PlayerSearch.paginator_list(punter, queries)
        limited_queries = queries[:200]
        p = Paginator(limited_queries, 50)
        players = p.get_page(page)
        names = ProfilePage.names_list(players)
        q = zip(names, players)
        pagecount = StatOrder.pagecount(players)

    elif team_select != "All NFL" and position_select != "All" and status_select == "Active" and lookup == "":

        if position_select == "QB":
            passer = Passing.objects.filter(year="2018", team=team_select, position="QB")
            PlayerSearch.paginator_list(passer, queries)
        elif position_select == "RB":
            rusher = Rushing.objects.filter(year="2018", team=team_select, position="RB")
            PlayerSearch.paginator_list(rusher, queries)
        elif position_select == "FB":
            rusher = Rushing.objects.filter(year="2018", team=team_select, position="FB")
            PlayerSearch.paginator_list(rusher, queries)
        elif position_select == "WR":
            receiver = Receiving.objects.filter(year="2018", team=team_select, position="WR")
            PlayerSearch.paginator_list(receiver, queries)
        elif position_select == "TE":
            receiver = Receiving.objects.filter(year="2018", team=team_select, position="TE")
            PlayerSearch.paginator_list(receiver, queries)
        elif position_select == "NT":
            defender = Defense.objects.filter(year="2018", team=team_select, position="NT")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "DT":
            defender = Defense.objects.filter(year="2018", team=team_select, position="DT")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "DE":
            defender = Defense.objects.filter(year="2018", team=team_select, position="DE")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "OLB":
            defender = Defense.objects.filter(year="2018", team=team_select, position="OLB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "ILB":
            defender = Defense.objects.filter(year="2018", team=team_select, position="ILB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "MLB":
            defender = Defense.objects.filter(year="2018", team=team_select, position="MLB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "LB":
            defender = Defense.objects.filter(year="2018", team=team_select, position="LB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "DB":
            defender = Defense.objects.filter(year="2018", team=team_select, position="DB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "CB":
            defender = Defense.objects.filter(year="2018", team=team_select, position="CB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "FS":
            defender = Defense.objects.filter(year="2018", team=team_select, position="FS")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "SS":
            defender = Defense.objects.filter(year="2018", team=team_select, position="SS")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "K":
            kicker = FieldGoals.objects.filter(year="2018", team=team_select, position="K")
            PlayerSearch.paginator_list(kicker, queries)
        elif position_select == "P":
            punter = Punting.objects.filter(year="2018", team=team_select, position="P")
            PlayerSearch.paginator_list(punter, queries)
        limited_queries = queries[:200]
        p = Paginator(limited_queries, 50)
        players = p.get_page(page)
        names = ProfilePage.names_list(players)
        q = zip(names, players)
        pagecount = StatOrder.pagecount(players)

    elif team_select == "All NFL" and position_select != "All" and status_select == "Active" and lookup == "":

        if position_select == "QB":
            passer = Passing.objects.filter(year="2018", position="QB")
            PlayerSearch.paginator_list(passer, queries)
        elif position_select == "RB":
            rusher = Rushing.objects.filter(year="2018", position="RB")
            PlayerSearch.paginator_list(rusher, queries)
        elif position_select == "FB":
            rusher = Rushing.objects.filter(year="2018", position="FB")
            PlayerSearch.paginator_list(rusher, queries)
        elif position_select == "WR":
            receiver = Receiving.objects.filter(year="2018", position="WR")
            PlayerSearch.paginator_list(receiver, queries)
        elif position_select == "TE":
            receiver = Receiving.objects.filter(year="2018", position="TE")
            PlayerSearch.paginator_list(receiver, queries)
        elif position_select == "NT":
            defender = Defense.objects.filter(year="2018", position="NT")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "DT":
            defender = Defense.objects.filter(year="2018", position="DT")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "DE":
            defender = Defense.objects.filter(year="2018", position="DE")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "OLB":
            defender = Defense.objects.filter(year="2018", position="OLB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "ILB":
            defender = Defense.objects.filter(year="2018", position="ILB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "MLB":
            defender = Defense.objects.filter(year="2018", position="MLB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "LB":
            defender = Defense.objects.filter(year="2018", position="LB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "DB":
            defender = Defense.objects.filter(year="2018", position="DB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "CB":
            defender = Defense.objects.filter(year="2018", position="CB")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "FS":
            defender = Defense.objects.filter(year="2018",position="FS")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "SS":
            defender = Defense.objects.filter(year="2018", position="SS")
            PlayerSearch.paginator_list(defender, queries)
        elif position_select == "K":
            kicker = FieldGoals.objects.filter(year="2018", position="K")
            PlayerSearch.paginator_list(kicker, queries)
        elif position_select == "P":
            punter = Punting.objects.filter(year="2018", position="P")
            PlayerSearch.paginator_list(punter, queries)
        limited_queries = queries[:200]
        p = Paginator(limited_queries, 50)
        players = p.get_page(page)
        names = ProfilePage.names_list(players)
        q = zip(names, players)
        pagecount = StatOrder.pagecount(players)

    elif status_select == "Active" and lookup != "": #if a GET request is passed through the "Quick Lookup" search bar, the only recogized GET request will be 'status'

        passing = Passing.objects.filter(year="2018")
        rushing = Rushing.objects.filter(year="2018")
        receiving = Receiving.objects.filter(year="2018")
        defending = Defense.objects.filter(year="2018")
        kicking = FieldGoals.objects.filter(year="2018")
        punting = Punting.objects.filter(year="2018")

        all_passers = [i.name for i in passing] #all names for a specific category
        all_rushers = [i.name for i in rushing]
        all_receivers = [i.name for i in receiving]
        all_defenders = [i.name for i in defending]
        all_kickers = [i.name for i in kicking]
        all_punters = [i.name for i in punting]

        passers = NameFilter.spaced_filter(lookup, all_passers) #if the string passed through the loopup GET request has a " " (space), this function will return a readable string for the functions below
        rushers = NameFilter.spaced_filter(lookup, all_rushers)
        receivers = NameFilter.spaced_filter(lookup, all_receivers)
        defenders = NameFilter.spaced_filter(lookup, all_defenders)
        kickers = NameFilter.spaced_filter(lookup, all_kickers)
        punters = NameFilter.spaced_filter(lookup, all_punters)

        passer = Passing.objects.filter(year="2018",name__in=passers,position="QB")
        PlayerSearch.paginator_list(passer, queries)
        rusher = Rushing.objects.filter(year="2018",name__in=rushers,position__in=["RB", "FB"])
        PlayerSearch.paginator_list(rusher, queries)
        receiver = Receiving.objects.filter(year="2018",name__in=receivers,position__in=["WR", "TE"])
        PlayerSearch.paginator_list(receiver, queries)
        defender = Defense.objects.filter(year="2018",name__in=defenders,position__in=["NT", "DT", "DE", "OLB", "ILB", "MLB", "LB", "CB", "DB", "FS", "SS"])
        PlayerSearch.paginator_list(defender, queries)
        kicker = FieldGoals.objects.filter(year="2018",name__in=kickers,position="K")
        PlayerSearch.paginator_list(kicker, queries)
        punter = Punting.objects.filter(year="2018",name__in=punters,position="P")
        PlayerSearch.paginator_list(punter, queries)
        limited_queries = queries[:200]
        p = Paginator(limited_queries, 50)
        players = p.get_page(page)
        names = ProfilePage.names_list(players)
        q = zip(names, players)
        pagecount = StatOrder.pagecount(players)

    elif status_select == "Retired" and lookup != "":

        profiles = RetiredProfiles.objects.all()
        all_retired = [i.name for i in profiles]
        names = NameFilter.spaced_filter(lookup, all_retired)
        retired = RetiredProfiles.objects.filter(name__in=names)
        PlayerSearch.paginator_list(retired, queries)
        limited_queries = queries[:200]
        p = Paginator(limited_queries, 50)
        players = p.get_page(page)
        names = ProfilePage.names_list(players)
        q = zip(names, players)
        pagecount = StatOrder.pagecount(players)

    context = {"team_menu":team_menu, "status_menu":statussearch_menu, "position_menu":position_menu,
               "queries_names":q, "queries":players, "pagecount":pagecount, "team_select":team_select, "status_select":status_select,
               "position_select":position_select, "lookup":lookup}

    return render(request, "main/playersearch.html", context)


def retired_profile(request):
    '''Variables passed to the html file are querysets from Profiles, ProfilePics, and all Retired... models'''
    raw_id = request.GET.get('player') #playerids for querysets


    '''The lists below are to catch if specific career categories have no integers or floats'''
    pass_empty = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    rush_empty = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    rec_empty = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    def_empty = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    kick_empty = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    punt_empty = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    kr_empty = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    pr_empty = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--']

    if raw_id != None: #if there is no GET request, the item in the ret_player list will be used
        if " -" in raw_id: #in 'Season Leaders', if the user clicks on a profle link, a " -" will appear in the GET request
            id = ProfilePage.get_filter_id(raw_id) #makes the GET request readable to the queryset
            ProfilePage.get_list(id, ret_player) #clears then appends the ret_player list with the GET request
        else:
            ProfilePage.get_list(raw_id, ret_player) #if the GET request doesn't have " -", it doesn't need get_filter_id()

    profile = RetiredProfiles.objects.filter(player_id=ret_player[-1]) #grabs the most recent entry in ret_player, in case an error in appending occurs
    fullname = ProfilePage.name([i.name for i in profile]) #returns a list that separates first and last name; ex ["Tom", "Brady"]
    first = fullname[0]
    last = fullname[1]
    height = ProfilePage.height([i.height for i in profile]) #filters height in inches to ft. in. ex. 72 inches --> 6-1
    p = [i.player_id for i in profile] #p = player id

    for i in p: #for each player id
        pic = ProfilePics.objects.filter(player_id=i)

        passer = RetiredPassing.objects.filter(player_id=i)
        pcar = ProfilePage.career_passing(passer) #...car variable are lists of each player's career stats in specific areas

        rusher = RetiredRushing.objects.filter(player_id=i)
        rushcar = ProfilePage.career_rushing(rusher)

        receiver = RetiredReceiving.objects.filter(player_id=i)
        reccar = ProfilePage.career_receiving(receiver)

        defender = RetiredDefense.objects.filter(player_id=i)
        defcar = ProfilePage.career_defense(defender)

        kicker = RetiredFieldGoals.objects.filter(player_id=i)
        kickcar = ProfilePage.career_kicking(kicker)

        punter = RetiredPunting.objects.filter(player_id=i)
        puntcar = ProfilePage.career_punting(punter)

        p_returner = RetiredPuntReturns.objects.filter(player_id=i)
        prcar = ProfilePage.career_pr(p_returner)

        k_returner = RetiredKickReturns.objects.filter(player_id=i)
        krcar = ProfilePage.career_kr(k_returner)

        hof = HOF.objects.filter(player_id=i)

    pass_att = ProfilePage.zero(pcar[2])
    rush_att = ProfilePage.zero(rushcar[1])
    recs = ProfilePage.zero(reccar[1])
    tackles = ProfilePage.zero(defcar[1])
    sacks = ProfilePage.zero(defcar[4])
    ints = ProfilePage.zero(defcar[7])
    kicks = ProfilePage.zero(kickcar[2])
    punts = ProfilePage.zero(puntcar[1])
    kr = ProfilePage.zero(krcar[1])
    pr = ProfilePage.zero(prcar[1])

    if pcar == pass_empty and rushcar == rush_empty and reccar == rec_empty and defcar == def_empty and kickcar == kick_empty and puntcar == punt_empty and prcar == pr_empty and krcar == kr_empty:
        years_and_teams = ["--", "--", ["--"]] #if a player has no career stats, then this is returned
    else:
        years_and_teams = ProfilePage.year_and_teams(passer, rusher, receiver, defender, kicker, punter, p_returner, k_returner) #calcuates the beginning year, final year, and all teams a player has played for. ex. ["1988", "1996", ["Baltimore Ravens", "Miami Dolphins"]]

    start = years_and_teams[0]
    finished = years_and_teams[1]
    teams = years_and_teams[2]

    career = ProfilePage.career_box(pass_att, rush_att, recs, tackles, sacks, ints, kicks, punts, kr, pr) #returns a string that will be passed to the html file and will determine which stats are displayed in the career box

    context = {"car_game":pcar[0], "firstname":first, "lastname":last, "height":height, "profile":profile, "career":career,
    "car_comp":pcar[1], "car_pass_att":pcar[2], "car_comp_pct":pcar[3], "car_pass_att_g":pcar[4],
    "car_pass_yards":pcar[5], "car_pass_yards_att":pcar[6], "car_pass_yards_g":pcar[7], "car_pass_td":pcar[8],
    "car_pass_ints":pcar[9], "car_pass_lng":pcar[10], "car_comp_twenty_plus":pcar[11], "car_comp_forty_plus":pcar[12],
    "car_pass_sck":pcar[13], "car_rating":pcar[14], "car_rush_games":rushcar[0], "car_rush_att":rushcar[1],
    "car_rush_att_g":rushcar[2], "car_rush_yds":rushcar[3], "car_rush_avg":rushcar[4], "car_rush_yds_g":rushcar[5],
    "car_rush_tds":rushcar[6], "car_rush_lng":rushcar[7], "car_rush_fds":rushcar[8], "car_rush_t_plus":rushcar[9],
    "car_rush_f_plus":rushcar[10], "car_rush_fums":rushcar[11], "car_rec_games":reccar[0], "car_recs":reccar[1],
    "car_rec_yds":reccar[2], "car_rec_avg":reccar[3], "car_rec_yds_g":reccar[4], "car_rec_td":reccar[5],
    "car_rec_lng":reccar[6], "car_rec_fds":reccar[7], "car_rec_t_plus":reccar[8],
    "car_rec_f_plus":reccar[9], "car_rec_fums":reccar[10], "car_def_games": defcar[0], "car_def_tot":defcar[1],
    "car_def_solo": defcar[2], "car_def_ass":defcar[3], "car_def_sck": defcar[4], "car_def_saf":defcar[5],
    "car_def_passd": defcar[6], "car_def_ints":defcar[7], "car_def_int_td": defcar[8], "car_def_int_yds":defcar[9],
    "car_def_lng": defcar[10], "car_k_games":kickcar[0], "car_k_fgs":kickcar[1], "car_k_att":kickcar[2],
    "car_k_pct":kickcar[3], "car_k_kb":kickcar[4], "car_k_lng":kickcar[5], "car_k_fg_twenty":kickcar[6],
    "car_k_fgtw_att":kickcar[7], "car_k_fgtw_pct":kickcar[8], "car_k_fg_thirty":kickcar[9], "car_k_fgth_att":kickcar[10],
    "car_k_fgth_pct":kickcar[11], "car_k_fg_forty":kickcar[12], "car_k_fgfo_att":kickcar[13], "car_k_fgfo_pct":kickcar[14],
    "car_k_fg_fifty":kickcar[15], "car_k_fgfi_att":kickcar[16], "car_k_fgfi_pct":kickcar[17], "car_k_ex":kickcar[18],
    "car_k_ex_att":kickcar[19], "car_k_ex_pct":kickcar[20], "car_k_ex_b":kickcar[21], "car_punt_games":puntcar[0],
    "car_punt_punts":puntcar[1], "car_punt_yds":puntcar[2], "car_punt_lng":puntcar[3], "car_punt_avg":puntcar[4],
    "car_punt_pb":puntcar[5], "car_punt_oob":puntcar[6], "car_punt_dps":puntcar[7], "car_punt_p_twenty":puntcar[8],
    "car_punt_tbs":puntcar[9], "car_punt_fcs":puntcar[10], "car_punt_p_ret":puntcar[11], "car_punt_ret_yds":puntcar[12],
    "car_punt_rettd":puntcar[13], "car_kr_games":krcar[0], "car_kr_kr":krcar[1], "car_kr_yds":krcar[2],
    "car_kr_avg":krcar[3], "car_kr_lng":krcar[4], "car_kr_tds":krcar[5],
    "car_kr_kr_twenty":krcar[6], "car_kr_kr_forty":krcar[7], "car_kr_fcs":krcar[8], "car_kr_fums":krcar[9],
    "car_pr_games":prcar[0], "car_pr_pr":prcar[1], "car_pr_yds":prcar[2], "car_pr_avg":prcar[3],
    "car_pr_lng":prcar[4], "car_pr_tds":prcar[5], "car_pr_pr_twenty":prcar[6], "car_pr_forty":prcar[7],
    "car_pr_fcs":prcar[8], "car_pr_fums":prcar[9], "pic":pic, "hof":hof, "teams":teams, "start":start, "finished":finished,
    "passer":passer, "rusher":rusher, "receiver":receiver, "defender":defender, "kicker":kicker,
    "punter":punter, "k_returner":k_returner, "p_returner":p_returner}

    return render(request, "main/retired_profile.html", context)


def profile(request):
    '''Most of the functionality is the same as the retired_profile()'''
    radio = ProfileRadio()
    radio_select = request.GET.get('radio')
    raw_id = request.GET.get('player')

    if raw_id != None:
        if " -" in raw_id:
            id = ProfilePage.get_filter_id(raw_id)
            ProfilePage.get_list(id, player)
        else:
            ProfilePage.get_list(raw_id, player)
    profile = Profiles.objects.filter(player_id=player[-1])

    fullname = ProfilePage.name([i.name for i in profile])
    first = fullname[0]
    last = fullname[1]
    height = ProfilePage.height([i.height for i in profile])
    p = [i.player_id for i in profile]

    for i in p:
        pic = ProfilePics.objects.filter(player_id=i)
        passer_now = Passing.objects.filter(year="2018",player_id=i)
        #the season_box...() functions are to elimnate any possible duplicate displays in the season box
        rusher_now = ProfilePage.season_box_rushing(Rushing.objects.filter(year="2018",player_id=i)) #this returns a list of four items, which will be used in the season box and separated into four separate variables to be passed to the html file
        rush_attempts = rusher_now[0]
        rush_yards = rusher_now[1]
        rush_avg = rusher_now[2]
        rush_tds = rusher_now[3]

        receiver_now = ProfilePage.season_box_receiving(Receiving.objects.filter(year="2018",player_id=i))
        rec_recs = receiver_now[0]
        rec_yards = receiver_now[1]
        rec_avg = receiver_now[2]
        rec_tds = receiver_now[3]

        defender_now = ProfilePage.season_box_defense(Defense.objects.filter(year="2018",player_id=i))
        def_total = defender_now[0]
        def_solo = defender_now[1]
        def_sacks = defender_now[2]
        def_ints = defender_now[3]

        kicker_now = ProfilePage.season_box_kicking(FieldGoals.objects.filter(year="2018",player_id=i))
        kick_fgs = kicker_now[0]
        kick_attempts = kicker_now[1]
        kick_pct = kicker_now[2]
        kick_lng = kicker_now[3]

        punter_now = ProfilePage.season_box_punting(Punting.objects.filter(year="2018",player_id=i))
        punt_punts = punter_now[0]
        punt_yards = punter_now[1]
        punt_avg = punter_now[2]
        punt_lng = punter_now[3]

        passer = Passing.objects.filter(player_id=i)
        pcar = ProfilePage.career_passing(passer)

        rusher = Rushing.objects.filter(player_id=i)
        rushcar = ProfilePage.career_rushing(rusher)

        receiver = Receiving.objects.filter(player_id=i)
        reccar = ProfilePage.career_receiving(receiver)

        defender = Defense.objects.filter(player_id=i)
        defcar = ProfilePage.career_defense(defender)

        kicker = FieldGoals.objects.filter(player_id=i)
        kickcar = ProfilePage.career_kicking(kicker)

        punter = Punting.objects.filter(player_id=i)
        puntcar = ProfilePage.career_punting(punter)

        p_returner = PuntReturns.objects.filter(player_id=i)
        prcar = ProfilePage.career_pr(p_returner)

        k_returner = KickReturns.objects.filter(player_id=i)
        krcar = ProfilePage.career_kr(k_returner)

    context = {"radio":radio, "radio_select":radio_select, "firstname":first, "lastname":last, "height":height, "profile":profile,
               "passer":passer, "passer_now":passer_now, "pic":pic, "car_game":pcar[0],
               "car_comp":pcar[1], "car_pass_att":pcar[2], "car_comp_pct":pcar[3], "car_pass_att_g":pcar[4],
               "car_pass_yards":pcar[5], "car_pass_yards_att":pcar[6], "car_pass_yards_g":pcar[7], "car_pass_td":pcar[8],
               "car_pass_ints":pcar[9], "car_pass_lng":pcar[10], "car_comp_twenty_plus":pcar[11], "car_comp_forty_plus":pcar[12],
               "car_pass_sck":pcar[13], "car_rating":pcar[14], "car_rush_games":rushcar[0], "car_rush_att":rushcar[1],
               "car_rush_att_g":rushcar[2], "car_rush_yds":rushcar[3], "car_rush_avg":rushcar[4], "car_rush_yds_g":rushcar[5],
               "car_rush_tds":rushcar[6], "car_rush_lng":rushcar[7], "car_rush_fds":rushcar[8], "car_rush_t_plus":rushcar[9],
               "car_rush_f_plus":rushcar[10], "car_rush_fums":rushcar[11], "car_rec_games":reccar[0], "car_recs":reccar[1],
               "car_rec_yds":reccar[2], "car_rec_avg":reccar[3], "car_rec_yds_g":reccar[4], "car_rec_td":reccar[5],
               "car_rec_lng":reccar[6], "car_rec_fds":reccar[7], "car_rec_t_plus":reccar[8],
               "car_rec_f_plus":reccar[9], "car_rec_fums":reccar[10], "car_def_games": defcar[0], "car_def_tot":defcar[1],
               "car_def_solo": defcar[2], "car_def_ass":defcar[3], "car_def_sck": defcar[4], "car_def_saf":defcar[5],
               "car_def_passd": defcar[6], "car_def_ints":defcar[7], "car_def_int_td": defcar[8], "car_def_int_yds":defcar[9],
               "car_def_lng": defcar[10], "car_k_games":kickcar[0], "car_k_fgs":kickcar[1], "car_k_att":kickcar[2],
               "car_k_pct":kickcar[3], "car_k_kb":kickcar[4], "car_k_lng":kickcar[5], "car_k_fg_twenty":kickcar[6],
               "car_k_fgtw_att":kickcar[7], "car_k_fgtw_pct":kickcar[8], "car_k_fg_thirty":kickcar[9], "car_k_fgth_att":kickcar[10],
               "car_k_fgth_pct":kickcar[11], "car_k_fg_forty":kickcar[12], "car_k_fgfo_att":kickcar[13], "car_k_fgfo_pct":kickcar[14],
               "car_k_fg_fifty":kickcar[15], "car_k_fgfi_att":kickcar[16], "car_k_fgfi_pct":kickcar[17], "car_k_ex":kickcar[18],
               "car_k_ex_att":kickcar[19], "car_k_ex_pct":kickcar[20], "car_k_ex_b":kickcar[21], "car_punt_games":puntcar[0],
               "car_punt_punts":puntcar[1], "car_punt_yds":puntcar[2], "car_punt_lng":puntcar[3], "car_punt_avg":puntcar[4],
               "car_punt_pb":puntcar[5], "car_punt_oob":puntcar[6], "car_punt_dps":puntcar[7], "car_punt_p_twenty":puntcar[8],
               "car_punt_tbs":puntcar[9], "car_punt_fcs":puntcar[10], "car_punt_p_ret":puntcar[11], "car_punt_ret_yds":puntcar[12],
               "car_punt_rettd":puntcar[13], "car_kr_games":krcar[0], "car_kr_kr":krcar[1], "car_kr_yds":krcar[2],
               "car_kr_avg":krcar[3], "car_kr_lng":krcar[4], "car_kr_tds":krcar[5],
               "car_kr_kr_twenty":krcar[6], "car_kr_kr_forty":krcar[7], "car_kr_fcs":krcar[8], "car_kr_fums":krcar[9],
               "car_pr_games":prcar[0], "car_pr_pr":prcar[1], "car_pr_yds":prcar[2], "car_pr_avg":prcar[3],
               "car_pr_lng":prcar[4], "car_pr_tds":prcar[5], "car_pr_pr_twenty":prcar[6], "car_pr_forty":prcar[7],
               "car_pr_fcs":prcar[8], "car_pr_fums":prcar[9], "rusher":rusher, "receiver":receiver, "defender":defender,
               "kicker":kicker, "punter":punter, "k_returner":k_returner, "p_returner":p_returner,
               "rush_attempts":rush_attempts, "rush_yards":rush_yards, "rush_avg":rush_avg, "rush_tds":rush_tds,
               "rec_recs":rec_recs, "rec_yards":rec_yards, "rec_avg":rec_avg, "rec_tds":rec_tds,
               "def_total":def_total, "def_solo":def_solo, "def_sacks":def_sacks, "def_ints":def_ints,
               "kick_fgs":kick_fgs, "kick_attempts":kick_attempts, "kick_pct":kick_pct, "kick_lng":kick_lng,
               "punt_punts":punt_punts, "punt_yards":punt_yards, "punt_avg":punt_avg, "punt_lng":punt_lng
              }

    return render(request, "main/profile.html", context)

def homepage(request):
    '''Extracts data from the MySQL datatbase for the top five-ranked players in six different statistical categories,
    for both active and retired players. For each category, a zip() object is returned with the top five-ranked players: names and querysets.'''

    form = YearDropdown(request.GET or None)
    year_select = request.GET.get('year')

    if year_select == None: #when the page opens without a GET request, the default year for query sets is "2018"

        passing = Passing.objects.filter(year="2018")
        yards_list = [player.yards for player in passing]
        int_list = StatOrder.greatest_least(yards_list)
        yards = StatOrder.add_commas(int_list) #function in data_functions.py
        queries = [] #used to hold queries
        for y in yards:
            obj = Passing.objects.filter(year="2018", yards=y)
            queries.append(obj)
        topfive_queries = queries[:5]
        top_names = StatOrder.real_topfive(topfive_queries) #returns a list of player IDs via queryset...function in data_functions.py
        topfive = []
        for i in top_names:
            obj = Passing.objects.filter(year="2018", player_id=i)
            topfive.append(obj)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players) #the names in the MySQL datatbase were inserted backwards (ex."Brady, Tom"). This returns the names in the normal way (ex."Tom Brady")...function in data_functions.py
        passers = zip(names, players) #example: [("Tom Brady", <QuerySet....>), ()...]

        #The same process is used to extract data for the other categories...

        rushing = Rushing.objects.filter(year="2018")
        yards_list = [player.yards for player in rushing]
        int_list = StatOrder.greatest_least(yards_list)
        yards = StatOrder.add_commas(int_list)
        queries = []
        for y in yards:
            obj = Rushing.objects.filter(year="2018", yards=y)
            queries.append(obj)
        topfive_queries = queries[:5]
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Rushing.objects.filter(year="2018", player_id=i)
            topfive.append(obj)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        rushers = zip(names, players)

        receiving = Receiving.objects.filter(year="2018")
        yards_list = [player.yards for player in receiving]
        int_list = StatOrder.greatest_least(yards_list)
        yards = StatOrder.add_commas(int_list)
        queries = []
        for y in yards:
            obj = Receiving.objects.filter(year="2018", yards=y)
            queries.append(obj)
        topfive_queries = queries[:5]
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Receiving.objects.filter(year="2018", player_id=i)
            topfive.append(obj)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        receivers = zip(names, players)

        defense = Defense.objects.filter(year="2018")

        tackles_list = [player.total_tkl for player in defense]
        int_list = StatOrder.greatest_least(tackles_list)
        tackles = [str(i) for i in int_list]
        queries = []
        for t in tackles:
            obj = Defense.objects.filter(year="2018", total_tkl=t)
            queries.append(obj)
        topfive_queries = queries[:5]
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Defense.objects.filter(year="2018", player_id=i)
            topfive.append(obj)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        tacklers = zip(names, players)

        sacks_list = [player.sck for player in defense]
        float_list = StatOrder.greatest_least_float(sacks_list)
        sacks = [str(i) for i in float_list]
        queries = []
        for s in sacks:
            obj = Defense.objects.filter(year="2018", sck=s)
            queries.append(obj)
        topfive_queries = queries[:5]
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Defense.objects.filter(year="2018", player_id=i)
            topfive.append(obj)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        sackers = zip(names, players)

        ints_list = [player.ints for player in defense]
        int_list = StatOrder.greatest_least(ints_list)
        ints = [str(i) for i in int_list]
        queries = []
        for i in ints:
            obj = Defense.objects.filter(year="2018", ints=i)
            queries.append(obj)
        topfive_queries = queries[:5]
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Defense.objects.filter(year="2018", player_id=i)
            topfive.append(obj)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        interceptors = zip(names, players)

    else:

        passing = Passing.objects.filter(year=year_select) #Stats for active players and retired players are stored in separate SQL tables
        passingret = RetiredPassing.objects.filter(year=year_select)
        yards_list = [player.yards for player in passing] + [player.yards for player in passingret]
        int_list = StatOrder.greatest_least(yards_list)
        yards = StatOrder.add_commas(int_list)
        queries = []
        for x, y in enumerate(yards):
            if x == 5:
                break
            else:
                obj = Passing.objects.filter(year=year_select, yards=y)
                if obj.exists():
                    queries.append(obj)
                objret = RetiredPassing.objects.filter(year=year_select, yards=y)
                if objret.exists():
                    queries.append(objret)
        topfive_queries = queries
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Passing.objects.filter(year=year_select, player_id=i)
            if obj.exists():
                topfive.append(obj)
            objret = RetiredPassing.objects.filter(year=year_select, player_id=i)
            if objret.exists():
                topfive.append(objret)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        passers = zip(names, players)

        rushing = Rushing.objects.filter(year=year_select)
        rushingret = RetiredRushing.objects.filter(year=year_select)
        yards_list = [player.yards for player in rushing] + [player.yards for player in rushingret]
        int_list = StatOrder.greatest_least(yards_list)
        yards = StatOrder.add_commas(int_list)
        queries = []
        for x, y in enumerate(yards):
            if x == 5:
                break
            else:
                obj = Rushing.objects.filter(year=year_select, yards=y)
                if obj.exists():
                    queries.append(obj)
                objret = RetiredRushing.objects.filter(year=year_select, yards=y)
                if objret.exists():
                    queries.append(objret)
        topfive_queries = queries
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Rushing.objects.filter(year=year_select, player_id=i)
            if obj.exists():
                topfive.append(obj)
            objret = RetiredRushing.objects.filter(year=year_select, player_id=i)
            if objret.exists():
                topfive.append(objret)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        rushers = zip(names, players)

        receiving = Receiving.objects.filter(year=year_select)
        receivingret = RetiredReceiving.objects.filter(year=year_select)
        yards_list = [player.yards for player in receiving] + [player.yards for player in receivingret]
        int_list = StatOrder.greatest_least(yards_list)
        yards = StatOrder.add_commas(int_list)
        queries = []
        for x, y in enumerate(yards):
            if x == 5:
                break
            else:
                obj = Receiving.objects.filter(year=year_select, yards=y)
                if obj.exists():
                    queries.append(obj)
                objret = RetiredReceiving.objects.filter(year=year_select, yards=y)
                if objret.exists():
                    queries.append(objret)
        topfive_queries = queries
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Receiving.objects.filter(year=year_select, player_id=i)
            if obj.exists():
                topfive.append(obj)
            objret = RetiredReceiving.objects.filter(year=year_select, player_id=i)
            if objret.exists():
                topfive.append(objret)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        receivers = zip(names, players)

        defense = Defense.objects.filter(year=year_select)
        defenseret = RetiredDefense.objects.filter(year=year_select)

        tackles_list = [player.total_tkl for player in defense] + [player.total_tkl for player in defenseret]
        int_list = StatOrder.greatest_least(tackles_list)
        tackles = [str(i) for i in int_list]
        queries = []
        for x, t in enumerate(tackles):
            if x == 5:
                break
            else:
                obj = Defense.objects.filter(year=year_select, total_tkl=t)
                if obj.exists():
                    queries.append(obj)
                objret = RetiredDefense.objects.filter(year=year_select, total_tkl=t)
                if objret.exists():
                    queries.append(objret)
        topfive_queries = queries
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Defense.objects.filter(year=year_select, player_id=i)
            if obj.exists():
                topfive.append(obj)
            objret = RetiredDefense.objects.filter(year=year_select, player_id=i)
            if objret.exists():
                topfive.append(objret)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        tacklers = zip(names, players)

        sacks_list = [player.sck for player in defense] + [player.sck for player in defenseret]
        float_list = StatOrder.greatest_least_float(sacks_list)
        sacks = [str(i) for i in float_list]
        queries = []
        for x, s in enumerate(sacks):
            if x == 5:
                break
            else:
                obj = Defense.objects.filter(year=year_select, sck=s)
                if obj.exists():
                    queries.append(obj)
                objret = RetiredDefense.objects.filter(year=year_select, sck=s)
                if objret.exists():
                    queries.append(objret)
        topfive_queries = queries
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Defense.objects.filter(year=year_select, player_id=i)
            if obj.exists():
                topfive.append(obj)
            objret = RetiredDefense.objects.filter(year=year_select, player_id=i)
            if objret.exists():
                topfive.append(objret)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        sackers = zip(names, players)

        ints_list = [player.ints for player in defense] + [player.ints for player in defenseret]
        int_list = StatOrder.greatest_least(ints_list)
        ints = [str(i) for i in int_list]
        queries = []
        for x, i in enumerate(ints):
            if x == 5:
                break
            else:
                obj = Defense.objects.filter(year=year_select, ints=i)
                if obj.exists():
                    queries.append(obj)
                objret = RetiredDefense.objects.filter(year=year_select, ints=i)
                if objret.exists():
                    queries.append(objret)
        topfive_queries = queries
        top_names = StatOrder.real_topfive(topfive_queries)
        topfive = []
        for i in top_names:
            obj = Defense.objects.filter(year=year_select, player_id=i)
            if obj.exists():
                topfive.append(obj)
            objret = RetiredDefense.objects.filter(year=year_select, player_id=i)
            if objret.exists():
                topfive.append(objret)
        players = topfive[:5]
        names = ProfilePage.names_extraforloop(players)
        interceptors = zip(names, players)


    context = {"passers":passers,
               "rushers":rushers,
               "receivers":receivers,
               "tacklers":tacklers,
               "sackers":sackers,
               "interceptors":interceptors,
               "c1": functools.partial(next, itertools.count(1)),
               "c2": functools.partial(next, itertools.count(1)),
               "c3": functools.partial(next, itertools.count(1)),
               "c4": functools.partial(next, itertools.count(1)),
               "c5": functools.partial(next, itertools.count(1)),
               "c6": functools.partial(next, itertools.count(1)),
               "form":form,
               "year":year_select}

    return render(request, "main/home.html", context)

##########Full Season Stats pages##########

def seasonstats(request):
    '''Extracts data from the MySQL datatbases for a maximum of 150 players, ranked from greatest to least,
    ofr each category. Each section returns a zip() object for names, rank, and paginated querysets.
    Stats from active players and retired players are stored in separate SQL tables.'''

    queries = [] #to hold raw querysets
    ordered = [] #to hold ordered querysets

    team_menu = TeamDropdown(request.GET or None)
    year_menu = YearDropdown(request.GET or None)
    status_menu = StatusDropdown(request.GET or None)
    category_menu = Categorydown(request.GET or None)

    year_select = request.GET.get('year')
    team_select = request.GET.get('team')
    category_select = request.GET.get('category')
    status_select = request.GET.get('status')
    page = request.GET.get('page') #this is for pagination

    if year_select == None and team_select == None and category_select == None and status_select == None: #when the page opens without a GET request

        yards = SeasonStats.yards(Passing.objects.filter(year="2018"), RetiredPassing.objects.filter(year="2018")) #returns a list of yards from each queryset. function in data_functions.py
        for y in yards:
            SeasonStats.act_ret_order(queries, Passing.objects.filter(year="2018", yards=y), RetiredPassing.objects.filter(year="2018", yards=y)) #puts each queryset in order from greatest to least. function in data_functions.py
        ids = StatOrder.real_topfive(queries) #extracts the player IDs from each queryset
        for i in ids:
            SeasonStats.act_ret_order(ordered, Passing.objects.filter(year="2018", player_id=i), RetiredPassing.objects.filter(year="2018", player_id=i))
        final = SeasonStats.limit(ordered) #puts a limit on the number of queries processed. function in data_functions.py
        num = list(range(1, len(final)+1)) #creating the 'ranks' by making a list of the number of items in the ordered list of querysets
        p2 = Paginator(num, 25) #paginator object for player ranks
        rank = p2.get_page(page) #can now iterate over the paginator object
        p = Paginator(ordered, 25) #paginator object for ordered querysets
        players = p.get_page(page)
        raw_names = ProfilePage.names_extraforloop(players) #processes the names of each player correctly. function in data_functions.py
        names = PlayerSearch.no_duplicate(raw_names) #returns another list with no duplicates. function in data_functions.py
        rank_players = zip(names,rank,players) #ex.[("Tom Brady", 1, <QuerySet..>), ()...]
        pagecount = StatOrder.pagecount(players) #insures accurate count of different pages in the paginator object. function in data_functions.py

    elif status_select == "All" and team_select == "All NFL":
        '''A very simiar process occurs below for all scenarios presented
        by the different GET requests.'''

        if category_select == "Passing":
            yards = SeasonStats.yards(Passing.objects.filter(year=year_select), RetiredPassing.objects.filter(year=year_select))
            for y in yards:
                SeasonStats.act_ret_order(queries, Passing.objects.filter(year=year_select, yards=y), RetiredPassing.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Passing.objects.filter(year=year_select, player_id=i), RetiredPassing.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Rushing":
            yards = SeasonStats.yards(Rushing.objects.filter(year=year_select), RetiredRushing.objects.filter(year=year_select))
            for y in yards:
                SeasonStats.act_ret_order(queries, Rushing.objects.filter(year=year_select, yards=y), RetiredRushing.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Rushing.objects.filter(year=year_select, player_id=i), RetiredRushing.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Receiving":
            yards = SeasonStats.yards(Receiving.objects.filter(year=year_select), RetiredReceiving.objects.filter(year=year_select))
            for y in yards:
                SeasonStats.act_ret_order(queries, Receiving.objects.filter(year=year_select, yards=y), RetiredReceiving.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Receiving.objects.filter(year=year_select, player_id=i), RetiredReceiving.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Tackles":
            tackles = SeasonStats.tackles(Defense.objects.filter(year=year_select), RetiredDefense.objects.filter(year=year_select))
            for t in tackles:
                SeasonStats.act_ret_order(queries, Defense.objects.filter(year=year_select, total_tkl=t), RetiredDefense.objects.filter(year=year_select, total_tkl=t))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Defense.objects.filter(year=year_select, player_id=i), RetiredDefense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Sacks":
            sacks = SeasonStats.sacks(Defense.objects.filter(year=year_select), RetiredDefense.objects.filter(year=year_select))
            for s in sacks:
                SeasonStats.act_ret_order(queries, Defense.objects.filter(year=year_select, sck=s), RetiredDefense.objects.filter(year=year_select, sck=s))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Defense.objects.filter(year=year_select, player_id=i), RetiredDefense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Interceptions":
            ints = SeasonStats.ints(Defense.objects.filter(year=year_select), RetiredDefense.objects.filter(year=year_select))
            for i in ints:
                SeasonStats.act_ret_order(queries, Defense.objects.filter(year=year_select, ints=i), RetiredDefense.objects.filter(year=year_select, ints=i))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Defense.objects.filter(year=year_select, player_id=i), RetiredDefense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Field Goals":
            fgs = SeasonStats.fgs(FieldGoals.objects.filter(year=year_select), RetiredFieldGoals.objects.filter(year=year_select))
            for f in fgs:
                SeasonStats.act_ret_order(queries, FieldGoals.objects.filter(year=year_select, fg=f), RetiredFieldGoals.objects.filter(year=year_select, fg=f))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, FieldGoals.objects.filter(year=year_select, player_id=i), RetiredFieldGoals.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punting":
            punts = SeasonStats.punts(Punting.objects.filter(year=year_select), RetiredPunting.objects.filter(year=year_select))
            for p in punts:
                SeasonStats.act_ret_order(queries, Punting.objects.filter(year=year_select, punts=p), RetiredPunting.objects.filter(year=year_select, punts=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Punting.objects.filter(year=year_select, player_id=i), RetiredPunting.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Kick Returns":
            krs = SeasonStats.krs(KickReturns.objects.filter(year=year_select), RetiredKickReturns.objects.filter(year=year_select))
            for k in krs:
                SeasonStats.act_ret_order(queries, KickReturns.objects.filter(year=year_select, kr=k), RetiredKickReturns.objects.filter(year=year_select, kr=k))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, KickReturns.objects.filter(year=year_select, player_id=i), RetiredKickReturns.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punt Returns":
            prs = SeasonStats.prs(PuntReturns.objects.filter(year=year_select), RetiredPuntReturns.objects.filter(year=year_select))
            for p in prs:
                SeasonStats.act_ret_order(queries, PuntReturns.objects.filter(year=year_select, pr=p), RetiredPuntReturns.objects.filter(year=year_select, pr=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, PuntReturns.objects.filter(year=year_select, player_id=i), RetiredPuntReturns.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

    elif team_select == "All NFL" and status_select == "Active":

        if category_select == "Passing":
            yards = SeasonStats.yards_one(Passing.objects.filter(year=year_select))
            for y in yards:
                queries.append(Passing.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Passing.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Rushing":
            yards = SeasonStats.yards_one(Rushing.objects.filter(year=year_select))
            for y in yards:
                queries.append(Rushing.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Rushing.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Receiving":
            yards = SeasonStats.yards_one(Receiving.objects.filter(year=year_select))
            for y in yards:
                queries.append(Receiving.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Receiving.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Tackles":
            tackles = SeasonStats.tackles_one(Defense.objects.filter(year=year_select))
            for t in tackles:
                queries.append(Defense.objects.filter(year=year_select, total_tkl=t))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Defense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Sacks":
            sacks = SeasonStats.sacks_one(Defense.objects.filter(year=year_select))
            for s in sacks:
                queries.append(Defense.objects.filter(year=year_select, sck=s))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Defense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Interceptions":
            ints = SeasonStats.ints_one(Defense.objects.filter(year=year_select))
            for i in ints:
                queries.append(Defense.objects.filter(year=year_select, ints=i))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Defense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Field Goals":
            fgs = SeasonStats.fgs_one(FieldGoals.objects.filter(year=year_select))
            for f in fgs:
                queries.append(FieldGoals.objects.filter(year=year_select, fg=f))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(FieldGoals.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punting":
            punts = SeasonStats.punts_one(Punting.objects.filter(year=year_select))
            for p in punts:
                queries.append(Punting.objects.filter(year=year_select, punts=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Punting.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Kick Returns":
            krs = SeasonStats.krs_one(KickReturns.objects.filter(year=year_select))
            for k in krs:
                queries.append(KickReturns.objects.filter(year=year_select, kr=k))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(KickReturns.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punt Returns":
            prs = SeasonStats.prs_one(PuntReturns.objects.filter(year=year_select))
            for p in prs:
                queries.append(PuntReturns.objects.filter(year=year_select, pr=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(PuntReturns.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

    elif team_select == "All NFL" and status_select == "Retired":

        if category_select == "Passing":
            yards = SeasonStats.yards_one(RetiredPassing.objects.filter(year=year_select))
            for y in yards:
                queries.append(RetiredPassing.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredPassing.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Rushing":
            yards = SeasonStats.yards_one(RetiredRushing.objects.filter(year=year_select))
            for y in yards:
                queries.append(RetiredRushing.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredRushing.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Receiving":
            yards = SeasonStats.yards_one(RetiredReceiving.objects.filter(year=year_select))
            for y in yards:
                queries.append(RetiredReceiving.objects.filter(year=year_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredReceiving.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Tackles":
            tackles = SeasonStats.tackles_one(RetiredDefense.objects.filter(year=year_select))
            for t in tackles:
                queries.append(RetiredDefense.objects.filter(year=year_select, total_tkl=t))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredDefense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Sacks":
            sacks = SeasonStats.sacks_one(RetiredDefense.objects.filter(year=year_select))
            for s in sacks:
                queries.append(RetiredDefense.objects.filter(year=year_select, sck=s))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredDefense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Interceptions":
            ints = SeasonStats.ints_one(RetiredDefense.objects.filter(year=year_select))
            for i in ints:
                queries.append(RetiredDefense.objects.filter(year=year_select, ints=i))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredDefense.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Field Goals":
            fgs = SeasonStats.fgs_one(RetiredFieldGoals.objects.filter(year=year_select))
            for f in fgs:
                queries.append(RetiredFieldGoals.objects.filter(year=year_select, fg=f))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredFieldGoals.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punting":
            punts = SeasonStats.punts_one(RetiredPunting.objects.filter(year=year_select))
            for p in punts:
                queries.append(RetiredPunting.objects.filter(year=year_select, punts=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredPunting.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Kick Returns":
            krs = SeasonStats.krs_one(RetiredKickReturns.objects.filter(year=year_select))
            for k in krs:
                queries.append(RetiredKickReturns.objects.filter(year=year_select, kr=k))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredKickReturns.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punt Returns":
            prs = SeasonStats.prs_one(RetiredPuntReturns.objects.filter(year=year_select))
            for p in prs:
                queries.append(RetiredPuntReturns.objects.filter(year=year_select, pr=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredPuntReturns.objects.filter(year=year_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

    elif status_select == "All" and team_select != "All NFL":

        if category_select == "Passing":
            yards = SeasonStats.yards(Passing.objects.filter(year=year_select,team=team_select), RetiredPassing.objects.filter(year=year_select,team=team_select))
            for y in yards:
                SeasonStats.act_ret_order(queries, Passing.objects.filter(year=year_select,team=team_select, yards=y), RetiredPassing.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Passing.objects.filter(year=year_select,team=team_select, player_id=i), RetiredPassing.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Rushing":
            yards = SeasonStats.yards(Rushing.objects.filter(year=year_select,team=team_select), RetiredRushing.objects.filter(year=year_select,team=team_select))
            for y in yards:
                SeasonStats.act_ret_order(queries, Rushing.objects.filter(year=year_select,team=team_select, yards=y), RetiredRushing.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Rushing.objects.filter(year=year_select,team=team_select, player_id=i), RetiredRushing.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Receiving":
            yards = SeasonStats.yards(Receiving.objects.filter(year=year_select,team=team_select), RetiredReceiving.objects.filter(year=year_select,team=team_select))
            for y in yards:
                SeasonStats.act_ret_order(queries, Receiving.objects.filter(year=year_select,team=team_select, yards=y), RetiredReceiving.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Receiving.objects.filter(year=year_select,team=team_select, player_id=i), RetiredReceiving.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Tackles":
            tackles = SeasonStats.tackles(Defense.objects.filter(year=year_select,team=team_select), RetiredDefense.objects.filter(year=year_select,team=team_select))
            for t in tackles:
                SeasonStats.act_ret_order(queries, Defense.objects.filter(year=year_select,team=team_select, total_tkl=t), RetiredDefense.objects.filter(year=year_select,team=team_select, total_tkl=t))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Defense.objects.filter(year=year_select,team=team_select, player_id=i), RetiredDefense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Sacks":
            sacks = SeasonStats.sacks(Defense.objects.filter(year=year_select,team=team_select), RetiredDefense.objects.filter(year=year_select,team=team_select))
            for s in sacks:
                SeasonStats.act_ret_order(queries, Defense.objects.filter(year=year_select,team=team_select, sck=s), RetiredDefense.objects.filter(year=year_select,team=team_select, sck=s))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Defense.objects.filter(year=year_select,team=team_select, player_id=i), RetiredDefense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Interceptions":
            ints = SeasonStats.ints(Defense.objects.filter(year=year_select,team=team_select), RetiredDefense.objects.filter(year=year_select,team=team_select))
            for i in ints:
                SeasonStats.act_ret_order(queries, Defense.objects.filter(year=year_select,team=team_select, ints=i), RetiredDefense.objects.filter(year=year_select,team=team_select, ints=i))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Defense.objects.filter(year=year_select,team=team_select, player_id=i), RetiredDefense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Field Goals":
            fgs = SeasonStats.fgs(FieldGoals.objects.filter(year=year_select,team=team_select), RetiredFieldGoals.objects.filter(year=year_select,team=team_select))
            for f in fgs:
                SeasonStats.act_ret_order(queries, FieldGoals.objects.filter(year=year_select,team=team_select, fg=f), RetiredFieldGoals.objects.filter(year=year_select,team=team_select, fg=f))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, FieldGoals.objects.filter(year=year_select,team=team_select, player_id=i), RetiredFieldGoals.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punting":
            punts = SeasonStats.punts(Punting.objects.filter(year=year_select,team=team_select), RetiredPunting.objects.filter(year=year_select,team=team_select))
            for p in punts:
                SeasonStats.act_ret_order(queries, Punting.objects.filter(year=year_select,team=team_select, punts=p), RetiredPunting.objects.filter(year=year_select,team=team_select, punts=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, Punting.objects.filter(year=year_select,team=team_select, player_id=i), RetiredPunting.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Kick Returns":
            krs = SeasonStats.krs(KickReturns.objects.filter(year=year_select,team=team_select), RetiredKickReturns.objects.filter(year=year_select,team=team_select))
            for k in krs:
                SeasonStats.act_ret_order(queries, KickReturns.objects.filter(year=year_select,team=team_select, kr=k), RetiredKickReturns.objects.filter(year=year_select,team=team_select, kr=k))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, KickReturns.objects.filter(year=year_select,team=team_select, player_id=i), RetiredKickReturns.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punt Returns":
            prs = SeasonStats.prs(PuntReturns.objects.filter(year=year_select,team=team_select), RetiredPuntReturns.objects.filter(year=year_select,team=team_select))
            for p in prs:
                SeasonStats.act_ret_order(queries, PuntReturns.objects.filter(year=year_select,team=team_select, pr=p), RetiredPuntReturns.objects.filter(year=year_select,team=team_select, pr=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                SeasonStats.act_ret_order(ordered, PuntReturns.objects.filter(year=year_select,team=team_select, player_id=i), RetiredPuntReturns.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

    elif status_select == "Active" and team_select != "All NFL":

        if category_select == "Passing":
            yards = SeasonStats.yards_one(Passing.objects.filter(year=year_select,team=team_select))
            for y in yards:
                queries.append(Passing.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Passing.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Rushing":
            yards = SeasonStats.yards_one(Rushing.objects.filter(year=year_select,team=team_select))
            for y in yards:
                queries.append(Rushing.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Rushing.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Receiving":
            yards = SeasonStats.yards_one(Receiving.objects.filter(year=year_select,team=team_select))
            for y in yards:
                queries.append(Receiving.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Receiving.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Tackles":
            tackles = SeasonStats.tackles_one(Defense.objects.filter(year=year_select,team=team_select))
            for t in tackles:
                queries.append(Defense.objects.filter(year=year_select,team=team_select, total_tkl=t))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Defense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Sacks":
            sacks = SeasonStats.sacks_one(Defense.objects.filter(year=year_select,team=team_select))
            for s in sacks:
                queries.append(Defense.objects.filter(year=year_select,team=team_select, sck=s))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Defense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Interceptions":
            ints = SeasonStats.ints_one(Defense.objects.filter(year=year_select,team=team_select))
            for i in ints:
                queries.append(Defense.objects.filter(year=year_select,team=team_select, ints=i))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Defense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Field Goals":
            fgs = SeasonStats.fgs_one(FieldGoals.objects.filter(year=year_select,team=team_select))
            for f in fgs:
                queries.append(FieldGoals.objects.filter(year=year_select,team=team_select, fg=f))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(FieldGoals.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punting":
            punts = SeasonStats.punts_one(Punting.objects.filter(year=year_select,team=team_select))
            for p in punts:
                queries.append(Punting.objects.filter(year=year_select,team=team_select, punts=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(Punting.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Kick Returns":
            krs = SeasonStats.krs_one(KickReturns.objects.filter(year=year_select,team=team_select))
            for k in krs:
                queries.append(KickReturns.objects.filter(year=year_select,team=team_select, kr=k))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(KickReturns.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punt Returns":
            prs = SeasonStats.prs_one(PuntReturns.objects.filter(year=year_select,team=team_select))
            for p in prs:
                queries.append(PuntReturns.objects.filter(year=year_select,team=team_select, pr=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(PuntReturns.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

    elif status_select == "Retired" and team_select != "All NFL":

        if category_select == "Passing":
            yards = SeasonStats.yards_one(RetiredPassing.objects.filter(year=year_select,team=team_select))
            for y in yards:
                queries.append(RetiredPassing.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredPassing.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Rushing":
            yards = SeasonStats.yards_one(RetiredRushing.objects.filter(year=year_select,team=team_select))
            for y in yards:
                queries.append(RetiredRushing.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredRushing.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Receiving":
            yards = SeasonStats.yards_one(RetiredReceiving.objects.filter(year=year_select,team=team_select))
            for y in yards:
                queries.append(RetiredReceiving.objects.filter(year=year_select,team=team_select, yards=y))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredReceiving.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Tackles":
            tackles = SeasonStats.tackles_one(RetiredDefense.objects.filter(year=year_select,team=team_select))
            for t in tackles:
                queries.append(RetiredDefense.objects.filter(year=year_select,team=team_select, total_tkl=t))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredDefense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Sacks":
            sacks = SeasonStats.sacks_one(RetiredDefense.objects.filter(year=year_select,team=team_select))
            for s in sacks:
                queries.append(RetiredDefense.objects.filter(year=year_select,team=team_select, sck=s))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredDefense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Interceptions":
            ints = SeasonStats.ints_one(RetiredDefense.objects.filter(year=year_select,team=team_select))
            for i in ints:
                queries.append(RetiredDefense.objects.filter(year=year_select,team=team_select, ints=i))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredDefense.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Field Goals":
            fgs = SeasonStats.fgs_one(RetiredFieldGoals.objects.filter(year=year_select,team=team_select))
            for f in fgs:
                queries.append(RetiredFieldGoals.objects.filter(year=year_select,team=team_select, fg=f))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredFieldGoals.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punting":
            punts = SeasonStats.punts_one(RetiredPunting.objects.filter(year=year_select,team=team_select))
            for p in punts:
                queries.append(RetiredPunting.objects.filter(year=year_select,team=team_select, punts=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredPunting.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Kick Returns":
            krs = SeasonStats.krs_one(RetiredKickReturns.objects.filter(year=year_select,team=team_select))
            for k in krs:
                queries.append(RetiredKickReturns.objects.filter(year=year_select,team=team_select, kr=k))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredKickReturns.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

        elif category_select == "Punt Returns":
            prs = SeasonStats.prs_one(RetiredPuntReturns.objects.filter(year=year_select,team=team_select))
            for p in prs:
                queries.append(RetiredPuntReturns.objects.filter(year=year_select,team=team_select, pr=p))
            ids = StatOrder.real_topfive(queries)
            for i in ids:
                ordered.append(RetiredPuntReturns.objects.filter(year=year_select,team=team_select, player_id=i))
            final = SeasonStats.limit(ordered)
            num = list(range(1, len(final)+1))
            p2 = Paginator(num, 25)
            rank = p2.get_page(page)
            p = Paginator(final, 25)
            players = p.get_page(page)
            raw_names = ProfilePage.names_extraforloop(players)
            names = PlayerSearch.no_duplicate(raw_names)
            rank_players = zip(names,rank,players)
            pagecount = StatOrder.pagecount(players)

    context = { "team_menu":team_menu,
              "year_menu":year_menu,
              "status_menu":status_menu,
              "category_menu":category_menu,
              "players":players,
              "category":category_select,
              "year":year_select,
              "status":status_select,
              "team":team_select,
              "pagecount":pagecount,
              "rank_players":rank_players
              }

    return render(request, "main/seasonstats.html", context)

def teamARI(request):
    '''Extracts data from each player on a specified team. The same process is done for each NFL team.
    Each section returns a zip() object with fullname and queryset'''

    qb = Profiles.objects.filter(position="QB",team="Arizona Cardinals") #queryset for each specified position on each team
    names = ProfilePage.names_list(qb) #processes the fullname of each player...function in data_functions.py
    qbs = zip(names, qb) #ex [("Larry Fitzgerald", <QuerySet...>), ()...]
    rb = Profiles.objects.filter(position="RB",team="Arizona Cardinals")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Arizona Cardinals")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Arizona Cardinals")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Arizona Cardinals")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Arizona Cardinals")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Arizona Cardinals")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Arizona Cardinals")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Arizona Cardinals")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Arizona Cardinals")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Arizona Cardinals")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Arizona Cardinals")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Arizona Cardinals")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Arizona Cardinals")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Arizona Cardinals")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Arizona Cardinals")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Arizona Cardinals")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Arizona Cardinals")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Arizona Cardinals")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Arizona Cardinals")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Arizona Cardinals")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Arizona Cardinals")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/ARI.html", context)

def teamATL(request):

    qb = Profiles.objects.filter(position="QB",team="Atlanta Falcons")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Atlanta Falcons")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Atlanta Falcons")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Atlanta Falcons")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Atlanta Falcons")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Atlanta Falcons")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Atlanta Falcons")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Atlanta Falcons")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Atlanta Falcons")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Atlanta Falcons")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Atlanta Falcons")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Atlanta Falcons")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Atlanta Falcons")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Atlanta Falcons")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Atlanta Falcons")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Atlanta Falcons")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Atlanta Falcons")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Atlanta Falcons")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Atlanta Falcons")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Atlanta Falcons")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Atlanta Falcons")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Atlanta Falcons")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/ATL.html", context)

def teamBAL(request):

    qb = Profiles.objects.filter(position="QB",team="Baltimore Ravens")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Baltimore Ravens")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Baltimore Ravens")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Baltimore Ravens")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Baltimore Ravens")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Baltimore Ravens")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Baltimore Ravens")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Baltimore Ravens")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Baltimore Ravens")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Baltimore Ravens")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Baltimore Ravens")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Baltimore Ravens")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Baltimore Ravens")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Baltimore Ravens")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Baltimore Ravens")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Baltimore Ravens")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Baltimore Ravens")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Baltimore Ravens")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Baltimore Ravens")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Baltimore Ravens")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Baltimore Ravens")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Baltimore Ravens")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/BAL.html", context)

def teamBUF(request):

    qb = Profiles.objects.filter(position="QB",team="Buffalo Bills")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Buffalo Bills")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Buffalo Bills")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Buffalo Bills")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Buffalo Bills")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Buffalo Bills")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Buffalo Bills")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Buffalo Bills")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Buffalo Bills")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Buffalo Bills")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Buffalo Bills")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Buffalo Bills")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Buffalo Bills")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Buffalo Bills")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Buffalo Bills")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Buffalo Bills")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Buffalo Bills")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Buffalo Bills")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Buffalo Bills")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Buffalo Bills")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Buffalo Bills")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Buffalo Bills")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/BUF.html", context)

def teamCAR(request):

    qb = Profiles.objects.filter(position="QB",team="Carolina Panthers")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Carolina Panthers")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Carolina Panthers")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Carolina Panthers")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Carolina Panthers")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Carolina Panthers")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Carolina Panthers")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Carolina Panthers")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Carolina Panthers")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Carolina Panthers")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Carolina Panthers")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Carolina Panthers")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Carolina Panthers")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Carolina Panthers")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Carolina Panthers")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Carolina Panthers")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Carolina Panthers")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Carolina Panthers")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Carolina Panthers")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Carolina Panthers")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Carolina Panthers")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Carolina Panthers")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/CAR.html", context)

def teamCHI(request):

    qb = Profiles.objects.filter(position="QB",team="Chicago Bears")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Chicago Bears")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Chicago Bears")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Chicago Bears")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Chicago Bears")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Chicago Bears")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Chicago Bears")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Chicago Bears")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Chicago Bears")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Chicago Bears")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Chicago Bears")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Chicago Bears")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Chicago Bears")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Chicago Bears")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Chicago Bears")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Chicago Bears")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Chicago Bears")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Chicago Bears")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Chicago Bears")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Chicago Bears")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Chicago Bears")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Chicago Bears")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/CHI.html", context)

def teamCIN(request):

    qb = Profiles.objects.filter(position="QB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Cincinnati Bengals")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Cincinnati Bengals")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Cincinnati Bengals")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Cincinnati Bengals")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Cincinnati Bengals")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Cincinnati Bengals")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Cincinnati Bengals")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Cincinnati Bengals")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Cincinnati Bengals")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Cincinnati Bengals")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Cincinnati Bengals")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Cincinnati Bengals")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Cincinnati Bengals")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Cincinnati Bengals")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/CIN.html", context)

def teamCLE(request):

    qb = Profiles.objects.filter(position="QB",team="Cleveland Browns")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Cleveland Browns")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Cleveland Browns")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Cleveland Browns")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Cleveland Browns")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Cleveland Browns")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Cleveland Browns")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Cleveland Browns")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Cleveland Browns")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Cleveland Browns")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Cleveland Browns")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Cleveland Browns")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Cleveland Browns")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Cleveland Browns")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Cleveland Browns")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Cleveland Browns")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Cleveland Browns")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Cleveland Browns")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Cleveland Browns")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Cleveland Browns")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Cleveland Browns")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Cleveland Browns")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/CLE.html", context)

def teamDAL(request):

    qb = Profiles.objects.filter(position="QB",team="Dallas Cowboys")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Dallas Cowboys")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Dallas Cowboys")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Dallas Cowboys")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Dallas Cowboys")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Dallas Cowboys")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Dallas Cowboys")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Dallas Cowboys")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Dallas Cowboys")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Dallas Cowboys")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Dallas Cowboys")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Dallas Cowboys")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Dallas Cowboys")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Dallas Cowboys")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Dallas Cowboys")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Dallas Cowboys")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Dallas Cowboys")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Dallas Cowboys")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Dallas Cowboys")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Dallas Cowboys")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Dallas Cowboys")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Dallas Cowboys")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/DAL.html", context)

def teamDEN(request):

    qb = Profiles.objects.filter(position="QB",team="Denver Broncos")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Denver Broncos")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Denver Broncos")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Denver Broncos")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Denver Broncos")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Denver Broncos")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Denver Broncos")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Denver Broncos")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Denver Broncos")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Denver Broncos")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Denver Broncos")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Denver Broncos")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Denver Broncos")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Denver Broncos")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Denver Broncos")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Denver Broncos")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Denver Broncos")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Denver Broncos")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Denver Broncos")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Denver Broncos")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Denver Broncos")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Denver Broncos")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/DEN.html", context)

def teamDET(request):

    qb = Profiles.objects.filter(position="QB",team="Detroit Lions")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Detroit Lions")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Detroit Lions")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Detroit Lions")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Detroit Lions")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Detroit Lions")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Detroit Lions")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Detroit Lions")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Detroit Lions")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Detroit Lions")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Detroit Lions")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Detroit Lions")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Detroit Lions")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Detroit Lions")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Detroit Lions")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Detroit Lions")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Detroit Lions")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Detroit Lions")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Detroit Lions")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Detroit Lions")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Detroit Lions")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Detroit Lions")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/DET.html", context)

def teamGB(request):

    qb = Profiles.objects.filter(position="QB",team="Green Bay Packers")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Green Bay Packers")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Green Bay Packers")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Green Bay Packers")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Green Bay Packers")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Green Bay Packers")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Green Bay Packers")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Green Bay Packers")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Green Bay Packers")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Green Bay Packers")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Green Bay Packers")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Green Bay Packers")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Green Bay Packers")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Green Bay Packers")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Green Bay Packers")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Green Bay Packers")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Green Bay Packers")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Green Bay Packers")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Green Bay Packers")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Green Bay Packers")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Green Bay Packers")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Green Bay Packers")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/GB.html", context)

def teamHOU(request):

    qb = Profiles.objects.filter(position="QB",team="Houston Texans")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Houston Texans")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Houston Texans")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Houston Texans")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Houston Texans")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Houston Texans")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Houston Texans")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Houston Texans")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Houston Texans")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Houston Texans")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Houston Texans")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Houston Texans")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Houston Texans")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Houston Texans")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Houston Texans")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Houston Texans")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Houston Texans")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Houston Texans")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Houston Texans")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Houston Texans")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Houston Texans")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Houston Texans")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/HOU.html", context)

def teamIND(request):

    qb = Profiles.objects.filter(position="QB",team="Indianapolis Colts")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Indianapolis Colts")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Indianapolis Colts")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Indianapolis Colts")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Indianapolis Colts")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Indianapolis Colts")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Indianapolis Colts")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Indianapolis Colts")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Indianapolis Colts")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Indianapolis Colts")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Indianapolis Colts")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Indianapolis Colts")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Indianapolis Colts")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Indianapolis Colts")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Indianapolis Colts")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Indianapolis Colts")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Indianapolis Colts")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Indianapolis Colts")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Indianapolis Colts")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Indianapolis Colts")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Indianapolis Colts")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Indianapolis Colts")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/IND.html", context)

def teamJAX(request):

    qb = Profiles.objects.filter(position="QB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Jacksonville Jaguars")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/JAX.html", context)

def teamKC(request):

    qb = Profiles.objects.filter(position="QB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Kansas City Chiefs")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Kansas City Chiefs")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Kansas City Chiefs")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Kansas City Chiefs")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Kansas City Chiefs")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Kansas City Chiefs")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Kansas City Chiefs")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Kansas City Chiefs")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Kansas City Chiefs")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Kansas City Chiefs")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Kansas City Chiefs")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Kansas City Chiefs")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Kansas City Chiefs")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Kansas City Chiefs")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/KC.html", context)

def teamLA(request):

    qb = Profiles.objects.filter(position="QB",team="Los Angeles Rams")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Los Angeles Rams")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Los Angeles Rams")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Los Angeles Rams")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Los Angeles Rams")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Los Angeles Rams")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Los Angeles Rams")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Los Angeles Rams")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Los Angeles Rams")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Los Angeles Rams")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Los Angeles Rams")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Los Angeles Rams")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Los Angeles Rams")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Los Angeles Rams")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Los Angeles Rams")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Los Angeles Rams")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Los Angeles Rams")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Los Angeles Rams")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Los Angeles Rams")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Los Angeles Rams")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Los Angeles Rams")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Los Angeles Rams")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/LA.html", context)

def teamLAC(request):

    qb = Profiles.objects.filter(position="QB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Los Angeles Chargers")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Los Angeles Chargers")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Los Angeles Chargers")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Los Angeles Chargers")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Los Angeles Chargers")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Los Angeles Chargers")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Los Angeles Chargers")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Los Angeles Chargers")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Los Angeles Chargers")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Los Angeles Chargers")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Los Angeles Chargers")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Los Angeles Chargers")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Los Angeles Chargers")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Los Angeles Chargers")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/LAC.html", context)

def teamMIA(request):

    qb = Profiles.objects.filter(position="QB",team="Miami Dolphins")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Miami Dolphins")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Miami Dolphins")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Miami Dolphins")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Miami Dolphins")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Miami Dolphins")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Miami Dolphins")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Miami Dolphins")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Miami Dolphins")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Miami Dolphins")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Miami Dolphins")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Miami Dolphins")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Miami Dolphins")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Miami Dolphins")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Miami Dolphins")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Miami Dolphins")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Miami Dolphins")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Miami Dolphins")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Miami Dolphins")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Miami Dolphins")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Miami Dolphins")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Miami Dolphins")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/MIA.html", context)

def teamMIN(request):

    qb = Profiles.objects.filter(position="QB",team="Minnesota Vikings")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Minnesota Vikings")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Minnesota Vikings")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Minnesota Vikings")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Minnesota Vikings")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Minnesota Vikings")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Minnesota Vikings")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Minnesota Vikings")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Minnesota Vikings")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Minnesota Vikings")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Minnesota Vikings")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Minnesota Vikings")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Minnesota Vikings")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Minnesota Vikings")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Minnesota Vikings")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Minnesota Vikings")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Minnesota Vikings")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Minnesota Vikings")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Minnesota Vikings")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Minnesota Vikings")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Minnesota Vikings")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Minnesota Vikings")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/MIN.html", context)

def teamNE(request):

    qb = Profiles.objects.filter(position="QB",team="New England Patriots")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="New England Patriots")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="New England Patriots")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="New England Patriots")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="New England Patriots")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="New England Patriots")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="New England Patriots")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="New England Patriots")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="New England Patriots")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="New England Patriots")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="New England Patriots")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="New England Patriots")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="New England Patriots")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="New England Patriots")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="New England Patriots")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="New England Patriots")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="New England Patriots")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="New England Patriots")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="New England Patriots")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="New England Patriots")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="New England Patriots")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="New England Patriots")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/NE.html", context)

def teamNO(request):

    qb = Profiles.objects.filter(position="QB",team="New Orleans Saints")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="New Orleans Saints")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="New Orleans Saints")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="New Orleans Saints")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="New Orleans Saints")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="New Orleans Saints")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="New Orleans Saints")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="New Orleans Saints")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="New Orleans Saints")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="New Orleans Saints")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="New Orleans Saints")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="New Orleans Saints")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="New Orleans Saints")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="New Orleans Saints")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="New Orleans Saints")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="New Orleans Saints")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="New Orleans Saints")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="New Orleans Saints")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="New Orleans Saints")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="New Orleans Saints")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="New Orleans Saints")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="New Orleans Saints")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/NO.html", context)

def teamNYG(request):

    qb = Profiles.objects.filter(position="QB",team="New York Giants")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="New York Giants")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="New York Giants")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="New York Giants")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="New York Giants")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="New York Giants")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="New York Giants")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="New York Giants")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="New York Giants")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="New York Giants")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="New York Giants")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="New York Giants")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="New York Giants")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="New York Giants")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="New York Giants")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="New York Giants")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="New York Giants")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="New York Giants")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="New York Giants")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="New York Giants")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="New York Giants")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="New York Giants")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/NYG.html", context)

def teamNYJ(request):

    qb = Profiles.objects.filter(position="QB",team="New York Jets")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="New York Jets")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="New York Jets")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="New York Jets")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="New York Jets")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="New York Jets")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="New York Jets")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="New York Jets")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="New York Jets")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="New York Jets")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="New York Jets")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="New York Jets")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="New York Jets")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="New York Jets")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="New York Jets")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="New York Jets")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="New York Jets")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="New York Jets")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="New York Jets")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="New York Jets")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="New York Jets")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="New York Jets")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/NYJ.html", context)

def teamOAK(request):

    qb = Profiles.objects.filter(position="QB",team="Oakland Raiders")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Oakland Raiders")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Oakland Raiders")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Oakland Raiders")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Oakland Raiders")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Oakland Raiders")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Oakland Raiders")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Oakland Raiders")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Oakland Raiders")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Oakland Raiders")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Oakland Raiders")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Oakland Raiders")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Oakland Raiders")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Oakland Raiders")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Oakland Raiders")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Oakland Raiders")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Oakland Raiders")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Oakland Raiders")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Oakland Raiders")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Oakland Raiders")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Oakland Raiders")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Oakland Raiders")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/OAK.html", context)

def teamPHI(request):

    qb = Profiles.objects.filter(position="QB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Philadelphia Eagles")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Philadelphia Eagles")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Philadelphia Eagles")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Philadelphia Eagles")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Philadelphia Eagles")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Philadelphia Eagles")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Philadelphia Eagles")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Philadelphia Eagles")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Philadelphia Eagles")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Philadelphia Eagles")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Philadelphia Eagles")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Philadelphia Eagles")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Philadelphia Eagles")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Philadelphia Eagles")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/PHI.html", context)

def teamPIT(request):

    qb = Profiles.objects.filter(position="QB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Pittsburgh Steelers")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/PIT.html", context)

def teamSEA(request):

    qb = Profiles.objects.filter(position="QB",team="Seattle Seahawks")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Seattle Seahawks")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Seattle Seahawks")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Seattle Seahawks")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Seattle Seahawks")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Seattle Seahawks")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Seattle Seahawks")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Seattle Seahawks")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Seattle Seahawks")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Seattle Seahawks")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Seattle Seahawks")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Seattle Seahawks")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Seattle Seahawks")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Seattle Seahawks")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Seattle Seahawks")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Seattle Seahawks")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Seattle Seahawks")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Seattle Seahawks")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Seattle Seahawks")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Seattle Seahawks")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Seattle Seahawks")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Seattle Seahawks")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/SEA.html", context)

def teamSF(request):

    qb = Profiles.objects.filter(position="QB",team="San Francisco 49ers")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="San Francisco 49ers")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="San Francisco 49ers")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="San Francisco 49ers")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="San Francisco 49ers")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="San Francisco 49ers")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="San Francisco 49ers")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="San Francisco 49ers")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="San Francisco 49ers")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="San Francisco 49ers")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="San Francisco 49ers")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="San Francisco 49ers")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="San Francisco 49ers")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="San Francisco 49ers")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="San Francisco 49ers")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="San Francisco 49ers")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="San Francisco 49ers")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="San Francisco 49ers")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="San Francisco 49ers")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="San Francisco 49ers")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="San Francisco 49ers")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="San Francisco 49ers")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/SF.html", context)

def teamTB(request):

    qb = Profiles.objects.filter(position="QB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Tampa Bay Buccaneers")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/TB.html", context)

def teamTEN(request):

    qb = Profiles.objects.filter(position="QB",team="Tennessee Titans")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Tennessee Titans")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Tennessee Titans")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Tennessee Titans")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Tennessee Titans")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Tennessee Titans")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Tennessee Titans")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Tennessee Titans")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Tennessee Titans")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Tennessee Titans")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Tennessee Titans")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Tennessee Titans")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Tennessee Titans")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Tennessee Titans")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Tennessee Titans")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Tennessee Titans")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Tennessee Titans")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Tennessee Titans")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Tennessee Titans")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Tennessee Titans")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Tennessee Titans")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Tennessee Titans")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/TEN.html", context)

def teamWAS(request):

    qb = Profiles.objects.filter(position="QB",team="Washington Redskins")
    names = ProfilePage.names_list(qb)
    qbs = zip(names, qb)
    rb = Profiles.objects.filter(position="RB",team="Washington Redskins")
    names = ProfilePage.names_list(rb)
    rbs = zip(names, rb)
    fb = Profiles.objects.filter(position="FB",team="Washington Redskins")
    names = ProfilePage.names_list(fb)
    fbs = zip(names, fb)
    wr = Profiles.objects.filter(position="WR",team="Washington Redskins")
    names = ProfilePage.names_list(wr)
    wrs = zip(names, wr)
    te = Profiles.objects.filter(position="TE",team="Washington Redskins")
    names = ProfilePage.names_list(te)
    tes = zip(names, te)
    ot = Profiles.objects.filter(position="OT",team="Washington Redskins")
    names = ProfilePage.names_list(ot)
    ots = zip(names, ot)
    og = Profiles.objects.filter(position="OG",team="Washington Redskins")
    names = ProfilePage.names_list(og)
    ogs = zip(names, og)
    c = Profiles.objects.filter(position="C",team="Washington Redskins")
    names = ProfilePage.names_list(c)
    cs = zip(names, c)
    nt = Profiles.objects.filter(position="NT",team="Washington Redskins")
    names = ProfilePage.names_list(nt)
    nts = zip(names, nt)
    dt = Profiles.objects.filter(position="DT",team="Washington Redskins")
    names = ProfilePage.names_list(dt)
    dts = zip(names, dt)
    de = Profiles.objects.filter(position="DE",team="Washington Redskins")
    names = ProfilePage.names_list(de)
    des = zip(names, de)
    olb = Profiles.objects.filter(position="OLB",team="Washington Redskins")
    names = ProfilePage.names_list(olb)
    olbs = zip(names, olb)
    ilb = Profiles.objects.filter(position="ILB",team="Washington Redskins")
    names = ProfilePage.names_list(ilb)
    ilbs = zip(names, ilb)
    mlb = Profiles.objects.filter(position="MLB",team="Washington Redskins")
    names = ProfilePage.names_list(mlb)
    mlbs = zip(names, mlb)
    lb = Profiles.objects.filter(position="LB",team="Washington Redskins")
    names = ProfilePage.names_list(lb)
    lbs = zip(names, lb)
    cb = Profiles.objects.filter(position="CB",team="Washington Redskins")
    names = ProfilePage.names_list(cb)
    cbs = zip(names, cb)
    db = Profiles.objects.filter(position="DB",team="Washington Redskins")
    names = ProfilePage.names_list(db)
    dbs = zip(names, db)
    fs = Profiles.objects.filter(position="FS",team="Washington Redskins")
    names = ProfilePage.names_list(fs)
    fss = zip(names, fs)
    ss = Profiles.objects.filter(position="SS",team="Washington Redskins")
    names = ProfilePage.names_list(ss)
    sss = zip(names, ss)
    k = Profiles.objects.filter(position="K",team="Washington Redskins")
    names = ProfilePage.names_list(k)
    ks = zip(names, k)
    p = Profiles.objects.filter(position="P",team="Washington Redskins")
    names = ProfilePage.names_list(p)
    ps = zip(names, p)
    ls = Profiles.objects.filter(position="LS",team="Washington Redskins")
    names = ProfilePage.names_list(ls)
    lss = zip(names, ls)

    context = {"qbs":qbs, "rbs":rbs, "fbs":fbs, "wrs":wrs,
               "tes":tes, "ots":ots, "ogs":ogs, "cs":cs,
               "nts":nts, "dts":dts, "des":des, "olbs":olbs,
               "ilbs":ilbs, "mlbs":mlbs, "lbs":lbs, "cbs":cbs,
               "dbs":dbs, "fss":fss, "sss":sss, "ks":ks,
               "ps":ps, "lss":lss}

    return render(request, "main/team/WAS.html", context)

def teams(request):
    return render(request, "main/teams.html", {})
