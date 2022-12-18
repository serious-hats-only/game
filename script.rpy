# define character variables here. 

default n = Character("")
default final_n = Character("")
default p = Character("Human")
default s = Character("Scout")
default r1 = Character("Tutorial Robot")
default r2 = Character("Claw Arm")
default r3 = Character("Boston Dynamics")
default r4 = Character("Bezos Hologram")
default r5 = Character("HAL9000")
default r6 = Character("TV Monster")

# define images and movie files here
# McQ made various emotion anims for the bots but i'm only calling the idles and splodes in their respective label sections for now
# call any of the emotion anims as desired - figured they might depend on meter state

image jamLogo = "jamLogo.png"
image gameover_overlay = "gui/overlay/confirm.png"

image scout_idle = Movie(channel="scout", play="scout_idle.webm", mask="scout_idle_mask.webm", framedrop=False)
image scout_angry = Movie(channel="scout", play="scout_angry.webm", mask="scout_angry_mask.webm", framedrop=False)
image scout_furious = Movie(channel="scout", play="scout_furious.webm", mask="scout_furious_mask.webm", framedrop=False)
image scout_happy = Movie(channel="scout", play="scout_happy.webm", mask="scout_happy_mask.webm", framedrop=False)
image scout_sad = Movie(channel="scout", play="scout_sad.webm", mask="scout_sad_mask.webm", framedrop=False)

image tut_idle = Movie(channel="tut", play="tut_idle.webm", mask="tut_idle_mask.webm", framedrop=False)
image tut_splode = Movie(channel="tut", play="tut_splode.webm", mask="tut_splode_mask.webm", framedrop=False, loop=False)
image tut_love = Movie(channel="tut", play="tut_love.webm", mask="tut_love_mask.webm", framedrop=False)

image claw_idle = Movie(channel="claw", play="claw_idle.webm", mask="claw_idle_mask.webm", framedrop=False)
image claw_splode = Movie(channel="claw", play="claw_splode.webm", mask="claw_splode_mask.webm", framedrop=False, loop=False)
image claw_wide = Movie(channel="claw", play="claw_wide.webm", mask="claw_wide_mask.webm", framedrop=False)
image claw_spin = Movie(channel="claw", play="claw_spin.webm", mask="claw_spin_mask.webm", framedrop=False)
image claw_clamp = Movie(channel="claw", play="claw_clamp.webm", mask="claw_clamp_mask.webm", framedrop=False)

image boston_idle = Movie(channel="boston", play="boston_idle.webm", mask="boston_idle_mask.webm", framedrop=False)
image boston_idle_plus_camera = Movie(channel="boston", play="idle_plus_camera.webm", mask="idle_plus_camera_mask.webm", framedrop=False)
image boston_splode = Movie(channel="boston", play="boston_splode.webm", mask="boston_splode_mask.webm", framedrop=False, loop=False)
image boston_nod = Movie(channel="boston", play="boston_nod.webm", mask="boston_nod_mask.webm", framedrop=False)
image boston_hop = Movie(channel="boston", play="boston_hop.webm", mask="boston_hop_mask.webm", framedrop=False)
image boston_hindlegs = Movie(channel="boston", play="boston_hindlegs.webm", mask="boston_hindlegs_mask.webm", framedrop=False)

image holo_idle = Movie(channel="holo", play="holo_idle.webm", mask="holo_idle_mask.webm", framedrop=False)
image holo_splode = Movie(channel="holo", play="holo_splode.webm", mask="holo_splode_mask.webm", framedrop=False, loop=False)
image holo_flicker = Movie(channel="holo", play="holo_flicker.webm", mask="holo_flicker_mask.webm", framedrop=False)
image holo_double = Movie(channel="holo", play="holo_double.webm", mask="holo_double_mask.webm", framedrop=False)
image holo_backforth = Movie(channel="holo", play="holo_backforth.webm", mask="holo_backforth_mask.webm", framedrop=False)

