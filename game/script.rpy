
define m = Character("Mik", color="#a527c4ff")
define o = Character("Oswald", color="#ee1212aa")
define t = Character("Tia", color="#f1d039ee")


label start:
    scene bg bus_station_morning with fade
    play music "audio/bgm/bgm home.mp3"
    "..."
    show mik mouth_c eye_full brow_down ex_blush at left:
        xzoom 0.8
        yzoom 0.8
    "Mik"
    show mik mouth_c eye_full brow_high ex_none
    pause
    show mik mouth_d eye_full brow_down ex_blush
    m "Hey"
    
    return
