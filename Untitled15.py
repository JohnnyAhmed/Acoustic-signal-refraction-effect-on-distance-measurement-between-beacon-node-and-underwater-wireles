#!/usr/bin/env python
# coding: utf-8

# In[1]:


t = {1:{10:{'a':10,'b':0,'x':0,'y':0,'z':0},20:{'a':20,'b':0,'x':0,'y':0,'z':0},30:{'a':30,'b':0,'x':0,'y':0,'z':0},40:{'a':40,'b':0,'x':0,'y':0,'z':0},50:{'a':50,'b':0,'x':0,'y':0,'z':0},60:{'a':60,'b':0,'x':0,'y':0,'z':0},70:{'a':70,'b':0,'x':0,'y':0,'z':0},'v':1546.1622,'d':2},
    2:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1536.3079,'d':100},
    3:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1530.3342,'d':200},
    4:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1521.2348,'d':300},
    5:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1509.5544,'d':400},
    6:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1497.5221,'d':500},
    7:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1491.1764,'d':600},
    8:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1486.0158,'d':700},
    9:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1484.6853,'d':800},
    10:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1483.2047,'d':900},
    11:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1483.0194,'d':1000},
    12:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1482.6096,'d':1100},
    13:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1482.4469,'d':1200},
    14:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1482.2493,'d':1300},
    15:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1483.3026,'d':1400},
    16:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1484.3744,'d':1500},
    17:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1485.6474,'d':1600},
    18:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1486.9140,'d':1700},
    19:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1488.0478,'d':1800},
    20:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1489.2183,'d':1900},
    21:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1490.4170,'d':2000},
    22:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1491.7980,'d':2100},
    23:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1493.4941,'d':2200},
    24:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1495.0129,'d':2300},
    25:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1496.6315,'d':2400},
    26:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1498.1654,'d':2500},
    27:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1499.8256,'d':2600},
    28:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1501.3305,'d':2700},
    29:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1502.9442,'d':2800},
    30:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1504.5347,'d':2900},
    31:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1506.1547,'d':3000},
    32:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1507.8220,'d':3100},
    33:{10:{'a':0,'b':0,'x':0,'y':0,'z':0},20:{'a':0,'b':0,'x':0,'y':0,'z':0},30:{'a':0,'b':0,'x':0,'y':0,'z':0},40:{'a':0,'b':0,'x':0,'y':0,'z':0},50:{'a':0,'b':0,'x':0,'y':0,'z':0},60:{'a':0,'b':0,'x':0,'y':0,'z':0},70:{'a':0,'b':0,'x':0,'y':0,'z':0},'v':1509.5145,'d':3200}}


# In[2]:


import math
for i in t:
    if(i>1):
        t[i][10]['a']=(math.asin((t[i]['v'])*(math.sin((t[i-1][10]['a'])*math.pi/180))/(t[i-1]['v'])))*180/math.pi
        t[i][20]['a']=(math.asin((t[i]['v'])*(math.sin((t[i-1][20]['a'])*math.pi/180))/(t[i-1]['v'])))*180/math.pi
        t[i][30]['a']=(math.asin((t[i]['v'])*(math.sin((t[i-1][30]['a'])*math.pi/180))/(t[i-1]['v'])))*180/math.pi
        t[i][40]['a']=(math.asin((t[i]['v'])*(math.sin((t[i-1][40]['a'])*math.pi/180))/(t[i-1]['v'])))*180/math.pi
        t[i][50]['a']=(math.asin((t[i]['v'])*(math.sin((t[i-1][50]['a'])*math.pi/180))/(t[i-1]['v'])))*180/math.pi
        t[i][60]['a']=(math.asin((t[i]['v'])*(math.sin((t[i-1][60]['a'])*math.pi/180))/(t[i-1]['v'])))*180/math.pi
        t[i][70]['a']=(math.asin((t[i]['v'])*(math.sin((t[i-1][70]['a'])*math.pi/180))/(t[i-1]['v'])))*180/math.pi
        
