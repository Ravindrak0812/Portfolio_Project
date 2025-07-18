{% extends 'base.html' %}
{% block title %}About{% endblock title %}
{% block stylecss %}
{% load static %}
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css" rel="stylesheet">

<style>
    body {
        background-color: #ffffff;
        color: #333333;
        font-family: 'Roboto', sans-serif;
        line-height: 1.8;
    }

    .about {
        padding: 80px 0;
    }

    .section-title h2 {
        color: #2c3e50;
        font-size: 2.5rem;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 20px;
        position: relative;
        display: inline-block;
    }

    .section-title h2:after {
        content: '';
        position: absolute;
        width: 60%;
        height: 3px;
        background: #3498db;
        bottom: -10px;
        left: 0;
    }

    .section-title p {
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-top: 20px;
    }

    .img-fluid {
        border-radius: 10px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
        width: 80%;
        margin: 0 auto;
        border: 5px solid #ecf0f1;
    }

    .content h3 {
        font-size: 2rem;
        color: #2c3e50;
        margin-bottom: 20px;
        text-transform: uppercase;
        font-weight: 700;
    }

    .content .fst-italic {
        color: #7f8c8d;
        font-size: 1.1rem;
        margin-bottom: 30px;
        font-style: italic;
        border-left: 3px solid #3498db;
        padding-left: 15px;
    }

    .content ul {
        list-style: none;
        padding: 0;
    }

    .content ul li {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
        padding: 10px;
        border-radius: 5px;
        transition: all 0.3s ease;
    }

    .content ul li:hover {
        background-color: #f8f9fa;
        transform: translateX(5px);
    }

    .content ul li i {
        color: #3498db;
        margin-right: 10px;
        width: 25px;
        text-align: center;
    }

    /* Skills Section */
    .skills-container {
        max-width: 800px;
        margin: 30px auto 0;
    }

    .skills-title {
        text-align: center;
        margin-bottom: 20px;
    }

    .skills-icons {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        justify-content: center;
        align-items: center;
    }

    .skill-item {
        position: relative;
        width: 40px;
        height: 40px;
    }

    .skills-icons img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        transition: all 0.3s ease;
        filter: grayscale(20%);
    }

    .skills-icons img:hover {
        transform: scale(1.2);
        filter: grayscale(0%);
    }

    .learning-badge {
        position: absolute;
        top: -5px;
        right: -5px;
        background-color: #e74c3c;
        color: white;
        padding: 2px 4px;
        border-radius: 8px;
        font-size: 0.5rem;
        font-weight: bold;
        z-index: 1;
    }

    /* Professional badge */
    .current-position {
        background-color: #3498db;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        margin-left: 10px;
        vertical-align: middle;
    }

    /* Timeline */
    .timeline {
        position: relative;
        margin: 30px 0;
    }

    .timeline:before {
        content: '';
        position: absolute;
        top: 0;
        left: 18px;
        height: 100%;
        width: 2px;
        background: #3498db;
    }

    .timeline-item {
        margin-bottom: 30px;
        position: relative;
        padding-left: 50px;
    }

    .timeline-dot {
        position: absolute;
        left: 10px;
        top: 5px;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: #3498db;
        border: 3px solid white;
    }

    .timeline-date {
        font-size: 0.9rem;
        color: #7f8c8d;
        margin-bottom: 5px;
    }

    .timeline-title {
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 5px;
    }

    .timeline-company {
        color: #3498db;
        font-weight: 500;
    }

    .timeline-description {
        color: #7f8c8d;
        font-size: 0.95rem;
    }

    .section-divider {
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(52, 152, 219, 0), rgba(52, 152, 219, 0.75), rgba(52, 152, 219, 0));
        margin: 40px 0;
    }

    .back-to-top {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 50%;
        padding: 15px;
        font-size: 24px;
        cursor: pointer;
        display: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        z-index: 99;
    }

    .back-to-top:hover {
        background-color: #2980b9;
        transform: translateY(-3px);
    }

</style>
{% endblock stylecss %}

