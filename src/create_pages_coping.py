import pandas as pd

df = pd.read_csv('src/coping_autism.csv')

for _, row in df.iterrows():
  title = row['title']
  img = row['url']
  


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
  <h2>{title}</h2>
  <p><img src="{img}" alt="Cayman Logo" class="logo"></p>

      </section>

    </body>
  </html>
  '''


 
  

  with open(f'coping/{row.post_id}.html', 'w', encoding='utf-8') as f:
      f.write(s)