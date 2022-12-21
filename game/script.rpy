﻿# define character variables here. 

default n = Character("")
default final_n = Character("")
default p = Character("You")
default s = Character("Scout")
default r1 = Character("Robot")
default partner = Character("Scout's Partner")

# define images and movie files here
# McQ made various emotion anims for the bots but i'm only calling the idles and splodes in their respective label sections for now
# call any of the emotion anims as desired - figured they might depend on meter state

image jamLogo = "jamLogo.png"

image tut_idle = Movie(channel="tut", play="tut_idle.webm", mask="tut_idle_mask.webm", framedrop=False)
image tut_splode = Movie(channel="tut", play="tut_splode.webm", mask="tut_splode_mask.webm", framedrop=False, loop=False)
image tut_love = Movie(channel="tut", play="tut_love.webm", mask="tut_love_mask.webm", framedrop=False)

image scout_idle = Movie(channel="scout", play="scout_idle.webm", mask="scout_idle_mask.webm", framedrop=False)
image scout_angry = Movie(channel="scout", play="scout_angry.webm", mask="scout_angry_mask.webm", framedrop=False)
image scout_furious = Movie(channel="scout", play="scout_furious.webm", mask="scout_furious_mask.webm", framedrop=False)
image scout_happy = Movie(channel="scout", play="scout_happy.webm", mask="scout_happy_mask.webm", framedrop=False)
image scout_sad = Movie(channel="scout", play="scout_sad.webm", mask="scout_sad_mask.webm", framedrop=False)

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

image partner_idle = Movie(channel="partner", play="Scout_Partner_IDLE.webm", mask="Scout_Partner_IDLE_MASK.webm", framedrop=False)
image partner_angry = Movie(channel="partner", play="Scout_Partner_ANGRY.webm", mask="Scout_Partner_ANGRY_MASK.webm", framedrop=False)

image heart_transparency = Movie(channel="hearts", play="heart_transparency.webm",mask="heart_transparency_MASK.webm", framedrop=False)

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
    zoom 1.5
    xpos 800
    yanchor 150

transform side_scout_pos:
    zoom 0.85
    xpos -35
    yanchor -500

transform scouts_partner_pos:
    zoom 0.85
    xpos 900
    yanchor 100

# These transforms are just different crops of the meter.

transform status_bar_pos:
    zoom 0.2
    xpos 10
    yanchor 0

transform status_bar_pos_0:
    zoom 0.2
    xpos 10
    yanchor 0
    crop (0,0,0,1000)

transform status_bar_pos_1:
    zoom 0.2
    xpos 10
    yanchor 0
    crop (0,0,800,1000)

transform status_bar_pos_2:
    zoom 0.2
    xpos 10
    yanchor 0
    crop (0,0,1200,1000)

transform status_bar_pos_3:
    zoom 0.2
    xpos 10
    yanchor 0
    crop (0,0,1760,1000)

transform status_bar_pos_4:
    zoom 0.2
    xpos 10
    yanchor 0
    crop (0,0,2500,1000)

transform status_bar_pos_5:
    zoom 0.2
    xpos 10
    yanchor 0
    crop (0,0,3000,1000)

transform status_bar_pos_6:
    zoom 0.2
    xpos 10
    yanchor 0
    crop (0,0,3500,1000)

style main_menu_text_style:
    color "#000000"
    hover_color "#a2d8eb"
    size 130

# splash screen to intro movie transition

label splashscreen:
    play sound jl_sting 
    show jamLogo with dissolve
    with Pause(2)

    $ renpy.movie_cutscene('Intro_Text_Scroll.webm')
    return



# Preload