for i in t:
    if(i==1):
        t[i][10]['x']=(t[i]['d'])/math.cos((t[i][10]['a'])*math.pi/180)
        t[i][10]['y']=t[i][10]['x']
        t[i][10]['b']=t[i][10]['x']
        t[i][10]['z']=t[i][10]['a']
        t[i][20]['x']=(t[i]['d'])/math.cos((t[i][20]['a'])*math.pi/180)
        t[i][20]['y']=t[i][20]['x']
        t[i][20]['b']=t[i][20]['x']
        t[i][20]['z']=t[i][20]['a']
        t[i][30]['x']=(t[i]['d'])/math.cos((t[i][30]['a'])*math.pi/180)
        t[i][30]['y']=t[i][30]['x']
        t[i][30]['b']=t[i][30]['x']
        t[i][30]['z']=t[i][30]['a']
        t[i][40]['x']=(t[i]['d'])/math.cos((t[i][40]['a'])*math.pi/180)
        t[i][40]['y']=t[i][40]['x']
        t[i][40]['b']=t[i][40]['x']
        t[i][40]['z']=t[i][40]['a']
        t[i][50]['x']=(t[i]['d'])/math.cos((t[i][50]['a'])*math.pi/180)
        t[i][50]['y']=t[i][50]['x']
        t[i][50]['b']=t[i][50]['x']
        t[i][50]['z']=t[i][50]['a']
        t[i][60]['x']=(t[i]['d'])/math.cos((t[i][60]['a'])*math.pi/180)
        t[i][60]['y']=t[i][60]['x']
        t[i][60]['b']=t[i][60]['x']
        t[i][60]['z']=t[i][60]['a']
        t[i][70]['x']=(t[i]['d'])/math.cos((t[i][70]['a'])*math.pi/180)
        t[i][70]['y']=t[i][70]['x']
        t[i][70]['b']=t[i][70]['x']
        t[i][70]['z']=t[i][70]['a']
    elif(i>1):
        t[i][10]['x']=((t[i]['d'])-((t[i-1]['d'])))/math.cos((t[i][10]['a'])*math.pi/180)
        
        t[i][10]['y']=math.sqrt(((t[i][10]['x'])**2)+((t[i-1][10]['y'])**2)-(2*(t[i][10]['x'])*(t[i-1][10]['y'])*(math.cos((90-(t[i-1][10]['z'])+90+(t[i][10]['a']))*math.pi/180))))
        t[i][10]['z']=(math.acos((((t[i][10]['x'])**2)+((t[i][10]['y'])**2)-((t[i-1][10]['y'])**2))/(2*(t[i][10]['x'])*(t[i][10]['y'])))*math.pi/180)+t[i][10]['a']
        t[i][10]['b']=t[i][10]['x']+t[i-1][10]['b']
        t[i][20]['x']=((t[i]['d'])-((t[i-1]['d'])))/math.cos((t[i][20]['a'])*math.pi/180)
        
        t[i][20]['y']=math.sqrt(((t[i][20]['x'])**2)+((t[i-1][20]['y'])**2)-(2*(t[i][20]['x'])*(t[i-1][20]['y'])*(math.cos((90-(t[i-1][20]['z'])+90+(t[i][20]['a']))*math.pi/180))))
        t[i][20]['z']=(math.acos((((t[i][20]['x'])**2)+((t[i][20]['y'])**2)-((t[i-1][20]['y'])**2))/(2*(t[i][20]['x'])*(t[i][20]['y'])))*math.pi/180)+t[i][20]['a']
        t[i][20]['b']=t[i][20]['x']+t[i-1][20]['b']
        t[i][30]['x']=((t[i]['d'])-((t[i-1]['d'])))/math.cos((t[i][30]['a'])*math.pi/180)
        
        t[i][30]['y']=math.sqrt(((t[i][30]['x'])**2)+((t[i-1][30]['y'])**2)-(2*(t[i][30]['x'])*(t[i-1][30]['y'])*(math.cos((90-(t[i-1][30]['z'])+90+(t[i][30]['a']))*math.pi/180))))
        t[i][30]['z']=(math.acos((((t[i][30]['x'])**2)+((t[i][30]['y'])**2)-((t[i-1][30]['y'])**2))/(2*(t[i][30]['x'])*(t[i][30]['y'])))*math.pi/180)+t[i][30]['a']
        t[i][30]['b']=t[i][30]['x']+t[i-1][30]['b']
        t[i][40]['x']=((t[i]['d'])-((t[i-1]['d'])))/math.cos((t[i][40]['a'])*math.pi/180)
        
        t[i][40]['y']=math.sqrt(((t[i][40]['x'])**2)+((t[i-1][40]['y'])**2)-(2*(t[i][40]['x'])*(t[i-1][40]['y'])*(math.cos((90-(t[i-1][40]['z'])+90+(t[i][40]['a']))*math.pi/180))))
        t[i][40]['z']=(math.acos((((t[i][40]['x'])**2)+((t[i][40]['y'])**2)-((t[i-1][40]['y'])**2))/(2*(t[i][40]['x'])*(t[i][40]['y'])))*math.pi/180)+t[i][40]['a']
        t[i][40]['b']=t[i][40]['x']+t[i-1][40]['b']
        t[i][50]['x']=((t[i]['d'])-((t[i-1]['d'])))/math.cos((t[i][50]['a'])*math.pi/180)
        
        t[i][50]['y']=math.sqrt(((t[i][50]['x'])**2)+((t[i-1][50]['y'])**2)-(2*(t[i][50]['x'])*(t[i-1][50]['y'])*(math.cos((90-(t[i-1][50]['z'])+90+(t[i][50]['a']))*math.pi/180))))
        t[i][50]['z']=(math.acos((((t[i][50]['x'])**2)+((t[i][50]['y'])**2)-((t[i-1][50]['y'])**2))/(2*(t[i][50]['x'])*(t[i][50]['y'])))*math.pi/180)+t[i][50]['a']
        t[i][50]['b']=t[i][50]['x']+t[i-1][50]['b']
        t[i][60]['x']=((t[i]['d'])-((t[i-1]['d'])))/math.cos((t[i][60]['a'])*math.pi/180)
        
        t[i][60]['y']=math.sqrt(((t[i][60]['x'])**2)+((t[i-1][60]['y'])**2)-(2*(t[i][60]['x'])*(t[i-1][60]['y'])*(math.cos((90-(t[i-1][60]['z'])+90+(t[i][60]['a']))*math.pi/180))))
        t[i][60]['z']=(math.acos((((t[i][60]['x'])**2)+((t[i][60]['y'])**2)-((t[i-1][60]['y'])**2))/(2*(t[i][60]['x'])*(t[i][60]['y'])))*math.pi/180)+t[i][60]['a']
        t[i][60]['b']=t[i][60]['x']+t[i-1][60]['b']
        t[i][70]['x']=((t[i]['d'])-((t[i-1]['d'])))/math.cos((t[i][70]['a'])*math.pi/180)
        
        t[i][70]['y']=math.sqrt(((t[i][70]['x'])**2)+((t[i-1][70]['y'])**2)-(2*(t[i][70]['x'])*(t[i-1][70]['y'])*(math.cos((90-(t[i-1][70]['z'])+90+(t[i][70]['a']))*math.pi/180))))
        t[i][70]['z']=(math.acos((((t[i][70]['x'])**2)+((t[i][70]['y'])**2)-((t[i-1][70]['y'])**2))/(2*(t[i][70]['x'])*(t[i][70]['y'])))*math.pi/180)+t[i][70]['a']
        t[i][70]['b']=t[i][70]['x']+t[i-1][70]['b']


