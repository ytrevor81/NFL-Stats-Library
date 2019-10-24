from django import forms
from django.utils.safestring import mark_safe

teams = ['All NFL', 'Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Diego Chargers', 'San Francisco 49ers', 'Seattle Seahawks', 'St. Louis Rams', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']

positions = ["All", "QB", "RB", "FB", "WR", "TE", "DE", "DT", "NT", "OLB", "ILB", "MLB", "LB", "CB", "DB", "FS", "SS", "K", "P"]

categories = ["Passing", "Rushing", "Receiving", "Tackles", "Sacks", "Interceptions", "Field Goals", "Punting", "Kick Returns", "Punt Returns"]

profile = [('Positional Stats', 'Positional Stats'), ('All Stats', 'All Stats')]

status = ['Active', 'Retired', 'All']

status_search = ['Active', 'Retired']


class YearDropdown(forms.Form):
    year = forms.ChoiceField(label="", choices=((str(x), x) for x in range(2018, 1959, -1)), widget=forms.Select(attrs={'name':'year', 'id': 'sel-year'}))


class TeamDropdown(forms.Form):
    team = forms.ChoiceField(label="", choices=((x, x) for x in teams), widget=forms.Select(attrs={'name': 'team', 'id':'sel-team'}))


class Categorydown(forms.Form):
    category = forms.ChoiceField(label="", choices=((x, x) for x in categories), widget=forms.Select(attrs={'name':'category', 'id':'sel_category'}))


class PositionDropdown(forms.Form):
    position = forms.ChoiceField(label="", choices=((x, x) for x in positions), widget=forms.Select(attrs={'class':'grey-dropdown'}))


class StatusDropdown(forms.Form):
    status = forms.ChoiceField(label="", choices=((x, x) for x in status), widget=forms.Select(attrs={'name':'status', 'id':'sel_status'}))


class StatusSearchDropdown(forms.Form):
    status = forms.ChoiceField(label="", choices=((x, x) for x in status_search), widget=forms.Select(attrs={'class':'grey-dropdown'}))

#attrs={'class':'radio-profile'} ,
class ProfileRadio(forms.Form):
    radio = forms.ChoiceField(label="",choices=profile,widget=forms.RadioSelect())
