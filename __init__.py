from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Hindustani Classical Raagas Blog",
        "thumb":"img/hindustani2.jpeg",
        "hero": "img/hindustani1.jpeg",
        "categories": ["Python", "Django", "HTML", "CSS"],
        "slug": "hindustani-raagas",
        "source-code":"https://github.com/ganesh-shet/hindustani-raagas-blog"
    },

     {
        "name": "Micro Blog Flask",
        "thumb":"img/MBFlask1.jpeg",
        "hero": "img/MBFlask2.png",
        "categories": ["Python", "Flask", "HTML", "CSS"],
        "slug": "micro-blog-flask",
        "source-code":"https://github.com/ganesh-shet/micro-blog-flask"
    },

    {
        "name": "AI Virtual Mouse",
        "thumb":"img/vmouse1jpeg.jpeg",
        "hero": "img/vmouse2.jpeg",
        "categories": ["Python", "Open-CV"],
        "slug": "ai-virtual-mouse",
        "source-code":"https://github.com/ganesh-shet/AI-Virtual-Mouse"
    },

    {
        "name": "Brain Tumor Detection",
        "thumb":"img/tumor2.jpeg",
        "hero": "img/tumor1.jpeg",
        "categories": ["Python", "Open-CV", "AI-ML", "Neural Networks"],
        "slug": "brain-tumor-detection",
        "source-code":"https://github.com/MohamedAliHabib/Brain-Tumor-Detection"
    },
]

slug_to_projects = { project['slug']: project for project in projects }

@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_projects:
        abort(404)

    return render_template(f"project_{slug}.html", project=slug_to_projects[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404