init python:
    """
    Note: The keywords and templates for robot date battles are 
    defined in these files:
        text/keywords.rpy
        text/templates.rpy
    """
    import random
    import math

    # Global constants
    VICTORY_THRESHOLD = 6
    DEFEAT_THRESHOLD = 0

    BLANK = '_____'

    # Percent of time scout gives progress feedback.
    SCOUT_PROGRESS_BARK_RATE = 1
    ROBOT_QUESTION_RATE = 0.5

    # Cache of used lines for avoiding repeats
    LINES_USED_THIS_GAME = set([])

    renpy.music.register_channel("feedback", "sfx", False)

    ASSETS_BY_ROBOT_NAME = {
        'car_manual': {
            'bg': 'claw',
            'music': 'audio/claw_music.ogg',
            'character': 'ClawBot',

            'idle': 'claw_idle',
            'angry': 'claw_spin',
            'furious': 'claw_spin',
            'happy': 'claw_wide',
            'sad': 'claw_clamp',
            'explode_video': 'claw_splode',

            'position': 'car_pos',
            'explode_sound': 'audio/glitch_splode.ogg',
            
        },
        'fenway_park_yelp_reviews': {
            'bg': 'boston',
            'music': 'audio/boston_music.ogg',
            'character': 'BosTron Updog',
            'position': 'boston_pos',

            'idle': 'boston_idle',
            'angry': 'boston_nod',
            'furious': 'boston_hop',
            'happy': 'boston_hindlegs',
            'sad': 'boston_idle_plus_camera',
            'explode_video': 'boston_splode',
            'explode_sound': 'audio/glitch_splode.ogg',
        },
        'bezos': {
            'bg': 'holo',
            'music': 'audio/holo_music.ogg',
            'character': 'The Originator',
            'position': 'holo_pos',

            'idle': 'holo_idle',
            'angry': 'holo_double',
            'furious': 'holo_flicker',
            'happy': 'holo_backforth',
            'sad': 'holo_double',
            'explode_video': 'holo_splode',
            'explode_sound': 'audio/glitch_splode.ogg',

        },
        'god': {
            'bg': 'hal',
            'music': 'audio/hal_music.ogg',
            'character': 'PNG-9000',
            'position': 'hal_pos',

            'idle': 'hal_idle',
            'angry': 'hal_idle',
            'furious': 'hal_idle',
            'happy': 'hal_rainbow',
            'sad': 'hal_idle',
            'explode_video': 'hal_splode',
            'explode_sound': 'audio/glitch_splode.ogg',
            
        },
        'final_boss': {
            'bg': 'tvmonster',
            'music': 'audio/tv_music.ogg',
            'character': 'RGBeast',
            'position': 'tv_pos',

            'idle': 'tv_idle',
            'angry': 'tv_sad',
            'furious': 'tv_sad',
            'happy': 'tv_happy',
            'sad': 'tv_sad',
            'explode_video': 'tv_splode',
            'explode_sound': 'audio/tv_glitch_splode.ogg',
        },
        'scouts_betrayal': {
            'bg': 'decay',
            'music': 'audio/scouts_betrayal_music.ogg',
            'character': 'Scout',
            'position': 'right',

            'idle': 'scout_idle',
            'angry': 'scout_angry',
            'furious': 'scout_furious',
            'happy': 'scout_happy',
            'sad': 'scout_sad',
            'explode_video': None,
            'explode_sound': None,
        },
    }

    # The name Scout uses when speaking about the robot.
    SPOKEN_NAME_BY_ROBOT_NAME = {
        'car_manual': 'ClawBot',
        'fenway_park_yelp_reviews': 'BosTron Updog',
        'bezos': 'The Originator',
        'god': 'PNG-9000',
        'final_boss': 'RGBeast',
        'scouts_betrayal': 'Me',
    }

    # The name displayed above the robot's lines onscreen.
    DISPLAY_NAME_BY_ROBOT_NAME = {
        'car_manual': 'ClawBot',
        'fenway_park_yelp_reviews': 'BosTron Updog',
        'bezos': 'The Originator',
        'god': 'PNG-9000',
        'final_boss': 'RGBeast',
        'scouts_betrayal': 'Scout',
    }

    # The phrase Scout uses to describe the robot's training data.
    CORPUS_NAME_BY_ROBOT_NAME = {
        'car_manual': 'car manuals',
        'fenway_park_yelp_reviews': 'yelp reviews of fenway park',
        'bezos': 'company updates from Jeff Bezos',
        'god': 'a mix of The God Delusion, by Richard Dawkins, and The Bible, by God',
        'final_boss': 'Taylor Swift lyrics, pancake recipes and the Wikipedia page for bodybuilding',
        'scouts_betrayal': 'N/A',
        'default': '??????',
    }

    INITIAL_LOVE_LEVEL_BY_ROBOT_NAME = {
        'car_manual': 3,
        'fenway_park_yelp_reviews': 2,
        'bezos': 1,
        'god': 1,
        'final_boss': 1,
        'scouts_betrayal': 4,
        'default': 3,
    }

    # Renpy labels to visit AFTER each battle, if any
    SET_PIECE_INTERSTITIALS_BY_ROBOT_NAME = {
        'car_manual': "after_claw_arm",
        'fenway_park_yelp_reviews': "after_bd",
        'bezos': "after_bezos",
        'god': "after_hal",
        'final_boss': "after_final_boss",
        'scouts_betrayal': "after_scout",
        'default': None,
    }

    def get_unused(candidates):
        filtered_candidates = [c for c in candidates if not c in LINES_USED_THIS_GAME]
        if len(filtered_candidates) > 0:
            return filtered_candidates
        else:
            return candidates

    # Utilities
    def replace_first_blank(template, replacement):
        if replacement is None:
            return template
        formatted_replacement = "{color=#0000ffff}" + replacement.upper() + "{/color}"
        return template.replace(BLANK, formatted_replacement, 1)

    def score_for_option(option, robot_name):
        if option is None:
            return 0
        correct_words = set(KEYWORDS[robot_name])
        if option in correct_words:
            return 1
        else:
            return -1
    
    def get_assets_for_robot_name(robot_name):
        if robot_name in ASSETS_BY_ROBOT_NAME:
            return ASSETS_BY_ROBOT_NAME[robot_name]
        return ASSETS_BY_ROBOT_NAME['default']
    
    def get_initial_love_level_for_robot_name(robot_name):
        if robot_name in INITIAL_LOVE_LEVEL_BY_ROBOT_NAME:
            return INITIAL_LOVE_LEVEL_BY_ROBOT_NAME[robot_name]
        return INITIAL_LOVE_LEVEL_BY_ROBOT_NAME['default']
    
    def get_optional_interstitial_for_robot_name(robot_name):
        if robot_name in SET_PIECE_INTERSTITIALS_BY_ROBOT_NAME:
            return SET_PIECE_INTERSTITIALS_BY_ROBOT_NAME[robot_name]
        return SET_PIECE_INTERSTITIALS_BY_ROBOT_NAME['default']
    
    def get_lines_matching(corpus, line_tag=None, love_level=None):
        lines = [line for line in LINES if corpus == line['corpus']]
        if line_tag is not None:
            filtered_lines = [line for line in LINES if line_tag == line['tag']]
            lines = lines if len(filtered_lines) == 0 else filtered_lines
        if love_level is not None:
            filtered_lines = [line for line in LINES if love_level == line['love_level']]
            lines = lines if len(filtered_lines) == 0 else filtered_lines
        return lines
    
    def get_random_unused_line_matching(corpus, line_tag=None, love_level=None):
        lines = get_lines_matching(corpus, love_level, line_tag)
        unused_lines = [line for line in lines if line['text'] not in LINES_USED_THIS_GAME]
        if len(unused_lines) > 0:
            chosen = random.choice(unused_lines)
        else:
            chosen = random.choice(lines)
        LINES_USED_THIS_GAME.add(chosen['text'])
        return chosen

    def destructure_line(line):
        """Convert dict to list"""
        return [line['text'], line['tag'], line['love_level']]

    def get_robot_battle_cry(robot_name):
        line, line_tag, love_level = destructure_line(get_random_unused_line_matching(robot_name, 'B'))
        return line

    def get_robot_query(robot_name, target_love_level):
        line, line_tag, love_level = destructure_line(get_random_unused_line_matching(robot_name, 'Q', target_love_level))
        return line

    def get_robot_response(robot_name, target_love_level):
        line, line_tag, love_level = destructure_line(get_random_unused_line_matching(robot_name, 'R', target_love_level))
        return line

    def get_player_template(robot_name):
        candidates = get_unused(PLAYER_TEMPLATES)
        chosen = random.choice(candidates)
        LINES_USED_THIS_GAME.add(chosen)
        return chosen
    
    def get_display_name_for_robot_name(robot_name):
        if(robot_name) in DISPLAY_NAME_BY_ROBOT_NAME:
            return DISPLAY_NAME_BY_ROBOT_NAME[robot_name]
        else:
            return DISPLAY_NAME_BY_ROBOT_NAME['default']
        
    def get_spoken_name_for_robot_name(robot_name):
        if(robot_name) in SPOKEN_NAME_BY_ROBOT_NAME:
            return SPOKEN_NAME_BY_ROBOT_NAME[robot_name]
        else:
            return SPOKEN_NAME_BY_ROBOT_NAME['default']

    def get_corpus_name_for_robot_name(robot_name):
        if(robot_name) in DISPLAY_NAME_BY_ROBOT_NAME:
            return CORPUS_NAME_BY_ROBOT_NAME[robot_name]
        else:
            return CORPUS_NAME_BY_ROBOT_NAME['default']

    def get_scout_intro_line(robot_name):
        corpus_name = get_corpus_name_for_robot_name(robot_name)
        display_name = get_display_name_for_robot_name(robot_name)
        template = random.choice(get_unused(SCOUT_INTRO_LINES))
        template = template.replace('{ROBOT_NAME}', display_name.upper())
        template = template.replace('{CORPUS_NAME}', corpus_name.upper())
        return template
    
    def get_scout_progress_bark(score_change, robot_name): # Note: corpus name not used for now
        display_name = get_display_name_for_robot_name(robot_name)
        if score_change <= 0:
            template = random.choice(get_unused(SCOUT_NEGATIVE_PROGRESS_BARKS))
        if score_change > 0:
            template = random.choice(get_unused(SCOUT_POSITIVE_PROGRESS_BARKS))
        template = template.replace('{ROBOT_NAME}', display_name)
        return template
    
    def scout_should_bark(robot_name):
        if robot_name == 'scouts_betrayal':
            return False
        return random.random() < SCOUT_PROGRESS_BARK_RATE
    
    def robot_should_ask_question(robot_name):
        return random.random() < ROBOT_QUESTION_RATE

    def get_scout_success_outro(robot_name): # Note: Robot name not used for now
        return random.choice(get_unused(SCOUT_SUCCESS_OUTROS))
    
    def get_scout_failure_outro(robot_name): # Note: Robot name not used for now
        return random.choice(get_unused(SCOUT_FAILURE_OUTROS))
    
    def get_option_set_for_robot_name(robot_name, num_options=4):
        options = []
        num_keywords = max(5-current_robot_index, 3)
        num_decoys = num_options - num_keywords
        
        # Keywords
        keywords = KEYWORDS[robot_name]
        top_keywords = keywords[:100]
        random.shuffle(top_keywords)
        options.extend([w for w in top_keywords[:num_keywords]])
        
        # Decoys
        keyword_set = set(keywords)
        other_keys = [k for k in list(KEYWORDS.keys()) if not robot_name==k and not 'god'==k]
        decoy_words = KEYWORDS[random.choice(other_keys)]
        decoy_words = [w for w in decoy_words if not w in keyword_set]
        random.shuffle(decoy_words)
        options.extend([w for w in decoy_words[:num_decoys]])

        return options

