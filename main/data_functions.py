class DataTypes(object):

    @classmethod
    def integers(cls, list):
        x = [i.replace(",", "") for i in list]
        y = [i for i in x if i != "--"]
        z = [i for i in y if i != "0"]
        ints = [int(i) for i in z]
        return ints

    @classmethod
    def floats(cls, list):
        x = [i for i in list if i != "--"]
        y = [i for i in x if i != "0"]
        real = [float(i) for i in y]
        return real

class StatOrder(object):

    @classmethod
    def lng(cls, list):
        separate = [x.partition("T") for x in list]
        strings = [x[0] for x in separate]
        clear = [i for i in strings if i != "--"]
        integers = [int(x) for x in clear]
        lngs = sorted(integers)
        if len(lngs) == 0:
            pass
        else:
            return lngs[-1]

    @classmethod
    def greatest_least(cls, list):
        '''Parameter has to be list of strings that are integers'''
        ints = DataTypes.integers(list)
        sorted_list = []
        for i in ints:
            if i not in sorted_list:
                sorted_list.append(i)
        sorted_list.sort(reverse=True)
        return sorted_list

    @classmethod
    def greatest_least_float(cls, list):
        '''Parameter has to be list of strings that are integers'''
        floats = DataTypes.floats(list)
        sorted_list = []
        for i in floats:
            if i not in sorted_list:
                sorted_list.append(i)
        sorted_list.sort(reverse=True)
        return sorted_list

    @classmethod
    def add_commas(cls, list):
        '''Parameter has to be integers'''
        strings = [str(i) for i in list]
        commas = []
        for i in strings:
            if len(i) == 4:
                ii = i[:1] + ',' + i[1:]
                commas.append(ii)
            else:
                commas.append(i)
        return commas

    @classmethod
    def real_topfive(cls, list):
        names = []
        for i in list:
            for x in i:
                names.append(x.player_id)
        return names

    @classmethod
    def pagecount(cls, pagination):
        pages = []
        plusone = pagination.paginator.num_pages + 1
        for i in range(1, plusone):
            pages.append(i)
        return pages

