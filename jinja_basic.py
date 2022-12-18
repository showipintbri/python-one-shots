from jinja2 import Template

def create_index_html(in_data,template_html,out_html):
    jinja2_template_string = open(template_html, 'rt').read()

    template = Template(jinja2_template_string)

    html_template_string = template.render(data=in_data)

    with open(out_html, 'wt') as index_html:
        index_html.write(html_template_string)
    
    return None

