"""
prompt the user with 'What is your problem?'
collect the user response
prompt the user with 'Have you had this problem before (yes or no)?'
collect user response
if yes 
print 'Well, you have it again.'
if no
print 'Well, you have it now.'
"""


user_problem = input('What is your problem? ')
user_response = input('Have you had this problem before (yes or no)? ')
if user_response == 'yes':
    print('Well, you have it again.')
if user_response == 'no':
    print('Well, you have it now.')



"""
The conversation won't convince the user that the entity at the other end exhibited intelligent behavior because the entity is not thinking about the problem'
"""
