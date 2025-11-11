post = 'Forza destra nazionalista patriottica di tutto il mondo fan c... la sinistra woke green lgtb.. pro invasione pro islam global-distruttiva'
option1 = 'destra nazionalista'
option2 = 'sì sì'
option3 = 'bla bla'
option4 = 'ciao'
s = f'''
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="UTF-8">
    <title>Cayman</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#157878">
    <link rel="stylesheet" href="../css/normalize.css">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="../css/cayman.css">
  </head>
  <body>
    <section class="page-header">
    </section>

    <section class="main-content">
<h2>Read the Telegram Message</h2>
<p>{post}</p>

<h2>Read the spans of text that highlight a conspiracy plan</h2>
<ul>
    <li><b>OPTION 1</b> {option1}</li>
    <li><b>OPTION 2</b> {option2}</li>
    <li><b>OPTION 3</b> {option3}</li>
    <li><b>OPTION 4</b> {option4}</li>
</ul>

    </section>

  </body>
</html>
'''

with open('posts/2.html', 'w', encoding='utf-8') as f:
    f.write(s)