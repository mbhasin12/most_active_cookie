import sys
import datetime
import os



def isValidDate(date):
    format_string = "%Y-%m-%d"
    datetime.datetime.strptime(date, format_string)


def buildCookieDict(cookie_log):
    cookie_dict = {}
    log_records = cookie_log.readlines() #read entire csv file in to a list of records
    for log_index, log_record in enumerate(log_records):
        if (log_index == 0):
            continue
        cookie_name, date_string_w_time = log_record.split(",") #split csv row into cookie and date_string
        date_string = date_string_w_time.split("T")[0] #remove Time from date_string since we are not concerned with it
        if date_string not in cookie_dict.keys():
            # create a dictionary entry whose value is also a dictionary which stores cookie name and num of occurances
            cookie_dict[date_string] = {cookie_name : 1}
        else:
            cookies_on_date = cookie_dict[date_string]
            if cookie_name in cookies_on_date.keys(): #increment or add cookie in nested dictionary

                cookies_on_date[cookie_name] += 1
            else:
                cookies_on_date[cookie_name] = 1



    return cookie_dict


def findMostActiveCookie(cookie_dict, date):

    if date in cookie_dict.keys():
        cookie_dict_on_date = cookie_dict[date]
        max_key = max(cookie_dict_on_date, key=cookie_dict_on_date.get) #find the cookie with the most occurances on specific day
        max_val = cookie_dict_on_date[max_key] #find value associated with that cookie in order to check if multiple keys have that value
        most_active_cookies = []

        for key in cookie_dict_on_date.keys():
            if (cookie_dict_on_date[key] == max_val):
                most_active_cookies.append(key) #add all cookies which have max value to a list

        return most_active_cookies
    else:
        return []




def printCookies(most_active_cookies):
    for cookie in most_active_cookies:
        print(cookie)

def main(sys_argv):

    ''' Following Code Checks For Command Line Arguments'''
    no_of_arguments = len(sys_argv)
    #print(sys_argv)
    if (no_of_arguments != 4):
        print("Invalid number of arguments. Usage Example: python3 most_active_cookie.py filename -d date")
        return
    elif (sys_argv[2] != '-d'):
        print("Invalid command line usage. Usage Example: python3 most_active_cookie.py filename -d date")
        return
    date = sys_argv[3]
    try:
        isValidDate(date)
    except ValueError:
        print("Invalid Date. Example Format: YYYY-MM-DD")
        return


    #Following Code Checks For Common File Exception Errors and Calls Func To Process Data
    csv_file_name = sys_argv[1]
    try:
        with open(csv_file_name) as cookie_log:
            if (os.path.getsize(csv_file_name) == 0):
                print("Empty File. No most active cooke")
                return
            else:
                cookie_dict = buildCookieDict(cookie_log)
                most_active_cookies = findMostActiveCookie(cookie_dict, date)

                if len(most_active_cookies) == 0: #if there is no cookies on specified date, print no cookies
                    print(f"No cookies on {date}")
                else:
                    printCookies(most_active_cookies) #helper function to print active cookies


    except FileNotFoundError:
        print(f"No such file or directory: {csv_file_name}.")
        return
    except IsADirectoryError:
        print(f"{csv_file_name} is a directory not a file")
        return
    except PermissionError:
        print(f"Permission Error: Cannot access {csv_file_name}")
        return

if __name__ == "__main__":
    main(sys.argv)

