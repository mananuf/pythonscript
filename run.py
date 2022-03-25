"""
A python script that takes in float numbers greater than 2.5,
performs computation, stores them in a list and it prints 
the largest number @ list min-length of 5 or max-length 7. 
"""


def largest_number():
    numbers = []                # empty list to stores numbers
    while len(numbers) < 7:     # continue while list length>7
        
        # check if user entered a number
        try:    
            p = float(input('Type a number: '))     # get input and store as float
            print(p) 

        # catch error (i.e: if input != digit)
        except:     
            print('value must be a number')     
            continue                            # prompt for user input again


        if p > 2.5:                             # only if input is >2.5, perform block action
            x = (p * 10) - 15                   # perform arithmetic operation and store in x

            numbers.append(x)                   # add value of x op. to end of list
            numbers = sorted(numbers)           # sort list in ascendin order

            print(numbers)                      # print sorted list
            largest = numbers[-1]               # let the last item of sorted list be the largest


            if len(numbers) == 5:               # if length of list reaches 5
                
                while True:                     # continue loop until user enters correct input
                    
                    # check if assert condition is met
                    try:
                        terminate = input("""
                                    \nDo you want to end this operation?
                                    \nType: 
                                    \nyes----> to terminate 
                                    \npress any key to continue previous operation
                                    \n> """).lower()       # prompt user to continue or stop loop
                        
                        assert terminate == 'yes' or terminate == 'no'      # assert condition

                    # if assert condition is not met, continue looping until condition is met
                    except AssertionError:
                        print( 12 * "-" + "invalid input" + 12 * "-")
                        continue 
                    

                    if terminate == 'yes':              # if user input is yes, perform block action
                        print('operation has ended!')
                        print(numbers)                  # print list
                        print(f'largest number = {largest} ')   # print largest number

                        return            # end the entire operation

                    elif terminate == 'no':
                        break            # stop loop and continue previous operation
                
        else:
            print('Oops! number must be greater than 2.5. TRY AGAIN')


        
    print(f"largest number = {largest} ")



largest_number()    # function call