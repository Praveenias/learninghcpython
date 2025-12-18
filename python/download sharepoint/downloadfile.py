# from shareplum import Site
# from shareplum import Office365

# try:
#   authcookie = Office365('https://ilensystech.sharepoint.com', username='praveen.ravikumar@ilensys.com', password='BQIndr@7708').GetCookies()
#   #print(authcookie)
#   site = Site('https://ilensystech.sharepoint.com/sites/Atom/development', authcookie=authcookie)
#   folder = site.Folder('')
#   #sp_list = site.List('DesignAndImplementation\\sso')
#   #print(sp)

#   #list_data = sp_list.GetListItems(fields=['Name'])  
#   folder = site.connect_folder('sso')
#   print(folder)
#   #file = folder.get_file(file_name)
#   #folder.get_file('source.txt')
# except Exception as e:
#   print(e)

import sharepy
s = sharepy.connect("https://ilensystech.sharepoint.com",username="praveen.ravikumar@ilensys.com", password="BQIndr@7708")
r = s.getfile("https://ilensystech.sharepoint.com/:t:/r/sites/Atom/development/DesignAndImplementation/readme.txt")
print(r)