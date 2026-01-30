from datetime import datetime
import re

with open("posts.txt", "r", encoding="utf-8") as f:
    raw_posts = f.read().strip().split("\n---\n")

processed_posts = []
posts_html = ""

timestamp_pattern = re.compile(r"^\[(.*?)\]\n", re.DOTALL)

for post in raw_posts:
    post = post.strip()

    match = timestamp_pattern.match(post)

    if match:
        timestamp = match.group(1)
        content = post[match.end():].strip()
    else:
        timestamp = datetime.now().strftime("%m-%d-%Y · %I:%M %p")
        content = post
        post = f"[{timestamp}]\n{content}"

    processed_posts.append(post)

    posts_html += f"""
  <div class="post">
    <div class="timestamp">{timestamp}</div>
    <div class="content">
{content}
    </div>
  </div>

  <hr>
"""

# Write back posts.txt ONLY if new timestamps were added
with open("posts.txt", "w", encoding="utf-8") as f:
    f.write("\n---\n".join(processed_posts))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Dystopian Ashtray</title>

<style>
body {{
  background-color: black;
  color: #27FF00;
  font-family: monospace;
  max-width: 800px;
  margin: 40px auto;
  padding: 0 20px;
}}

.subtitle {{
  color: #D900FF;
  margin-bottom: 40px;
}}

.timestamp {{
  color: #666;
  font-size: 0.9em;
  margin-bottom: 8px;
}}

.content {{
  white-space: pre-wrap;
  line-height: 1.6;
}}

hr {{
  border: none;
  border-top: 1px solid #222;
  margin: 40px 0;
}}
</style>
</head>

<body>

<h1>Dystopian Ashtray.</h1>
<div class="subtitle">The digital dumpster for my brain.</div>

{posts_html}

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated. Timestamps preserved.")