{% block body %}
<section id="about" class="about">
    <div class="container">
        <div class="section-title text-center" data-aos="fade-up">
            <h2>About Me</h2>
            <p>Hi 👋, I'm Ravindra Kumar<br>Data Engineer at Kfintech Technologies</p>
        </div>

        <div class="row align-items-center">
            <div class="col-lg-4" data-aos="fade-right">
                <img style="border-radius:20%" height="300px" width="300px" src="{% static 'assets/img/ravi1.jpg' %}" class="img-fluid" alt="Profile Image">
            </div>
            <div class="col-lg-8 pt-4 pt-lg-0 content" data-aos="fade-left">
                <h3>Data Engineer <span class="current-position">Currently Working</span></h3>
                <p class="fst-italic">
                    "Transforming raw data into meaningful insights. Building robust data pipelines and architectures to empower data-driven decision making. Passionate about cloud technologies and scalable data solutions."
                </p>

                <div class="row">
                    <div class="col-lg-6">
                        <ul>
                            <li data-aos="fade-up"><i class="fas fa-birthday-cake"></i> <strong>Birthday:</strong> <span>08 Dec 2003</span></li>
                            <li data-aos="fade-up"><i class="fas fa-briefcase"></i> <strong>Company:</strong> <span>Kfintech Technologies</span></li>
                            <li data-aos="fade-up"><i class="fas fa-phone"></i> <strong>Phone:</strong> <span>+91 9115344392</span></li>
                            <li data-aos="fade-up"><i class="fas fa-map-marker-alt"></i> <strong>Location:</strong> <span>India</span></li>
                        </ul>
                    </div>
                    <div class="col-lg-6">
                        <ul>
                            <li data-aos="fade-up"><i class="fas fa-user"></i> <strong>Age:</strong> <span>22</span></li>
                            <li data-aos="fade-up"><i class="fas fa-graduation-cap"></i> <strong>Education:</strong> <span>Master Of Computer Application</span></li>
                            <li data-aos="fade-up"><i class="fas fa-envelope"></i> <strong>Email:</strong> <span>ravindrak0812@gmail.com</span></li>
                            <li data-aos="fade-up"><i class="fas fa-calendar-alt"></i> <strong>Experience:</strong> <span>1+ Years</span></li>
                        </ul>
                    </div>
                </div>

                <!-- Experience Timeline -->
                <div class="experience mt-5">
                    <h4 data-aos="fade-up">Professional Journey</h4>
                    <div class="timeline">
                        <div class="timeline-item" data-aos="fade-up">
                            <div class="timeline-dot"></div>
                            <div class="timeline-date">June 2024 - Present</div>
                            <div class="timeline-title">Data Engineer Intern</div>
                            <div class="timeline-company">Kfintech Technologies</div>
                            <div class="timeline-description">
                                Working on building and optimizing data pipelines, implementing ETL processes, and contributing to data architecture solutions.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <hr class="section-divider">

        <!-- Compact Technical Skills Section -->
        <div class="skills-container" data-aos="fade-up">
            <h4 class="skills-title">Technical Skills</h4>
            <div class="skills-icons">
                <!-- Row 1 -->
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" title="Google Cloud">
                    <span class="learning-badge">Learn</span>
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg" title="AWS">
                    <span class="learning-badge">Learn</span>
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="Python">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" title="MySQL">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apache/apache-original.svg" title="Apache">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" title="Java">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" title="C++">
                </div>
                
                <!-- Row 2 -->
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" title="Django">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" title="HTML5">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" title="CSS3">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" title="JavaScript">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" title="Bootstrap">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" title="Git">
                </div>
                <div class="skill-item" data-aos="zoom-in">
                    <img height="30px" width="30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" title="GitHub">
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Back to Top Button -->
<button class="back-to-top" id="back-to-top-btn"><i class="fas fa-arrow-up"></i></button>

<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
<script>
    AOS.init({ duration: 1000 });
    
    // Back to Top Button
    const backToTopBtn = document.getElementById('back-to-top-btn');
    window.onscroll = function() {
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
            backToTopBtn.style.display = "block";
        } else {
            backToTopBtn.style.display = "none";
        }
    };
    backToTopBtn.onclick = function() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    };
</script>
{% endblock body %}