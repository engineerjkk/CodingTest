def shap_to_lower(s):
    s=s.replace('A#','a').replace('B#','b').replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g')
    return s

def solution(m, musicinfos):
    answer = [0,'(None)']
    m=shap_to_lower(m)
    for musicinfo in musicinfos:
        s,e,name,music=musicinfo.split(',')
        music=shap_to_lower(music)
        time_length=(int(e[:2])-int(s[:2]))*60+(int(e[3:])-int(s[3:]))
        full_music=music*(time_length//len(music))+music[:time_length%len(music)]
        if m in full_music and time_length>answer[0]:
            answer=[time_length,name]
    return answer[1]