image hal_idle = Movie(channel="hal", play="hal_idle.webm", mask="hal_idle_mask.webm", framedrop=False)
image hal_splode = Movie(channel="hal", play="hal_splode.webm", mask="hal_splode_mask.webm", framedrop=False, loop=False)
image hal_rainbow = Movie(channel="hal", play="hal_rainbow.webm", mask="hal_rainbow_mask.webm", framedrop=False)

image tv_idle = Movie(channel="tv", play="tv_idle.webm", mask="tv_idle_mask.webm", framedrop=False)
image tv_splode = Movie(channel="tv", play="tv_splode.webm", mask="tv_splode_mask.webm", framedrop=False, loop=False)
image tv_happy = Movie(channel="tv", play="tv_happy.webm", mask="tv_happy_mask.webm", framedrop=False)
image tv_sad = Movie(channel="tv", play="tv_sad.webm", mask="tv_sad_mask.webm", framedrop=False)

# sets custom enemy spawn sizes and positions
# this was needed because some of the anims rendered at different coordinates

transform tut_pos:
    zoom 1.2
    xpos 1100
    yanchor -25

transform claw_pos:
    zoom 0.85
    xpos 900
    yanchor 150

transform boston_pos:
    zoom 0.85
    xpos 900
    yanchor 230

transform holo_pos:
    zoom 0.80
    xpos 1100
    yanchor 25

transform hal_pos:
    zoom 0.40
    xpos 1220
    yanchor -35

transform tv_pos:
    zoom 1.0
    xpos 1000
    yanchor -150

transform side_scout_pos:
    zoom 0.85
    xpos -35
    yanchor -500


# splash screen to intro movie transition

label splashscreen:
    play sound jl_sting 
    show jamLogo with dissolve
    with Pause(2)

    $ renpy.movie_cutscene('intro_text_scroll.webm')
    return

# game intro and tutorial. still needs its own bot and an edit pass on the text
# scout's emotion anims do get called here since there's no meter state to contend with

label start:
    define r2_choice1 = ""

    stop music
    scene bg decay
    play music tut_music

    show screen text_2x2grid

    screen text_2x2grid:
        grid 2 2:
            xalign 0.5
            yalign 0.5
            spacing 20
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                textbutton "apples" action [SetVariable("r2_choice1", "apples"), ToggleScreen("text_2x2grid"), Jump("r2_choice1_react")]
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                textbutton "roadkill" action [SetVariable("r2_choice1", "roadkill"), ToggleScreen("text_2x2grid"), Jump("r2_choice1_react")]
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                textbutton "Fidel Castro" action [SetVariable("r2_choice1", "Fidel Castro"), ToggleScreen("text_2x2grid"), Jump("r2_choice1_react")]
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                textbutton "yeast" action [SetVariable("r2_choice1", "yeast"), ToggleScreen("text_2x2grid"), Jump("r2_choice1_react")]
    p "Hey, loverboy. I see you like ______."

label r2_choice1_react:
    p "Hey, loverboy. I see you like [r2_choice1]."
    r1 "What is this I am feeling?"
    play sound glitch_splode
    show tut_splode at tut_pos
    pause
    jump robot_2
    return
    
    
    
    # n "You roam the decaying remains of a once great city."
    # show tut_idle at tut_pos with moveinright
    # r1 "HALT! You know baby thinking deep wanna hurt your hella good breathe yeaaaah."
    # show scout_angry at left with vpunch
    # s "Back off! Get MARRIED and always remember that night we found WONDERLAND."
    # r1 "..............."
    # play sound glitch_splode
    # show tut_splode at tut_pos
    # pause
    # show scout_idle at left
    # s "Close one, human. My scanner indicated that this robot's AI was trained using Taylor Swift lyrics."
    # s "If you can guess their programming, just say the right keywords to make them love you. That's their one weakness."
    # s "If they feel love, they die. Otherwise you're toast." 
    # show scout_happy at left
    # s "Good luck!"
    # jump robot_2
    # return

