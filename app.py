from flask import Flask, render_template

app = Flask(__name__)

# Portfolio Data
PROJECTS = [
    {
        "id": 1,
        "title": "SwiftDeploy Core",
        "category": "DevOps",
        "description": "Automated deployments across multi-cloud infrastructure (Vercel, Netlify, AWS, Render). Orchestrated build hooks and webhook notifications.",
        "tags": ["React", "C#", "MongoDB", "Docker"],
        "github": "https://github.com/example/swiftdeploy-core",
        "demo": "https://example.com/swiftdeploy",
        "color_class": "gradient-purple"
    },
    {
        "id": 2,
        "title": "Apex Stock Engine",
        "category": "Finance",
        "description": "Real-time stock dashboard using WebSockets and statistical regression. Displays predictive trends for major financial assets.",
        "tags": ["Python", "Pandas", "Flask", "Chart.js"],
        "github": "https://github.com/example/stock-engine",
        "demo": "https://example.com/stocks",
        "color_class": "gradient-blue"
    },
    {
        "id": 3,
        "title": "Helios Smart Home",
        "category": "IoT",
        "description": "Cross-platform interface to regulate IoT smart thermostats and lighting based on environmental ambient light levels.",
        "tags": ["Flutter", "FastAPI", "PostgreSQL", "C++"],
        "github": "https://github.com/example/helios-iot",
        "demo": "https://example.com/helios",
        "color_class": "gradient-gold"
    },
    {
        "id": 4,
        "title": "Quantum Cryptography",
        "category": "Security",
        "description": "Prototype simulation demonstrating quantum key distribution (QKD) using BB84 protocol model visualization.",
        "tags": ["Python", "Numpy", "Qiskit", "WebGL"],
        "github": "https://github.com/example/quantum-crypto",
        "demo": "https://example.com/quantum",
        "color_class": "gradient-red"
    },
    {
        "id": 5,
        "title": "OmniSearch Agent",
        "category": "AI / ML",
        "description": "Semantic searching crawler indexing academic papers using OpenAI embeddings and Pinecone vector database.",
        "tags": ["Python", "OpenAI", "Pinecone", "Next.js"],
        "github": "https://github.com/example/omnisearch",
        "demo": "https://example.com/omni",
        "color_class": "gradient-emerald"
    },
    {
        "id": 6,
        "title": "Scribe Collaborative Editor",
        "category": "Web Apps",
        "description": "Real-time document editor using operational transformations, enabling concurrent editing and auto-syncing storage.",
        "tags": ["Node.js", "Express", "Socket.io", "Redis"],
        "github": "https://github.com/example/scribe-editor",
        "demo": "https://example.com/scribe",
        "color_class": "gradient-orange"
    }
]

SKILLS = [
    {"name": "Python", "category": "Languages", "proficiency": 95},
    {"name": "JavaScript / TypeScript", "category": "Languages", "proficiency": 90},
    {"name": "C# (.NET)", "category": "Languages", "proficiency": 80},
    {"name": "HTML5 / CSS3", "category": "Languages", "proficiency": 95},
    {"name": "Flask / Django / FastAPI", "category": "Frameworks", "proficiency": 90},
    {"name": "React / Next.js", "category": "Frameworks", "proficiency": 85},
    {"name": "Docker & Kubernetes", "category": "DevOps & Cloud", "proficiency": 85},
    {"name": "Git & CI/CD Pipelines", "category": "DevOps & Cloud", "proficiency": 90},
    {"name": "PostgreSQL / MongoDB / Redis", "category": "Databases", "proficiency": 85},
]

TIMELINE = [
    {
        "type": "experience",
        "year": "2024 - Present",
        "title": "Senior Solutions Engineer",
        "subtitle": "SwiftDeploy Technologies",
        "details": "Engineered multi-tenant deployment gateways. Integrated OAuth providers, serverless runner orchestration, and automated health checks."
    },
    {
        "type": "experience",
        "year": "2022 - 2024",
        "title": "Full Stack Software Developer",
        "subtitle": "NexaCloud Innovations",
        "details": "Developed custom microservices in Flask and Node.js. Designed sleek user dashboard UI elements with modern CSS, improving customer signups by 24%."
    },
    {
        "type": "education",
        "year": "2018 - 2022",
        "title": "B.S. in Computer Science",
        "subtitle": "Apex Tech University",
        "details": "Specialized in Software Engineering and Distributed Systems. Graduated with Honors."
    }
]

@app.route("/")
def index():
    # Render main home template
    return render_template("index.html")

@app.route("/projects/")
def projects():
    # Extract unique categories for filtering
    categories = sorted(list(set(proj["category"] for proj in PROJECTS)))
    return render_template("projects.html", projects=PROJECTS, categories=categories)

@app.route("/skills/")
def skills():
    return render_template("skills.html", skills=SKILLS, timeline=TIMELINE)

@app.route("/contact/")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
