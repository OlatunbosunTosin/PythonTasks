while True:
    print("""          
                         Menu
                    1. Phonebook
                    2. Messages
                    3. Chat
                    4. Call register
                    5. Set tones
                    6. Settings
                    7. Call divert
                    8. Games
                    9. Calculator
                    10. Reminders
                    11. Clock
                    12. Profiles
                    13. SIM services 
                     0.back \n"""
    )

    menu = int(input())      
    if menu == 0:
        break   
    match menu:
        case 1:
            while True:
                print("""   
                            Phonebook
                          1. Search
                          2. Service Nos.
                          3. Add name
                          4. Erase
                          5. Edit
                          6. Assign tone
                          7. Send b’card
                          8. Options
                          9. Speed dials
                         10. Voice tags 
                          0.back \n"""
                )
                phone_book = int(input())
                if phone_book == 0:
                    break
                
                match phone_book:
                    case 1: print("Search\n")
                            
                   
                    case 2: print("Service Nos.\n")
                           

                    case 3: print("Add name\n")
                            
                    
                    case 4: print("Erase\n")
                           
                    
                    case 5: print("Edit\n")
                           
                    
                    case 6: print("Assign tone\n")
                         
                    
                    case 7: print("Send b’card\n")
                          
                    
                    case 8: 
                        while True:
                            print("""   
                                        Options\n
                                     1. Type of view
                                     2. Memory status 
                                     0. back \n"""
                            )
                                
                               
                    
                            options = int(input())
                            if options == 0:
                                break
                            match options:
                                case 1: print("Type of view\n")
                                        

                                case 2: print("Memory status\n")
                                        

                                case 0: print("back\n")

                                case _: print("invalid\n")

                            
             
                    case 9: print("Speed dials")
                           
                    
                    case 10: print("Voice tags")
                            

                    case 0: print("back\n")

                    case _: print("invalid\n")


        case 2: 
            while True:
                print("""       Messages
                          1. Write messages
                          2. Inbox
                          3. Outbox
                          4. Picture messages
                          5. Templates
                          6. Smileys
                          7. Message settings
                          8. Info service
                          9. Voice mailbox number
                          10. Service command editor 
                           0. back      \n"""
                )
                messages = int(input())
                if messages == 0:
                    break

                match messages:
                    case 1: print("Write messages\n")
                    
                    case 2: print("Inbox\n")
                    
                    case 3: print("Outbox\n")
                            
                    case 4: print("Picture messages\n")
                           
                    case 5: print("Templates\n")
                           
                    case 6: print("Smileys\n")
                           
                    case 7: 
                        while True:
                            print("""       Message settings\n
                                            1. Set
                                            2. Common \n"""
                            )
                            message_settings = int(input())
                            if message_settings == 0:
                                break

                            match message_settings:
                                case 1: 
                                    while True:
                                        print("""       Set

                                                   1. Message centre number
                                                   2. Messages sent as
                                                   3. Message validity \n"""    
                                            )
                                        set1 = int(input())
                                        if set1 == 0:
                                            break
    
                                        match set1:
                                            case 1: print("Message centre number\n")
                                    
                                            case 2: print(" Messages sent as\n")
                                                   
                                            case 3: print("Message validity\n")
                                                  
                                            case 0: print("back\n")
                                                  
                                            case _: print("Invalid")
                                              
                                case 2: 
                                    while True:
                                        print("""      Common\n

                                                    1. Delivery reports
                                                    2. Reply via same centre
                                                    3. Character support \n"""
                                        )
                                        common = int(input())
                                        if common == 0:
                                            break
                                        match common:
                                            case 1: print("Delivery reports\n")
                                    
                                            case 2: print("Reply via same centre\n")
                                    
                                            case 3: print("Character support\n")

                                            case 0: print("back\n")
                                                    
                                            case _: print("Invalid")
                                      
                                case 0: print("back\n")
                                        
                                case _: print("Invalid")

                    case 8: print("Info service\n");

                    case 9: print("Voice mailbox number\n");
                         
                    case 10: print("Service command editor\n");
                             
                    case 0: print("back\n");
                            
                    case _: print("Invalid");

        case 3: print("Chats") 

        case 4: 
            while True:
               print("""        Call register
                            1. Missed calls
                            2. Received calls
                            3. Dialled numbers
                            4. Erase recent call lists
                            5. Show call duration
                            6. Show call costs
                            7. Call cost settings
                            8. Prepaid credit \n"""
               )
               call_register = int(input())

               if call_register == 0:
                   break
                
               match call_register:
                   case 1: print("Missed calls\n")
                          
                   case 2: print("Received calls\n")
                           
                   case 3: print("Dialled numbers\n")
                         
                   case 4: print("Erase recent call lists\n")
                           
                   case 5: 
                       while True:
                           print("""        Show call duration

                                            1. Last call duration
                                            2. All calls’ duration
                                            3. Received calls’ duration
                                            4. Dialled calls’ duration
                                            5. Clear timers  \n"""
                           )
                           show_call_duration = int(input())

                           if show_call_duration == 0:
                               break

                           match show_call_duration:
                                case 1: print("Last call duration\n")
                                
                                case 2: print("All calls’ duration\n")
                                
                                case 3: print("Received calls’ duration\n")
                                
                                case 4: print("Dialled calls’ duration\n")
                                       
                                case 5: print("Clear timers\n")
    
                                case 0: print("back\n")
                                       
                                case _: print("Invalid\n")
                               
                            
                   case 6: 
                        while True:
                            print("""   Show call costs

                                        1. Last call cost
                                        2. All calls’ cost
                                        3. Clear counters \n"""
                            )
                            c = int(input())

                            if show_call_costs == 0:
                                break

                            match show_call_costs:
                                case 1: print("Last call cost\n")
                                
                                case 2: print("All calls’ cost\n")
                                        
                                case 3: print("Clear counters\n")
                                      
                                case 0: print("Clear counters\n")
                                      
                                case _: print("Invalid\n")
                           
                   case 7: 
                        while True:
                            print(""" Call cost settings
                                            1. Call cost limit
                                            2. Show costs in \n"""
                            )
                            call_cost_settings = int(input()) 
                            
                            if call_cost_settings == 0:
                                break

                            match call_cost_settings:
                                case 1: print("Call cost limit\n")
                                
                                case 2: print("Show costs in\n")

                                case 0: print("back\n")
                                        
                                case _: print("Invalid\n")

                   case 8: print("Prepaid credit\n")
                           
                   case 0: print("back\n")

                   case _: print("Invalid")

        case 5: 
            while True:
                print("""                Tones
                                    1. Ringing tone
                                    2. Ringing volume
                                    3. Incoming call alert
                                    4. Composer
                                    5. Message alert tone
                                    6. Keypad tones
                                    7. Warning and game tones
                                    8. Vibrating alert
                                    9. Screen saver \n"""
                )
                tones = int(input()) 

                if tones == 0:
                    break
                
                match tones:
                    case 1: print("Ringing tone\n")
                    
                    case 2: print("Ringing volume\n")
                            
                    case 3: print("Incoming call alert\n")
                            
                    case 4: print("Composer\n")
                          
                    case 5: print("Message alert tone\n")
                           
                    case 6: print("Assign tone\n")
                            
                    case 7: print("Warning and game tones\n")
                           
                    case 8: print("Vibrating alert\n")
                           
                    case 9: print("Screen saver\n")
                           
                    case 0: print("back\n")
                           
                    case _: print("Invalid");       
                    
        case 6: 
            while True:
                print("""      Settings
                            1. Call settings
                            2. Phone settings
                            3. Security settings
                            4. Restore factory settings \n"""
                )
                settings = int(input()) 

                if settings == 0: 
                    break
                
                match settings:
                    case 1: 
                        while True:
                            print("""  Call settings
                                    1. Automatic redial
                                    2. Speed dialling
                                    3. Call waiting options
                                    4. Own number sending
                                    5. Phone line in use
                                    6. Automatic answer  \n"""
                            )
                            call_settings = int(input()) 

                            if call_settings == 0:
                                break
                            
                            match call_settings:
                                case 1: print("Automatic redial\n")

                                case 2: print("Speed dialling\n")
                                        
                                case 3: print("Call waiting options\n")

                                case 4: print("Own number sending\n")
                                
                                case 5: print("Phone line in use\n")
                                
                                case 6: print("Phone Automatic answer\n")

                                case 0: print("back\n")
                                        
                                case _: print("Invalid\n")
                   

                    case 2:     
                        while True:
                            print("""  Phone settings
                                1. Language
                                2. Cell info display
                                3. Welcome note
                                4. Network selection
                                5. Lights2
                                6. Confirm SIM service actions  \n """
                                )
                            phone_settings = int(input()) 

                            if phone_settings == 0:
                                break
                            
                            match phone_settings:
                                case 1: print("Language\n")
                                        
                                case 2: print("Cell info display\n")

                                case 3: print("Welcome note\n")
                                       
                                case 4: print("Network selection\n")
                                
                                case 5: print("Lights\n")
                                        
                                case 6: print("Confirm SIM service actions\n");
                                case 0: print("back\n")

                                case _: print("Invalid\n")
                               

                    case 3: 
                        while True:
                            print("""  Security settings
                                    1. PIN code request
                                    2. Call barring service
                                    3. Fixed dialling
                                    4. Closed user group
                                    5. Phone security
                                    6. Change access codes \n"""                   
                            )
                            security_settings = int(input())
                            if security_settings == 0:
                                break
                            
                            match security_settings:

                                case 1: print("PIN code request\n")

                                case 2: print("Call barring service\n")
                                
                                case 3: print("Fixed dialling\n")
                                
                                case 4: print("Closed user group\n")
                                
                                case 5: print("Phone security\n")
                                
                                case 6: print("Change access codes\n")

                                case 0: print("back\n")

                                case _: print("Invalid\n")
                                

                    case 4: print("Restore factory settings\n")

                    case 0: print("back\n")
                           
                    case _: print("Invalid\n")

        case 7: print("Call divert\n")

        case 8: print("Games\n")
                
        case 9: print("Calculator\n")

        case 10: print("Reminders\n")

        case 11: 
             while True:
                 print("""          Clock
                                1. Alarm clock
                                2. Clock settings
                                3. Date setting
                                4. Stopwatch
                                5. Countdown timer
                                6. Auto update of date and time \n """
                 )
                 clock = int(input()) 

                 if clock == 0:
                     break
                 match clock:
                     case 1: print("Alarm clock\n")
                     
                     case 2: print("Clock settings\n")

                     case 3: print("Date setting\n")
                     
                     case 4: print("Stopwatch\n")
                     
                     case 5: print("Countdown timer\n")

                     case 6: print("Auto update of date and time\n")
                     
                     case 0: print("back\n")
                               
                     case _: print("Invalid\n")

        case 12: print("Profiles\n")

        case 13: print("SIM services\n")
                
        case 0:  print("back\n")
        
        case _: print("Invalid\n")
               
                    
                                 

                   

              



       