# robot_2 is Claw Arm
# note that there's an example of scout popping in to say something during the battle. can be copied anywere for a similar moment

label robot_2:

    stop music 
    scene bg claw with fade
    play music claw_music

    n "You've moved on to Claw Arm"
    show claw_idle at claw_pos with moveinright
    r2 "This is my Battlecry!"
    p "This is my first Question or Response line"
    show scout_idle at side_scout_pos onlayer over_screens with moveinbottom
    s "Just popping into deliver a player progress bark from the side!"
    hide scout_idle onlayer over_screens with dissolve
    r2 "This is my Deathrattle."
    play sound glitch_splode
    show claw_splode at claw_pos
    pause
    jump robot_3
    return

# robot_3 is Boston Dynamics.

label robot_3:

    stop music
    scene bg boston with fade
    play music boston_music

    n "You've moved on to Boston Dynamics"
    show boston_idle at boston_pos with moveinright
    r3 "This is my Battlecry!"
    p "This is my first Question or Response line"
    r3 "This is my Deathrattle."
    play sound glitch_splode
    show boston_splode at boston_pos
    pause
    jump robot_4
    return

# robot_4 is Bezos Hologram.

label robot_4:

    stop music
    scene bg holo with fade
    play music holo_music

    n "You've moved on to Bezos Hologram"
    show holo_idle at holo_pos with moveinright
    r4 "This is my Battlecry!"
    p "This is my first Question or Response line"
    r4 "This is my Deathrattle."
    play sound glitch_splode
    show holo_splode at holo_pos
    pause
    stop music
    jump robot_5
    return

# robot_5 is HAL9000.

label robot_5:

    stop music
    scene bg hal with fade
    play music hal_music

    n "You've moved on to HAL9000"
    show hal_idle at hal_pos with moveinright
    r5 "This is my Battlecry!"
    p "This is my first Question or Response line"
    r5 "This is my Deathrattle."
    play sound glitch_splode
    show hal_splode at hal_pos
    pause
    jump robot_6
    return

# robot_6 is TV Monster - the Final Boss

label robot_6:

    stop music
    scene bg tvmonster with fade
    play music tv_music

    n "You've moved on to TV Monster"
    show tv_idle at tv_pos with moveinright
    r6 "This is my Battlecry!"
    p "This is my first Question or Response line"
    r6 "This is my Deathrattle."
    play sound glitch_splode
    show tv_splode at tv_pos
    pause
    jump scout_betrayal
    return

# scout_betrayal is the game ending wrap-up where Scout reveals her true identity and you fight to avoid loving each other

label scout_betrayal:

    stop music
    scene bg decay with fade
    play music scouts_betrayal_music

    n "You've moved on to Scout's Betrayal"
    show scout_idle at right with moveinright
    s "This is my Battlecry!"
    p "This is my first Question or Response line"
    s "This is my Deathrattle."
    # if she dies, we have that cool fullscreen anim, filename Scout_Transform_3 - it's still in discord, not dl'ed to images directory
    # would need a matching glitch_splode sound here too
    pause
    jump tease_sequel
    return

# some sort of ending, a sequel tease or a Ru Paul quote about love were options.

label tease_sequel:
    
    stop music
    scene bg blackout with fade
    # need tease_sequel music here unless there's a video that contains its own music
    window hide

    final_n "You've defeated these bots, but many more await and you've now taught them to better resist flirtation."
    final_n "The only way to defeat them now is through the seductive power of dance in…"
    final_n "LOVE THEM TO DEATH: IT TAKES 2.0 TO TANGO"
    return

# Game Over screen
# Triggers if meter reaches 0
# Replace LABEL_NAME with whatever level you're currently on

# label game_over:

#     scene bg blackout 
        
#     menu:
#         "GAME OVER"

#         "Get back out there and CONTINUE loving?":
#             # jump LABEL_NAME
        
#         "Lose the spark and RETURN TO MAIN MENU":
#             return