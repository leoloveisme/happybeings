from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import numpy as np, subprocess, json, sys
out=Path(__file__).parent
text=(out/'narration.txt').read_text().strip()
(out/'narration.txt').write_text(text+'\n')
W,H=1920,1080; fps=24; horizon=180; tw=1500
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',64)
lines=[]; y=0; cues=[]
for para in text.split('\n\n'):
 cues.append({'text':para,'texture_y':y})
 line=''
 for word in para.split():
  trial=(line+' '+word).strip()
  if font.getlength(trial)>tw-80:
   lines.append((line,y));y+=88;line=word
  else: line=trial
 lines.append((line,y));y+=88+65
tex=Image.new('L',(tw,y+100));d=ImageDraw.Draw(tex)
for line,yy in lines:d.text(((tw-font.getlength(line))/2,yy),line,font=font,fill=255,stroke_width=0)
tex.save(out/'text-plane.png')
start=12; speed=y/82; K=900*tw/1580; A=K*780; duration=126
for cue in cues:cue['approx_entry_seconds']=round(start+cue['texture_y']/speed,2)
(out/'timing.json').write_text(json.dumps({'fps':fps,'duration':duration,'crawl_start':start,'paragraphs':cues},indent=2))
rng=np.random.default_rng(27)
bg=Image.new('RGB',(W,H));d=ImageDraw.Draw(bg)
for i in range(800):
 x=int(rng.integers(W)); yy=int(rng.integers(H)); bright=int(rng.integers(45,165));r=1 if i<70 else 0
 d.ellipse((x-r,yy-r,x+r,yy+r),fill=(bright,bright,min(190,bright+12)))
bg.save(out/'starfield.png')
fade=np.clip((np.arange(H)-260)/200,0,1).astype(np.float32)[:,None]
title=Image.new('L',(1600,350));d=ImageDraw.Draw(title)
for word,size,yy in [('HAPPY BEINGS',145,0),('EPISODE IV — NEW HORIZONS',65,210)]:
 f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',size)
 d.text(((1600-f.getlength(word))/2,yy),word,font=f,fill=255)
def frame(t):
 b=bg.copy()
 if t<4:b=Image.blend(Image.new('RGB',(W,H)),b,max(0,min(1,(t-2)/2)))
 if 4<=t<12:
  q=max(0,(t-7)/5); scale=max(.015,(1-q)**2)
  im=title.resize((max(1,int(1600*scale)),max(1,int(350*scale))),Image.Resampling.LANCZOS)
  alpha=max(0,min(1,(t-4)/.6))*min(1,(12-t)/.6)
  im=im.point(lambda v:int(v*alpha));cy=int(510-290*q)
  b.paste((245,200,70),(int((W-im.width)/2),cy-im.height//2,int((W+im.width)/2),cy-im.height//2+im.height),im)
 if t>=start:
  offset=(t-start)*speed+A/(H-horizon)
  coeff=(-K/horizon,-tw/(2*horizon),K*(W/2)/horizon+tw/2,0,-offset/horizon,offset+A/horizon,0,-1/horizon)
  mask=tex.transform((W,H),Image.Transform.PERSPECTIVE,coeff,Image.Resampling.BICUBIC)
  arr=np.asarray(mask).astype(np.float32)*fade
  arr[:horizon+1]=0
  arr*=min(1,max(0,(122-t)/4))
  b.paste((245,200,70),(0,0,W,H),Image.fromarray(arr.astype('uint8')))
 return b
if '--stills' in sys.argv:
 for t in [0,5,10,20,40,65,90,110,124]:frame(t).save(out/f'frame-{t:03}.jpg')
else:
 proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(fps),'-i','-','-an','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(out/'Opening crawl v1 - silent.mp4')],stdin=subprocess.PIPE)
 for n in range(duration*fps):
  proc.stdin.write(frame(n/fps).tobytes())
  if n%(fps*10)==0:print(f'Rendered {n/fps:.0f}/{duration}s',flush=True)
 proc.stdin.close();assert proc.wait()==0
