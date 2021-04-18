import os

def getting_scoreboard():
    os.system('curl https://ctftime.org/team/61083 > score')

def get_rating_table():
    f = open('score','r')
    data = f.read()
    return data

def tabulation(data):
    a = data.partition('<tr><th colspan="2">Place</th><th>Event</th><th>CTF points</th><th>Rating points</th></tr>')[2].partition('</table>')[0].strip()
    arr = a.split("\n")
    del arr[1::2]
    del arr[0]
    rating = []
    for i in arr:
        b = i.split('<td>')
        rating.append((b[3].partition('</td>')[0]))
    rating = [ float(x) for x in rating ]
    return rating

def sorting(rating):
    print(rating)
    rating.sort(reverse=True)
    return rating

def total_rating(rating):
    sum = 0
    for i in range(10):
        sum += rating[i]
    print(sum)
    print(rating)
    print("lowest rating : " + str(rating[9]))

getting_scoreboard()
data = get_rating_table()
rating = tabulation(data)
rating = sorting(rating)
total_rating(rating)
