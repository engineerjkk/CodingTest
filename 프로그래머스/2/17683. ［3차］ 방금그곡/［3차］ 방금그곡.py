def shap_to_lower(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
    return s

def solution(m,musicinfos):
    answer=[0,'(None)']
    m=shap_to_lower(m)
    for musicinfo in musicinfos:
        start,end,name,music=musicinfo.split(',')
        time_length=(int(end[:2])-int(start[:2]))*60+(int(end[-2:])-int(start[-2:]))
        music=shap_to_lower(music)
        full_music=music*(time_length//len(music))+music[:time_length%(len(music))]
        if m in full_music and time_length>answer[0]:
            answer=[time_length,name]
    return answer[-1]
