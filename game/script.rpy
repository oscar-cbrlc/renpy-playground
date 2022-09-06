
define mc = Character("You", color="#173979ff")
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
    mc "Mik"
    show mik mouth_c eye_full brow_high ex_none
    #pause
    show mik mouth_d eye_full brow_down ex_blush
    with dissolve
    m "Hey"
    show mik at left
    #with ease
    show tia mouth_d eye_full brow_high ex_blush at right:
        xzoom 0.8
        yzoom 0.8
    with easeinright
    #pause
    t "{cps=*2.5}{nw}Hello Mik, I've been waiting soo much to s-{/cps}"
    stop music
    show os_angry at center with vpunch:
        xzoom 1.5
        yzoom 1.5
    show tia mouth_s eye_half brow_low ex_blush
    show mik mouth_d eye_full brow_up ex_none
    mc "{cps=*3}WAAAAAAAAAAAAHHH{/cps}"
    pause
    return
