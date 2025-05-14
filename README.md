
# Scholar Stats Embed iFrame card

This project allows you to display your Google Scholar citation metrics in a clean, responsive card via an iframe. It's ideal for embedding on academic or personal websites.

## Features

- Displays total and recent citations
- Shows research impact metrics (h-index)
- Modern, mobile-friendly design
- Easily embeddable via iframe
- No external dependencies beyond standard Python and browser JS

## Demo

```html
<iframe src="/scholar-box.html" width="100%" height="340" style="border: none;"></iframe>
```
How It Works
	1.	A Python script scrapes your Google Scholar profile.
	2.	It generates a scholar-stats.json file with the key metrics.
	3.	A styled scholar-box.html reads this JSON and displays it.
	4.	This page can be embedded via iframe on any website.

## Setup

1. Clone the repository
```
git clone https://github.com/sjhilt/scholar-card.git
cd scholar-card
```
2. Install Python dependencies

Use a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Set your Google Scholar ID

Edit generate_scholar_stats.py and replace:
```
USER_ID = 'YOUR_GOOGLE_SCHOLAR_ID'
```
4. Generate the JSON
```
python scholar_stats.py
```
5. Serve the site

You can test locally with:
```
python3 -m http.server
```
Or host it under /var/www/html/ for Apache/Nginx.

6. Embed the iframe

On your main website, embed the following:
```
<iframe src="/scholar-box.html" width="100%" height="340" style="border: none;"></iframe>
```
Automate Updates (Optional)

You can set up a cron job to refresh the data periodically.
```
crontab -e
```
Add this line (adjust paths as needed):
```
0 2 * * * /full/path/to/venv/bin/python /full/path/to/scholar_stats.py
```
## License

This project is open-source and available under the MIT License.

