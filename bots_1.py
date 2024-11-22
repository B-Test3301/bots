import os

def generate_bot_script(template_file, output_dir, num_scripts):
    with open(template_file, 'r') as file:
        template = file.read()

    for i in range(num_scripts):
        script_name = f'bot_{i}.py'
        output_file = os.path.join(output_dir, script_name)
        with open(output_file, 'w') as file:
            file.write(template)

# Usage example
template_file = 'bot_1.py'
output_dir = 'bots'
num_scripts = 10

generate_bot_script(template_file, output_dir, num_scripts)
