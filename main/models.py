from django.db import models


class Profiles(models.Model):
    age = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    college = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=50)
    player_id = models.CharField(max_length=200, primary_key=True)
    position = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " - " + self.player_id


class RetiredProfiles(models.Model):
    age = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    college = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    player_id = models.CharField(max_length=200, primary_key=True)
    weight = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " - " + self.player_id


class ProfilePics(models.Model):
    player_id = models.CharField(max_length=200)
    urls = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.urls


class Passing(models.Model):
    player_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    att = models.CharField(max_length=50)
    comp = models.CharField(max_length=50)
    comp_pct = models.CharField(max_length=50)
    att_g = models.CharField(max_length=50)
    yards = models.CharField(max_length=50)
    yards_att = models.CharField(max_length=50)
    yards_g = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    ints = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    comp_twenty_plus = models.CharField(max_length=50)
    comp_forty_plus = models.CharField(max_length=50)
    sck = models.CharField(max_length=50)
    sck_yards = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    team_short = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.position


class RetiredPassing(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    att = models.CharField(max_length=50)
    comp = models.CharField(max_length=50)
    comp_pct = models.CharField(max_length=50)
    att_g = models.CharField(max_length=50)
    yards = models.CharField(max_length=50)
    yards_att = models.CharField(max_length=50)
    yards_g = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    ints = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    comp_twenty_plus = models.CharField(max_length=50)
    comp_forty_plus = models.CharField(max_length=50)
    sck = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Rushing(models.Model):
    player_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    att = models.CharField(max_length=50)
    att_g = models.CharField(max_length=50)
    yards = models.CharField(max_length=50)
    yards_g = models.CharField(max_length=50)
    yards_c = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    fd = models.CharField(max_length=50)
    rush_twenty_plus = models.CharField(max_length=50)
    rush_forty_plus = models.CharField(max_length=50)
    fum = models.CharField(max_length=50)
    team_short = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.position


class RetiredRushing(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    att = models.CharField(max_length=50)
    att_g = models.CharField(max_length=50)
    yards = models.CharField(max_length=50)
    yards_g = models.CharField(max_length=50)
    yards_c = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    fd = models.CharField(max_length=50)
    rush_twenty_plus = models.CharField(max_length=50)
    rush_forty_plus = models.CharField(max_length=50)
    fum = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Receiving(models.Model):
    player_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    rec = models.CharField(max_length=50)
    yards = models.CharField(max_length=50)
    yards_rec = models.CharField(max_length=50)
    yards_g = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    rec_twenty_plus = models.CharField(max_length=50)
    rec_forty_plus = models.CharField(max_length=50)
    fd = models.CharField(max_length=50)
    fum = models.CharField(max_length=50)
    team_short = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.position


class RetiredReceiving(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    rec = models.CharField(max_length=50)
    yards = models.CharField(max_length=50)
    yards_rec = models.CharField(max_length=50)
    yards_g = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    rec_twenty_plus = models.CharField(max_length=50)
    rec_forty_plus = models.CharField(max_length=50)
    fd = models.CharField(max_length=50)
    fum = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RetiredOL(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games_p = models.CharField(max_length=50)
    games_s = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Defense(models.Model):
    player_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    total_tkl = models.CharField(max_length=50)
    solo_tkl = models.CharField(max_length=50)
    assisted_tkl = models.CharField(max_length=50)
    sck = models.CharField(max_length=50)
    safties = models.CharField(max_length=50)
    pass_def = models.CharField(max_length=50)
    ints = models.CharField(max_length=50)
    int_td = models.CharField(max_length=50)
    int_yards = models.CharField(max_length=50)
    yards_int = models.CharField(max_length=50)
    lng_int_return = models.CharField(max_length=50)
    team_short = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.position


class RetiredDefense(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    total_tkl = models.CharField(max_length=50)
    solo_tkl = models.CharField(max_length=50)
    assisted_tkl = models.CharField(max_length=50)
    sck = models.CharField(max_length=50)
    safties = models.CharField(max_length=50)
    pass_def = models.CharField(max_length=50)
    ints = models.CharField(max_length=50)
    int_td = models.CharField(max_length=50)
    int_yards = models.CharField(max_length=50)
    yards_int = models.CharField(max_length=50)
    lng_int_return = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FieldGoals(models.Model):
    player_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    kb = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    fg = models.CharField(max_length=50)
    fg_att = models.CharField(max_length=50)
    fg_perc = models.CharField(max_length=50)
    fg_twenty = models.CharField(max_length=50)
    fg_twenty_att = models.CharField(max_length=50)
    fg_twenty_perc = models.CharField(max_length=50)
    fg_thirty = models.CharField(max_length=50)
    fg_thirty_att = models.CharField(max_length=50)
    fg_thirty_perc = models.CharField(max_length=50)
    fg_forty = models.CharField(max_length=50)
    fg_forty_att = models.CharField(max_length=50)
    fg_forty_perc = models.CharField(max_length=50)
    fg_fifty = models.CharField(max_length=50)
    fg_fifty_att = models.CharField(max_length=50)
    fg_fifty_perc = models.CharField(max_length=50)
    ex = models.CharField(max_length=50)
    ex_att = models.CharField(max_length=50)
    ex_perc = models.CharField(max_length=50)
    ex_b = models.CharField(max_length=50)
    team_short = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.position


class RetiredFieldGoals(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    kb = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    fg = models.CharField(max_length=50)
    fg_att = models.CharField(max_length=50)
    fg_perc = models.CharField(max_length=50)
    fg_twenty = models.CharField(max_length=50)
    fg_twenty_att = models.CharField(max_length=50)
    fg_twenty_perc = models.CharField(max_length=50)
    fg_thirty = models.CharField(max_length=50)
    fg_thirty_att = models.CharField(max_length=50)
    fg_thirty_perc = models.CharField(max_length=50)
    fg_forty = models.CharField(max_length=50)
    fg_forty_att = models.CharField(max_length=50)
    fg_forty_perc = models.CharField(max_length=50)
    fg_fifty = models.CharField(max_length=50)
    fg_fifty_att = models.CharField(max_length=50)
    fg_fifty_perc = models.CharField(max_length=50)
    ex = models.CharField(max_length=50)
    ex_att = models.CharField(max_length=50)
    ex_perc = models.CharField(max_length=50)
    ex_b = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Punting(models.Model):
    player_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    punts = models.CharField(max_length=50)
    p_yards = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    p_avg = models.CharField(max_length=50)
    pb = models.CharField(max_length=50)
    obp = models.CharField(max_length=50)
    dp = models.CharField(max_length=50)
    p_twenty = models.CharField(max_length=50)
    tb = models.CharField(max_length=50)
    fc = models.CharField(max_length=50)
    p_ret = models.CharField(max_length=50)
    p_ret_yards = models.CharField(max_length=50)
    p_ret_td = models.CharField(max_length=50)
    team_short = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.position


class RetiredPunting(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    punts = models.CharField(max_length=50)
    p_yards = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    p_avg = models.CharField(max_length=50)
    pb = models.CharField(max_length=50)
    obp = models.CharField(max_length=50)
    dp = models.CharField(max_length=50)
    p_twenty = models.CharField(max_length=50)
    tb = models.CharField(max_length=50)
    fc = models.CharField(max_length=50)
    p_ret = models.CharField(max_length=50)
    p_ret_yards = models.CharField(max_length=50)
    p_ret_td = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class KickReturns(models.Model):
    player_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    kr = models.CharField(max_length=50)
    kr_yards = models.CharField(max_length=50)
    yards_kr = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    kr_twenty_plus = models.CharField(max_length=50)
    kr_forty_plus = models.CharField(max_length=50)
    fc = models.CharField(max_length=50)
    fum = models.CharField(max_length=50)
    team_short = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.position


class RetiredKickReturns(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    kr = models.CharField(max_length=50)
    kr_yards = models.CharField(max_length=50)
    yards_kr = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    kr_twenty_plus = models.CharField(max_length=50)
    kr_forty_plus = models.CharField(max_length=50)
    fc = models.CharField(max_length=50)
    fum = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PuntReturns(models.Model):
    player_id = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    pr = models.CharField(max_length=50)
    pr_yards = models.CharField(max_length=50)
    yards_pr = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    pr_twenty_plus = models.CharField(max_length=50)
    pr_forty_plus = models.CharField(max_length=50)
    fc = models.CharField(max_length=50)
    fum = models.CharField(max_length=50)
    team_short = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.position


class RetiredPuntReturns(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    games = models.CharField(max_length=50)
    pr = models.CharField(max_length=50)
    pr_yards = models.CharField(max_length=50)
    yards_pr = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    td = models.CharField(max_length=50)
    pr_twenty_plus = models.CharField(max_length=50)
    pr_forty_plus = models.CharField(max_length=50)
    fc = models.CharField(max_length=50)
    fum = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class HOF(models.Model):
    player_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " -- " + self.year
