import pymongo



myclient = pymongo.MongoClient("mongodb://cloud-resume-db-mtui:MVV6ggpWlP4oeubHMfbEw1h027dyXo3NcMhYPDajUVB3VGF8Z0efGOOHEDPxKLdRXJXHjTCuX1LtACDbGxW8Rg==@cloud-resume-db-mtui.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@cloud-resume-db-mtui@")


def update():
    mydb = myclient["view-counter"]


    mycol = mydb["view-counter"]



    mycol.find_one_and_update(
        {'_id': '6525aeef1b5696176499f2fc'},
        {'$inc': {'value': 1}}


        )

    x = mycol.find_one()

    return x['value']



