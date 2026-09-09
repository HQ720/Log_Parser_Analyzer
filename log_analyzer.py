#!/usr/bin/env python3

import re # python built in pattern recognition matching engine
from pathlib import Path
from collections import Counter # dictionary will be used to count automatically 


files_metric_lst=[]


def parse_log(full_path):
    # reference 192.168.1.5  - -  [10/Sep/2026...]  "GET /page..."  200   1452
    #           [  PART 1  ]→[PART2]→[ PART3 ]→[ PART4 ]→[PART5]→[PART6]

    invalid_lines=0
    count_success= 0
    count_error= 0

    ip=[]
    time_dates=[]
    all_codes=[]
    request_type=[]
    data_size=[]

    log_pattern= re.compile(
        r'(\d{1,3}(?:\.\d{1,3}){3})' # pattern for IP address X.X.X.X
        r' - - '
        r'(\[.*?\])' # pattern for time stamp 
        r' '
        r'(\".*?\")' # pattern for the request
        r' '
        r'(\d{3})' #pattern for the code like error or success
        r' '
        r'(\d+|-)' # patter for the kb (of data sent or recieved)
    )

    try:
        with open(full_path, 'r') as f:
            for line in f:
                line=line.strip() # removes spaces at the start and at the end of the line
                
                if not line: continue

                matching= log_pattern.fullmatch(line)

                if matching:
                    ip_add= matching.group(1)
                    Time= matching.group(2)
                    request= matching.group(3)
                    code=matching.group(4)
                    size= matching.group(5)

                    ip.append(ip_add)
                    time_dates.append(Time)
                    request_type.append(request)
                    all_codes.append(code)
                    data_size.append(size)
                else:
                    invalid_lines += 1
    
    except FileNotFoundError:
        print(f"Your file {full_path} was not found.")
        return None
    
    for code in all_codes:
        if code.startswith("2") or code.startswith("3"):
            count_success += 1
        elif code.startswith("4") or code.startswith("5"):
            count_error += 1
        else:
            continue
    return {
        "ip_addresses": ip,
        "time_dates": time_dates,
        "request_types": request_type,        
        "status_codes": all_codes,        
        "data_sizes": data_size,
        "invalid_lines": invalid_lines,
        "successful_count":count_success,
        "unsuccessful_count":count_error,     
        }






def success_vs_failed(metrics):
    return ("\nSUCCESS AND ERROR INFO:\n\n"
    f"Successful: {metrics['successful_count']}\n"
    f"Unsuccessful/ERROR : {metrics['unsuccessful_count']}\n"
    )

def users(metrics):
    user_metric=f"\nUSER INFO :::\n\n"
    user_ip=Counter(metrics['ip_addresses'])
    if not user_ip.items():
        return user_metric + "No users were found from the file:\n\n"
    
    for usr , num in user_ip.items():
        user_metric += f"\nUSERS: {usr}    Number: {num}\n"

    return  user_metric




def codes_counts(metrics):
    code_metrics=f"\nSTATUS CODES INFO:::\n\n"
    status_co=Counter(metrics['status_codes'])
    if not status_co.items():
        return code_metrics + "No status codes were found from the file:\n\n"

    for code, count in status_co.items():
        code_metrics += f"\nCODE: {code}    Number: {count}\n"
    return code_metrics




def all_metrics(metrics):
    return (        
        f"{users(metrics)}\n"        
        f"{codes_counts(metrics)}\n"        
        f"{success_vs_failed(metrics)}\n"        
        f"Invalid lines: {metrics['invalid_lines']}\n"    
    )




def create_file(full_path, metrics):
    while True:
        user_input=input(f"Would you like to save the analysis to review later? (y/n): ").strip().lower()
        if user_input in ("yes", "y"):
            original_file_name= Path(full_path).stem
            new_file=Path(f"Metric_Analyzed_{original_file_name}.txt")
            
            with new_file.open( "w", encoding="utf-8") as f:
                f.write(all_metrics(metrics)) 

            files_metric_lst.append(new_file)
            print(f"Great! A new file called {new_file} has been made and the analyzed data was saved to it.")
            return new_file 

        elif user_input in ("no", "n"):
            print("The analysis was not saved.")
            return None

        else:
            print("Please enter either y or n\n")
            continue




def start(full_path):
    metrics= parse_log(full_path)
    if metrics is None:
        return

    print(        "\nThe file was analyzed. Choose from the following options:\n"        
    "1 - Status-code metrics\n"        
    "2 - User metrics\n"        
    "A - All metrics\n"        
    "E - Exit\n"    )
            
    while True:
        choice= input("Please enter the number for which stat you would like to see : ").strip().lower()
        
        if choice == "1":
            print(codes_counts(metrics))
            

        elif choice == "2":
            print(users(metrics))
            

        elif choice=="a":
            print(all_metrics(metrics))            
            

        elif choice=="e":
            break
        else:
            print("\n\nPlease enter a valid number like 1,2,A or E.")
            continue
    create_file(full_path, metrics)







def view_lst_metric_files():
    show_files="Current files to view:::\n\n"
    list_of_files= files_metric_lst
    if not list_of_files:
        return "There are no files that have been saved"

        
    for i in list_of_files:
        show_files += f"- {i}\n"
    print(show_files)

    while True:
        choice= input(
        "Please enter the name of which file you would like"
        "to view or q if you would like to go back: ").strip().lower()
        
        if choice.lower()== "q":
            return
        
        try:
            with open(choice, "r", encoding="utf-8") as f:
                contents=f.read()
            print(contents)
            return contents

        except FileNotFoundError:
            print(f"That file {choice} does not exist. please choose from the list"
            f"{show_files}")
            continue



def menu():
    while True:

        choice=input("Would you like to:\n\n1-View a file from list\n2-Analze a new file\nq- to exit just type q\n\nPlease enter either 1 or 2 or q from the options above: ")
        
        if choice == "1":
            view_lst_metric_files()
            continue

        elif choice == "2":
            while True:
                user_input= input("Please enter the file name OR file path OR q to exit : ").strip()
                if not user_input:
                    print("Please enter something.\n")
                    continue
                elif user_input.lower() == "q":
                    return None

                full_path= Path(user_input).expanduser().resolve()

                if not full_path.is_file():
                    print("Please enter a valid file name or file path\n")
                    continue
                

                try:
                    with full_path.open('r', encoding="utf-8") as f:
                        f.read(1)
                
                except PermissionError:
                    print("Python does not have access to this file\n")
                    continue
                
                except OSError as error:
                    print(f"Python could not access this file : {error}\n")
                    continue
                

                print(f"FOUND THE FILE !!!\nFile was found and readable: {full_path}")
                
                while True:
                    user_confirm= input(
                    f"Please confirm {full_path} is the file you would like"
                    " to analyse. (y/n): ").lower().strip()
                    if user_confirm in ("yes", "y"):
                        start(full_path)
                        break
                        
                    elif user_confirm in ("no", "n"):
                        break

                    else:
                        print("Please enter either y or n\n")
                        continue
                    
                continue

        elif choice.lower().strip() == "q":
                return None 
        else:
            print("Please enter a valid choice like 1 or 2 or q")
            continue

if __name__ == "__main__":
    menu()



    


