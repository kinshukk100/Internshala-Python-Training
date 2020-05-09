p1={'name':'Virat Kohli', 'role':'bat', 'runs':112, 'fours':10, 'sixes':0, 'balls':119, 'field':0}
p2={'name':'du Plessis', 'role':'bat', 'runs':120, 'fours':11, 'sixes':2, 'balls':112, 'field':0}
p3={'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10, 'runs':71, 'field':1}
p4={'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10, 'runs':45, 'field':0}
p5={'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0}
def batting(player):
    points=0
    sr=float(player['runs'])/float(player['balls'])*100
    points=player['runs']/2
    if player['runs']>=50:
        points=points+5
    if player['runs']>=100:
        points=points+10
    if sr>=80.0 and sr<=100.0:
        points=points+2
    if sr>100:
        points=points+4
    if player['fours']!=0:
        points+=player['fours']*1
    if player['sixes']!=0:
        points+=player['sixes']*2
    if player['field']!=0:
        points+=player['field']*10
    return(int(points))

def bowling(player):
    points=0
    economy=float(player['runs'])/float(player['overs'])
    points=10*player['wkts']
    if player['wkts']>=3:
        points=points+5
    if player['wkts']>=5:
        points=points+10
    if economy>=3.5 and economy<=4.5:
        points=points+4
    if economy>=2 and economy<=3.5:
        points=points+7
    if economy<2:
        points=points+10
    if player['field']!=0:
        points+=player['field']*10
    return(int(points))

print({'name' : p1['name'],'batscore' : batting(p1)})
print({'name' : p2['name'],'batscore' : batting(p2)})
print({'name' : p3['name'],'ballscore' : bowling(p3)})
print({'name' : p4['name'],'ballscore' : bowling(p4)})
print({'name' : p5['name'],'ballscore' : bowling(p5)})
