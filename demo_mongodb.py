# imports
import pymongo

# connection
myclient = pymongo.MongoClient('mongodb+srv://kaix1134:<password>@cluster0.dedts.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# create connection
mydb = myclient['mydatabase']
mycol = mydb['customers']

# create new documents
#mycol.insert_one({'id': 101, 'companyname': 'KEA', 'contact': 'Tue Hellstern'})
#mycol.insert_one({'id': 102, 'companyname': 'ITU', 'contact': 'Peter Jensen'})
#mycol.insert_one({'id': 103, 'companyname': 'CPH Business', 'contact': 'Ole Hansen'})
#mycol.insert_one({'id': 104, 'companyname': 'DTU', 'contact': 'Ole Rasmussen', 'country': 'DEN'})

# delete database and collections
#mycol.drop()

# find/show/print
# find all
#for x in mycol.find({}, {'id' : 0, 'companyname': 0}):
#    print(x)

# update one collection
myquery = {'companyname' : 'DTU', 'contact': 'Tue Hellstern'}
newvalues = {'$set': {'companyname': 'KEA'}}
mycol.update_one(myquery, newvalues)