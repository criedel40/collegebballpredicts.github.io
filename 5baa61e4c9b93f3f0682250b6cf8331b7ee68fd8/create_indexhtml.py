import glob

ml_figs = sorted(glob.glob('Figs/moneyline_*.jpg'))
score_figs = sorted(glob.glob('Figs/score_*.jpg'))

new_str = []
new_str.append('<!DOCTYPE html>\n')
new_str.append('<html>\n')
new_str.append('<body>\n')
new_str.append('<header>\n')
new_str.append('<h1><center>College Basketball Predictions</center></h1>\n')
new_str.append('<h1><center>Predictions and figures produced by Christopher Riedel</center></h1>\n')
new_str.append('<h1><center>Data for game predictions is from <a href="https://barttorvik.com/#">barttorvik website</a></center></h1>\n')
new_str.append('</header>\n')
new_str.append('<hr height="10px" style="color:black;background-color:black;" />\n')
for l in range(0,len(ml_figs)):
  new_str.append('<div class="row">\n')
  new_str.append('<div class="column">\n')
  new_str.append('<img src="{0}" alt="Snow" style="width:35%">\n'.format(ml_figs[l]))
  new_str.append('<img src="{0}" alt="Forest" style="width:64%">\n'.format(score_figs[l]))
  new_str.append('</div>\n')
  new_str.append('</div>\n')
  new_str.append('<hr height="4px" style="color:black;background-color:black;" />')
new_str.append('</body>\n')
new_str.append('</html>\n')

new_file = open('index.html','w')
for l in new_str:
 new_file.writelines(l)
new_file.close()


