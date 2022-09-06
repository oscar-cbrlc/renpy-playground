
define m = Character("Mik", color="#a527c4ff")
define o = Character("Oswald", color="#ee1212aa")
define t = Character("Tia", color="#f1d039ee")


label start:
    scene bg bus_station_morning with fade
    play music "audio/bgm/bgm home.mp3"
    "..."
    show mik mouth_c eye_full brow_down ex_blush at center:
        xzoom 0.8
        yzoom 0.8
    with dissolve
    "Mik"
    show mik mouth_c eye_full brow_high ex_none
    #pause
    show mik mouth_d eye_full brow_down ex_blush
    with dissolve
    m "Hey"
    show mik at left
    #with ease
    show tia mouth_c eye_full brow_down ex_blush at right:
        xzoom 0.8
        yzoom 0.8
    with easeinright
    #pause
    t "Hello Mik {nw}"
    stop music
    show os_angry at center with vpunch:
        xzoom 1.5
        yzoom 1.5
    pause
    return
