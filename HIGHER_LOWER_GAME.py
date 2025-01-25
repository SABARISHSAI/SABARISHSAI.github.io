import random
data = [
    {
        'name': 'Taylor Swift',
        'follower_count': 260000000,
        'description': 'Singer and songwriter',
        'country': 'USA'
    },
    {
        'name': 'BTS',
        'follower_count': 72000000,
        'description': 'K-pop group',
        'country': 'South Korea'
    },
    {
        'name': 'Drake',
        'follower_count': 130000000,
        'description': 'Rapper and singer',
        'country': 'Canada'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 380000000,
        'description': 'Singer and actress',
        'country': 'USA'
    },
    {
        'name': 'Ed Sheeran',
        'follower_count': 230000000,
        'description': 'Singer and songwriter',
        'country': 'UK'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 110000000,
        'description': 'Singer and songwriter',
        'country': 'USA'
    },
    {
        'name': 'The Weeknd',
        'follower_count': 290000000,
        'description': 'Singer and producer',
        'country': 'Canada'
    },
    {
        'name': 'Bad Bunny',
        'follower_count': 45000000,
        'description': 'Rapper and singer',
        'country': 'Puerto Rico'
    },
    {
        'name': 'Rihanna',
        'follower_count': 150000000,
        'description': 'Singer and entrepreneur',
        'country': 'Barbados'
    },
    {
        'name': 'Shakira',
        'follower_count': 88000000,
        'description': 'Singer and dancer',
        'country': 'Colombia'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 280000000,
        'description': 'Singer and songwriter',
        'country': 'Canada'
    },
    {
        'name': 'Dua Lipa',
        'follower_count': 110000000,
        'description': 'Singer and songwriter',
        'country': 'UK'
    },
    {
        'name': 'Kanye West',
        'follower_count': 120000000,
        'description': 'Rapper and producer',
        'country': 'USA'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 250000000,
        'description': 'Singer and actress',
        'country': 'USA'
    },
    {
        'name': 'Bruno Mars',
        'follower_count': 90000000,
        'description': 'Singer and songwriter',
        'country': 'USA'
    },
    {
        'name': 'Lady Gaga',
        'follower_count': 54000000,
        'description': 'Singer and actress',
        'country': 'USA'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 430000000,
        'description': 'Singer and actress',
        'country': 'USA'
    },
    {
        'name': 'Post Malone',
        'follower_count': 24000000,
        'description': 'Rapper and singer',
        'country': 'USA'
    },
    {
        'name': 'Harry Styles',
        'follower_count': 95000000,
        'description': 'Singer and actor',
        'country': 'UK'
    },
    {
        'name': 'Adele',
        'follower_count': 55000000,
        'description': 'Singer and songwriter',
        'country': 'UK'
    },
    {
        'name': 'Marshmello',
        'follower_count': 60000000,
        'description': 'DJ and producer',
        'country': 'USA'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 73000000,
        'description': 'Singer and songwriter',
        'country': 'Canada'
    }
]

score = 0
result = True
choice = ''
c=''
print(r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
""")
def versus(c, a):
    print(f"Compare A: {c['name']}, {c['description']}, from {c['country']}.")
    print(r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
""")
    print(f"against B: {a['name']}, {a['description']}, from {a['country']}.")


def game(c,a,choice):
    global score
    if choice=='A':
        if c['follower_count']>=a['follower_count']:
            score+=1
            return True,a

        else:
            print("you lost")
            print(f"sorry that's wrong, your final score is {score}")
            exit()
    if choice=='B':
        if c['follower_count']<=a['follower_count']:
            score+=1
            return True,a

        else:
            print("you lost")
            print(f"sorry that's wrong, your final score is {score}")
            exit()
while result:
    if score>0:
        print(f"your score is {score}")
    if score == 0:
        c = random.choice(data)
        a = random.choice(data)
    if score != 0:
        a = random.choice(data)
    versus(c, a)
    choice = input("Who has more followers? Type 'A' or 'B':").upper()
    result,c = game(c,a, choice)