class ProfilePage(object):

    @classmethod
    def name(cls, list):
        for name in list:
            rawname = name.partition(", ")
            first = rawname[2]
            last = rawname[0]
        firstlast = [first, last]
        return firstlast

    @classmethod
    def names_list(cls, players):
        names = []
        raw_names = [x.name for x in players]
        for i in raw_names:
            rawname = i.partition(", ")
            first = rawname[2]
            last = rawname[0]
            name = first + " " + last
            names.append(name)
        return names

    @classmethod
    def names_extraforloop(cls, players):
        names = []
        for player in players:
            raw_names = [x.name for x in player]
            for i in raw_names:
                rawname = i.partition(", ")
                first = rawname[2]
                last = rawname[0]
                name = first + " " + last
                names.append(name)
        return names

    @classmethod
    def many_names(cls, list, listtwo):
        for x in list:
            raw = x.partition(", ")
            first = raw[2]
            last = raw[0]
            firstlast = [first, last]
            listtwo.append(firstlast)

    @classmethod
    def height(cls, list):
        for string in list:
            num = int(string)
            feet = num // 12
            inches = num % 12
            ft = str(feet)
            i = str(inches)
        h = ft + "-" + i
        return h

    @classmethod
    def career_passing(cls, list):
        g = [x.games for x in list]

        if len(g) == 0:
            return ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]

        else:
            pre_games = DataTypes.integers(g)
            games = sum(pre_games)

            c = [x.comp for x in list]
            pre_comp = DataTypes.integers(c)
            comp = sum(pre_comp)

            a = [x.att for x in list]
            pre_att = DataTypes.integers(a)
            att = sum(pre_att)

            if att == 0:
                pct = 0
            else:
                pct = round(((comp/att) * 100), 1)

            if games == 0:
                att_g = 0
            else:
                att_g = round((att/games), 1)

            y = [x.yards for x in list]
            pre_yds = DataTypes.integers(y)
            yds = sum(pre_yds)

            avg = round((yds/att), 1)

            if games == 0:
                yds_g = 0
            else:
                yds_g = round((yds/games), 1)

            td = [x.td for x in list]
            pre_tds = DataTypes.integers(td)
            tds = sum(pre_tds)

            i = [x.ints for x in list]
            pre_ints = DataTypes.integers(i)
            ints = sum(pre_ints)

            l = [x.lng for x in list]
            lng = StatOrder.lng(l)
            if lng == None:
                lng = "--"

            tp = [x.comp_twenty_plus for x in list]
            pre_t_plus = DataTypes.integers(tp)
            t_plus = sum(pre_t_plus)

            fp = [x.comp_forty_plus for x in list]
            pre_f_plus = DataTypes.integers(fp)
            f_plus = sum(pre_f_plus)

            s = [x.sck for x in list]
            pre_sck = DataTypes.integers(s)
            sck = sum(pre_sck)

            if att == 0:
                rate = 0.0
            else:
                x = ((comp/att) - .3) * 5
                xx = ((yds/att) - 3) * .25
                xxx = (tds/att) * 20
                xxxx = 2.375 - ((ints/att) * 25)
                rate = round((((x + xx + xxx + xxxx)/6) * 100), 1)

            career = [games, comp, att, pct, att_g, yds, avg, yds_g, tds, ints, lng, t_plus, f_plus, sck, rate]

            return career

    @classmethod
    def career_rushing(cls, list):

        g = [x.games for x in list]
        if len(g) == 0:
            return ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]

        else:
            pre_games = DataTypes.integers(g)
            games = sum(pre_games)

            a = [x.att for x in list]
            pre_att = DataTypes.integers(a)
            att = sum(pre_att)

            if games == 0:
                att_g = 0
            else:
                att_g = round((att/games), 1)

            y = [x.yards for x in list]
            pre_yds = DataTypes.integers(y)
            yds = sum(pre_yds)

            if att == 0:
                avg = 0
            else:
                avg = round((yds/att), 1)

            if games == 0:
                yds_g = 0
            else:
                yds_g = round((yds/games), 1)

            td = [x.td for x in list]
            pre_tds = DataTypes.integers(td)
            tds = sum(pre_tds)

            l = [x.lng for x in list]
            lng = StatOrder.lng(l)
            if lng == None:
                lng = "--"

            fd = [x.fd for x in list]
            pre_fds = DataTypes.integers(fd)
            fds = sum(pre_fds)

            tp = [x.rush_twenty_plus for x in list]
            pre_t_plus = DataTypes.integers(tp)
            t_plus = sum(pre_t_plus)

            fp = [x.rush_forty_plus for x in list]
            pre_f_plus = DataTypes.integers(fp)
            f_plus = sum(pre_f_plus)

            fum = [x.fum for x in list]
            pre_fums = DataTypes.integers(fum)
            fums = sum(pre_fums)

            career = [games, att, att_g, yds, avg, yds_g, tds, lng, fds, t_plus, f_plus, fums]

            return career

    @classmethod
    def career_receiving(cls, list):

        g = [x.games for x in list]

        if len(g) == 0:
            return ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]

        else:
            pre_games = DataTypes.integers(g)
            games = sum(pre_games)

            r = [x.rec for x in list]
            pre_recs = DataTypes.integers(r)
            recs = sum(pre_recs)

            y = [x.yards for x in list]
            pre_yds = DataTypes.integers(y)
            yds = sum(pre_yds)

            if recs == 0:
                avg = 0
            else:
                avg = round((yds/recs), 1)

            if games == 0:
                yds_g = 0
            else:
                yds_g = round((yds/games), 1)

            td = [x.td for x in list]
            pre_tds = DataTypes.integers(td)
            tds = sum(pre_tds)

            l = [x.lng for x in list]
            lng = StatOrder.lng(l)
            if lng == None:
                lng = "--"

            fd = [x.fd for x in list]
            pre_fds = DataTypes.integers(fd)
            fds = sum(pre_fds)

            tp = [x.rec_twenty_plus for x in list]
            pre_t_plus = DataTypes.integers(tp)
            t_plus = sum(pre_t_plus)

            fp = [x.rec_forty_plus for x in list]
            pre_f_plus = DataTypes.integers(fp)
            f_plus = sum(pre_f_plus)

            fum = [x.fum for x in list]
            pre_fums = DataTypes.integers(fum)
            fums = sum(pre_fums)

            career = [games, recs, yds, avg, yds_g, tds, lng, fds, t_plus, f_plus, fums]

            return career

    @classmethod
    def career_defense(cls, list):

        g = [x.games for x in list]

        if len(g) == 0:
            return ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]

        else:
            pre_games = DataTypes.integers(g)
            games = sum(pre_games)

            tt = [x.total_tkl for x in list]
            pre_tot = DataTypes.integers(tt)
            tot = sum(pre_tot)

            so = [x.solo_tkl for x in list]
            pre_solo = DataTypes.integers(so)
            solo = sum(pre_solo)

            a = [x.assisted_tkl for x in list]
            pre_ass = DataTypes.integers(a)
            ass = sum(pre_ass)

            s = [x.sck for x in list]
            pre_sck = DataTypes.floats(s)
            sck = sum(pre_sck)

            s = [x.safties for x in list]
            pre_saf = DataTypes.integers(s)
            saf = sum(pre_saf)

            pd = [x.pass_def for x in list]
            pre_passd = DataTypes.integers(pd)
            passd = sum(pre_passd)

            i = [x.ints for x in list]
            pre_ints = DataTypes.integers(i)
            ints = sum(pre_ints)

            itd = [x.int_td for x in list]
            pre_int_td = DataTypes.integers(itd)
            int_td = sum(pre_int_td)

            ity = [x.int_yards for x in list]
            pre_int_yds = DataTypes.integers(ity)
            int_yds = sum(pre_int_yds)

            l = [x.lng_int_return for x in list]
            lng = StatOrder.lng(l)
            if lng == None:
                lng = "--"

            career = [games, tot, solo, ass, sck, saf, passd, ints, int_td, int_yds, lng]

            return career


    @classmethod
    def career_kicking(cls, list):

        g = [x.games for x in list]

        if len(g) == 0:
            return ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]

        else:
            pre_games = DataTypes.integers(g)
            games = sum(pre_games)

            fg = [x.fg for x in list]
            pre_fgs = DataTypes.integers(fg)
            fgs = sum(pre_fgs)

            a = [x.fg_att for x in list]
            pre_att = DataTypes.integers(a)
            att = sum(pre_att)

            if att == 0:
                pct = 0
            else:
                pct = round(((fgs/att) * 100), 1)

            b = [x.kb for x in list]
            pre_kb = DataTypes.integers(b)
            kb = sum(pre_kb)

            l = [x.lng for x in list]
            lng = StatOrder.lng(l)
            if lng == None:
                lng = "--"

            fgtw = [x.fg_twenty for x in list]
            pre_fg_twenty = DataTypes.integers(fgtw)
            fg_twenty = sum(pre_fg_twenty)

            fgtwa = [x.fg_twenty_att for x in list]
            pre_fgtw_att = DataTypes.integers(fgtwa)
            fgtw_att = sum(pre_fgtw_att)

            if fgtw_att == 0:
                fgtw_pct = 0
            else:
                fgtw_pct = round(((fg_twenty/fgtw_att) * 100), 1)

            fgth = [x.fg_thirty for x in list]
            pre_fg_thirty = DataTypes.integers(fgth)
            fg_thirty = sum(pre_fg_thirty)

            fgtha = [x.fg_thirty_att for x in list]
            pre_fgth_att = DataTypes.integers(fgtha)
            fgth_att = sum(pre_fgth_att)

            if fgth_att == 0:
                fgth_pct = 0
            else:
                fgth_pct = round(((fg_thirty/fgth_att) * 100), 1)

            fgfo = [x.fg_forty for x in list]
            pre_fg_forty = DataTypes.integers(fgfo)
            fg_forty = sum(pre_fg_forty)

            fgfoa = [x.fg_forty_att for x in list]
            pre_fgfo_att = DataTypes.integers(fgfoa)
            fgfo_att = sum(pre_fgfo_att)

            if fgfo_att == 0:
                fgfo_pct = 0
            else:
                fgfo_pct = round(((fg_forty/fgfo_att) * 100), 1)

            fgfi = [x.fg_fifty for x in list]
            pre_fg_fifty = DataTypes.integers(fgfi)
            fg_fifty = sum(pre_fg_fifty)

            fgfia = [x.fg_fifty_att for x in list]
            pre_fgfi_att = DataTypes.integers(fgfia)
            fgfi_att = sum(pre_fgfi_att)

            if fgfi_att == 0:
                fgfi_pct = 0
            else:
                fgfi_pct = round(((fg_fifty/fgfi_att) * 100), 1)

            e = [x.ex for x in list]
            pre_ex = DataTypes.integers(e)
            ex = sum(pre_ex)

            ea = [x.ex_att for x in list]
            pre_ex_att = DataTypes.integers(ea)
            ex_att = sum(pre_ex_att)

            if ex_att == 0:
                ex_pct = 0
            else:
                ex_pct = round(((ex/ex_att) * 100), 1)

            eb = [x.ex_b for x in list]
            pre_ex_b = DataTypes.integers(eb)
            ex_b = sum(pre_ex_b)

            career = [games, fgs, att, pct, kb, lng, fg_twenty, fgtw_att, fgtw_pct, fg_thirty, fgth_att, fgth_pct, fg_forty, fgfo_att, fgfo_pct, fg_fifty, fgfi_att, fgfi_pct, ex, ex_att, ex_pct, ex_b]

            return career

    @classmethod
    def career_punting(cls, list):

        g = [x.games for x in list]
        if len(g) == 0:
            return ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]

        else:
            pre_games = DataTypes.integers(g)
            games = sum(pre_games)

            p = [x.punts for x in list]
            pre_punts = DataTypes.integers(p)
            punts = sum(pre_punts)

            py = [x.p_yards for x in list]
            pre_yds = DataTypes.integers(py)
            yds = sum(pre_yds)

            l = [x.lng for x in list]
            lng = StatOrder.lng(l)
            if lng == None:
                lng = "--"

            if punts == 0:
                avg = 0
            else:
                avg = round((yds/punts), 1)

            b = [x.pb for x in list]
            pre_pb = DataTypes.integers(b)
            pb = sum(pre_pb)

            obp = [x.obp for x in list]
            pre_oob = DataTypes.integers(obp)
            oob = sum(pre_oob)

            dp = [x.dp for x in list]
            pre_dps = DataTypes.integers(dp)
            dps = sum(pre_dps)

            ptw = [x.p_twenty for x in list]
            pre_p_twenty = DataTypes.integers(ptw)
            p_twenty = sum(pre_p_twenty)

            tb = [x.tb for x in list]
            pre_tbs = DataTypes.integers(tb)
            tbs = sum(pre_tbs)

            fc = [x.fc for x in list]
            pre_fcs = DataTypes.integers(fc)
            fcs = sum(pre_fcs)

            ret = [x.p_ret for x in list]
            pre_p_ret = DataTypes.integers(ret)
            p_ret = sum(pre_p_ret)

            rety = [x.p_ret_yards for x in list]
            pre_retyds = DataTypes.integers(rety)
            retyds = sum(pre_retyds)

            rtd = [x.p_ret_td for x in list]
            pre_rettd = DataTypes.integers(rtd)
            rettd = sum(pre_rettd)

            career = [games, punts, yds, lng, avg, pb, oob, dps, p_twenty, tbs, fcs, p_ret, retyds, rettd]

            return career

    @classmethod
    def career_kr(cls, list):

        g = [x.games for x in list]

        if len(g) == 0:
            return ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]

        else:
            pre_games = DataTypes.integers(g)
            games = sum(pre_games)

            k = [x.kr for x in list]
            pre_kr = DataTypes.integers(k)
            kr = sum(pre_kr)

            y = [x.kr_yards for x in list]
            pre_yds = DataTypes.integers(y)
            yds = sum(pre_yds)

            if kr == 0:
                avg = 0
            else:
                avg = round((yds/kr), 1)

            l = [x.lng for x in list]
            lng = StatOrder.lng(l)
            if lng == None:
                lng = "--"

            td = [x.td for x in list]
            pre_tds = DataTypes.integers(td)
            tds = sum(pre_tds)

            krtw = [x.kr_twenty_plus for x in list]
            pre_kr_twenty = DataTypes.integers(krtw)
            kr_twenty = sum(pre_kr_twenty)

            krfo = [x.kr_forty_plus for x in list]
            pre_kr_forty = DataTypes.integers(krfo)
            kr_forty = sum(pre_kr_forty)

            fc = [x.fc for x in list]
            pre_fcs = DataTypes.integers(fc)
            fcs = sum(pre_fcs)

            fum = [x.fum for x in list]
            pre_fums = DataTypes.integers(fum)
            fums = sum(pre_fums)

            career = [games, kr, yds, avg, lng, tds, kr_twenty, kr_forty, fcs, fums]

            return career

    @classmethod
    def career_pr(cls, list):

        g = [x.games for x in list]

        if len(g) == 0:
            return ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]

        else:
            pre_games = DataTypes.integers(g)
            games = sum(pre_games)

            p = [x.pr for x in list]
            pre_pr = DataTypes.integers(p)
            pr = sum(pre_pr)

            y = [x.pr_yards for x in list]
            pre_yds = DataTypes.integers(y)
            yds = sum(pre_yds)

            if pr == 0:
                avg = 0
            else:
                avg = round((yds/pr), 1)

            l = [x.lng for x in list]
            lng = StatOrder.lng(l)
            if lng == None:
                lng = "--"

            td = [x.td for x in list]
            pre_tds = DataTypes.integers(td)
            tds = sum(pre_tds)

            prtw = [x.pr_twenty_plus for x in list]
            pre_pr_twenty = DataTypes.integers(prtw)
            pr_twenty = sum(pre_pr_twenty)

            prfo = [x.pr_forty_plus for x in list]
            pre_pr_forty = DataTypes.integers(prfo)
            pr_forty = sum(pre_pr_forty)

            fc = [x.fc for x in list]
            pre_fcs = DataTypes.integers(fc)
            fcs = sum(pre_fcs)

            fum = [x.fum for x in list]
            pre_fums = DataTypes.integers(fum)
            fums = sum(pre_fums)

            career = [games, pr, yds, avg, lng, tds, pr_twenty, pr_forty, fcs, fums]

            return career

    @classmethod
    def zero(cls, variable):
        if variable == "--":
            return 0
        else:
            return variable

    @classmethod
    def career_box(cls, pass_att, rush_att, recs, tackles, sacks, ints, kicks, punts, kr, pr):
        if pass_att > rush_att and pass_att > recs and pass_att > tackles and pass_att > sacks and pass_att > ints and pass_att > kicks and pass_att > punts and pass_att > kr and pass_att > pr:
            return "passer"
        elif rush_att > pass_att and rush_att > recs and rush_att > tackles and rush_att > sacks and rush_att > ints and rush_att > kicks and rush_att > punts and rush_att > kr and rush_att > pr:
            return "rusher"
        elif recs > pass_att and recs > rush_att and recs > tackles and recs > sacks and recs > ints and recs > kicks and recs > punts and recs > kr and recs > pr:
            return "receiver"
        elif tackles > pass_att and tackles > rush_att and tackles > recs and tackles > sacks and tackles > ints and tackles > kicks and tackles > punts and tackles > kr and tackles > pr:
            return "defender"
        elif sacks > pass_att and sacks > rush_att and sacks > recs and sacks > tackles and sacks > ints and sacks > kicks and sacks > punts and sacks > kr and sacks > pr:
            return "defender"
        elif ints > pass_att and ints > rush_att and ints > recs and ints > tackles and ints > sacks and ints > kicks and ints > punts and ints > kr and ints > pr:
            return "defender"
        elif kicks > pass_att and kicks > rush_att and kicks > recs and kicks > tackles and kicks > sacks and kicks > ints and kicks > punts and kicks > kr and kicks > pr:
            return "kicker"
        elif punts > pass_att and punts > rush_att and punts > recs and punts > tackles and punts > sacks and punts > ints and punts > kicks and punts > kr and punts > pr:
            return "punter"
        elif kr > pass_att and kr > rush_att and kr > recs and kr > tackles and kr > sacks and kr > ints and kr > kicks and kr > punts and kr > pr:
            return "kr"
        elif pr > pass_att and pr > rush_att and pr > rush_att and pr > recs and pr > tackles and pr > sacks and pr > ints and pr > kicks and pr > punts and pr > kr:
            return "pr"
        else:
            return "--"

    @classmethod
    def get_list(cls, x, list):
        list.clear()
        list.append(x)

    @classmethod
    def get_filter_id(cls, x):
        separate = x.partition("- ")
        id = separate[2]
        return id

    @classmethod
    def year_and_teams(cls, passer, rusher, receiver, defender, kicker, punter, p_returner, k_returner):
        final_list = []
        allyears = [x.year for x in passer] + [x.year for x in rusher] + [x.year for x in receiver] + [x.year for x in defender] + [x.year for x in kicker] + [x.year for x in punter] + [x.year for x in p_returner] + [x.year for x in k_returner]
        for i in passer:
            if i == None:
                pass
            for i in [x.team for x in passer] :
                if i == "--":
                    pass
                else:
                    teams = [x.team for x in passer]
        for i in rusher:
            if i == None:
                pass
            for i in [x.team for x in rusher] :
                if i == "--":
                    pass
                else:
                    teams = [x.team for x in rusher]
        for i in receiver:
            if i == None:
                pass
            for i in [x.team for x in receiver] :
                if i == "--":
                    pass
                else:
                    teams = [x.team for x in receiver]
        for i in defender:
            if i == None:
                pass
            for i in [x.team for x in defender] :
                if i == "--":
                    pass
                else:
                    teams = [x.team for x in defender]
        for i in kicker:
            if i == None:
                pass
            for i in [x.team for x in kicker] :
                if i == "--":
                    pass
                else:
                    teams = [x.team for x in kicker]
        for i in punter:
            if i == None:
                pass
            for i in [x.team for x in punter] :
                if i == "--":
                    pass
                else:
                    teams = [x.team for x in punter]
        for i in p_returner:
            if i == None:
                pass
            for i in [x.team for x in p_returner] :
                if i == "--":
                    pass
                else:
                    teams = [x.team for x in p_returner]
        for i in k_returner:
            if i == None:
                pass
            for i in [x.team for x in k_returner] :
                if i == "--":
                    pass
                else:
                    teams = [x.team for x in k_returner]
        str_years = PlayerSearch.no_duplicate(allyears)
        years = [int(x) for x in str_years]
        single_teams = PlayerSearch.no_duplicate(teams)
        final_list.append(years[-1])
        final_list.append(years[0])
        final_list.append(single_teams)
        return final_list


