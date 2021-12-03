# most_active_cookie

# Files:

  most_active_cookie.py - contains the code to parse the command line arguments and print the most active cookie for the specified date

  cookie_log_tests.py   - contains unit tests to test the output of functions in most_active_cookie.py

  empty_file.csv  - empty csv file used for testing

  one_element.csv - csv file with just one element

  test.csv - csv file with a number of entries of cookies and their timestamps
  
# How I tested the code:
  Ran all 8 unit tests using the following command:
  
    python3 cookie_log_tests.py
    
  The following tests ran directly from the terminal
  
   No most active cookie (Date does not exist in file)
   
    python3 most_active_cookie.py test.csv -d 2018-12-01
    
   Multiple most active cookies for a particular date 
   
    python3 most_active_cookie.py test.csv -d 2018-12-08
    
   One active cookie for a particular date 
   
    python3 most_active_cookie.py test.csv -d 2018-12-09
    
   
   
    
  
  
