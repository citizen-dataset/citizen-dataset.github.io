import pandas as pd

df = pd.read_csv('src/data.csv')

for _, row in df.iterrows():
  post = row['text']
  if row['all_plan']==0:
    row.secret = eval(row['secret'])
    option1 = row['secret'][0]
    option2 = row['secret'][1]
    option3 = row['secret'][2]
    option4 = row['secret'][3]
    inst = "Read the spans of text that highlight a secret plan"
  else:
    row.plan = eval(row['plan'])
    option1 = row['plan'][0]
    option2 = row['plan'][1]
    option3 = row['plan'][2]
    option4 = row['plan'][3]
    inst = "Read the spans of text that highlight a conspiracy plan"


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

  <h2>{inst}</h2>
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

  with open(f'posts/{row.page_id}.html', 'w', encoding='utf-8') as f:
      f.write(s)