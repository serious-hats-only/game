import json


def generate_file(variable_name):
    path = f'lines/{variable_name}.txt'
    prefix = f"""init python:
    {variable_name.upper()} = """
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
    with open(f'output/{variable_name}.rpy', 'w') as f:
        f.write(prefix + json.dumps(lines)+'\n')

generate_file('player_templates')
generate_file('scout_intro_lines')
generate_file('scout_failure_outros')
generate_file('scout_success_outros')
generate_file('scout_positive_progress_barks')
generate_file('scout_negative_progress_barks')