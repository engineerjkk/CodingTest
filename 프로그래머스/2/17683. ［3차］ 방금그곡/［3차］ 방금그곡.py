def shap_to_lower(m):
    m=m.replace('A#','a').replace('B#','b').replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g')
    return m

def solution(m, musicinfos):
    answer = [0,"(None)"]
    m=shap_to_lower(m)
    for musicinfo in musicinfos:
        s,e,name,music=musicinfo.split(",")
        s=int(s[:2])*60+int(s[3:])
        e=int(e[:2])*60+int(e[3:])
        music=shap_to_lower(music)
        time_length=e-s
        full_music=music*(time_length//len(music))+music[:time_length%len(music)]
        if m in full_music and answer[0]<time_length:
            answer=[time_length,name]
    return answer[1]