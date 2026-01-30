@echo off
echo 🔥 Building Dystopian Ashtray...
python generate.py

echo.
echo 📦 Staging changes...
git add index.html posts.txt

echo.
echo 📝 Committing...
git commit -m "Update blog"

echo.
echo 🚀 Pushing to GitHub...
git push https://github.com/chippedpaintrecords-sudo/dystopianashtray.git

echo.
echo 🎉 Done! Your thoughts are live on GitHub Pages.
pause
