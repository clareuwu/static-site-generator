from ast import parse
from markdown2 import markdown
import os
import caldav
from jinja2 import Template

"""
Commandline arguments - input_dir output_dir 
TODO
Add templating
Add css formatting
[[]] Links
Home page
"""

def get_templates():
    templates = dict()
    templates['layout'] = open("templates/layout.html").read()
    templates['header'] = open("templates/header.html").read()
    templates['nav'] = open("templates/nav.html").read()
    templates['body'] = open("templates/body.html").read()
    templates['footer'] = open("templates/footer.html").read()
    return templates
    
def process_frontmatter(file):
    pass

def parse_md(file):
    parsed_md = markdown(file.read(), extras=[
        'metadata', 'break-on-newline', 'code-friendly', 
        'fenced-code-blocks', 'smarty-pants', 'spoiler', 'target-blank-links', 'tables', 'task_list'
        ])
    return parsed_md

# what kind of content do we want?
# home page, personal site
# projects/github/portfolio page
# 
def get_output_name(file):
    out = file.split('.')[0]
    out = f'output/{out}.html'
    return out

def save_file(filename, text):
    print(filename)
    dir = '/'.join(filename.split('/')[:-1])
    if not os.path.exists(dir):
        os.makedirs(dir)
    print(filename)
    f = open(filename, 'w')
    f.write(text)
    f.close()


# should probably do something like
# process() - processes a single, non home page file
def process():
    layout = get_templates()
    layout_template = Template(layout['layout'])
    for subdir, dirs, files in os.walk('content'):
        for file in files:
            with open(os.path.join(subdir, file), 'r') as cur:
                parsed_md = parse_md(cur)


                templated = layout_template.render({
                    'header': layout['header'], 
                    'nav': layout['nav'],
                    'body': parsed_md,
                    'footer': layout['footer']
                    })
                templated_name = get_output_name(os.path.join(subdir, file))
                save_file(templated_name, templated)

process()