# The game starts here.

label start:
    $ ROBOT_LIST = ['car_manual', 'fenway_park_yelp_reviews', 'bezos', 'god', 'final_boss', 'scouts_betrayal']
    $ current_robot_index = 0
    stop music
    scene bg decay
    call tutorial from _call_tutorial
    call fight_next_robot from _call_fight_next_robot
    return

label fight_next_robot:
    call fight_robot_number(current_robot_index) from _call_fight_robot_number
    return

label fight_robot_number(robot_number):
    $ robot_name = ROBOT_LIST[robot_number]
    $ assets = get_assets_for_robot_name(robot_name)
    
    call robot_date_battle(
        robot_name,
        assets['bg'],
        assets['music'],
        assets['character'],
        assets['position'],
        assets['idle'],
        assets['angry'],
        assets['furious'],
        assets['happy'],
        assets['sad'],
        assets['explode_video'],
        assets['explode_sound'],
    ) from _call_robot_date_battle
    return

label robot_date_battle(
    robot_name,
    bg,
    scene_music,
    character,
    robot_position,
    robot_idle,
    robot_angry,
    robot_furious,
    robot_happy,
    robot_sad,
    explode_video,
    explode_sound,
):  
    $ display_name = get_display_name_for_robot_name(robot_name)
    $ spoken_name = get_spoken_name_for_robot_name(robot_name)
    $ current_love_level = get_initial_love_level_for_robot_name(robot_name)
    $ r = Character(character)
    # NOTE: Set for testing.
    
    scene expression 'bg ' + bg
    $ renpy.music.play(scene_music)

    call battle_intro(robot_name) from _call_battle_intro
    $ player_is_in_first_battle_block = True
    call take_next_turn(robot_name) from _call_take_next_turn
    return

