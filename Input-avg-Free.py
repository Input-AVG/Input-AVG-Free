print("Please be patient, loading takes longer on first opening...")
print("Loading...")
print("   Importing Libraries...")
import requests
import re
print("\n\nWelcome to Input-Average (Free)")
print(" {Do not distribute) - LostDev404")
print("   Change Logs: \n   Fixed Errors in 'View'")
print("      psst, Paid version gives you acces to:\n         Auto Scans\n         App download\n         Data Graphing\n         File/Data saving\n         More info on scan\n         No item limit on a scan\n         Plus More")
while 1:
        print("")
        print("")
        message = input("Type 'Run' to scan a website\nType 'Auto' (Paid) to set up an automattic scan\nType 'View' (Paid) to analyze data and/or edit files: ")
        if message == "Run":
            ItemName = input("Enter the item name: ")
            print("The item is '{}'".format(ItemName))
            ItemName = ItemName.replace(" ", "+")
            URL = 'http://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&_ipg=60'.format(ItemName)
            print("")
            num_items = input("How many items do you want to use for the average? (Rec 20-30): ")
            num_items = int(num_items)
            if num_items > 60:
                num_items = 60
                print("\nError: \n  Can't use more than 60 items with free version, setting items to 60")
            else:
                print("You put: '{}'".format(num_items))
            print("")
            file_name = input("What file do you want the info to be put in?: ")
            print("\nError: \n  Can't save file name with free version")
            del file_name
            print("\nProcessing...\n")
            page = requests.get(URL)
            dollar_elements = re.findall(r'(?<=price).*?\$[\d.,]+\b', page.text, flags=re.MULTILINE)
            if len(dollar_elements) > 0:
                elements_list = []
                for element in dollar_elements[2:num_items]:
                    element = element.replace("$", "")
                    element = element.replace(".", "")
                    element = element.replace(">", "")
                    element = element.replace("<", "")
                    try:
                        float_element = float(element)
                        elements_list.append(float_element)
                    except ValueError:
                        pass
                elements_list.sort()
                element_sum = sum(elements_list)
                element_avg = element_sum / len(elements_list)
                element_avg /= 100
                print("The average price with #{} items was ${:.2f}".format(num_items, element_avg))
                print("\nError: \n  Can't print highest and lowest prices, or time and date of scan with free version")
                del dollar_elements
                del element_sum
                del element_avg
                del elements_list
                del element
                del ItemName
        else:
            Print("")

                                
                                
                        

                        
                                
                        
