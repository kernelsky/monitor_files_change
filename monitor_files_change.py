


def org_mate(org):
    with open("D:\python\monitor_files\org.txt", mode='r', encoding='utf-8') as f:
        ftextlist = f.readlines()
        print(ftextlist)
        for org_list in ftextlist:
            org_list=org_list.split(" ")
            if org_list[0] == org:
                print(org_list[2])
            else:
                pass

org_mate("B")