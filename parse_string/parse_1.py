#coding=utf-8
import glob
import csv

def slip_filter_url():
    f1 = open('/workspace/appannie/aa/tests/quick_smoke/cases/cases_async_csv.py')
    f2 = open('/workspace/appannie/aa/tests/quick_smoke/cases/cases_web.py')
    with open('url.csv', 'w') as csvfile:
        fieldnames = ['base_url', 'csv_url', 'web_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for line1 in f1:
            # filter csv
            if "url" in line1:
                # print line1
                if "?" in line1:
                    str1 = line1.split('\'#')
                    str1 = str1[1]
                    # print str1
                    if "?" in str1:
                        str1 = str1.split('?')
                        # print str1[0]
                        f2 = open('/workspace/appannie/aa/tests/quick_smoke/cases/cases_web.py')
                        for line2 in f2:
                            if "url" in line2:
                                if "?" in line2:
                                    str2 = line2.split('\'#')
                                    str2 = str2[1]
                                    if "?" in str2:
                                        str2 = str2.split('?')
                                        # print str2[0]
                                        # print 'web:' + str2[0]
                                        if str1[0] == str2[0]:
                                            # write to csv
                                            writer.writerow(
                                                {'base_url': str1[0], 'csv_url': str1[0]+'?'+str1[1], 'web_url': str1[0]+'?'+str2[1]})
                                            print 'csv:' + str1[0] + '---' + str1[1]
                                            print 'web:' + str2[0] + '---' + str2[1]
    # for line1 in f1:
    #     #filter csv
    #     if "url" in line1:
    #         #print line1
    #         if "?" in line1:
    #             str1=line1.split('\'#')
    #             str1 = str1[1]
    #             #print str1
    #             if "?" in str1:
    #                 str1=str1.split('?')
    #                 #print str1[0]
    #                 f2 = open('/workspace/appannie/aa/tests/quick_smoke/cases/cases_web.py')
    #                 for line2 in f2:
    #                     if "url" in line2:
    #                         if "?" in line2:
    #                             str2 = line2.split('\'#')
    #                             str2 = str2[1]
    #                             if "?" in str2:
    #                                 str2 = str2.split('?')
    #                                 #print str2[0]
    #                                 #print 'web:' + str2[0]
    #                                 if str1[0] == str2[0]:
    #                                     #write to csv
    #                                     writer.writerow({'base_url': str1[0], 'csv_url': str1[1], 'web_url': str2[1]})
    #                                     print 'csv:' + str1[0] + '---' + str1[1]
    #                                     print 'web:' + str2[0] + '---' + str2[1]

#cmp(sStr1,sStr2)
if __name__  == "__main__":

    #parse_file()
    slip_filter_url()
    print 'ok!'