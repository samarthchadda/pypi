from bs4 import BeautifulSoup

html="""
<!DOCTYPE html>
<html>
<head>
	<title>First HTML Page</title>
</head>
<body>
<div id="first">
	<h3 data-example="yes">Hi</h3>
	<p>More text.</p>
</div>
<ol>
	<li class="special">This item is special.</li>
	<li class="special">This item is special.</li>
	<li>This item is not special.</li>
</ol>
<div>Bye</div>
</body>
</html>
"""

soup=BeautifulSoup(html,"html.parser")
# print(soup.body)
# print(soup.find("div"))
# d=soup.find_all("div")
d=soup.select("#first")
# d=soup.select("#first")[0]
print(d)
# print(type(soup))
