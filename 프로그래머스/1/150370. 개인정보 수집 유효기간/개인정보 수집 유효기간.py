def solution(today, terms, privacies):
    t_year,t_month,t_day=today.split(".")
    t_year,t_month,t_day=int(t_year),int(t_month),int(t_day)
    term_dic={}
    answer=[]
    for term in terms:
        c,num=term.split()
        if c not in term_dic:
            term_dic[c]=num
            
    for i,privacie in enumerate(privacies):
        something,condition=privacie.split()
        year,month,day=something.split(".")
        year,month,day=int(year),int(month),int(day)
        

        
        limit=int(term_dic[condition])
        limit=limit*28
        usingTime=(t_year-year)*28*12+(t_month-month)*28+(t_day-day)
        if usingTime>=limit:
            answer.append(i+1)
    return answer