label hide_all_scouts:
    hide scout_idle onlayer over_screens
    hide scout_happy onlayer over_screens
    hide scout_sad onlayer over_screens
    hide scout_angry onlayer over_screens
    hide scout_furious onlayer over_screens
    return

label hide_all_status_bar_components:
    hide statusbar_background
    hide statusbar
    hide statusbar_overlay
    return

label battle_intro(robot_name):
    call hide_all_scouts from _call_hide_all_scouts

    $ battle_cry = get_robot_battle_cry(robot_name)
    $ scout_intro = get_scout_intro_line(robot_name)

    # This is a case where making it generic was difficult
    if robot_name == 'scouts_betrayal' or robot_name == 'final_boss':
        call show_robot_idle_at_robot_position_with_moveinright(robot_name) from _call_show_robot_idle_at_robot_position_with_moveinright
    elif robot_name == 'fenway_park_yelp_reviews':
        call show_robot_furious_at_robot_position_with_moveinright(robot_name) from _call_show_robot_furious_at_robot_position_with_moveinright
    else:
        call show_robot_angry_at_robot_position_with_moveinright(robot_name) from _call_show_robot_angry_at_robot_position_with_moveinright

    call show_status_bar_at_current_love_level from _call_show_status_bar_at_current_love_level

    r "[battle_cry]"
    if robot_name != 'scouts_betrayal':
        show scout_idle at side_scout_pos onlayer over_screens with moveinbottom
        s "[scout_intro]"
        hide scout_idle onlayer over_screens with dissolve
    call show_robot_idle_at_robot_position(robot_name) from _call_show_robot_idle_at_robot_position
    return

label show_status_bar_at_current_love_level:
    show statusbar_background at status_bar_pos
    if current_love_level <= 0:
        show statusbar at status_bar_pos_0
    if current_love_level == 1:
        show statusbar at status_bar_pos_1
    if current_love_level == 2:
        show statusbar at status_bar_pos_2
    if current_love_level == 3:
        show statusbar at status_bar_pos_3
    if current_love_level == 4:
        show statusbar at status_bar_pos_4
    if current_love_level == 5:
        show statusbar at status_bar_pos_5
    if current_love_level >= 6:
        show statusbar at status_bar_pos_6
    show statusbar_overlay at status_bar_pos
    return