# In[3]:


print(t)


# In[4]:


q={1:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     2:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     3:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     4:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     5:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     6:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     7:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     8:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     9:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     10:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     11:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     12:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     13:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     14:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     15:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     16:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     17:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     18:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     19:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     20:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     21:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     22:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     23:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     24:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     25:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     26:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     27:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     28:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     29:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     30:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     31:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}},
     32:{10:{'a':0,'b':0,'c':0,'d':0},20:{'a':0,'b':0,'c':0,'d':0},30:{'a':0,'b':0,'c':0,'d':0},40:{'a':0,'b':0,'c':0,'d':0},50:{'a':0,'b':0,'c':0,'d':0},60:{'a':0,'b':0,'c':0,'d':0},70:{'a':0,'b':0,'c':0,'d':0}}}

for i in t:
    if(i>1):   
        q[i-1][10]['a']=t[i][10]['b']*1000
        q[i-1][10]['b']=t[i][10]['y']*1000
        q[i-1][10]['c']=(t[i][10]['b']-t[i][10]['y'])*1000
        q[i-1][10]['d']=((t[i][10]['b']-t[i][10]['y'])*1000)/(t[i][10]['y']*1000)*100
        q[i-1][20]['a']=t[i][20]['b']*1000
        q[i-1][20]['b']=t[i][20]['y']*1000
        q[i-1][20]['c']=(t[i][20]['b']-t[i][20]['y'])*1000
        q[i-1][20]['d']=((t[i][20]['b']-t[i][20]['y'])*1000)/(t[i][20]['y']*1000)*100
        q[i-1][30]['a']=t[i][30]['b']*1000
        q[i-1][30]['b']=t[i][30]['y']*1000
        q[i-1][30]['c']=(t[i][30]['b']-t[i][30]['y'])*1000
        q[i-1][30]['d']=((t[i][30]['b']-t[i][30]['y'])*1000)/(t[i][30]['y']*1000)*100
        q[i-1][40]['a']=t[i][40]['b']*1000
        q[i-1][40]['b']=t[i][40]['y']*1000
        q[i-1][40]['c']=(t[i][40]['b']-t[i][40]['y'])*1000
        q[i-1][40]['d']=((t[i][40]['b']-t[i][40]['y'])*1000)/(t[i][40]['y']*1000)*100
        q[i-1][50]['a']=t[i][50]['b']*1000
        q[i-1][50]['b']=t[i][50]['y']*1000
        q[i-1][50]['c']=(t[i][50]['b']-t[i][50]['y'])*1000
        q[i-1][50]['d']=((t[i][50]['b']-t[i][50]['y'])*1000)/(t[i][50]['y']*1000)*100
        q[i-1][60]['a']=t[i][60]['b']*1000
        q[i-1][60]['b']=t[i][60]['y']*1000
        q[i-1][60]['c']=(t[i][60]['b']-t[i][60]['y'])*1000
        q[i-1][60]['d']=((t[i][60]['b']-t[i][60]['y'])*1000)/(t[i][60]['y']*1000)*100
        q[i-1][70]['a']=t[i][70]['b']*1000
        q[i-1][70]['b']=t[i][70]['y']*1000
        q[i-1][70]['c']=(t[i][70]['b']-t[i][70]['y'])*1000
        q[i-1][70]['d']=((t[i][70]['b']-t[i][70]['y'])*1000)/(t[i][70]['y']*1000)*100


# In[5]:


print(q)


# In[ ]:




