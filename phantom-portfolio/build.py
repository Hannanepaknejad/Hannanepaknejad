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
							<span class="symbol"><img src="images/logo.svg" alt="" /></span><span class="title">Hannane Paknejad</span>
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
							<li><a href="https://instagram.com/yourhandle" target="_blank" rel="noopener" class="icon brands style2 fa-instagram"><span class="label">Instagram</span></a></li>
							<li><a href="https://linkedin.com/in/yourhandle" target="_blank" rel="noopener" class="icon brands style2 fa-linkedin-in"><span class="label">LinkedIn</span></a></li>
							<li><a href="mailto:hannane@example.com" class="icon solid style2 fa-envelope"><span class="label">Email</span></a></li>
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

def page_start(title):
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
								<h1>I'm Hannane Paknejad, an architect designing spaces<br />
								that balance function, light, and material honesty.</h1>
								<p>This is a selection of my residential, commercial, cultural and urban work. Replace this paragraph with your own introduction — who you are, what you focus on, and what makes your approach distinct.</p>
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
about_html = page_start("About") + '''
				<!-- Main -->
					<div id="main">
						<div class="inner">
							<h1>About</h1>
							<span class="image main"><img src="images/pic13.jpg" alt="" /></span>
							<p>Replace this paragraph with your real biography: where you studied, the offices or studios you've worked with, and the kind of projects you're drawn to — residential, adaptive reuse, public space, and so on.</p>
							<p>Replace this paragraph with your design philosophy: how you approach a brief, the principles you always return to, and what a client or collaborator can expect from working with you.</p>
							<p>Replace this paragraph with tools and skills: software (AutoCAD, Revit, SketchUp, Rhino, Lumion, V-Ray), languages, and any certifications or awards worth mentioning.</p>
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