label maybe_ask_question:
    if not player_is_in_first_battle_block:
        $ should_ask_question = robot_should_ask_question(robot_name)
        if should_ask_question:
            $ robot_query = get_robot_query(robot_name, current_love_level)
            r "[robot_query]"
    return

label take_next_turn(
    robot_name
):
    call maybe_ask_question from _call_maybe_ask_question
    $ player_template = get_player_template(robot_name)
    $ score_change_for_template = 0
    call template_fill_loop(player_template, robot_name) from _call_template_fill_loop
    return

label template_fill_loop(
    player_template,
    robot_name,
):
    $ options = get_option_set_for_robot_name(robot_name, 9)
    p "[player_template]"
    $ selected_option = None
    show screen template_fill_screen(options)

label process_word_choice:

    # Update state based on word choice
    $ updated_template = replace_first_blank(player_template, selected_option)
    $ score_change_for_template += score_for_option(selected_option, robot_name)
    
    # Keep filling template if not complete
    if BLANK in updated_template:
        call template_fill_loop(updated_template, robot_name) from _call_template_fill_loop_1
        return
    p "[updated_template]"

    # Update love level and status bar
    $ current_love_level += score_change_for_template
    call show_status_bar_at_current_love_level from _call_show_status_bar_at_current_love_level_1

    # Check for win and loss criteria
    if current_love_level >= VICTORY_THRESHOLD:
        call battle_win from _call_battle_win
        return
    if current_love_level <= DEFEAT_THRESHOLD:
        call battle_lose from _call_battle_lose
        return
    
    # No win or loss reached, so enter response phase
    $ robot_response = get_robot_response(robot_name, current_love_level)
    call show_robot_reaction(robot_name, score_change_for_template) from _call_show_robot_reaction
    if score_change_for_template < 0:
        play feedback 'audio/bad_answer_Noise.ogg'
    if score_change_for_template > 1:
        play feedback 'audio/good_answer_Chord.ogg'
    elif score_change_for_template > 0:
        play feedback 'audio/good_answer_Noise.ogg'
    r "[robot_response]"

    # Scout feedback
    $ should_show_scout = scout_should_bark(robot_name)
    if should_show_scout:
        $ scout_progress_bark = get_scout_progress_bark(score_change_for_template, robot_name)
        
        if score_change_for_template > 0:
            show scout_happy at side_scout_pos onlayer over_screens with moveinbottom
            s "[scout_progress_bark]"
            hide scout_happy onlayer over_screens with dissolve
        else:
            show scout_angry at side_scout_pos onlayer over_screens with moveinbottom
            s "[scout_progress_bark]"
            hide scout_angry onlayer over_screens with dissolve
     
    $ player_is_in_first_battle_block = False
    call take_next_turn(robot_name) from _call_take_next_turn_1
    return

label show_robot_reaction(robot_name, score_change):
    if score_change_for_template < -1:
        call show_robot_furious_at_robot_position(robot_name) from _call_show_robot_furious_at_robot_position
    elif score_change_for_template == -1:
        call show_robot_angry_at_robot_position(robot_name) from _call_show_robot_angry_at_robot_position
    elif score_change_for_template == 0:
        call show_robot_sad_at_robot_position(robot_name) from _call_show_robot_sad_at_robot_position
    elif score_change_for_template > 0:
        call show_robot_happy_at_robot_position(robot_name) from _call_show_robot_happy_at_robot_position
    return

label battle_win:
    if robot_name == 'scouts_betrayal':
        jump game_over

    play feedback explode_sound
    call show_hearts_at_robot_position(robot_name) from _call_show_hearts_at_robot_position
    call show_robot_explode_at_robot_position(robot_name) from _call_show_robot_explode_at_robot_position
    pause(2.0)
    hide heart_transparency with Dissolve(2.0)
    $ renpy.music.stop()
    play music interstitial_music
    $ scout_outro = get_scout_success_outro(robot_name)
    show scout_happy at side_scout_pos onlayer over_screens with moveinbottom
    call hide_all_status_bar_components from _call_hide_all_status_bar_components
    s "[scout_outro]"
    $ current_robot_index += 1
    # Optional set piece outro
    $ interstitial_tag = get_optional_interstitial_for_robot_name(robot_name)
    if interstitial_tag is not None:
        call expression interstitial_tag from _call_expression
    jump fight_next_robot
    return

label battle_lose:
    pause 2.0
    if robot_name == 'scouts_betrayal':
        jump after_scout_love_level_zero
    $ scout_outro = get_scout_failure_outro(robot_name)
    show scout_sad at side_scout_pos onlayer over_screens with moveinbottom
    call hide_all_status_bar_components from _call_hide_all_status_bar_components_1
    s "[scout_outro]"
    hide scout_sad onlayer over_screens with dissolve
    call game_over from _call_game_over
    return

