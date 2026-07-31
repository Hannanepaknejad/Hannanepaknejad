# -*- coding: utf-8 -*-
import os

OUT = "/home/claude/phantom-final"

CATEGORIES = ["Residential", "Commercial", "Cultural", "Urban", "Interior", "Educational"]
YEARS = ["2022", "2023", "2024", "2025"]
STYLES = ["style1", "style2", "style3", "style4", "style5", "style6",
          "style2", "style3", "style1", "style5", "style6", "style4"]

def project_meta(i):
    return {
        "n": i,
        "code": f"P{i:02d}",
        "cat": CATEGORIES[(i - 1) % len(CATEGORIES)],
        "year": YEARS[(i - 1) % len(YEARS)],
        "title": f"Project {i:02d}",
        "file": f"project-{i:02d}.html",
        "img": f"images/pic{((i - 1) % 15) + 1:02d}.jpg",
        "style": STYLES[(i - 1) % len(STYLES)],
    }

PROJECTS = [project_meta(i) for i in range(1, 13)]

HEADER = '''<!-- Header -->
			<header id="header">
				<div class="inner">

					<!-- Logo -->
						<a href="index.html" class="logo">
							<span class="symbol"><img src="images/HANA1.png" alt="HANA logo" /></span><span class="title">Hannane Paknejad</span>
						</a>

					<!-- Nav -->
						<nav>
							<ul>
								<li><a href="#menu">Menu</a></li>
							</ul>
						</nav>

				</div>
			</header>

		<!-- Menu -->
			<nav id="menu">
				<h2>Menu</h2>
				<ul>
					<li><a href="index.html">Home</a></li>
					<li><a href="about.html">About</a></li>
				</ul>
			</nav>
'''

def footer():
    return '''<!-- Footer -->
			<footer id="footer">
				<div class="inner">
					<section>
						<h2>Get in touch</h2>
						<form method="post" action="#">
							<div class="fields">
								<div class="field half">
									<input type="text" name="name" id="name" placeholder="Name" />
								</div>
								<div class="field half">
									<input type="email" name="email" id="email" placeholder="Email" />
								</div>
								<div class="field">
									<textarea name="message" id="message" placeholder="Message"></textarea>
								</div>
							</div>
							<ul class="actions">
								<li><input type="submit" value="Send" class="primary" /></li>
							</ul>
						</form>
					</section>
					<section>
						<h2>Follow</h2>
						<ul class="icons">
							<li><a href="https://www.instagram.com/hannane.paknejad/" target="_blank" rel="noopener" class="icon brands style2 fa-instagram"><span class="label">Instagram</span></a></li>
							<li><a href="https://www.linkedin.com/in/hannane-paknejad/" target="_blank" rel="noopener" class="icon brands style2 fa-linkedin-in"><span class="label">LinkedIn</span></a></li>
							<li><a href="mailto:hannanepaknejad@gmail.com" class="icon solid style2 fa-envelope"><span class="label">Email</span></a></li>
						</ul>
					</section>
					<ul class="copyright">
						<li>&copy; Hannane Paknejad. All rights reserved</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
					</ul>
				</div>
			</footer>

		</div>

	<!-- Scripts -->
		<script src="assets/js/jquery.min.js"></script>
		<script src="assets/js/browser.min.js"></script>
		<script src="assets/js/breakpoints.min.js"></script>
		<script src="assets/js/util.js"></script>
		<script src="assets/js/main.js"></script>

</body>
</html>
'''

def page_start(title, extra_head=""):
    return f'''<!DOCTYPE HTML>
<!--
	Phantom by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
	Personalized for Hannane Paknejad — Architecture Portfolio
-->
<html>
	<head>
		<title>{title} - Hannane Paknejad</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
		{extra_head}
	</head>
	<body class="is-preload">
		<!-- Wrapper -->
			<div id="wrapper">

				{HEADER}
'''

