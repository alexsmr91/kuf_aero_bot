"""
'S7-1080':
['05:20', '07.03.2022', 'S7 Airlines', 'Москва', 'DME', 'Вылетел',
'05:28', '07.03.2022', ['LY-8930', 'AT-9014', 'B2-180', 'KC-1438', 'A3-3540']],
"""


class Flights:

    def __init__(self, *args, **kwargs):
        self.aw_time, self.aw_date, self.airlines, self.dest_city, self.dest_airport, self.status, self.rl_time, self.rl_date, self.combi_flights = args

    def __eq__(self, other):
        return self.aw_time == other.aw_time and self.aw_date == other.aw_date and self.airlines == other.airlines and self.dest_city == other.dest_city and self.dest_airport == other.dest_airport and self.status == other.status and self.rl_time == other.rl_time and self.rl_date == other.rl_date and self.combi_flights == other.combi_flights

    def difference(self, other):
        res = ''
        if self.aw_time != other.aw_time:
            res = f'{res}at+'
        if self.aw_date != other.aw_date:
            res = f'{res}ad+'
        if self.airlines != other.airlines:
            res = f'{res}al+'
        if self.dest_city != other.dest_city:
            res = f'{res}dc+'
        if self.dest_airport != other.dest_airport:
            res = f'{res}da+'
        if self.status != other.status:
            res = f'{res}s+'
        if self.rl_time != other.rl_time:
            res = f'{res}rt+'
        if self.rl_date != other.rl_date:
            res = f'{res}rd+'
        if self.combi_flights != other.combi_flights:
            res = f'{res}cf+'
        return res.strip('+')

    def __repr__(self):
        if self.rl_time != self.aw_time:
            res = f'<s>{self.aw_time}</s>\n{self.rl_time}\n{self.dest_city}\n{self.status}\n'
        else:
            res = f'{self.rl_time}\n{self.dest_city}\n{self.status}\n'
        return res



if __name__ == '__main__':

    fl = Flights('05:20', '07.03.2022', 'S7 Airlines', 'Москва', 'DME', 'Вылетел', '05:28', '07.03.2022', ['LY-8930', 'AT-9014', 'B2-180', 'KC-1438', 'A3-3540'])
    fl2 = Flights('05:20', '07.03.2022', 'S7 Airlines', 'Москва', 'DME', 'Вылете', '05:25', '07.03.2022', ['LY-8930', 'AT-9014', 'B2-180', 'KC-1438', 'A3-3540'])
    print(fl.difference(fl2))