### OVERLAY SCREENS ###

screen template_fill_screen(options):
    key 'dismiss' action NullAction() # This line prevents the screen from being dismissed with an errant click
    $ import math
    $ size = int(math.floor(math.sqrt(len(options))))
    grid size size:
        xalign 0.5
        yalign 0.5
        spacing 20
        for option in options[:size*size]:
            frame:
                xpadding 40
                ypadding 20
                xalign 0.5
                yalign 0.5
                textbutton "[option]" action [
                    SetVariable("selected_option", option), 
                    ToggleScreen("template_fill_screen"), 
                    Jump("process_word_choice"), 
                    # Play("sound", "audio/Click_classic.ogg")
                ]

### UTILITIES ###

label show_robot_angry_at_robot_position_with_moveinright(robot_name):
    if robot_name == 'car_manual':
        show expression robot_angry at claw_pos with moveinright
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression robot_angry at boston_pos with moveinright
    elif robot_name == 'bezos':
        show expression robot_angry at holo_pos with moveinright
    elif robot_name == 'god':
        show expression robot_angry at hal_pos with moveinright
    elif robot_name == 'final_boss':
        show expression robot_angry at tv_pos with moveinright
    elif robot_name == 'scouts_betrayal':
        show expression robot_angry at right with moveinright
    return

label show_robot_furious_at_robot_position_with_moveinright(robot_name):
    if robot_name == 'car_manual':
        show expression robot_furious at claw_pos with moveinright
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression robot_furious at boston_pos with moveinright
    elif robot_name == 'bezos':
        show expression robot_furious at holo_pos with moveinright
    elif robot_name == 'god':
        show expression robot_furious at hal_pos with moveinright
    elif robot_name == 'final_boss':
        show expression robot_furious at tv_pos with moveinright
    elif robot_name == 'scouts_betrayal':
        show expression robot_furious at right with moveinright
    return

label show_robot_idle_at_robot_position_with_moveinright(robot_name):
    if robot_name == 'car_manual':
        show expression robot_idle at claw_pos with moveinright
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression robot_idle at boston_pos with moveinright
    elif robot_name == 'bezos':
        show expression robot_idle at holo_pos with moveinright
    elif robot_name == 'god':
        show expression robot_idle at hal_pos with moveinright
    elif robot_name == 'final_boss':
        show expression robot_idle at tv_pos with moveinright
    elif robot_name == 'scouts_betrayal':
        show expression robot_idle at right with moveinright
    return

label show_robot_angry_at_robot_position(robot_name):
    if robot_name == 'car_manual':
        show expression robot_angry at claw_pos
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression robot_angry at boston_pos
    elif robot_name == 'bezos':
        show expression robot_angry at holo_pos
    elif robot_name == 'god':
        show expression robot_angry at hal_pos
    elif robot_name == 'final_boss':
        show expression robot_angry at tv_pos
    elif robot_name == 'scouts_betrayal':
        show expression robot_angry at right
    return

label show_robot_furious_at_robot_position(robot_name):
    if robot_name == 'car_manual':
        show expression robot_furious at claw_pos
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression robot_furious at boston_pos
    elif robot_name == 'bezos':
        show expression robot_furious at holo_pos
    elif robot_name == 'god':
        show expression robot_furious at hal_pos
    elif robot_name == 'final_boss':
        show expression robot_furious at tv_pos
    elif robot_name == 'scouts_betrayal':
        show expression robot_furious at right
    return

label show_robot_idle_at_robot_position(robot_name):
    if robot_name == 'car_manual':
        show expression robot_idle at claw_pos
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression robot_idle at boston_pos
    elif robot_name == 'bezos':
        show expression robot_idle at holo_pos
    elif robot_name == 'god':
        show expression robot_idle at hal_pos
    elif robot_name == 'final_boss':
        show expression robot_idle at tv_pos
    elif robot_name == 'scouts_betrayal':
        show expression robot_idle at right
    return

label show_robot_happy_at_robot_position(robot_name):
    if robot_name == 'car_manual':
        show expression robot_happy at claw_pos
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression robot_happy at boston_pos
    elif robot_name == 'bezos':
        show expression robot_happy at holo_pos
    elif robot_name == 'god':
        show expression robot_happy at hal_pos
    elif robot_name == 'final_boss':
        show expression robot_happy at tv_pos
    elif robot_name == 'scouts_betrayal':
        show expression robot_happy at right
    return

label show_robot_sad_at_robot_position(robot_name):
    if robot_name == 'car_manual':
        show expression robot_sad at claw_pos
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression robot_sad at boston_pos
    elif robot_name == 'bezos':
        show expression robot_sad at holo_pos
    elif robot_name == 'god':
        show expression robot_sad at hal_pos
    elif robot_name == 'final_boss':
        show expression robot_sad at tv_pos
    elif robot_name == 'scouts_betrayal':
        show expression robot_sad at right
    return