# ---------------- index.html ----------------
tiles = []
for p in PROJECTS:
    tiles.append(f'''				<article class="{p['style']}">
					<span class="image">
						<img src="{p['img']}" alt="" />
					</span>
					<a href="{p['file']}">
						<h2>{p['title']}</h2>
						<div class="content">
							<p>{p['cat']} — {p['year']}. Replace this line with a one-sentence summary of the project.</p>
						</div>
					</a>
				</article>''')

tiles_html = "\n".join(tiles)

index_html = page_start("Home") + f'''
				<!-- Main -->
					<div id="main">
						<div class="inner">
							<header>
								<h1>I'm Hannane Paknejad, an architect who turns<br />
								ideas into livable, thoughtful spaces.</h1>
								<p>I design residential, commercial, and cultural spaces with an emphasis on light, proportion, and material honesty. Each project starts with a question — how people will actually move through and live in the space — and the design follows from there. Below is a selection of my recent work.</p>
							</header>
							<section class="tiles">
{tiles_html}
							</section>
						</div>
					</div>

				''' + footer()

with open(f"{OUT}/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

# ---------------- about.html ----------------
ABOUT_STYLE = '''<style>
  .about-photo {
    height: 360px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
    background-image: url('images/about-by.jpg');
    background-size: cover;
    background-position: center;
    border-radius: 6px;
  }
  .about-photo__logo {
    width: 300px;
    height: auto;
    opacity: 1;
  }
  #main p {
    color: #222222;
    font-weight: 600;
  }
</style>'''

about_html = page_start("About", extra_head=ABOUT_STYLE) + '''
				<!-- Main -->
					<div id="main">
						<div class="inner">
							<h1>About</h1>
							<div class="about-photo">
								<img src="images/HANA1.png" alt="HANA logo" class="about-photo__logo" />
							</div>
							<p>I'm an architect now based in Vancouver, Canada, with five years of experience designing residential, commercial, and cultural spaces in Tabriz, Iran. Over that time I've worked on projects ranging from private homes to small public spaces, always with close attention to how a building responds to its site, its climate, and the people who use it.</p>
							<p>My approach starts with the brief, not the form — I ask what a space needs to do before I decide what it should look like. I care about natural light, honest materials, and details that hold up over time, not just in a rendering. Good architecture, to me, is quiet: it serves the people in it without demanding attention for itself.</p>
							<p>Software: AutoCAD, Revit, SketchUp, and Lumion for visualization. I work in both Persian and English, and I'm currently looking to bring that experience into new projects in Vancouver and beyond.</p>
						</div>
					</div>

				''' + footer()

with open(f"{OUT}/about.html", "w", encoding="utf-8") as f:
    f.write(about_html)

# ---------------- project-XX.html ----------------
for idx, p in enumerate(PROJECTS):
    gallery_img = p["img"]
    page = page_start(p["title"]) + f'''
				<!-- Main -->
					<div id="main">
						<div class="inner">
							<h1>{p['title']} <span style="font-size:0.5em; color:#999;">— replace with the real project name</span></h1>
							<span class="image main"><img src="{gallery_img}" alt="" /></span>
							<p><strong>Type:</strong> {p['cat']} &nbsp; | &nbsp; <strong>Year:</strong> {p['year']} &nbsp; | &nbsp; <strong>Location:</strong> — &nbsp; | &nbsp; <strong>Area:</strong> — m&sup2;</p>
							<p>Replace this paragraph with the project brief: what problem the design solved, the site and its constraints, and the core concept behind the project.</p>
							<p>Replace this paragraph with more detail: materials, structure, natural light strategy, or any technical/conceptual detail that makes this project distinct.</p>
							<p>Replace this paragraph with the outcome: how the finished project performs, and anything notable about how it was received or used.</p>
						</div>
					</div>

				''' + footer()

    with open(f"{OUT}/{p['file']}", "w", encoding="utf-8") as f:
        f.write(page)

print("Generated:", 2 + len(PROJECTS), "pages")