class PlayerSearch(object):

    @classmethod
    def get_filter_name(cls, x):
        separate = x.partition(" ")
        first = separate[0]
        last = separate[2]
        name = last + ", " + first
        print(name)
        return name

    @classmethod
    def search_results(cls, x, y):
        results = []
        for i in y:
            if x in i:
                results.append(i)
        return results

    @classmethod
    def paginator_list(cls, queries, list):
        for q in queries:
            list.append(q)

    @classmethod
    def no_duplicate(cls, used_list):
        new_list = []
        for i in used_list:
            if i in new_list:
                pass
            else:
                new_list.append(i)
        return new_list


class SeasonStats(object):

    '''These are the main functions for the Season Stats view'''

    @classmethod
    def yards(cls, active, retired):
        limit = []
        yards_list = [player.yards for player in active] + [player.yards for player in retired]
        int_list = StatOrder.greatest_least(yards_list)
        yards = StatOrder.add_commas(int_list)
        for x, y in enumerate(yards):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def yards_one(cls, status):
        limit = []
        yards_list = [player.yards for player in status]
        int_list = StatOrder.greatest_least(yards_list)
        yards = StatOrder.add_commas(int_list)
        for x, y in enumerate(yards):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def tackles(cls, active, retired):
        limit = []
        tackles_list = [player.total_tkl for player in active] + [player.total_tkl for player in retired]
        int_list = StatOrder.greatest_least(tackles_list)
        tackles = StatOrder.add_commas(int_list)
        for x, y in enumerate(tackles):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def tackles_one(cls, status):
        limit = []
        tackles_list = [player.total_tkl for player in status]
        int_list = StatOrder.greatest_least(tackles_list)
        tackles = StatOrder.add_commas(int_list)
        for x, y in enumerate(tackles):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def sacks(cls, active, retired):
        limit = []
        sacks_list = [player.sck for player in active] + [player.sck for player in retired]
        float_list = StatOrder.greatest_least_float(sacks_list)
        sacks = [str(x) for x in float_list]
        for x, y in enumerate(sacks):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def sacks_one(cls, status):
        limit = []
        sacks_list = [player.sck for player in status]
        float_list = StatOrder.greatest_least_float(sacks_list)
        sacks = [str(x) for x in float_list]
        for x, y in enumerate(sacks):
            if x == 150:
                break
            else:
                limit.append(y)
        print(limit)
        return limit

    @classmethod
    def ints(cls, active, retired):
        limit = []
        ints_list = [player.ints for player in active] + [player.ints for player in retired]
        int_list = StatOrder.greatest_least(ints_list)
        ints = StatOrder.add_commas(int_list)
        for x, y in enumerate(ints):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def ints_one(cls, status):
        limit = []
        ints_list = [player.ints for player in status]
        int_list = StatOrder.greatest_least(ints_list)
        ints = StatOrder.add_commas(int_list)
        for x, y in enumerate(ints):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def fgs(cls, active, retired):
        limit = []
        fgs_list = [player.fg for player in active] + [player.fg for player in retired]
        int_list = StatOrder.greatest_least(fgs_list)
        fgs = StatOrder.add_commas(int_list)
        for x, y in enumerate(fgs):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def fgs_one(cls, status):
        limit = []
        fgs_list = [player.fg for player in status]
        int_list = StatOrder.greatest_least(fgs_list)
        fgs = StatOrder.add_commas(int_list)
        for x, y in enumerate(fgs):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def punts(cls, active, retired):
        limit = []
        punts_list = [player.punts for player in active] + [player.punts for player in retired]
        int_list = StatOrder.greatest_least(punts_list)
        punts = StatOrder.add_commas(int_list)
        for x, y in enumerate(punts):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def punts_one(cls, status):
        limit = []
        punts_list = [player.punts for player in status]
        int_list = StatOrder.greatest_least(punts_list)
        punts = StatOrder.add_commas(int_list)
        for x, y in enumerate(punts):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def krs(cls, active, retired):
        limit = []
        krs_list = [player.kr for player in active] + [player.kr for player in retired]
        int_list = StatOrder.greatest_least(krs_list)
        krs = StatOrder.add_commas(int_list)
        for x, y in enumerate(krs):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def krs_one(cls, status):
        limit = []
        krs_list = [player.kr for player in status]
        int_list = StatOrder.greatest_least(krs_list)
        krs = StatOrder.add_commas(int_list)
        for x, y in enumerate(krs):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def prs(cls, active, retired):
        limit = []
        prs_list = [player.pr for player in active] + [player.pr for player in retired]
        int_list = StatOrder.greatest_least(prs_list)
        prs = StatOrder.add_commas(int_list)
        for x, y in enumerate(prs):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def prs_one(cls, status):
        limit = []
        prs_list = [player.pr for player in status]
        int_list = StatOrder.greatest_least(prs_list)
        prs = StatOrder.add_commas(int_list)
        for x, y in enumerate(prs):
            if x == 150:
                break
            else:
                limit.append(y)
        return limit

    @classmethod
    def act_ret_order(cls, list, active, retired):
        if active.exists():
            list.append(active)
        if retired.exists():
            list.append(retired)

    @classmethod
    def limit(cls, list):
        new = []
        for x, y in enumerate(list):
            if x == 150:
                break
            else:
                new.append(y)
        return new