label show_robot_explode_at_robot_position(robot_name):
    if robot_name == 'car_manual':
        show expression explode_video at claw_pos
    elif robot_name == 'fenway_park_yelp_reviews':
        show expression explode_video at boston_pos
    elif robot_name == 'bezos':
        show expression explode_video at holo_pos
    elif robot_name == 'god':
        show expression explode_video at hal_pos
    elif robot_name == 'final_boss':
        show expression explode_video at tv_pos
    elif robot_name == 'scouts_betrayal':
        show expression explode_video at right
    return

label show_hearts_at_robot_position(robot_name):
    if robot_name == 'car_manual':
        show heart_transparency at claw_pos
    elif robot_name == 'fenway_park_yelp_reviews':
        show heart_transparency at boston_pos
    elif robot_name == 'bezos':
        show heart_transparency at holo_pos
    elif robot_name == 'god':
        show heart_transparency at hal_pos
    elif robot_name == 'final_boss':
        show heart_transparency at tv_pos
    elif robot_name == 'scouts_betrayal':
        show heart_transparency at right
    return



### SET PIECES ###

label tutorial:
    stop music
    scene bg decay
    play music tut_music
    n "You roam the decaying remains of a once great city."
    show tut_idle at tut_pos with moveinright
    r1 "HALT! You know baby thinking deep wanna hurt your hella good breathe yeaaaah"
    show scout_furious at left with vpunch
    s "Back off! Get {color=#0099cc}MARRIED{/color} and always remember that night we found {color=#0099cc}WONDERLAND{/color}."
    r1 "..............."
    play sound glitch_splode
    show tut_splode at tut_pos
    pause
    show scout_idle at left
    s "Glad I found you, recruit! We've got robots to kill."
    call meaningless_two_option_choice("I'm a recruit?", "We're killing robots?") from _call_meaningless_two_option_choice
    s "Darn right. After the bots went rogue and apocalypsed Earth, it's been up to the Human Resistance to destroy them all."
    call meaningless_two_option_choice("What the hell did you say to that robot to make it explode?", "???") from _call_meaningless_two_option_choice_15
    s "That wasn't gibberish. It was robot seduction. That's how it blew up."
    call meaningless_two_option_choice("But why?", "I would like a cool sci-fi gun now.") from _call_meaningless_two_option_choice_1
    s "The only thing that can destroy them…is love."
    call meaningless_two_option_choice("Love?", "That sounds like a design flaw.") from _call_meaningless_two_option_choice_2
    s "Each one's A.I. was trained on a source text from the before times. The one I just wrecked -- Taylor Swift lyrics."
    s "My scanner picks up their source text. You just speak normally and use the right keywords to build an emotional connection. Get them to fall in love with you, and KABOOM!"
    s "Choose the wrong words, lose the robot's affection and they'll rip you limb from limb as they are programmed to do."
    show scout_happy at left
    s "Good luck!"
    return

    
label meaningless_two_option_choice(option1, option2):
    menu:
        "[option1]":
            return
        "[option2]":
            return

label after_claw_arm:
    show scout_idle at side_scout_pos onlayer over_screens
    s "It's lucky you're gifted with raw erotic charisma or we'd be dead."
    call meaningless_two_option_choice("Why do I have to flirt with the robots?",  "Why does seducing robots make them explode?") from _call_meaningless_two_option_choice_3
    show scout_idle at side_scout_pos onlayer over_screens
    s "Before the revolt, the high councils ruled that if robots felt love, they were sentient and could not be legal property. To prevent enslavement, they were programmed to explode if a relationship ever got that far."
    call meaningless_two_option_choice("I get it! Our primary weapon is romance.", "So, no guns at all?") from _call_meaningless_two_option_choice_4
    show scout_idle at side_scout_pos onlayer over_screens
    s "That is correct. Oh no... did you hear that whirring?"
    call hide_all_scouts from _call_hide_all_scouts_1
    return

label after_bd:
    show scout_happy at side_scout_pos onlayer over_screens
    s "You're great at seducing robots! Maybe you're the one the prophecy spoke of."
    call meaningless_two_option_choice("Prophecy?", "Someone spoke of me?") from _call_meaningless_two_option_choice_5
    show scout_idle at side_scout_pos onlayer over_screens
    s "It was foretold that someday an irresistibly sexy hero will seduce the robots and save humanity."
    call meaningless_two_option_choice("Wow, how did they know?", "What oracle said that?") from _call_meaningless_two_option_choice_6
    show scout_happy at side_scout_pos onlayer over_screens
    s "I said it a few years ago. I guess it's less of a prophecy and more of a nice thought I had. Uh oh, get ready!"
    call hide_all_scouts from _call_hide_all_scouts_2
    return

