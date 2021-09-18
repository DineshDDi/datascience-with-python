"""
import pandas as pd

XYZ_web = {'Days':[1,2,3,4,5,6], 'Visitors':[100,150,90,100,75,89], 'Bounce':[3,6,7,9,2,1]}

e = pd.DataFrame(XYZ_web)

print(e)

#slicing
print(e.head(2))
print(e.tail(2))
"""


"""
#merge the dataframe
import pandas as pd

dlf = pd.DataFrame({'team':['RR','DC','CSK','CSK'],'keyplayers':['yusaf','gilchist','dhoni','raina'],'avg':[7,8,9,10]},
                   index = [2008,2009,2010,2011])

pepsi = pd.DataFrame({'team':['KKR','MI','KKR','MI'],'keyplayers':['kalis','pollard','gowtham','rohit'],'avg':[7,8,9,10]},
                   index = [2012,2013,2014,2015])


merge = pd.merge(dlf,pepsi, on='avg')

print(merge)
"""


"""
#join the 2 dataframe
import pandas as pd

dlf = pd.DataFrame({'keyplayers':['yusaf','gilchist','dhoni','raina'],'team':['RR','DC','CSK','CSK']},
                   index = [2008,2009,2010,2011])

dlf1 = pd.DataFrame({'avg':[22.6,24.9,44.8,40.6],'HS':[101,90,78,100]},
                    index = [2008,2009,2010,2011])

joining = dlf.join(dlf1)

print(joining)
"""


'''
#replace the index value to userdefined value
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

a = pd.DataFrame({'Day':[1,2,3,4],'visitors':[200,100,150,250],'bounces':[9,5,7,12]})

a.set_index('Day', inplace=True)

#show the replace index in Day
print(a)

#show the DataFrame in graph format
a.plot()
plt.show()
'''


"""
#change the coloum heading
import pandas as pd

a = pd.DataFrame({'Day':[1,2,3,4],'visitors':[200,100,150,250],'bounces':[9,5,7,12]})

d = a.rename(columns={'visitors': 'users'})

print(d)
"""


#concatenation

"""
import pandas as pd

dlf = pd.DataFrame({'team':['RR','DC','CSK','CSK'],'keyplayers':['yusaf','gilchist','dhoni','raina'],'avg':[7,8,9,10]},
                   index = [2008,2009,2010,2011])

pepsi = pd.DataFrame({'team':['KKR','MI','KKR','MI'],'keyplayers':['kalis','pollard','gowtham','rohit'],'avg':[7,8,9,10]},
                   index = [2012,2013,2014,2015])

a = pd.concat([dlf,pepsi])

print(a)

"""


"""
#change xlsx, csv file to html file
import pandas as pd

a = pd.read_excel('PlayStoreData.xlsx')

a.to_html('psd.html')
"""


'''
#different between 2 datas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
#import seaborn as sns

style.use('fivethirtyeight')

bt = pd.read_csv("Top_100_batsman.csv",index_col=0)

df = bt.head(10)

df = df.set_index(["PLAYER"])

rn = df.reindex(columns=['Inns','Mat'])

#print(rn)

#df = df.set_index(["PLAYER"])
#plt.figure(figsize=(20,32))

#sns.countplot(y=best.PLAYER,palette="Paired")

#plt.show()

db = rn.diff(axis=1)

db.plot(kind='bar')
plt.show()
'''

"""
import pandas as pd

a = pd.read_csv("Top_100_batsman.csv")

print(a.head(10))
"""


'''
import pandas as pd
a = {'employee': {'karan': {'id': '032','salary': 25000, 'designation': 'ML'},
                  'naresh': {'id': '142','salary': 27000, 'designation': 'AI'}}}

df = pd.DataFrame(a['employee'])

print(df)
'''




