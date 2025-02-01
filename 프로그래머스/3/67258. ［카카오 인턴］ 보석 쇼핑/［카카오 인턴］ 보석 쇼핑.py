def solution(gems):
    n_gems=len(set(gems))
    gem_count={}
    answer=[1,len(gems)]
    start=0
    end=0 
    while end<len(gems):
        if gems[end] not in gem_count:
            gem_count[gems[end]]=1
        else:
            gem_count[gems[end]]+=1
        
        while len(gem_count)==n_gems:
            if end-start<answer[1]-answer[0]:
                answer=[start+1,end+1]
            gem_count[gems[start]]-=1
            if gem_count[gems[start]]==0:
                del gem_count[gems[start]]
            start+=1
        end+=1
    return answer