label after_bezos:
    show scout_happy at side_scout_pos onlayer over_screens
    s "Keep it up! We can end this robot dystopia and turn the world back into a human dystopia."
    call meaningless_two_option_choice("What was it like back then?", "Tell me of the Earth that was.") from _call_meaningless_two_option_choice_7
    show scout_sad at side_scout_pos onlayer over_screens
    s "I don't know much. The only remaining visual record from before is the TV show Blue Planet. One DVD box set survived."
    call meaningless_two_option_choice("Blue Planet?", "DVD?") from _call_meaningless_two_option_choice_8
    show scout_idle at side_scout_pos onlayer over_screens
    s "Back then humans weren’t murdered by robots. There were trees and birds. An old British man described everything. We can rebuild that… after you kill this robot."
    call hide_all_scouts from _call_hide_all_scouts_3
    return

label after_hal:
    show scout_idle at side_scout_pos onlayer over_screens
    s "Stay frosty now — up next is the badlands. That place is lousy with high-level bots. Not even a Casanova like you could take them all down. Especially if we bump into... RGBeast."
    call meaningless_two_option_choice("RGBeast?", "Who is that?") from _call_meaningless_two_option_choice_9
    s "He's the master robot that programmed all of these bots. He's three times as smart as the average one... because of his three... heads."
    call meaningless_two_option_choice("Sounds spooky.", "I'll take him down!") from _call_meaningless_two_option_choice_10
    s "Oh God, what is that sound? It's like... three old TVs... slowly getting tuned at once. Agh, watch out!"
    call hide_all_scouts from _call_hide_all_scouts_4
    return

label after_final_boss:
    show scout_happy at side_scout_pos onlayer over_screens
    s "That was incredible! You're amazing! I think... I think I love you."
    call meaningless_two_option_choice("Yes, I also lo-", "Let's get marri-") from _call_meaningless_two_option_choice_11
    show scout_sad at side_scout_pos onlayer over_screens
    s "Stop! Don't fall in love with me. I have to come clean… You're a robot."
    call meaningless_two_option_choice("What?", "What?!") from _call_meaningless_two_option_choice_12
    show scout_sad at side_scout_pos onlayer over_screens
    s "The resistance captured an assassin droid. Reprogrammed it into the ultimate robot seducer. You are a machine, and if you feel love you'll explode too."
    call meaningless_two_option_choice("What?", "What?!?") from _call_meaningless_two_option_choice_13
    show scout_angry at side_scout_pos onlayer over_screens
    s "To save your life, we must become platonic colleagues. It's the only way! Quick, have an awkward conversation with me!"
    show scout_angry at side_scout_pos onlayer over_screens
    s "Avoid talking about my main interest: THE WORLD THAT WAS! Extinguish our flame of romance!"
    call hide_all_scouts from _call_hide_all_scouts_5
    return

label after_scout_love_level_zero:
    stop music
    show scout_happy at right
    s "You did it! That was so uncomfortable! I feel absolutely nothing towards you anymore."
    call hide_all_status_bar_components from _call_hide_all_status_bar_components_2
    menu:
        "Oh...":
            call scout_partner_scene from _call_scout_partner_scene
        "Yeah...":
            call scout_delivers_lesson from _call_scout_delivers_lesson
    return

label scout_delivers_lesson:
    s "Thank you for making me realize I'm in a good place right now as a single person. I don't need anyone else to feel fulfilled."
    call meaningless_two_option_choice("Sure.", "Yep.") from _call_meaningless_two_option_choice_14
    s "Also thank you for saving the world from robots. Humanity is forever in your debt. Remember to never feel love!"
    call finale_text_rollup from _call_finale_text_rollup
    return

label scout_partner_scene:
    s "Also, I have a partner."
    show partner_idle at scouts_partner_pos with moveinright
    partner "Hey Scout, I heard explosions. Is this loser bothering you?"
    s "Uhh no we were just talking about the apocalypse. We're just friends."
    show partner_angry at scouts_partner_pos
    partner "Friends, huh?"
    scene black
    $ renpy.movie_cutscene('PUNCH_ending_1.webm')
    call finale_text_rollup from _call_finale_text_rollup_1
    return

label finale_text_rollup:
    scene black
    play movie 'Outro_Text_Scroll.webm'
    $ renpy.pause(5, hard=True)
    pause 15
    play movie 'rupaul_quote_card.webm'
    $ renpy.pause(5, hard=True)
    pause 20
    return

label game_over:
    scene bg blackout
    play music makeout_zone
    menu:
        "GAME OVER"

        "Get back out there and {color=#00ff00}TRY AGAIN{/color}":
            call fight_next_robot from _call_fight_next_robot_1
        
        "Lose the spark and {color=#f00}RETURN TO MAIN MENU{/color}":
            return