qa = [
    {'id': 1, 'surname': 'Koba', 'skills': ['test_design_writers', 'reviewer'], 'working_time': 'out_of_office_today'},
    {'id': 2, 'surname': 'Moloko', 'skills': ['scripter', 'reviewer'], 'working_time': 'out_of_office_today'},
    {'id': 3, 'surname': 'Skyba', 'skills': ['scripter', 'test_design_writers', 'reviewer'], 'working_time': 'in_office_today'},
    {'id': 4, 'surname': 'Fonko', 'skills': 'scripter', 'working_time': 'in_office_today'},
    {'id': 5, 'surname': 'Terko', 'skills': 'test_design_writers', 'working_time': 'out_of_office_today'},
    {'id': 6, 'surname': 'Granko', 'skills': 'scripter', 'working_time': 'out_of_office_today'},
    {'id': 7, 'surname': 'Derko', 'skills': 'scripter', 'working_time': 'in_office_today'},
    {'id': 8, 'surname': 'Gak', 'skills': 'scripter', 'working_time': 'in_office_today'},
    {'id': 9, 'surname': 'Hryn', 'skills': 'reviewer', 'working_time': 'in_office_today'},
    {'id': 10, 'surname': 'Lom', 'skills': 'reviewer', 'working_time': 'in_office_today'},
]
qa2 = [i['id'] for i in qa if 'reviewer' in i['skills']]
qa3 = [i['id']for i in qa if 'scripter' in i['skills']]
qa4 = [i['id'] for i in qa if 'test_design_writers' in i['skills']]
qa5 = [i['id'] for i in qa if 'out_of_office_today' in i['working_time']]
qa6 = [i['id'] for i in qa]
qa7 = [i['id'] for i in qa if i['skills'] == 'scripter']
qa8 = [i['id'] for i in qa if i['working_time'] != 'out_of_office_today']
qa_set2 = set(qa2)
qa_set3 = set(qa3)
qa_set8 = set(qa8)
qa_set = qa_set2.intersection(qa_set8)
qa_setfinal = qa_set.intersection(qa_set3)
qa9 = list(qa_setfinal)
print("reviewers =", qa2)
print("scripters =", qa3)
print("test_design_writers =", qa4)
print("out_of_office_today =", qa5)
print("all qa =", qa6)
print("only scripter =", qa7)
print("in office today =", qa8)
print("scripter, reviewer, in office today =", qa9)
